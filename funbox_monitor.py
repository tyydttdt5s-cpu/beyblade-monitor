import requests
import re

url = "https://shop.funbox.com.tw/collections/beyblade-x"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = response.text

print("頁面長度:", len(html))

matches = re.findall(
    r'/products/[a-zA-Z0-9\-_]+',
    html
)

matches = sorted(set(matches))

print("商品數量:", len(matches))
print()

for item in matches:
    print(item)
