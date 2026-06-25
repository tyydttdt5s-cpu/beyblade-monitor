import requests
import re

url = "https://shop.funbox.com.tw/collections/beyblade-x"

html = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
).text

for keyword in [
    "__INITIAL_STATE__",
    "__NUXT__",
    "window.__",
    "collections",
    "products",
    "variants",
    "inventory"
]:
    pos = html.find(keyword)
    print(keyword, "=>", pos)
