import requests
from datetime import datetime
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}

token = "49538c4d13af14cd3a35864f1a470a23430395edcdf87ad7d3f065f98c19690e95ebbae21407bd02b240a"
groupsession = "106569786"
vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, groupsession)
vk = vk_session.get_api()

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
        info = ("Сумма корзины: " + str(
            convert_in_rub(price)) + "р." + "\n" + "Вычет Vat: " + str(
            convert_in_rub(vat)) + "р." + "\n" + "Доставка: " + str(
            convert_in_rub(postage)) + "\n" + "Общаяя сумма заказа: " + str(convert_in_rub(order_total)) + "р.")

    elif price_with_vat > 200.0:
        vat = price_with_vat - price
        nalog = price_with_vat - 200.0
        nalog *= 0.15
        order_total = price_with_vat + nalog
        info = ("Сумма корзины: " + str(
            convert_in_rub(price)) + "р." + "\n" + "Вычет Vat: " + str(
            convert_in_rub(vat)) + "р." + "\n" + "Налог Рф: " + str(
            convert_in_rub(nalog)) + "р." + "\n" + "Общаяя сумма заказа: " + str(convert_in_rub(order_total)) + "р.")

    return info

def create_course():
    course = "Текущий курс Сбербанка: 1 евро = " + str(parse_course()) + "р."
    return course

def create_keyboard(id, message):
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button("Калькулятор", color=VkKeyboardColor.POSITIVE)
    vk.messages.send(user_id=id, random_id=0, keyboard=keyboard.get_keyboard(), message=message)

def create_calc(id):
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button("Курс", color=VkKeyboardColor.SECONDARY)
    keyboard.add_button("Выход", color=VkKeyboardColor.NEGATIVE)
    vk.messages.send(user_id=id, random_id=0, keyboard=keyboard.get_keyboard(), message="Чтобы расчитать стоимость покупки в рублях введите стоимость товара в евро.")
    while True:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.object.text.lower()
                user = event.object.from_id
                if text == "курс":
                    vk.messages.send(user_id=user, random_id=0, message=create_course())

                elif text == "выход":
                    create_keyboard(user, "Выхожу....")
                    return

                else:
                    try:
                        count = float(text)
                        vk.messages.send(user_id=user, random_id=0, message=create_price(count))
                        create_keyboard(user, "Удачного дропа!")
                        return
                    except:
                        vk.messages.send(user_id=user, random_id=0,
                                         message="Неккоректный ввод. Введите стоимость покупки.")






while True:
     for event in longpoll.listen():
         if event.type == VkBotEventType.MESSAGE_NEW:
             usertext = event.object.text.lower()
             user = event.object.from_id
             if usertext == "начать":
                create_keyboard(user, "Привет, чтобы использовать мои функции нажми соответсвуюущую кнопку")

             elif usertext == "калькулятор":
                 create_calc(user)

             else:
                 vk.messages.send(user_id=user, random_id=0, message="Не знаю такой команды((")


