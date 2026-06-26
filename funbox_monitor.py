import requests
import re

url = "https://shop.funbox.com.tw/collections/beyblade-x"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

js_list = re.findall(
    r'https://cdn\.cybassets\.com[^"\']+\.js',
    html
)

keywords = [
    "/api/",
    "search",
    "product",
    "products",
    "graphql"
]

for js in js_list:

    print("=" * 80)
    print(js)

    text = requests.get(
        js,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    ).text

    lower = text.lower()

    for key in keywords:
        pos = lower.find(key.lower())

        if pos != -1:
            print(f"\n==== {key} ====")
            start = max(0, pos - 300)
            end = min(len(text), pos + 500)
            print(text[start:end])
