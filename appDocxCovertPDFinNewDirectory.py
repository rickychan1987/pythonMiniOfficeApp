### DOCX to PDF Converter This script converts all .docx files in a specified directory to PDF format###
# Package required: docx2pdf [pip install docx2pdf]
# import os
# from docx2pdf import convert

# def convert_docx_to_pdf(input_dir, output_dir="PDF"):
#     """Convert all .docx files in input_dir to PDF and save in output_dir"""
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     for filename in sorted(os.listdir(input_dir)):
#         if filename.lower().endswith(".docx"):
#             docx_path = os.path.join(input_dir, filename)
#             pdf_path = os.path.join(output_dir, filename.replace(".docx", ".pdf"))
#             print(f"Converting: {filename} -> {pdf_path}")
#             try:
#                 convert(docx_path, pdf_path)
#             except Exception as e:
#                 print(f"Failed to convert {filename}: {e}")

# if __name__ == "__main__":
#     # Change this to your directory path
#     input_directory = "D:\learning\Docs"
#     convert_docx_to_pdf(input_directory, "PDF")
#     print("✅ Conversion complete. PDFs saved in 'PDF' folder.")