import requests
import re

url = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

for key in ["KB2X", "UX-", "category", "collection"]:
    idx = html.find(key)

    print("\n====================")
    print(key)

    if idx == -1:
        print("找不到")
        continue

    start = max(0, idx - 500)
    end = idx + 1500

    print(html[start:end])
