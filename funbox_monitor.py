import requests
import re
import json
import os

URL = "https://shop.funbox.com.tw/collections/beyblade-x"

def send_line_message(message):
    token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    user_id = os.getenv("LINE_USER_ID")

    if not token:
        print("❌ 找不到 LINE_CHANNEL_ACCESS_TOKEN")
        return

    if not user_id:
        print("❌ 找不到 LINE_USER_ID")
        return

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    try:
        r = requests.post(
            "https://api.line.me/v2/bot/message/push",
            headers=headers,
            json=payload,
            timeout=30
        )

        print("LINE推播狀態:", r.status_code)

        if r.status_code != 200:
            print(r.text)

    except Exception as e:
        print("LINE推播失敗:", e)

print("目前目錄:", os.getcwd())
print("products.json存在:", os.path.exists("products.json"))
print("=" * 50)

# 抓取網頁
response = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = response.text

print("HTTP狀態碼:", response.status_code)
print("HTML長度:", len(html))
print("=" * 50)

# 新增除錯資訊
print("HTML前3000字:")
print(html[:3000])
print("=" * 50)

# 抓商品
matches = re.findall(
    r'href="(/products/[^"]+)".*?data-name="(.*?)"',
    html,
    re.S
)

products = {}

for link, name in matches:
    products[link] = name

print("目前商品數:", len(products))
print("=" * 50)

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

        name = products[link]

        if not re.search(r"(BX-|UX-|CX-)", name):
            print("跳過非相關商品:", name)
            continue

        full_url = f"https://shop.funbox.com.tw{link}"

        print(name)
        print(full_url)
        print("-" * 50)

        message = (
            f"🚨 Funbox 發現新品！\n\n"
            f"{name}\n\n"
            f"{full_url}"
        )

        send_line_message(message)

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

print("\nproducts.json 已更新")
