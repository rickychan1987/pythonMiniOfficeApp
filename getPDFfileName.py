from pathlib import Path

# Get current directory
current_dir = Path.cwd()

# Find all PDF files
pdf_files = list(current_dir.glob("*.pdf"))

# Export to text file
output_file = current_dir / "get_name_of_pdf.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for pdf in pdf_files:
        f.write(pdf.name + "\n")

print(f"Found {len(pdf_files)} PDF files.")
print(f"Saved names to: {output_file}")
