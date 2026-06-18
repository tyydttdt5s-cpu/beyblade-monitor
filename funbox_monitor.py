import requests
import re

url = "https://shop.funbox.com.tw/products/bbpr09652"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

patterns = [
    "68051695",
    "BBPR09652",
    "products/",
    "productId",
    "api",
    "graphql"
]

for p in patterns:
    print(f"\n===== {p} =====")

    idx = html.find(p)

    if idx == -1:
        print("找不到")
        continue

    start = max(0, idx - 300)
    end = idx + 1000

    print(html[start:end])
