# get_data.py
# Downloads the World Bank Pink Sheet (monthly commodity prices).

import requests
import os

os.makedirs("data/raw", exist_ok=True)

URL = ("https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e"
       "-0050012026/related/CMO-Historical-Data-Monthly.xlsx")

response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=60)
with open("data/raw/CMO-Historical-Data-Monthly.xlsx", "wb") as f:
    f.write(response.content)
print("Downloaded:", len(response.content) // 1024, "KB")