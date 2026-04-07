import os
from PIL import Image   # Pillow library for image processing
import shutil   #for zip folder

input_folder = os.getcwd()   # folder containing .tiff files
output_folder = "pdf" # folder to save .pdf files (change folder name if needed)

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

#Loop through all TIFF files
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".tiff"):
        tiff_path = os.path.join(input_folder, filename)
        pdf_path = os.path.join(output_folder, filename.rsplit(".", 1)[0] + ".pdf")

        image = Image.open(tiff_path)
        image_list = []

        # Handle multi-page TIFF
        try:
            while True:
                image_list.append(image.convert("RGB"))
                image.seek(image.tell() + 1)
        except EOFError:
            pass

        if image_list:
            image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])
            print(f"Converted: {tiff_path} -> {pdf_path}")

#Move current directory existing PDF files to output folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
        src = os.path.join(input_folder, filename)
        dst = os.path.join(output_folder, filename)
        # Only move if src and dst are different paths
        if os.path.abspath(src) != os.path.abspath(dst):
            shutil.move(src, dst)
            print(f"Moved existing PDF: {src} -> {dst}")


# Zip the output_folder after conversion
zip_filename = output_folder + ".zip"
shutil.make_archive(output_folder, 'zip', output_folder)
print(f"All PDFs zipped into: {zip_filename}")

###This app is converting tiff files to pdf and move existing pdf files to output folder. as well as zip the file###