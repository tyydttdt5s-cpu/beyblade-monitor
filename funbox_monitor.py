import requests

url = "https://shop.funbox.com.tw/collections/beyblade-x"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

index = html.find("api")

print("api 位置:", index)

if index != -1:
    start = max(0, index - 500)
    end = index + 1500
    print(html[start:end])
