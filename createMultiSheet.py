from openpyxl import Workbook
from pathlib import Path

out = Path(r"d:\testApp\multi_sheet.xlsx")
wb = Workbook()

# Sheet1 with numeric data and a formula
ws1 = wb.active
ws1.title = "Sheet1"
ws1.append(["ID", "Name", "Age"])
ws1.append([1, "Alice", 30])
ws1.append([2, "Bob", 25])
ws1.append([3, "Charlie", 40])
# put average formula in C6 (leave a blank row first)
ws1.append([None, None, None])
ws1.append([None, "Average age", None])
ws1["C6"] = "=AVERAGE(C2:C4)"

# Sheet2 with contacts
ws2 = wb.create_sheet("Contacts")
ws2.append(["Email", "Phone"])
ws2.append(["alice@example.com", "123-456"])
ws2.append(["bob@example.com", "555-010"])

wb.save(out)
print("Wrote", out)