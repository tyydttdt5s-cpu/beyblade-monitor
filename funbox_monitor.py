import requests
import re

url = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

html = r.text

print("狀態碼:", r.status_code)

print("\n===== script來源 =====\n")

scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)

for s in scripts:
    print(s)
