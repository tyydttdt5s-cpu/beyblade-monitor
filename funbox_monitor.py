import requests

url = "https://shop.funbox.com.tw/products/bbpr09652"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

print("狀態碼:", 200)

keywords = [
    "__NEXT_DATA__",
    "__NUXT__",
    "product",
    "variants",
    "product_id",
    "graphql",
    "api"
]

for k in keywords:
    print(k, "✅" if k in html else "❌")

print("\n===== 前3000字 =====\n")
print(html[:3000])
