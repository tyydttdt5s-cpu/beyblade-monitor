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

print("實際網址:")
print(response.url)

print()
print("標題附近:")
print(html[:2000])
