import requests
from dhooks import Webhook, Embed
import time
hook = Webhook("https://discord.com/api/webhooks/782830885657116672/6G7KkY2twhRA9qkdPJ575SS3m9H2vX_UUfaV00Tx3nYnsj-R3g3ijpal579PF6v7MZXp")

url = "https://www.adidas.ru/api/products/F36640/availability"
url1 = "https://www.adidas.com/yeezy"
HEADERS = {"Accept": "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}


def get_html(url, params=""):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


while True:
    html = get_html(url)
    if html.status_code == 200:
        a = html.text.split(",")
        a = a[1].split(":")
        hook.send("Status: " + str(a[1]))

    else:
        print(html.status_code)
    time.sleep(60)
