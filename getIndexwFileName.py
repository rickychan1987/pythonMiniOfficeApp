from pathlib import Path
import argparse
import re
from typing import List, Tuple

ID_RE = re.compile(r'---\s*(\d+)')

def list_files(directory: Path, exts: List[str] | None = None) -> List[Path]:
    files = [p for p in directory.iterdir() if p.is_file()]
    if exts:
        exts_norm = {e if e.startswith('.') else f'.{e}' for e in exts}
        files = [p for p in files if p.suffix.lower() in exts_norm]
    return sorted(files, key=lambda p: p.name)

def extract_id(name: str) -> str | None:
    m = ID_RE.search(name)
    return m.group(1) if m else None

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Print 0-based index and numeric ID after '---' from filenames.")
    ap.add_argument("dir", nargs="?", default=r"d:\testApp\testMultipleFiles", help="Directory to scan")
    ap.add_argument("--ext", "-e", nargs="*", help="Optional extensions to include (e.g. xls xlsx)")
    ap.add_argument("--out", "-o", help="Output text file (one line per file: index: id). If omitted writes indexes.txt in the directory.")
    args = ap.parse_args()

    dir_path = Path(args.dir)
    files = list_files(dir_path, exts=args.ext)

    lines: List[str] = []
    for idx, p in enumerate(files):
        id_part = extract_id(p.name)
        # skip files that don't contain an ID (ignore None)
        if id_part is None:
            continue
        # write only index and the extracted numeric id (no 'None' entries)
        line = f"{idx}: {id_part}"
        print(line)
        lines.append(line)

    # decide output path
    out_path = Path(args.out) if args.out else dir_path / "indexes.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote results to {out_path}")
# filepath: d:\testApp\testMultipleFiles\getIndexwFileName.py
from pathlib import Path
import argparse
import re
from typing import List, Tuple

ID_RE = re.compile(r'---\s*(\d+)') #

def list_files(directory: Path, exts: List[str] | None = None) -> List[Path]:
    files = [p for p in directory.iterdir() if p.is_file()]
    if exts:
        exts_norm = {e if e.startswith('.') else f'.{e}' for e in exts}
        files = [p for p in files if p.suffix.lower() in exts_norm]
    return sorted(files, key=lambda p: p.name)

def extract_id(name: str) -> str | None:
    m = ID_RE.search(name)
    return m.group(1) if m else None

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Print 0-based index and numeric ID after '---' from filenames.")
    ap.add_argument("dir", nargs="?", default=r"d:\testApp\testMultipleFiles", help="Directory to scan")
    ap.add_argument("--ext", "-e", nargs="*", help="Optional extensions to include (e.g. xls xlsx)")
    ap.add_argument("--out", "-o", help="Output text file (one line per file: index: id). If omitted writes indexes.txt in the directory.")
    args = ap.parse_args()

    dir_path = Path(args.dir)
    files = list_files(dir_path, exts=args.ext)

    lines: List[str] = []
    for idx, p in enumerate(files):
        id_part = extract_id(p.name)
        if not id_part:
            continue
        # append only the numeric id (no index or colon)
        lines.append(id_part)
        print(id_part)

    out_path = Path(args.out) if args.out else dir_path / "indexes.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path} ({len(lines)} ids)")
# ...existing code...
# filepath: d:\testApp\testMultipleFiles\getIndexwFileName.py
# ...existing code...
    lines: List[str] = []
    for idx, p in enumerate(files):
        id_part = extract_id(p.name)
        if not id_part:
            continue
        # append only the numeric id (no index or colon)
        lines.append(id_part)
        print(id_part)

    out_path = Path(args.out) if args.out else dir_path / "indexes.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path} ({len(lines)} ids)")


### This app were get 
    