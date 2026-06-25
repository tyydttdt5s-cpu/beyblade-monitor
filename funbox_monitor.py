import requests
import re

url = "https://shop.funbox.com.tw/collections/beyblade-x"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

apis = re.findall(
    r'https://[^"\']+',
    html
)

for api in apis:
    if "api" in api.lower():
        print(api)
