from pathlib import Path
import pandas as pd

# Get current directory
current_dir = Path.cwd()

# Find all PDF files
pdf_files = list(current_dir.glob("*.pdf"))

# Process file names: remove .pdf and split by space
split_data = [pdf.stem.split() for pdf in pdf_files]

# Convert to DataFrame
df = pd.DataFrame(split_data)

# Optional: add column names
df.columns = [f"Part_{i+1}" for i in range(df.shape[1])]

# Export to Excel
output_file = current_dir / "pdf_names.xlsx"
df.to_excel(output_file, index=False)

print(f"Found {len(pdf_files)} PDF files.")
print(f"Saved Excel file to: {output_file}")