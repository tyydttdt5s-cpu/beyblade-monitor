import requests
import json

url = "https://shop.funbox.com.tw/categories.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print("狀態碼:", r.status_code)

try:
    data = r.json()

    print("\n===== JSON前3筆 =====\n")

    for item in data[:3]:
        print(json.dumps(item, ensure_ascii=False, indent=2))

except Exception as e:
    print("JSON解析失敗:", e)
    print(r.text[:2000])
