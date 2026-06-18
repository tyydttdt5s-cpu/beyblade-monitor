import requests
import re
import json
import os

URL = "https://shop.funbox.com.tw/collections/戰鬥陀螺"

print("目前目錄:", os.getcwd())
print("products.json存在:", os.path.exists("products.json"))
print("-" * 50)

# 抓取頁面
html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

# 擷取商品
matches = re.findall(
    r'href="(/products/[^"]+)".*?data-name="([^"]+)"',
    html,
    re.S
)

# 去重
products = {}

for link, name in matches:
    products[link] = name

print("目前商品數:", len(products))
print("-" * 50)

# 讀取舊資料
if os.path.exists("products.json"):
    with open("products.json", "r", encoding="utf-8") as f:
        old_products = set(json.load(f))
else:
    old_products = set()

current_products = set(products.keys())

print("舊資料:", old_products)
print("目前資料:", current_products)

new_products = current_products - old_products

print("新品資料:", new_products)

if new_products:
    print("\n發現新品：\n")

    for link in new_products:
        print(products[link])
        print("https://shop.funbox.com.tw" + link)
        print("-" * 50)
else:
    print("沒有新品")

# 更新 products.json
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(
        list(current_products),
        f,
        ensure_ascii=False,
        indent=2
    )

print("\nproducts.json內容：")

with open("products.json", "r", encoding="utf-8") as f:
    print(f.read())
