import requests

url = "https://cdn-general.cybassets.com/s/files/11114/theme/33501/assets/js/1670494228_3d183fc4_category.js"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print("狀態碼:", r.status_code)

print("\n===== JS前10000字 =====\n")
print(r.text[:10000])
