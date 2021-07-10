# legal-letter-pdf-separator
This python program takes an input PDF and split it into two PDFs by legal and letter size. The GUI is built with `tkinter` and wraps the underlying command-line tool.

## Graphical User Interface
Start it with `python gui.py`

![image](https://user-images.githubusercontent.com/7364664/125169732-5db22c80-e160-11eb-8994-14e18f022fa1.png)

## Command-line

### Install
```bash
virtualenv
source ./venv/bin/activate   # Linux/OSX
./venv/Scripts/activate.ps1  # Windows powershell
pip install -r requirements.txt
```

### Usage
```
usage: page_separator.py [-h] [--legal_pdf LEGAL_PDF] [--letter_pdf LETTER_PDF] source_pdf

Splits a PDF into two PDFs by letter and legal page size.

positional arguments:
  source_pdf            Name of the source PDF with mixed page size, E.g. SamplePrint-MultipleSize.pdf

optional arguments:
  -h, --help            show this help message and exit
  --legal_pdf LEGAL_PDF
                        Name of the PDF to write to containing legal pages (default: <source_pdf>_legal.pdf)
  --letter_pdf LETTER_PDF
                        Name of the PDF to write to containing letter pages (default: <source_pdf>_letter.pdf)
```
