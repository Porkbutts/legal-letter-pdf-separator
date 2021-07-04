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
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Splits a PDF into two PDFs by letter and legal page size.")
    parser.add_argument("source_pdf", help="Name of the source PDF with mixed page size, E.g. SamplePrint-MultipleSize.pdf")
    parser.add_argument("--letter_pdf", help="Name of the PDF to write to containing letter pages (default: <source_pdf>_letter.pdf)")
    parser.add_argument("--legal_pdf", help="Name of the PDF to write to containing legal pages (default: <source_pdf>_legal.pdf)")
    args = parser.parse_args()
    
    letter_pdf = args.letter_pdf if args.letter_pdf else insert_suffix(args.source_pdf, "_letter")
    legal_pdf = args.legal_pdf if args.legal_pdf else insert_suffix(args.source_pdf, "_legal")
    
    reader = PdfFileReader(open(args.source_pdf, "rb"))
    letter_writer = PdfFileWriter()
    legal_writer = PdfFileWriter()
    
    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        ptype = page_type(page)
        if ptype == PageType.LETTER:
            letter_writer.addPage(page)
        elif ptype == PageType.LEGAL:
            legal_writer.addPage(page)
        else:
            sys.exit("Could not infer page size for page #{}".format(i))
        
    with open(letter_pdf, "wb") as f:
        letter_writer.write(f)
        
    with open(legal_pdf, "wb") as f:
        legal_writer.write(f)
