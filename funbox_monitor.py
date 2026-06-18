import requests

url = "https://shop.funbox.com.tw/collections/戰鬥陀螺"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

idx = html.find("/products/")

print("位置:", idx)

if idx != -1:
    print(html[idx-500:idx+1500])
else:
    print("找不到 /products/")
