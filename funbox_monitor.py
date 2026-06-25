import requests

url = "https://shop.funbox.com.tw/collections/beyblade-x"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

for keyword in [
    "collection-products",
    "product-grid",
    "products",
    "ProductGrid",
    "product-card",
    "api"
]:
    print(keyword, "=>", html.find(keyword))
