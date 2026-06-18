import requests

urls = [
    "https://shop.funbox.com.tw/collections/XIKBXA",
    "https://shop.funbox.com.tw/collections/XIKBXB",
    "https://shop.funbox.com.tw/collections/XIKBXC",
    "https://shop.funbox.com.tw/collections/XIKBXD",
    "https://shop.funbox.com.tw/collections/XIKBXP",
    "https://shop.funbox.com.tw/collections/KB2X"
]

for url in urls:
    r = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0"
    })

    print()
    print("=" * 60)
    print(url)
    print("狀態碼:", r.status_code)

    html = r.text

    if "BX-" in html:
        print("✅ 發現 BX")
    if "UX-" in html:
        print("✅ 發現 UX")
    if "CX-" in html:
        print("✅ 發現 CX")

    print("HTML長度:", len(html))
