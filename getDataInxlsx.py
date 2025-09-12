# import pandas as pd
# from pathlib import Path

# file = Path(r"d:\testApp\thongquanData.xls")
# df = pd.read_excel(file)  # uses first row as header by default

# for i, row in df.iterrows():
#     # i is the DataFrame index (usually starts at 0). show 1-based index with i+1:
#     print(f"{i+1}: {row.to_dict()}")



# # Below is the improved version with error handling and JSON output
# import pandas as pd
# from pathlib import Path
# import json

# file = Path(r"d:\testApp\thongquanData.xls")

# # choose engine by extension (install xlrd for .xls, openpyxl for .xlsx)
# ext = file.suffix.lower()
# engine = "xlrd" if ext == ".xls" else "openpyxl"

# try:
#     df = pd.read_excel(file, engine=engine)  # uses first row as header by default
# except ImportError as e:
#     raise ImportError(f"Missing engine '{engine}'. Install with: pip install {engine}") from e

# # convert to list of dicts (one dict per row)
# rows_list = df.to_dict(orient="records")

# # print count and first 20 rows for quick inspection
# print(f"Total rows: {len(rows_list)}")
# for i, row in enumerate(rows_list[:20], start=1):
#     print(f"{i}: {row}")

# # save full list to JSON for easier viewing/editing
# out = file.with_suffix(".json")
# with open(out, "w", encoding="utf-8") as f:
#     json.dump(rows_list, f, ensure_ascii=False, indent=2)
# print("Wrote JSON:", out)


# # ...existing code...
# import pandas as pd
# from pathlib import Path
# import json

# file = Path(r"d:\testApp\thongquanData.xls")

# # choose engine by extension (install xlrd for .xls, openpyxl for .xlsx)
# ext = file.suffix.lower()
# engine = "xlrd" if ext == ".xls" else "openpyxl"

# try:
#     df = pd.read_excel(file, engine=engine)  # uses first row as header by default
# except ImportError as e:
#     raise ImportError(f"Missing engine '{engine}'. Install with: pip install {engine}") from e

# # convert to list of dicts (one dict per row)
# rows_list = df.to_dict(orient="records")

# # print total and a preview (first 50 rows)
# print(f"Total rows: {len(rows_list)}")
# for i, row in enumerate(rows_list[:50], start=1):
#     print(f"{i}: {row}")

# # save full list to JSON for easier viewing/editing
# out = file.with_suffix(".json")
# with open(out, "w", encoding="utf-8") as f:
#     json.dump(rows_list, f, ensure_ascii=False, indent=2)
# print("Wrote JSON:", out)

import pandas as pd
from pathlib import Path
import json

file = Path(r"d:\testApp\thongquanData.xls")

# choose engine by extension (install xlrd for .xls, openpyxl for .xlsx)
ext = file.suffix.lower()
engine = "xlrd" if ext == ".xls" else "openpyxl"

try:
    df = pd.read_excel(file, engine=engine)  # uses first row as header by default
except ImportError as e:
    raise ImportError(f"Missing engine '{engine}'. Install with: pip install {engine}") from e

print("Original rows:", len(df))

# Option 1: replace NaN with None (JSON will use null)
df_none = df.where(pd.notnull(df), None)
rows_list = df_none.to_dict(orient="records")

out = file.with_suffix(".json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(rows_list, f, ensure_ascii=False, indent=2)
print("Wrote JSON with nulls:", out)

# Option 2: remove keys that are null (so keys with NaN/null are omitted)
rows_clean = [{k: v for k, v in rec.items() if v is not None} for rec in rows_list]

out_clean = file.with_suffix(".clean.json")
with open(out_clean, "w", encoding="utf-8") as f:
    json.dump(rows_clean, f, ensure_ascii=False, indent=2)
print("Wrote cleaned JSON (no null keys):", out_clean)

