import os
import shutil

# Set your working directory (adjust if needed)
base_dir = os.getcwd()

for i in range(1, 201):
    folder_name = f"HNVN{i:03d}"
    folder_path = os.path.join(base_dir, folder_name)

    if os.path.isdir(folder_path):
        # Loop through files inside the folder
        for filename in os.listdir(folder_path):
            src = os.path.join(folder_path, filename)
            dst = os.path.join(base_dir, filename)
            
            if os.path.isfile(src):
                shutil.move(src, dst)
                print(f"Moved back: {filename} -> {base_dir}")

