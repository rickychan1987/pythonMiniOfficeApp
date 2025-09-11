import os
from PIL import Image

input_folder = os.getcwd()   # folder containing .tiff files
output_folder = "XiaYongMing" # folder to save .pdf files (change folder name if needed)
os.makedirs(output_folder, exist_ok=True) # Make sure output folder exists

#below this code is counting pdf and tiff files with current directory
pdfs_in_input = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')] # Check for existing PDFs
tiffs_in_input = [f for f in os.listdir(input_folder) if f.lower().endswith('.tiff')] # Check for existing TIFFs
#Please add more extension files if needed
print(f"PDFs in current directory before move: {len(pdfs_in_input)}") # Check for existing PDFs
print(f"TIFFs in current directory before conversion: {len(tiffs_in_input)}") # Check for existing TIFFs
#Print more sentence with file extension if needed


# Make sure output folder exists
pdfs_in_output = [f for f in os.listdir(output_folder) if f.lower().endswith('.pdf')] # Check for existing PDFs
pdfs_in_output = [f for f in os.listdir(output_folder) if f.lower().endswith('.tiff')] # Check for existing TIFFs
print(f"PDFs in output folder after move: {len(pdfs_in_output)}")     
print(f"TIFFs in current directory before conversion: {len(tiffs_in_input)}") 
#Make sure those code here match with above code

###This app is only counting pdf and tiff files in current directory and output folder.###
