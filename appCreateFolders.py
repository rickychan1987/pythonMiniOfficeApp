import os
import shutil

# Set the working directory (where your files are)
# Change this to your target path if needed
base_dir = os.getcwd()

for i in range(1, 21):
    folder_name = f"HNVN{i:03d}"  # HNVN001 ... HNVN20
    folder_path = os.path.join(base_dir, folder_name)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

