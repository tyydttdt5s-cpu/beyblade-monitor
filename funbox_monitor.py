import requests
import re

url = "https://shop.funbox.com.tw/collections/beyblade-x"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

js = re.findall(
    r'https://cdn\.cybassets\.com[^"\']+\.js',
    html
)

for j in js:
    print("="*80)
    print(j)

    text = requests.get(
        j,
        headers={"User-Agent":"Mozilla/5.0"},
        timeout=30
    ).text

    for word in [
        "graphql",
        "products",
        "product",
        "collection",
        "inventory",
        "variants",
        "/api/",
        "search"
    ]:

        if word in text.lower():
            print("找到：", word)
