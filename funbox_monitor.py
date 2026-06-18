import requests
import re

url = "https://shop.funbox.com.tw/products/bbpr09652"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

print("script 數量:", html.count("<script"))

matches = re.findall(
    r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
    html,
    re.DOTALL
)

print("JSON-LD 數量:", len(matches))

for i, m in enumerate(matches[:5]):
    print(f"\n===== JSON {i+1} =====")
    print(m[:1000])
