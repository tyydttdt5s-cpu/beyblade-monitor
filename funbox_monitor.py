import requests

url = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

print("狀態碼:", 200)

for key in [
    "/products/",
    "BBPR",
    "KB2X",
    "UX-",
    "BX-",
    "productData",
    "product"
]:
    print(key, html.count(key))
