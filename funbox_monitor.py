import requests

url = "https://shop.funbox.com.tw/products/bbpr09652"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

for key in [
    "KB2X",
    "XIKBXA",
    "XIKBXB",
    "XIKBXC",
    "XIKBXD",
    "collections",
    "category"
]:
    print(key, html.count(key))
