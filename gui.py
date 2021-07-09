import os
import ntpath
import tkinterdnd2

from tkinter import *
from tkinterdnd2 import *

from page_separator import insert_suffix, main

BG_COLOR = "#D4F1F4"

def on_drop(event):
    source_pdf.set(event.data)
    output_dir.set(os.path.dirname(event.data))

def on_clicked():
    source_pdf_str = source_pdf.get()
    base = ntpath.basename(source_pdf_str)
    output_dir_str = output_dir.get()
    legal_pdf_path = os.path.join(output_dir_str, insert_suffix(base, "_legal"))
    letter_pdf_path = os.path.join(output_dir_str, insert_suffix(base, "_letter"))
    main(source_pdf_str, legal_pdf_path, letter_pdf_path)

if __name__ == '__main__':   
    # Main window
    ws = tkinterdnd2.Tk()
    ws.title('Legal/Letter PDF Separator')
    ws.geometry('300x300')
    ws.config(bg=BG_COLOR)

    # Variable declarations
    source_pdf = StringVar()
    output_dir = StringVar()

    # Drag-and-Drop area
    lframe = LabelFrame(ws, text='Instructions', bg=BG_COLOR)
    Label(
        lframe, 
        bg=BG_COLOR,
        text='Drag and drop your PDF here.'
        ).pack(fill=BOTH, expand=True)
    lframe.drop_target_register(DND_FILES)
    lframe.dnd_bind('<<Drop>>', on_drop)
    lframe.pack(fill=BOTH, expand=True, padx=10)

    # Read-only text input displaying the source PDF filepath
    Label(ws, text='Path to the file:', bg=BG_COLOR).pack(anchor=NW, padx=10)
    source_pdf_text = Entry(ws, textvar=source_pdf, width=80, state=DISABLED)
    source_pdf_text.pack(fill=X, padx=10, pady=5)

    # Text input for the output directory. User can change after populated.
    Label(ws, text='Output directory:', bg=BG_COLOR).pack(anchor=NW, padx=10)
    out_dir_text = Entry(ws, textvar=output_dir, width=80)
    out_dir_text.pack(fill=X, padx=10, pady=5)

    # Button to start the process
    btn = Button(ws, justify="center", text="Separate", height=1, width=10, command=on_clicked)
    btn.pack(side=TOP, pady=5)
        
    ws.mainloop()