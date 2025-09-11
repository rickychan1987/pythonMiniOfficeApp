import os

# Set working directory
base_dir = os.getcwd()   # or change to a specific path
os.makedirs(base_dir, exist_ok=True)

# How many sets of files you want
start, end = 1, 10   # HNVN001 ... HNVN010

for i in range(start, end + 1):
    name = f"HNVN{i:03d}"  # HNVN001, HNVN002, ...
    
    # Define filenames
    txt_file = os.path.join(base_dir, f"{name}.txt")
    csv_file = os.path.join(base_dir, f"{name}.csv")
    
    # Write test content
    with open(txt_file, "w") as f:
        f.write(f"This is a test TXT file for {name}\n")
    
    with open(csv_file, "w") as f:
        f.write("id,name\n")
        f.write(f"{i},{name}\n")

print(f"Created TXT and CSV files from HNVN{start:03d} to HNVN{end:03d} in {base_dir}")
