import requests
import re

url = "https://shop.funbox.com.tw"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

print("頁面長度:", len(html))

for keyword in [
    "__NEXT_DATA__",
    "__NUXT__",
    "products",
    "Product",
    "product",
    "/products/",
    "bb09726",
    "beyblade"
]:
    print(keyword, "=>", html.count(keyword))
