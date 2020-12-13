import os
import discord
import re
import requests
from datetime import datetime
from dhooks import Webhook, Embed

hook = Webhook(os.environ.get('BOT_HOOK'))

api = os.environ.get('BOT_TOKEN')

HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"}

client = discord.Client()



def create_url():
    now = datetime.now().strftime("%d" + "." + "%m" + "." + "%Y")
    URL = "https://www.sberbank.ru/portalserver/proxy/?pipe=shortCachePipe&url=http%3A%2F%2Flocalhost%2Frates-web%2FrateService%2Frate%2Fcurrent%3FregionId%3D77%26rateCategory%3Dcards%26currencyCode%3D978%26date%3D" + now + "%2023%3A59%3A59"
    return URL


def get_html(url, params=""):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def parse_course():
    html = get_html(create_url())
    if html.status_code == 200:
        k = html.text.split(":")
        z = k[11].split(",")
        return float(z[0])
    else:
        print("Error")

def convert_in_rub(cost):
    cost *= parse_course()
    cost = ("%.2f" % cost)
    return cost

def create_price(price):
    postage = 36.0
    price_with_vat = price * 0.83333333333
    if price_with_vat < 200.0:
        order_total = price_with_vat + (postage * 0.83333333333)
        vat = order_total - (price + postage)
        info = ("🛒 Сумма корзины: " + str(
            convert_in_rub(price)) + "р." + "\n" + "💶 Вычет Vat: " + str(
            convert_in_rub(vat)) + "р." + "\n" + "📦 Доставка: " + str(
            convert_in_rub(postage)) + "\n" + "💳 Общая сумма заказа: " + str(convert_in_rub(order_total)) + "р.")

    elif price_with_vat > 200.0:
        vat = price_with_vat - price
        nalog = price_with_vat - 200.0
        nalog *= 0.15
        order_total = price_with_vat + nalog
        info = ("🛒 Сумма корзины: " + str(
            convert_in_rub(price)) + "р." + "\n" + "💶 Вычет Vat: " + str(
            convert_in_rub(vat)) + "р." + "\n" + "🇷🇺 Налог РФ: " + str(
            float(convert_in_rub(nalog)) + float(1600)) + "р." + "\n" + "💳 Общая сумма заказа: " + str(float(convert_in_rub(order_total)) + float(1600.00)) + "р.")

    return info

def create_course():
    course = "💰Текущий курс Сбербанка: 1 евро = " + str(parse_course()) + "р."
    return course


def create_atc(url):
    atc1 = ""
    atc2 = ""
    atc3 = ""
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        product_name = "Model: " + re.search('headline-5 pb3-sm[^>]+?(.+?<)', resp.text).groups()[0] + "\n" + \
                       "Color: " + re.search('headline-1 pb3-sm[^>]+?(.+?<)', resp.text).groups()[0]
        product_img = re.search('twitter:image[^>]+?content="(.+?)"', resp.text).groups()[0]

        product_id = re.search('branch:deeplink:productId[^>]+?content="([a-f0-9\-]+)".*?/>',
                               resp.text).groups()[0]

        sizes = [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15]
        for size in sizes:
            args = "productId=%s&size=%s" % (product_id, size)
            if size < 8:
                atc1 += "[" + str(size) + "]" + "(" "%s?%s" % (url, args) + ")" + "\n"
            if 8 <= size < 12:
                atc2 += "[" + str(size) + "]" + "(" "%s?%s" % (url, args) + ")" + "\n"
            if 12 <= size <= 15:
                atc3 += "[" + str(size) + "]" + "(" "%s?%s" % (url, args) + ")" + "\n"
    except:
        pass

    return product_name, product_img, atc1, atc2, atc3



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if int(message.channel.id) != 782648561031446550:
        return

    #if message.channel.id == "782648561031446550"
    #calculation function with course
    if message.content.startswith('$help'):
        print(message.author.id)
        await message.channel.send("Hi")

    if message.content.startswith('$calc'):
        usertxt = message.content.split(" ")

        try:
            if usertxt[1] == "c":
                await message.channel.send(create_course())
            else:
                price = float(usertxt[1])
                await message.channel.send(create_price(price))
        except:
            await message.channel.send('Неправильно задана команда или параметр!')

    if message.content.startswith('$atc'):
        try:
            usertxt = message.content.split(" ")
            link = usertxt[1]
            product_info = create_atc(link)
            embed = Embed(
                description='Your **ATC** is created! :smiley:',
                color=0x5CDBF0,
                timestamp='now')  # sets the timestamp to current time
            image1 = product_info[1]
            embed.set_author(name=product_info[0])
            embed.add_field(name='ATC', value=product_info[2])
            print(product_info[2])
            embed.add_field(name='ATC', value=product_info[3])
            embed.add_field(name='ATC', value=product_info[4])
            embed.set_footer(text='Suck AIO v1.0')
            embed.set_thumbnail(image1)
            hook.send(embed=embed)
        except:
            await message.channel.send("Неправильно задана команда или параметр!")


client.run(api)
