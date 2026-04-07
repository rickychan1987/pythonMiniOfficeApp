import os
import shutil

# Set working directory (adjust if needed)
base_dir = os.getcwd() # Current directory

# Loop through all items in base_dir
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)

    # Only process folders
    if os.path.isdir(folder_path):
        # Find files in base_dir that start with the folder name
        for filename in os.listdir(base_dir):
            file_path = os.path.join(base_dir, filename)
            if (filename.startswith(folder_name) 
                and os.path.isfile(file_path)):
                # Move file into its matching folder
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder_name}/")
