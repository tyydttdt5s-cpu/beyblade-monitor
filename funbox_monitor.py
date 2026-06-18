import requests

url = "https://shop.funbox.com.tw/categories/takara-tomy"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("狀態碼:", response.status_code)

html = response.text

keywords = [
    "BX-49",
    "蒼龍突擊",
    "蒼龍",
]

print("\n開始搜尋商品...\n")

found = False

for keyword in keywords:
    if keyword in html:
        print(f"✅ 找到商品：{keyword}")
        found = True
    else:
        print(f"❌ 沒找到：{keyword}")

if found:
    print("\n🎉 商品可能已出現在頁面中")
else:
    print("\n⚠️ 頁面中找不到商品關鍵字")
