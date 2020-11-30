import requests
from dhooks import Webhook, Embed
import time
hook = Webhook("https://discord.com/api/webhooks/782830885657116672/6G7KkY2twhRA9qkdPJ575SS3m9H2vX_UUfaV00Tx3nYnsj-R3g3ijpal579PF6v7MZXp")

url = "https://www.adidas.com/api/products/F36640/availability"
url1 = "https://www.adidas.com/yeezy"
HEADERS = {"Accept": "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
           "Coockie": "geo_ip=95.84.155.199; geo_country=RU; onesite_country=RU; AKA_A2=A; akacd_plp_prod_adidas_grayling=3784160282~rv=46~id=3ec8cb8d32d5d4e3e4b8cb1797075e9b; bm_sz=1918B7E03A6FE7E15DB1E3D50D803093~YAAQHYBtaNtOmIl1AQAAtZI6FwldkeG3fOdTXRMhccz5x2Vqqw/svhYlDCuTSDqWVAeCEQo27vdcVWojAgrC2jMY7mjRrAQeaeTlUTW9waRTLHAw3t8Ao5Enkghd7GjCMRbGxu45oFiXjQ2jfxrhKq9nPnxzNTRz6aUKHDy2EnJuBAsZK4fZTi+O+M6lutE3CSgZrz6B6tLQq+c6DR4P7VKMwCB6wTzs1T71Xj0OMFdjK7MgOSauoEP+pdVsqOXxJAFkVUQ5r+/qv3hMhvcjzKSdPEz1d8VJVPYx15iTABQ=; geo_ip=95.84.155.199; bm_mi=833F148F73A245C999CBCEC176C1FEB6~MCgBvhNROCBCjVHUxvIYDP+NcWavmG/mStVEL+FCwJO+hFdztLJ3SLpjaN9Mvn122rzemxbT1/63S7Xd9/YkAyFFJRmitGFKETnoE0TFYqur+CWwo9X08VifhsFHdOUME1GYk8Y7w6TURwpKqtDm16HFyppkSo3NpETILF3yFqd/N+phVhaHCHOo0wRNDIL4n/9s1VJdIRZmeKN3MxzKMYuuZdFxSB6mSCmpHpiovPlEJffbqwlgN/hTzQDwUotaQ+O1X2vwBUBA6x+ZGPVVqA==; __cfduid=d2850ac1e1d41699d267e865e31b11d581606707840; akacd_generic_prod_grayling_adidas=3784160639~rv=62~id=7c15c688e2b8243ef3a534ea40269135; ak_bmsc=2CCF06DB8BCC0328B04B7419BB7C1A64686D801D963500001B69C45F0C83165A~plzKx7wTfSJbdJ6YubaaFA9g23CJGlR7AO6+1lnVlhuh2K8tJ7A57HavxOD0N7Sz37W8p7sIoaEfiRuXtssm8gefM8e9pBGK7I+puUV53vX/xKJZ2BnLh3L0AHo2PByNH4kdNtgQBT4W1/WbOC1rSw0mfV9mnoFoaUExHsI3btBHdSk5YFSijFrxcrGJMjitr7ttG+R0C7SYY0aT+iqCXrPjclBPUQBgWVji9UZQQUK0NsCZBtpZVB819zrk2ylWVLxLKsRZnUx20QwG8jtrdYESLMNxL6yESYBt5iNKV+kwG3sP7MWqEr6MiZ1I6osNsuCrkSZR/kDhxTDzNThjeGeQ==; ab_decibel=a; criteo_dedupe=0; RES_TRACKINGID=43232388424870760; RES_SESSIONID=70855219424870760; ResonanceSegment=1; tmr_lvid=1a2fc9e52e9964952085c39369f34d6f; tmr_lvidTS=1606707843059; _ga=GA1.2.1841173099.1606707843; _gid=GA1.2.295865902.1606707843; _ym_uid=1606707843416335928; _ym_d=1606707843; _gcl_au=1.1.1630657166.1606707843; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; _ym_isad=1; s_cc=true; _fbp=fb.1.1606707843705.485116905; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18597%7CMCMID%7C08730294022094670477578490722713883069%7CMCAAMLH-1607312643%7C6%7CMCAAMB-1607312643%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1606715044s%7CNONE%7CMCAID%7CNONE; NujTerVZWUM68Dv=exp=1606709072~acl=%2f*~data=43344441393433363234323933413146324233303136363643373831423646414630413133333242343741343641343735414145393742383934373043454341~hmac=a667147d7c017c3dfd31f85960f021ac3dbb1ff5f64daf32150c89f0387b39a1; utag_main=v_id:017617400c3f0017482a8ea67e1b03079001b07100942$_sn:1$_se:2$_ss:0$_st:1606710274542$ses_id:1606707842112%3Bexp-session$_pn:2%3Bexp-session$ab_dc:TEST%3Bexp-1611892474556$_prevpage:BRAND%7CKANYE%20YEEZY%7CORIGINALS%7CHOME%3Bexp-1606712074578; tmr_detect=1%7C1606708474970; _abck=DBE899625FC3B15088DAF27F3C8C3756~-1~YAAQHYBtaKTGmIl1AQAAocNJFwQ1dseLX7lod7ZkPH0QnDHNscQW7T9UupzxChWN3rE51WWoYcjPO/487fs7Wy4OBqC7ws9TKdDZXS4Ygq7v0yD6BkoPoVc4B9OEiUg3L13vB5xNZmYNKWyr7p5PfuE/pIS0lF3n/atfZZqrEaO5WSffII1jK7CICBBJ+EvrboHoeHyf+Mhj6+714y+K1JaAMl7Wa+7Sy17mrytnP713e1eWkS8ttBZB35IytVY0yOciQOBfnrJyfkpPodoWNYl35G+PGlOVk4HPOiBpDVYmByPVZ+GazJPAJgSlU0iusZqPqCo7an9Rk3EI5jGipbOyv4EFZ11qKhxCsoFRWXGwFB3N61tLSnlXIZAUjTqfU1KE3ZTdjfuw4YeX3C7eA6jNfkHiD2XdGVdKsEv68BAoqPpZAniyOO5rcMkviWWvJITkJBcwJNWj~-1~-1~-1; s_pers=%20s_vnum%3D1606770000599%2526vn%253D1%7C1606770000599%3B%20pn%3D2%7C1609300474783%3B%20s_invisit%3Dtrue%7C1606710278925%3B; tmr_reqNum=9",
           "Sec-fetch-dest": "document",
           "Sec-fetch-mode": "navigate",
           "Sec-fetch-site": "none",
           "Sec-fetch-user": "?1",
           "Upgrade-insecure-requests":"1"}


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
