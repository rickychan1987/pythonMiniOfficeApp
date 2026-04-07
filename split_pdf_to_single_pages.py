from pypdf import PdfReader, PdfWriter
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_folder, "split done")

os.makedirs(output_folder, exist_ok=True)

file_index = 1

for filename in os.listdir(current_folder):
    if filename.lower().endswith(".pdf") and filename != os.path.basename(__file__):
        pdf_path = os.path.join(current_folder, filename)
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            writer = PdfWriter()
            writer.add_page(page)

            output_name = f"abc{file_index}.pdf"
            output_path = os.path.join(output_folder, output_name)

            with open(output_path, "wb") as f:
                writer.write(f)

            file_index += 1

print("All PDFs have been split into the 'split done' folder with abc1, abc2, abc3 ...")


###Before run this split page in multiple page pdf file, please make sure the multiple page pdf file is not open in any pdf viewer application.###
###As well as same for the output folder "split done"###