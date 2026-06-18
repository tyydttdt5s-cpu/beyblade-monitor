import requests
import re

url = "https://shop.funbox.com.tw/products/bbpr09652"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

matches = re.findall(
    r'var productData = (.*?);',
    html,
    re.DOTALL
)

print("找到:", len(matches))

if matches:
    print(matches[0][:3000])
