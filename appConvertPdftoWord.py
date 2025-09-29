###Below code is for simple text extraction from PDF to DOCX without formatting
# import os
# from docx import Document
# from PyPDF2 import PdfReader

# input_folder = os.getcwd()

# def pdf_to_docx(pdf_path, input_folder):
#     """Extract text from a PDF and save into a DOCX file"""
#     reader = PdfReader(pdf_path)
#     doc = Document()

#     for page_num, page in enumerate(reader.pages, start=1):
#         text = page.extract_text()
#         if text:
#             doc.add_paragraph(text)
#         else:
#             doc.add_paragraph(f"[Page {page_num} had no extractable text]")

#     doc.save(input_folder)

# def convert_pdfs_to_docx(input_folderr, output_dir="DOCX"):
#     """Convert all PDF files in input_dir to DOCX and save in output_dir"""
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     for filename in sorted(os.listdir(input_folder)):
#         if filename.lower().endswith(".pdf"):
#             pdf_path = os.path.join(input_folder, filename)
#             docx_path = os.path.join(output_dir, filename.replace(".pdf", ".docx"))
#             print(f"Converting: {filename} -> {docx_path}")
#             try:
#                 pdf_to_docx(pdf_path, docx_path)
#             except Exception as e:
#                 print(f"Failed to convert {filename}: {e}")

# if __name__ == "__main__":
#     # Change this to your directory path
#     input_directory = "your_directory_path_here"
#     convert_pdfs_to_docx(input_directory, "DOCX")
#     print("✅ Conversion complete. DOCX files saved in 'DOCX' folder.")

###Below code is covert PDF UTF8 keep those text formattings
from pdf2docx import Converter
import os

input_dir = os.getcwd()

def convert_pdfs_to_docx(input_dir, output_dir="DOCX"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in sorted(os.listdir(input_dir)):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            docx_path = os.path.join(output_dir, filename.replace(".pdf", ".docx"))
            print(f"Converting: {filename} -> {docx_path}")
            try:
                cv = Converter(pdf_path)
                cv.convert(docx_path, start=0, end=None)  # keeps UTF-8 automatically
                cv.close()
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    input_directory = input_dir 
    convert_pdfs_to_docx(input_directory, "DOCX")
    print("✅ Conversion complete. DOCX files saved in 'DOCX' folder.")


###Please choose which style of convert PDF to DOCX you want to use.