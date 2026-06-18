import requests
import re

url = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

html = r.text

print("狀態碼:", r.status_code)

print("\n===== 找出含 api 的內容 =====\n")

for m in re.finditer(r".{0,150}api.{0,150}", html, re.IGNORECASE):
    print(m.group())
    print("-" * 80)

print("\n===== 找出 JSON URL =====\n")

urls = re.findall(r'https?://[^"\']+', html)

for u in urls:
    if "api" in u.lower() or "json" in u.lower():
        print(u)
