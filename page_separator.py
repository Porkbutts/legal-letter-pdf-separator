import argparse
import sys

from enum import Enum

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.pdf import PageObject

LETTER_RATIO = 11 / 8.5
LEGAL_RATIO = 14 / 8.5
MARGIN_OF_ERROR = 0.05 # page ratio should differ by at most this percent
if MARGIN_OF_ERROR >= 0.12:
    sys.exit("MARGIN_OF_ERROR is too large! page type detection will overlap")

class PageType(Enum):
    UNKNOWN = 0
    LETTER = 1
    LEGAL = 2
    

def page_type(page: PageObject) -> PageType:
    ratio = page.mediaBox.getHeight() / page.mediaBox.getWidth()
    if abs(1 - ratio/LETTER_RATIO) < MARGIN_OF_ERROR:
        return PageType.LETTER
    elif abs(1 - ratio/LEGAL_RATIO) < MARGIN_OF_ERROR:
        return PageType.LEGAL
    return PageType.UNKNOWN


def insert_suffix(pdf: str, suffix: str) -> str:
    return pdf.split(".pdf")[0] + suffix + ".pdf"
    
def main(source_pdf: str, legal_pdf: str = None, letter_pdf: str = None, unknown_pdf: str = None):
    legal_pdf = legal_pdf if legal_pdf else insert_suffix(source_pdf, "_legal")
    letter_pdf = letter_pdf if letter_pdf else insert_suffix(source_pdf, "_letter")
    unknown_pdf = unknown_pdf if unknown_pdf else insert_suffix(source_pdf, "_unknown")
    
    reader = PdfFileReader(open(source_pdf, "rb"))
    legal_writer = PdfFileWriter()
    letter_writer = PdfFileWriter()
    unknown_writer = PdfFileWriter()
    
    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        ptype = page_type(page)
        if ptype == PageType.LEGAL:
            legal_writer.addPage(page)
        elif ptype == PageType.LETTER:
            letter_writer.addPage(page)
        else:
            unknown_writer.addPage(page)
        
    with open(legal_pdf, "wb") as f:
        legal_writer.write(f)
        
    with open(letter_pdf, "wb") as f:
        letter_writer.write(f)
        
    if unknown_writer.getNumPages():
        with open(unknown_pdf, "wb") as f:
            unknown_writer.write(f)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Splits a PDF into two PDFs by letter and legal page size.")
    parser.add_argument("source_pdf", help="Name of the source PDF with mixed page size, E.g. SamplePrint-MultipleSize.pdf")
    parser.add_argument("--legal_pdf", help="Name of the PDF to write to containing legal pages (default: <source_pdf>_legal.pdf)")
    parser.add_argument("--letter_pdf", help="Name of the PDF to write to containing letter pages (default: <source_pdf>_letter.pdf)")
    parser.add_argument("--unknown_pdf", help="Failed to detect pages will be written here if any (default: <source_pdf>_unknown.pdf)")
    args = parser.parse_args()
    main(args.source_pdf, args.legal_pdf, args.letter_pdf, args.unknown_pdf)
    