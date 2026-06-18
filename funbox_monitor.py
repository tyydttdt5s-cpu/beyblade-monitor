import requests
import re

url = "https://shop.funbox.com.tw/products/bbpr09652"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

# 抓所有 js 檔
js_files = re.findall(
    r'<script[^>]+src="([^"]+\.js[^"]*)"',
    html
)

print("JS數量:", len(js_files))

for js in js_files[:50]:
    print(js)
