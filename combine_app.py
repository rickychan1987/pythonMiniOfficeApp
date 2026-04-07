import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

# --- CONFIGURATION ---
folder_path = r"D:\Administrator\Pictures\Camera Roll\LRDG"
output_txt = os.path.join(folder_path, "LRDG_photo_list.txt")
csv_file = os.path.join(folder_path, "dg_list.csv")
output_csv = os.path.join(folder_path, "add_photoname.csv")
photo_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.heic', '.tiff'}

# ============================================================
# STEP 1: GET PHOTO NAMES AND EXPORT TO TXT
# ============================================================
photo_files = [f for f in os.listdir(folder_path)
               if os.path.splitext(f)[1].lower() in photo_extensions]

with open(output_txt, 'w', encoding='utf-8') as f:
    for filename in photo_files:
        f.write(filename + '\n')

print(f"✅ Step 1 complete: Photo names exported to {output_txt}")

# ============================================================
# STEP 2: READ CSV AND APPEND PHOTO NAMES AS NEW COLUMN
# ============================================================
df = pd.read_csv(csv_file)
with open(output_txt, 'r', encoding='utf-8') as f:
    photo_list = [line.strip() for line in f if line.strip()]

# Pad list if needed
while len(photo_list) < len(df):
    photo_list.append("(no photo name)")

df["PhotoName"] = photo_list[:len(df)]
df.to_csv(output_csv, index=False, encoding='utf-8-sig')
print(f"✅ Step 2 complete: Added 'PhotoName' column to {output_csv}")

# ============================================================
# STEP 3: RENAME PHOTOS USING ID + NAME FROM UPDATED CSV
# ============================================================
df = pd.read_csv(output_csv)
df.columns = df.columns.str.strip().str.lower()

required_columns = {'id', 'name', 'photoname'}
if not required_columns.issubset(df.columns):
    print(f"⚠️ CSV must contain columns: {required_columns}")
    print("Found columns:", df.columns.tolist())
    raise SystemExit

for _, row in df.iterrows():
    id_val = str(row['id']).strip()
    name_val = str(row['name']).strip().replace(" ", "_")  # safe for filenames
    photo_name = str(row['photoname']).strip()

    old_path = os.path.join(folder_path, photo_name)
    if not os.path.exists(old_path):
        print(f"❌ File not found: {photo_name}")
        continue

    _, ext = os.path.splitext(photo_name)
    new_filename = f"{id_val}_{name_val}{ext}"
    new_path = os.path.join(folder_path, new_filename)

    try:
        os.rename(old_path, new_path)
        print(f"✅ Renamed: {photo_name} → {new_filename}")
    except Exception as e:
        print(f"⚠️ Error renaming {photo_name}: {e}")

print("🎯 All steps complete — photos renamed successfully!")

# ============================================================
# STEP 4: CREATE EXCEL FILE WITH PHOTO LINKS
# ============================================================

excel_output = os.path.join(folder_path, "photo_links.xlsx")

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Photo Links"

# Headers
ws.append(["ID", "Name", "Photo Link"])

# Make header bold
for cell in ws[1]:
    cell.font = Font(bold=True)

# Read the updated CSV (after renaming)
for _, row in df.iterrows():
    id_val = str(row['id']).strip()
    name_val = str(row['name']).strip()
    # Recreate the new photo name
    safe_name = name_val.replace(" ", "_")
    photo_filename = f"{id_val}_{safe_name}"
    
    # Find the correct file extension in the folder
    matched_file = None
    for ext in photo_extensions:
        possible_path = os.path.join(folder_path, photo_filename + ext)
        if os.path.exists(possible_path):
            matched_file = os.path.basename(possible_path)
            break

    if matched_file:
        link_path = os.path.join(folder_path, matched_file)
        ws.append([id_val, name_val, f'=HYPERLINK("{link_path}", "{matched_file}")'])
    else:
        ws.append([id_val, name_val, "(no photo found)"])

# Adjust column widths for readability
ws.column_dimensions["A"].width = 10
ws.column_dimensions["B"].width = 25
ws.column_dimensions["C"].width = 60

# Save Excel file
wb.save(excel_output)
print(f"✅ Step 4 complete: Created Excel file with photo links → {excel_output}")