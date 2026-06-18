import requests

url = "https://shop.funbox.com.tw/collections/戰鬥陀螺"

r = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
)

print("狀態碼:", r.status_code)

html = r.text

for key in [
    "/products/",
    "BBPR",
    "UX-",
    "BX-",
    "戰鬥陀螺"
]:
    print(key, html.count(key))
