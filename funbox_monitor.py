import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

urls = [
    "https://shop.funbox.com.tw/products.json",
    "https://shop.funbox.com.tw/api/products",
    "https://shop.funbox.com.tw/api/products.json",
    "https://shop.funbox.com.tw/api/v1/products",
]

for url in urls:
    try:
        r = requests.get(url, headers=headers, timeout=20)

        print("\n=================")
        print(url)
        print("狀態碼:", r.status_code)

        print(r.text[:500])

    except Exception as e:
        print(url, e)
