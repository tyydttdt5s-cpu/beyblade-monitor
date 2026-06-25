import requests

url = "https://shop.funbox.com.tw/collections/beyblade-x"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = response.text

index = html.find("/products/")

print("位置:", index)

if index != -1:
    start = max(0, index - 300)
    end = index + 500
    print(html[start:end])
