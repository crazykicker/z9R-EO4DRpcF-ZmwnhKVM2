
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

print(time.ctime())
groupsession = "174863134"
users_id = (37916557, 179099319, 166608781, 214172854, 156660737, 171561963, 409943726, 288452948, 146482440, 49920565, 158855545, 54790058, 157485694, 22440645)


chislitel_poned = open("poned_shisl.txt").read()
#print(chislitel_poned)

chislitel_vtor = "Вторник. \n \nНоводаниловская набережная, д. 2, корп. 1 \n  \n1 Пара: 9:00 - 10:35 \n Теория и практика управления транспортными системами \n Преподаватель: Зеленков М.Ю \n Аудитория: В-423 \n ___________ \n \n2 Пара: 10:45 - 11:20 \n Экономика отрасли \n Преподаватель: проф. Милославская \n Аудитория: В-446\n ___________ \n \n3 Пара: 13:10 - 14:45 \n Экономика отрасли \n Преподаватель: проф. Милославская \n Аудитория: В-446\n ___________ \n"
#print(chislitel_vtor)

chislitel_sred = "Среда. \n \nНоводаниловская набережная, д. 2, корп. 1 \n  \n2 Пара: 10:45 - 11:20 \n Деловой английский язык \n Преподаватель: доц. Гайнуллина Л.С. / Гончаренко Е.С. \n Аудитория: В-501 / В-510\n ___________ \n \n3 Пара: 13:10 - 14:45 \n Логистика: \n Преподаватель: доц. Шепелин Г.И. \n Аудитория: В-423\n ___________ \n"
#print(chislitel_sred)

chislitel_chet = "Четверг. \n \n1 Пара: 9:00 - 10:35 \n Безопасность жизнедеятельности \n Преподаватель: доц. Баранов Е.Ф \n Аудитория: А-303 \n ___________ \n \n2 Пара: 10:45 - 11:20 \n Безопасность жизнедеятельности \n Преподаватель: доц. Баранов Е.Ф \n Аудитория: П-20\n ___________ \n \n3 Пара: 13:10 - 14:45 \n Транспортное право \n Преподаватель: Чирук А.А. \n Аудитория: В-416\n ___________ \n"
#print(chislitel_chet)

chislitel_pyat = "Пятница. \n \nНоводаниловская набережная, д. 2, корп. 1 \n  \n3 Пара: 13:10 - 14:45 \n Общий курс транспорта \n Преподаватель: проф. Конталев В.А. \n Аудитория: В-431\n ___________ \n"
#print(chislitel_pyat)

subbota = "Суббота. \n \nЗанятий не запланировано"
voskresenye = "Воскресенье \n \nЗанятий не запланировано"



znamenatel_poned = "Понедельник. \n \nНоводаниловская набережная, д. 2, корп. 1 \n  \n2 Пара: 10:45 - 11:20 \n Деловой английский язык \n Преподаватель: доц. Гайнуллина Л.С. / Гончаренко Е.С. \n Аудитория: В-501 / В-510 \n ___________ \n \n3 Пара: 13:10 - 14:45 \n Логистика \nПреподаватель: доц. Шепелин Г.И. \n Аудитория: В-423\n ___________ \n \n4 Пара: 14:55 - 16:30 \n Основы системного анализа и научных исследований \nПреподаватель: доц. Шепелин Г.И. \n Аудитория: В-423\n ___________ \n"

znamenatel_vtor = "Вторник. \n \nНоводаниловская набережная, д. 2, корп. 1 \n  \n1 Пара: 9:00 - 10:35 \n Экономика отрасли \n Преподаватель: проф.Милославская \n Аудитория: В-1 \n ___________ \n \n2 Пара: 10:45 - 11:20 \n Метрология, стандартизация, сертификаци \n Преподаватель: доц. Бакаев С.В. \n Аудитория: В-443\n ___________ \n \n3 Пара: 13:10 - 14:45 \n Теория и практика управления транспортными системами \n Преподаватель: проф. Зеленков М.Ю. \n Аудитория: В-423\n ___________ \n"

znamenatel_sred = "Среда. \n \nНоводаниловская набережная, д. 2, корп. 1 \n  \n2 Пара: 10:45 - 11:20 \n Деловой английский язык \n Преподаватель: доц. Гайнуллина Л.С. / Гончаренко Е.С. \n Аудитория: В-501 / В-510\n ___________ \n \n3 Пара: 13:10 - 14:45 \n Элективные курсы по физической культуре и спорту  \n Преподаватель: Неизвестно \n Аудитория: Спортзал\n ___________ \n \n4 Пара: 14:55 - 16:30 \n Логистика \nПреподаватель: доц. Шепелин Г.И. \n Аудитория: В-423"

znamenatel_chet = "Четверг. \n \n2 Пара: 10:45 - 11:20 \n Транспортное право \n Преподаватель: Фалкенберг И.С. \n Аудитория: В-416 \n ___________ \n \n3 Пара: 13:10 - 14:45 \n Безопасность жизнедеятельности \n Преподаватель: доц. Баранов Е.Ф \n Аудитория: А-303\n ___________ \n \n4 Пара: 14:55 - 16:30 \n  Безопасность жизнедеятельности \n Преподаватель: доц. Баранов Е.Ф \n Аудитория: А-303\n ___________ \n"

znamenatel_pyat = "Пятница. \n \nНоводаниловская набережная, д. 2, корп. 1 \n  \n3 Пара: 13:10 - 14:45 \n Общий курс транспорта \n Преподаватель: проф. Конталев В.А. \n Аудитория: В-431\n ___________ \n"



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
        raspis_if_nedela_chisl(case1, case2, firsttext, secondtext)
    else:
        raspis_if_nedela_znam(case1, case2, firsttext, secondtext)

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
















