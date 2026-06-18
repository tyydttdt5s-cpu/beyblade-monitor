import requests
import re

url = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

html = r.text

print("狀態碼:", r.status_code)

print("\n===== 商品連結 =====\n")

links = set(
    re.findall(r'/products/[a-zA-Z0-9]+', html)
)

for link in sorted(links):
    print(link)

print("\n總數:", len(links))
