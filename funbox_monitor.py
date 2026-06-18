import requests
import re

url = "https://shop.funbox.com.tw/collections/戰鬥陀螺"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

products = re.findall(
    r'href="(/products/[^"]+)".*?data-name="([^"]+)"',
    html,
    re.S
)

print("商品數量:", len(products))
print()

for link, name in products:
    print(name)
    print(link)
    print("-" * 50)
