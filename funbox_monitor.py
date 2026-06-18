import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

urls = [
    "https://shop.funbox.com.tw/collections/XIKBXA",
    "https://shop.funbox.com.tw/collections/XIKBXB",
    "https://shop.funbox.com.tw/collections/XIKBXC",
    "https://shop.funbox.com.tw/collections/XIKBXD",
    "https://shop.funbox.com.tw/collections/XIKBXP",
    "https://shop.funbox.com.tw/collections/KB2X"
]

for url in urls:
    print("\n======================")
    print(url)

    r = requests.get(url, headers=headers, timeout=30)

    print("狀態碼:", r.status_code)

    html = r.text

    keywords = ["BX-", "UX-", "CX-", "/products/"]

    for k in keywords:
        print(
            f"{k}:",
            "✅" if k in html else "❌"
        )
