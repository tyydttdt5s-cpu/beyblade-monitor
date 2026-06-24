import requests
import re

URL = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("===== Funbox測試 =====")

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)

html = response.text

print("狀態碼:", response.status_code)
print("實際網址:", response.url)
print("頁面長度:", len(html))

print("\n===== 搜尋關鍵字 =====")

keywords = [
    "戰鬥陀螺",
    "BEYBLADE",
    "BX-",
    "UX-",
    "CX-",
    "/products/",
    "product",
    "products"
]

for keyword in keywords:
    count = html.count(keyword)
    print(f"{keyword}: {count}")

print("\n===== 搜尋 /products/ =====")

matches = re.findall(
    r'/products/[^"\']+',
    html
)

matches = list(set(matches))

print("找到數量:", len(matches))

for item in matches[:50]:
    print(item)

print("\n===== 搜尋 BX =====")

bx_matches = re.findall(
    r'BX-\d+',
    html
)

bx_matches = list(set(bx_matches))

print("BX數量:", len(bx_matches))

for item in sorted(bx_matches):
    print(item)

print("\n===== 搜尋 UX =====")

ux_matches = re.findall(
    r'UX-\d+',
    html
)

ux_matches = list(set(ux_matches))

print("UX數量:", len(ux_matches))

for item in sorted(ux_matches):
    print(item)

print("\n===== 搜尋 JSON =====")

json_patterns = [
    "__NEXT_DATA__",
    "__NUXT__",
    "products",
    "Product",
    "product",
    "api"
]

for p in json_patterns:
    print(f"{p}: {html.count(p)}")

print("\n===== HTML前3000字 =====")
print(html[:3000])
