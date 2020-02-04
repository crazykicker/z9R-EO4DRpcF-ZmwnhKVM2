
#импорт нужных бибиотек
import os
import datetime
from datetime import timedelta
import time
from time import gmtime, strftime
import vk_api
import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from config import  groupsession
from config import users_id
from raspisanie import chislitel_poned, chislitel_vtor, chislitel_sred, chislitel_chet, chislitel_pyat
from raspisanie import subbota, voskresenye
from raspisanie import znamenatel_poned, znamenatel_vtor, znamenatel_sred, znamenatel_chet, znamenatel_pyat

#подключение к сообществу вк и извлечение расписания с файла
token = os.environ.get("bot_tocken")
vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, groupsession)
vk = vk_session.get_api()
raspis_chisl = (voskresenye, chislitel_poned, chislitel_vtor, chislitel_sred, chislitel_chet, chislitel_pyat, subbota)
raspis_znam = (voskresenye, znamenatel_poned, znamenatel_vtor, znamenatel_sred, znamenatel_chet, znamenatel_pyat, subbota)

#создание начальной кнопки
def create_welcome():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Расписание', color=VkKeyboardColor.POSITIVE)
    vk.messages.send(user_id=event.object.from_id, random_id=0, keyboard=keyboard.get_keyboard(),message="Привет друг. Возможно ты первый раз меня используешь, но здесь все просто, у тебя снизу есть кнопка, послее ее нажатия ты получишь меню с моими функциями. \n \n Совет: чтобы обновить текущую дату в меню расписания нажми выход и снова открой расписание.")

#создание выхода в меню
def create_keyboard1():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Расписание', color=VkKeyboardColor.POSITIVE)
    vk.messages.send(user_id=event.object.from_id, random_id=0, keyboard=keyboard.get_keyboard(),message='Ок. выбери новую команду.')

#создание дат на 7 дней вперед и  кнопок с датами
def create_keyboard2():
    currentdate = []
    ld = []
    a = datetime.date.today()
    one_day = timedelta(1)
    now = a - one_day
    days = {0: u"Вс", 1: u"Пн", 2: u"Вт", 3: u"Ср", 4: u"Чт", 5: u"Пт", 6: u"Сб"}
    i = 0
    while i < 7:
        now = now + one_day
        key = str(now)
        key1 = key[8] + key[9] + " " + key[5] + key[6] + " " + key[0] + key[1] + key[2] + key[3]
        rday = time.strptime(key1, "%d %m %Y")
        nWeek = strftime("%w", rday)
        date = key1
        #DEBUG print(nWeek)
        day = [days[int(nWeek)]]
        inday = str(key1) + str(day)
        #DEBUG print(inday)
        ld.append(inday)
        i = i + 1

    count = (len(ld))
    g = 0

    while g < int(count):
        a = ld[g]
        b = a[0] + a[1] + "." + a[3] + a[4] + "," + a[12] + a[13]
        currentdate.append(b)
        g = g + 1
    #DEBUG print(currentdate)
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button(currentdate[1], color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(currentdate[2], color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(currentdate[3], color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button(currentdate[4], color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(currentdate[5], color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(currentdate[6], color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button(currentdate[0] + " " + "-" + " " + "Сегодня", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Выход", color=VkKeyboardColor.NEGATIVE)
    vk.messages.send(user_id=event.object.from_id, random_id=0, keyboard=keyboard.get_keyboard(),message="Выбери нужную дату.")

#проверка на весокосный год
def year_cheak():
    nowyear = int(datetime.date.today().strftime("%Y"))
    if nowyear % 4 == 0:
        if nowyear % 100 == 0:
            if nowyear % 400 == 0:
                date_check_vesokos(case1, case2)
            else:
                date_check_nevesokos(case1, case2)
        else:
            date_check_vesokos(case1, case2)
    else:
        date_check_nevesokos(case1, case2)

#проверка валидности дней для весокосного года
def date_check_vesokos(case1, case2):
    if case2 == 2:
        if case1 > 29:
            vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректная дата')
        else:
            week_check(case1, case2)
    elif case2 == 1 or case2 == 3 or case2 == 5 or case2 == 7 or case2 == 8 or case2 == 10 or case2 == 12:
        week_check(case1, case2)
    elif case2 == 4 or case2 == 6 or case2 == 9 or case2 == 11:
        if case1 > 30:
            vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректная дата')
        else:
            week_check(case1, case2)

#проверка валидности для обычного года
def date_check_nevesokos(case1, case2):
    if case2 == 2:
        if case1 > 28:
            vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректная дата')
        else:
            week_check(case1, case2)
    elif case2 == 1 or case2 == 3 or case2 == 5 or case2 == 7 or case2 == 8 or case2 == 10 or case2 == 12:
        week_check(case1, case2)
    elif case2 == 4 or case2 == 6 or case2 == 9 or case2 == 11:
        if case1 > 30:
            vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректная дата')
        else:
            week_check(case1, case2)

#проверка числителя знаменателя
def week_check(case1, case2):

    allcase = str(case1) + " " + str(case2) + " " + datetime.date.today().strftime("%Y")
    weekcase = time.strptime(allcase, "%d %m %Y")
    weeckcheck = int(strftime("%W", weekcase))
    #DEBUG print(weeckcheck)
    if weeckcheck % 2 == 0:
        raspis_if_nedela_znam(case1, case2, firsttext, secondtext)
    else:
        raspis_if_nedela_chisl(case1, case2, firsttext, secondtext)

#проверка дня недели для числителя
def raspis_if_nedela_chisl(case1, case2, firsttext, secondtext):
    datecase = str(case1) + " " + str(case2) + " " + datetime.date.today().strftime("%Y")
    createday = time.strptime(datecase, "%d %m %Y")
    daycheck = int(strftime("%w", createday))
    raspisinday = "Неделя: Числитель." + "\n" + "День: " + firsttext + "." + secondtext + " " + "-" + " " + raspis_chisl[daycheck]
    #print(raspisinday)
    vk.messages.send(user_id=event.object.from_id, random_id=0, message=raspisinday)

def raspis_if_nedela_znam(case1, case2, firsttext, secondtext):
    datecase = str(case1) + " " + str(case2) + " " + datetime.date.today().strftime("%Y")
    createday = time.strptime(datecase, "%d %m %Y")
    daycheck = int(strftime("%w", createday))
    raspisinday = "Неделя: Знаменатель." + "\n" + "День: " + firsttext + "." + secondtext + " " + "-" + " " + raspis_znam[daycheck]
    #print(raspisinday)
    vk.messages.send(user_id=event.object.from_id, random_id=0, message=raspisinday)

#рассылка сообщений
def send_notification(users_id):
    u = 0
    while u < len(users_id):
        usrsended = users_id[u]
        vk.messages.send(user_id=usrsended, random_id=0, message=admintext)
        u = u + 1
    vk.messages.send(user_id=148077344, random_id=0, message="Уведомление отправлено")

#работа с longpoll api и проверка команд пользователя
while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            usertext = event.object.text.lower()
            admintext = event.object.text
            #Debug print(usertext)
            if len(usertext) < 5:
                vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректный ввод')
            else:
                firsttext = usertext[0] + usertext[1]
                secondtext = usertext[3] + usertext[4]

                if usertext[0] == ":" and int(event.object.from_id) == 148077344:
                    admintext = "Сообщение от старосты!   " + admintext
                    send_notification(users_id)
                else:

                    if usertext.isalpha():
                        if usertext == "начать" or usertext == "привет":
                            create_welcome()
                        elif usertext == "расписание":
                            create_keyboard2()
                        elif usertext == "выход":
                            create_keyboard1()
                        else:
                            vk.messages.send(user_id=event.object.from_id, random_id=0, message='Я тебя не понял')

                    elif usertext[2] == ".":
                        if firsttext.isdigit() and secondtext.isdigit():
                            if int(firsttext) > 31 or int(firsttext) < 1:
                                vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректный ввод')
                            else:
                                if int(usertext[3] + usertext[4]) > 12 or int(usertext[3] + usertext[4]) < 1:
                                    vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректный ввод')
                                else:
                                    case1 = int(firsttext)
                                    case2 = int(secondtext)
                                    year_cheak()
                        else:
                            vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректный ввод')
                    else:
                        vk.messages.send(user_id=event.object.from_id, random_id=0, message='Некорректный ввод')
















