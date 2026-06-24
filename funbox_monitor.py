import requests
import re

URL = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("===== Funbox測試 =====")

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)

print("狀態碼:", response.status_code)
print("實際網址:", response.url)
print("頁面長度:", len(response.text))

html = response.text

print("\n===== 搜尋關鍵字 =====")

keywords = [
    "戰鬥陀螺",
    "BEYBLADE",
    "BX-",
    "UX-",
    "CX-"
]

for keyword in keywords:
    if keyword in html:
        print(f"✅ {keyword}")
    else:
        print(f"❌ {keyword}")

print("\n===== 商品連結測試 =====")

links = re.findall(
    r'href="(/products/[^"]+)"',
    html
)

links = list(set(links))

print("找到商品連結數:", len(links))

for link in links[:20]:
    print(link)

printprint("\n===== HTML前1000字 =====")
print(html[:1000])

print("\n===== 搜尋 products =====")
print("products 出現次數:", html.count("/products/"))

index = html.find("/products/")

if index != -1:
    print("\n===== products附近內容 =====")
    print(html[index-500:index+1500])
else:
    print("找不到 /products/")
