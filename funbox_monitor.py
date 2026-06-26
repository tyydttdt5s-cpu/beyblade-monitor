import requests
import re

url = "https://shop.funbox.com.tw/collections/beyblade-x"

html = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
).text

matches = re.findall(
    r'https://[^"\']+',
    html
)

for m in matches:
    if "api" in m.lower():
        print(m)
