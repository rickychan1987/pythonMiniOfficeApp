import os
import shutil

# Set the working directory (where your files are)
# Change this to your target path if needed
base_dir = os.getcwd()

start = 1
end = 300

for i in range(start, end + 1):
    folder_name = f"HNVN{i:04d}"  # HNVN0001 ... HNVN0300
    folder_path = os.path.join(base_dir, folder_name)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

