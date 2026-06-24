import requests

url = "https://www.eslite.com/exhibitions/CU202503-00091"

print("開始測試誠品...")

try:
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    html = response.text

    print("狀態碼:", response.status_code)
    print("頁面長度:", len(html))

    keywords = [
        "戰鬥陀螺",
        "BEYBLADE",
        "BX-49",
        "蒼龍突擊"
    ]

    print("\n===== 關鍵字測試 =====")

    for keyword in keywords:
        print(f"{keyword}: {keyword in html}")

except Exception as e:
    print("錯誤:", e)
