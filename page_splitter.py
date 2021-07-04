from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse
from PyPDF2.pdf import PageObject

def is_letter(page) -> bool:
    if page.mediaBox.getHeight() == 792:
        return True
    return False


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
        if is_letter(page):
            letter_writer.addPage(page)
        else:
            legal_writer.addPage(page)
        
    with open(letter_pdf, "wb") as f:
        letter_writer.write(f)
        
    with open(legal_pdf, "wb") as f:
        legal_writer.write(f)
