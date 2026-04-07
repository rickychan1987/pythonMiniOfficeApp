import os
import pandas as pd


# --- 1. Paths ---
folder_path = r"D:\Administrator\Pictures\Camera Roll\LRDG_test"
csv_file = r"D:\Administrator\Pictures\Camera Roll\LRDG_test\add_photoname.csv"

# --- 2. Read CSV file ---
df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip().str.lower()  # Normalize header names

# --- 3. Validate required columns ---
required_columns = {'id', 'name', 'photoname'}
if not required_columns.issubset(df.columns):
    print(f"⚠️ The CSV must contain columns: {required_columns}")
    print("Found columns:", df.columns.tolist())
    raise SystemExit

# --- 4. Rename photos ---
for _, row in df.iterrows():
    id_val = str(row['id']).strip()
    name_val = str(row['name']).strip().replace(" ", "_")  # safe for filenames
    photo_name = str(row['photoname']).strip()

    old_path = os.path.join(folder_path, photo_name)
    if not os.path.exists(old_path):
        print(f"❌ File not found: {photo_name}")
        continue

    # Keep original file extension
    _, ext = os.path.splitext(photo_name)

    # Build new filename: ID_Name.ext
    new_filename = f"{id_val}_{name_val}{ext}"
    new_path = os.path.join(folder_path, new_filename)

    try:
        os.rename(old_path, new_path)
        print(f"✅ Renamed: {photo_name} → {new_filename}")
    except Exception as e:
        print(f"⚠️ Error renaming {photo_name}: {e}")

print("🎯 All matching photos renamed successfully!")