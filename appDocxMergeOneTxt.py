### DOCX to TXT Merger This script converts all .docx files in a specified directory to text and merges them into a single text file ###
# Package required: python-docx [pip install python-docx]
# import os
# from docx import Document

# def docx_to_text(docx_path):
#     """Extract text from a .docx file"""
#     doc = Document(docx_path)
#     return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

# def merge_docx_to_txt(input_dir, output_file="total.txt"):
#     """Convert all .docx files in input_dir to text and merge into output_file"""
#     with open(output_file, "w", encoding="utf-8") as outfile:
#         for filename in sorted(os.listdir(input_dir)):
#             if filename.lower().endswith(".docx"):
#                 file_path = os.path.join(input_dir, filename)
#                 print(f"Processing: {filename}")
#                 try:
#                     text = docx_to_text(file_path)
#                     outfile.write(f"--- {filename} ---\n")
#                     outfile.write(text + "\n\n")
#                 except Exception as e:
#                     print(f"Failed to process {filename}: {e}")

# if __name__ == "__main__":
#     # Change this to your directory path
#     input_directory = "your_directory_path_here"
#     merge_docx_to_txt(input_directory, "total.txt")
#     print("✅ Conversion complete. All text saved to total.txt")