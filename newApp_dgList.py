import os
import pandas as pd

# --- Step 1: Get photo names and export to TXT ---
folder_path = r"D:\Administrator\Pictures\Camera Roll\LRDG_test"
output_txt = r"D:\Administrator\Pictures\Camera Roll\LRDG_test\LRDG_photo_list.txt"
photo_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.heic', '.tiff'}

# Collect all photo names
photo_files = [f for f in os.listdir(folder_path)
               if os.path.splitext(f)[1].lower() in photo_extensions]

# Save photo names to TXT
with open(output_txt, 'w', encoding='utf-8') as f:
    for filename in photo_files:
        f.write(filename + '\n')

print(f"✅ Step 1 complete: Photo names exported to {output_txt}")

# --- Step 2: Read CSV and append photo names as new column ---
csv_file = r"D:\Administrator\Pictures\Camera Roll\LRDG_test\dg_list.csv"
output_csv = r"D:\Administrator\Pictures\Camera Roll\LRDG_test\add_photoname.csv"

# Read CSV
df = pd.read_csv(csv_file)

# Read photo names from TXT (one per line)
with open(output_txt, 'r', encoding='utf-8') as f:
    photo_list = [line.strip() for line in f if line.strip()]

# Ensure lengths match (pad with blanks if needed)
while len(photo_list) < len(df):
    photo_list.append("(no photo name)")

# Add new column
df["PhotoName"] = photo_list[:len(df)]

# Save to new CSV
df.to_csv(output_csv, index=False, encoding='utf-8-sig')

print(f"✅ Step 2 complete: Added 'PhotoName' column to {output_csv}")
