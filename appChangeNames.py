import os

# Set your working directory
base_dir = os.getcwd()

old_prefix = "Something"
new_prefix = "HNVN"

for filename in os.listdir(base_dir):
    if filename.startswith(old_prefix) and os.path.isfile(os.path.join(base_dir, filename)):
        name, ext = os.path.splitext(filename)              # e.g. HNVN001 -> (HNVN001, .txt)
        number = name[len(old_prefix):]                     # keep the number part (001, 002...)
        new_name = f"{new_prefix}{number}{ext}"             # Something001.txt
        os.rename(
            os.path.join(base_dir, filename),
            os.path.join(base_dir, new_name)
        )
        print(f"Renamed: {filename} -> {new_name}")
