import requests
import re

url = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    r = requests.get(url, headers=headers, timeout=30)

    print("狀態碼:", r.status_code)

    if r.status_code != 200:
        print("❌ 網頁讀取失敗")
        exit()

    html = r.text

    print("\n===== HTML前5000字 =====\n")
    print(html[:5000])

    print("\n===== 搜尋BX/UX/CX型號 =====\n")

    models = sorted(set(
        re.findall(r"(?:BX|UX|CX)-\d+", html, re.IGNORECASE)
    ))

    if models:
        print("找到型號：")
        for model in models:
            print("✅", model)
    else:
        print("❌ HTML中找不到 BX/UX/CX 型號")

    print("\n===== 關鍵字測試 =====\n")

    keywords = [
        "BX-49",
        "BX-35",
        "UX-01",
        "戰鬥陀螺",
        "BEYBLADE"
    ]

    for keyword in keywords:
        if keyword.lower() in html.lower():
            print(f"✅ 找到：{keyword}")
        else:
            print(f"❌ 沒找到：{keyword}")

except Exception as e:
    print("發生錯誤：", e)
