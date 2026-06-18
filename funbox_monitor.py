import requests
import re

url = "https://shop.funbox.com.tw/collections/戰鬥陀螺"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

links = sorted(set(
    re.findall(r'/products/[^"\']+', html)
))

print("找到", len(links), "個商品連結\n")

for link in links:
    print(link)
