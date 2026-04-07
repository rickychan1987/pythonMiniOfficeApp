from PyPDF2 import PdfReader, PdfWriter

# Input and output file paths
input_pdf_path = "33589337-88e8-4893-bf77-61b2d5ac2112.pdf"     # Replace with your file path
output_pdf_path = "33589337.pdf"   # The new merged PDF

# Create PDF reader and writer
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# Loop through pages and add all except page 2 (index 1, since it's zero-based)
for i in range(len(reader.pages)):
    if i != 1:  # Skip page 2 (index 1)
        writer.add_page(reader.pages[i])

# Write the result to a new PDF
with open(output_pdf_path, "wb") as output_pdf:
    writer.write(output_pdf)

print(f"✅ New PDF created successfully: {output_pdf_path}")
