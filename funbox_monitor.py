import requests

url = "https://shop.funbox.com.tw/categories/takaratomy/beyblade"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

print("狀態碼:", response.status_code)
print(response.text[:1000])
