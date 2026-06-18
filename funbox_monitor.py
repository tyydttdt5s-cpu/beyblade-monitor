import requests
import re

url = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print("狀態碼:", r.status_code)

html = r.text

print("\n===== API相關關鍵字 =====\n")

patterns = [
    "products",
    "product",
    "api",
    "graphql",
    "json",
    "__NEXT_DATA__",
    "category"
]

for p in patterns:
    if p.lower() in html.lower():
        print("✅", p)
