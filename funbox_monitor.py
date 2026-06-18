import requests
import re
import json
import os

URL = "https://shop.funbox.com.tw/collections/戰鬥陀螺"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

matches = re.findall(
    r'href="(/products/[^"]+)".*?data-name="([^"]+)"',
    html,
    re.S
)

products = {}

for link, name in matches:
    products[link] = name

print("目前商品數:", len(products))

# 讀取舊資料
if os.path.exists("products.json"):
    with open("products.json", "r", encoding="utf-8") as f:
        old_products = set(json.load(f))
else:
    old_products = set()

current_products = set(products.keys())

new_products = current_products - old_products

if new_products:
    print("\n發現新品：\n")

    for link in new_products:
        print(products[link])
        print("https://shop.funbox.com.tw" + link)
        print("-" * 50)

else:
    print("沒有新品")

# 更新資料庫
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(
        list(current_products),
        f,
        ensure_ascii=False,
        indent=2
    )
