import os
import shutil
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

# --- CONFIGURATION ---
folder_path = r"D:\Administrator\Pictures\Camera Roll\LRDG"  # where your photos + csv are
csv_file = os.path.join(folder_path, "dg_list.csv")
excel_output = os.path.join(folder_path, "dg_photo_links.xlsx")

# 👇 Set your destination folder for Step 5
destination_folder = r"D:\Administrator\Pictures\Camera Roll\tong_hop_folder"

photo_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.heic', '.tiff'}

# ============================================================
# STEP 1: Read CSV
# ============================================================
df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip().str.lower()
if not {'id', 'name'}.issubset(df.columns):
    raise ValueError("CSV must contain 'ID' and 'Name' columns.")

# ============================================================
# STEP 2: Collect Photos
# ============================================================
photo_files = [f for f in os.listdir(folder_path)
               if os.path.splitext(f)[1].lower() in photo_extensions]

# ============================================================
# STEP 3: Rename Photos Based on CSV
# ============================================================
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

# ============================================================
# STEP 4: Create Excel with Photo Links
# ============================================================
wb = Workbook()
ws = wb.active
ws.title = "Photo Links"

ws.append(["ID", "Name", "Photo Link"])
for cell in ws[1]:
    cell.font = Font(bold=True)

for i, row in df.iterrows():
    id_val = str(row['id']).strip()
    name_val = str(row['name']).strip()
    if i < len(renamed_files):
        photo_file = renamed_files[i]
        link_path = os.path.join(folder_path, photo_file)
        ws.append([id_val, name_val, f'=HYPERLINK("{link_path}", "{photo_file}")'])
    else:
        ws.append([id_val, name_val, "(no photo)"])

ws.column_dimensions["A"].width = 10
ws.column_dimensions["B"].width = 25
ws.column_dimensions["C"].width = 60
wb.save(excel_output)
print(f"✅ Step 4 complete: Created Excel file → {excel_output}")

# ============================================================
# STEP 5: Move Excel File to Another Folder
# ============================================================
os.makedirs(destination_folder, exist_ok=True)
dest_path = os.path.join(destination_folder, os.path.basename(excel_output))

try:
    shutil.move(excel_output, dest_path)
    print(f"📦 Step 5 complete: Moved Excel to → {dest_path}")
except Exception as e:
    print(f"⚠️ Could not move file: {e}")

print("🎯 All steps done successfully!")
