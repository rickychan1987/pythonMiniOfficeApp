import random
from pathlib import Path
import pandas as pd

random.seed(42)  # reproducible output

first_names = [
    "Alice","Bob","Charlie","David","Eva","Fiona","George","Hannah","Ian","Julia",
    "Kevin","Laura","Mike","Nina","Oliver","Paula","Quinn","Rachel","Sam","Tina",
    "Uma","Victor","Wendy","Xander","Yara","Zoe"
]
last_names = [
    "Smith","Johnson","Williams","Brown","Jones","Miller","Davis","Garcia","Rodriguez",
    "Wilson","Martinez","Anderson","Taylor","Thomas","Hernandez","Moore","Martin",
    "Jackson","Thompson","White"
]

rows = []
for i in range(1, 301):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 80)
    rows.append({"ID": i, "Name": name, "Age": age})

df = pd.DataFrame(rows)
out = Path(r"d:\testApp\dummy_300.xlsx")
df.to_excel(out, index=False)
print("Wrote", out)