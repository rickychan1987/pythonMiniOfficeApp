import pandas as pd
from pathlib import Path

out = Path(r"d:\testApp\dummy.xlsx")
df = pd.DataFrame(
    [
        {"ID": 1, "Name": "Alice", "Age": 30},
        {"ID": 2, "Name": "Bob", "Age": 25},
        {"ID": 3, "Name": "Charlie", "Age": 40},
    ]
)
df.to_excel(out, index=False)
print("Wrote", out)
