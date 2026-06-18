import requests
import re

url = "https://shop.funbox.com.tw/collections/戰鬥陀螺"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=30
).text

models = sorted(set(
    re.findall(r'(?:BX|UX|CX)-\d+', html)
))

print(models)
