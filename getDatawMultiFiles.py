import pandas as pd
from pathlib import Path
import json

IN_DIR = Path(r"d:\testApp\testMultipleFiles")
EXT_TO_ENGINE = {".xls": "xlrd", ".xlsx": "openpyxl", ".xlsm": "openpyxl"}
combined = {}

for file in sorted(IN_DIR.iterdir()):
    if file.suffix.lower() not in EXT_TO_ENGINE:
        continue
    engine = EXT_TO_ENGINE[file.suffix.lower()]
    try:
        df = pd.read_excel(file, engine=engine)
    except ImportError as ie:
        print(f"Missing engine '{engine}' for {file.name}. Install with: pip install {engine}")
        continue
    except Exception as e:
        print(f"Failed to read {file.name}: {e}")
        continue

    # drop rows that are entirely empty
    df = df.dropna(how="all")
    # convert remaining NaN to None for JSON, then remove keys with None values
    df_none = df.where(pd.notnull(df), None)
    rows = df_none.to_dict(orient="records")
    rows_clean = [{k: v for k, v in rec.items() if v is not None} for rec in rows]

    out_clean = file.with_suffix(".clean.json")
    with open(out_clean, "w", encoding="utf-8") as f:
        json.dump(rows_clean, f, ensure_ascii=False, indent=2)

    # remove original plain .json if it exists (keep only .clean.json)
    original_json = file.with_suffix(".json")
    if original_json.exists():
        try:
            original_json.unlink()
            print(f"Removed original JSON: {original_json.name}")
        except Exception as e:
            print(f"Failed to remove {original_json.name}: {e}")

    combined[file.name] = rows_clean
    print(f"Wrote {out_clean} ({len(rows_clean)} rows)")

# write combined output for all processed files
if combined:
    out_all = IN_DIR / "all_files.clean.json"
    with open(out_all, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"Wrote combined JSON: {out_all}")

    # remove any old combined plain JSON if present
    old_all = IN_DIR / "all_files.json"
    if old_all.exists():
        try:
            old_all.unlink()
            print(f"Removed old combined JSON: {old_all.name}")
        except Exception as e:
            print(f"Failed to remove {old_all.name}: {e}")
else:
    print("No files were processed.")