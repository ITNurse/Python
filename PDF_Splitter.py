from PyPDF2 import PdfReader, PdfWriter

# Define file name
file_name = 'ENTER FILE NAME HERE'


# Define start and end pages for each chapter
section_ranges = {
    'Section 1': (0, 9),
    'Section 2': (10,19),
    'Section 3': (20,29)
}

# Open the PDF
input_pdf = PdfReader(file_name)

# Split the PDF
for chapter, (start, end) in section_ranges.items():
    pdf_writer = PdfWriter()
    for page_num in range(start, end + 1):
        pdf_writer.add_page(input_pdf.pages[page_num])

    # Save the chapter to a new PDF file
    filename = f'{file_name} - {chapter}.pdf'
    with open(filename, 'wb') as out_file:
        pdf_writer.write(out_file)