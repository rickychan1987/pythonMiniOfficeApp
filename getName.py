from pathlib import Path
import re
import argparse

def write_filenames_with_dash(directory: Path, out_file: Path, ext_filter: list | None = None):
    directory = directory.expanduser()
    files = sorted(p for p in directory.iterdir() if p.is_file())
    if ext_filter:
        ext_filter = [e.lower() if e.startswith('.') else f'.{e.lower()}' for e in ext_filter]
        files = [p for p in files if p.suffix.lower() in ext_filter]

    with out_file.open('w', encoding='utf-8') as f:
        for p in files:
            f.write(f"{p.name}\n")

def parse_names_from_lines(txt_file: Path) -> list:
    """Return list of file names found after '---' in each line."""
    pattern = re.compile(r's*(.+)')
    names = []
    for line in txt_file.read_text(encoding='utf-8').splitlines():
        m = pattern.match(line)
        if m:
            names.append(m.group(1).strip())
    return names

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Write filenames prefixed with '---' and optionally parse them back.")
    ap.add_argument("dir", nargs="?", default=r"d:\testApp\testMultipleFiles", help="Directory to scan")
    ap.add_argument("--out", "-o", default=r"d:\testApp\testMultipleFiles\filenames.txt", help="Output text file")
    ap.add_argument("--ext", "-e", nargs="*", help="Optional extension filter (e.g. xls xlsx)")
    args = ap.parse_args()

    dir_path = Path(args.dir)
    out_path = Path(args.out)

    write_filenames_with_dash(dir_path, out_path, ext_filter=args.ext)
    print(f"Wrote file list to: {out_path}")

    # example: read back and print parsed names
    parsed = parse_names_from_lines(out_path)
    print(f"Parsed {len(parsed)} names (first 10):", parsed[:10])