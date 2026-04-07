import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

# --- CONFIGURATION ---
folder_path = r"D:\Administrator\Pictures\Camera Roll\LRDG"
csv_file = os.path.join(folder_path, "dg_list.csv")
excel_output = os.path.join(folder_path, "photo_links.xlsx")
photo_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.heic', '.tiff'}

# --- STEP 1: Read CSV ---
df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip().str.lower()
if not {'id', 'name'}.issubset(df.columns):
    raise ValueError("CSV must contain 'ID' and 'Name' columns.")

# --- STEP 2: Collect photos in folder ---
photo_files = [f for f in os.listdir(folder_path)
               if os.path.splitext(f)[1].lower() in photo_extensions]

# --- STEP 3: Rename photos based on CSV ---
renamed_files = []
for i, row in df.iterrows():
    if i >= len(photo_files):
        break

    old_name = photo_files[i]
    id_val = str(row['id']).strip()
    name_val = str(row['name']).strip().replace(" ", "_")
    _, ext = os.path.splitext(old_name)
    new_name = f"{id_val}_{name_val}{ext}"

    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    renamed_files.append(new_name)
    print(f"✅ Renamed: {old_name} → {new_name}")

# --- STEP 4: Create Excel with photo links ---
wb = Workbook()
ws = wb.active
ws.title = "Photo Links"

# Headers
ws.append(["ID", "Name", "Photo Link"])
for cell in ws[1]:
    cell.font = Font(bold=True)

# Fill Excel with hyperlinks
for i, row in df.iterrows():
    id_val = str(row['id']).strip()
    name_val = str(row['name']).strip()
    if i < len(renamed_files):
        photo_file = renamed_files[i]
        link_path = os.path.join(folder_path, photo_file)
        ws.append([id_val, name_val, f'=HYPERLINK("{link_path}", "{photo_file}")'])
    else:
        ws.append([id_val, name_val, "(no photo)"])

# Adjust column widths
ws.column_dimensions["A"].width = 10
ws.column_dimensions["B"].width = 25
ws.column_dimensions["C"].width = 60

wb.save(excel_output)
print(f"🎯 Done! Created Excel file with photo links → {excel_output}")
