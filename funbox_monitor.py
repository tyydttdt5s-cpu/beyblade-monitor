import requests

url = "https://shop.funbox.com.tw"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

with open("funbox.html", "w", encoding="utf-8") as f:
    f.write(html)

print("已輸出 funbox.html")
