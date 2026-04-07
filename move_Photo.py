import os
import shutil

# 👇 Define multiple destination folders in a list
destination_folders = [
    r"D:\Administrator\Pictures\Camera Roll\LRDG",
    r"D:\Administrator\Pictures\Camera Roll\spray",
    r"D:\Administrator\Pictures\Camera Roll\SX"
]

# 👇 Choose which folder to use (1, 2, or 3)
choice = 1  # you can change this to 2 or 3

destination_folder = destination_folders[choice - 1]

# Supported photo extensions
photo_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

current_folder = os.getcwd()
os.makedirs(destination_folder, exist_ok=True)

for file_name in os.listdir(current_folder):
    file_path = os.path.join(current_folder, file_name)
    if os.path.isfile(file_path) and os.path.splitext(file_name)[1].lower() in photo_extensions:
        shutil.move(file_path, os.path.join(destination_folder, file_name))
        print(f"Moved: {file_name}")

print(f"✅ All photos moved to: {destination_folder}")
