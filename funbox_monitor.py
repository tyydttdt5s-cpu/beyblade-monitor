import requests

url = "https://cdn-general.cybassets.com/frontend/appStoreSDK/main.99d97ccccdb618b576bb.js"

js = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

print("長度:", len(js))

for key in [
    "product",
    "products",
    "category",
    "categories",
    "search",
    "graphql",
    "collection"
]:
    print(key, js.count(key))
