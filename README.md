# legal-letter-pdf-separator
This Python script will take an input PDF and split it into two PDFs by legal and letter size.

## Install
```bash
python3 -m virtualenv ./venv
./venv/bin/activate          # Linux/OSX
./venv/Scripts/activate.ps1  # Windows powershell
pip install -r requirements.txt
```

## Usage
```
usage: page_separator.py [-h] [--letter_pdf LETTER_PDF] [--legal_pdf LEGAL_PDF] source_pdf

Splits a PDF into two PDFs by letter and legal page size.

positional arguments:
  source_pdf            Name of the source PDF with mixed page size, E.g. SamplePrint-MultipleSize.pdf

optional arguments:
  -h, --help            show this help message and exit
  --letter_pdf LETTER_PDF
                        Name of the PDF to write to containing letter pages (default: <source_pdf>_letter.pdf)
  --legal_pdf LEGAL_PDF
                        Name of the PDF to write to containing legal pages (default: <source_pdf>_legal.pdf)
```