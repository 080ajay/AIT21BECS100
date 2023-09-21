import PyPDF2

def combine_selected_pages(input_pdfs, output_pdf, pages_to_combine):
    pdf_writer = PyPDF2.PdfWriter()

    
    for pdf_path, page_numbers in pages_to_combine.items():
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_number in page_numbers:
                pdf_writer.add_page(pdf_reader.pages[page_number - 1])

    #ADD THE COMMENTS
    
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)


if __name__ == "__main__":
    input_pdfs = [
        "C:/Users/Ajay/OneDrive/Desktop/Module 3_Deadlocks and Memory Management_LectureNotes.pdf",
        "C:/Users/Ajay/OneDrive/Desktop/Module 4_Virtual memory and File Systems_LectureNotes.pdf"
        # Add more input PDF paths as needed
    ]

    
    output_pdf = 'laptop.pdf'

    
    # Dictionary where keys are PDF paths and values are lists of page numbers to combine
    pages_to_combine = {
        "C:/Users/Ajay/OneDrive/Desktop/Module 3_Deadlocks and Memory Management_LectureNotes.pdf": [1, 23, 3],
         "C:/Users/Ajay/OneDrive/Desktop/Module 4_Virtual memory and File Systems_LectureNotes.pdf": [4, 5]
        # Add more entries as needed
    }

    
    combine_selected_pages(input_pdfs, output_pdf, pages_to_combine)
    print("PDFs combined successfully!")
