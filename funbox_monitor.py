import requests
import json

url = "https://shop.funbox.com.tw/categories.json"

r = requests.get(url)

data = r.json()

print("===== 搜尋戰鬥陀螺 =====")

text = json.dumps(data, ensure_ascii=False)

keywords = [
    "戰鬥陀螺",
    "BEYBLADE",
    "beyblade",
    "TAKARATOMY",
    "TAKARA TOMY"
]

for keyword in keywords:
    if keyword.lower() in text.lower():
        print("✅", keyword)
    else:
        print("❌", keyword)

print("\n===== 含戰鬥陀螺附近內容 =====\n")

idx = text.find("戰鬥陀螺")

if idx != -1:
    start = max(0, idx - 1000)
    end = idx + 3000
    print(text[start:end])
else:
    print("找不到戰鬥陀螺")
