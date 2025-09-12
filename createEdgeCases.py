from openpyxl import Workbook
from pathlib import Path

out = Path(r"d:\testApp\edge_cases.xlsx")
wb = Workbook()
ws = wb.active
ws.title = "EdgeCases"

# empty header row
ws.append([None, None, None])
# data rows with missing values and mixed types
ws.append([1, None, 3.14])
ws.append([None, "Text", None])
ws.append([4, 5, None])
ws.append([None, None, None])  # blank row

wb.save(out)
print("Wrote", out)