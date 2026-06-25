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

matches = re.findall(
    r'/products/[^"]+',
    html
)

matches = sorted(list(set(matches)))

print("商品數量:", len(matches))
print()

for item in matches:
    print(item)
