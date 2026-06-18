import requests
import re

url = "https://shop.funbox.com.tw/products/bbpr09652"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

matches = re.findall(
    r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
    html,
    re.DOTALL
)

if matches:
    print(matches[0][:5000])
else:
    print("找不到 JSON")
