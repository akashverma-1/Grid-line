import PyPDF2

# Example: Merge multiple PDF files into a single PDF
def merge_pdfs(input_paths, output_path):
    pdf_writer = PyPDF2.PdfWriter()
    
    for path in input_paths:
        pdf_reader = PyPDF2.PdfFileReader(path)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)
    
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)
    print("PDFs merged successfully.")

# Example: Split a PDF into multiple separate PDF files
def split_pdf(input_path, output_dir):
    pdf_reader = PyPDF2.PdfFileReader(input_path)
    
    for page_num in range(pdf_reader.numPages):
        pdf_writer = PyPDF2.PdfWriter()
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)
        output_path = f"{output_dir}/page_{page_num + 1}.pdf"
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
    print("PDF split successfully.")

# Example: Extract text from a PDF
def extract_text(input_path):
    with open(input_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfFileReader(input_file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

# Example usage
input_paths = ["input1.pdf", "input2.pdf"]
output_path = "merged_output.pdf"
output_dir = "split_output"
input_path = "input.pdf"

# Merge PDFs
merge_pdfs(input_paths, output_path)

# Split PDF
split_pdf(input_path, output_dir)

# Extract text from a PDF
text = extract_text(input_path)
print("Text extracted from PDF:", text)
