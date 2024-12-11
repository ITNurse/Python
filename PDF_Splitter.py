"""
Script Name: PDF_Splitter.py
Purpose: This script automates the process of splitting a single PDF 
file into multiple smaller PDF files based on predefined page ranges. 
It is particularly useful for organizing large PDF documents into separate s
ections or chapters, saving each section as an individual file.  To use this 
script, update the file name and section range sections below.

Usage: Run this script in Python 3.8+ with the required libraries:
       - PyPDF2

Author: ITNurse
Date: December 11, 2024
Version: 1.0
"""

from PyPDF2 import PdfReader, PdfWriter

# Define file name
file_name = 'FILE_NAME.py'


# Define start and end pages for each section
section_ranges = {
    'Section 1': (0, 9),
    'Section 2': (10,19),
    'Section 3': (20,29)
}

# Open the PDF
input_pdf = PdfReader(file_name)

# Split the PDF
for section, (start, end) in section_ranges.items():
    pdf_writer = PdfWriter()
    for page_num in range(start, end + 1):
        pdf_writer.add_page(input_pdf.pages[page_num])

    # Save the section to a new PDF file
    filename = f'{file_name} - {section}.pdf'
    with open(filename, 'wb') as out_file:
        pdf_writer.write(out_file)