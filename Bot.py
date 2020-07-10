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

token = "1a81d5301232b0ef640f04232701ea7b88965c7fc850df3068fe9a6b896c5a0854ed1cafc240da79b4a0b"
groupsession = "196998990"

vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, groupsession)
vk = vk_session.get_api()

def step1():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            text1 = event.object.text.lower()
            if text1 == "7425":
                vk.messages.send(user_id=event.object.from_id, random_id=0, message='Молодец! Ты быстро справился дружок, но за тобой еще должок, чтоб дальше следовать пути придется первый код ввести. Возьми ты первую коробку и код с нее сюда введи !')
                step2()
                break

            else:
                vk.messages.send(user_id=event.object.from_id, random_id=0, message='Не торопись же ты дружок, подумай ты еще чуток!')


def step2():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            text1 = event.object.text.lower()
            if text1 == "143288":
                vk.messages.send(user_id=event.object.from_id, random_id=0, message='А что же со второй коробкой? Ты от нее пароль введи!')
                step4()
                break

            else:
                vk.messages.send(user_id=event.object.from_id, random_id=0, message='Увы, но код неверен этот! Не жульничал ли ты?')


def step4():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            text1 = event.object.text.lower()
            if text1 == "171266":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('ДА!', color=VkKeyboardColor.POSITIVE)
                vk.messages.send(user_id=event.object.from_id, random_id=0, keyboard=keyboard.get_keyboard(), message='Друг, ты на верном пути, но он труден впереди... готов ли ты его пройти чтоб ключик счастья обрести?)')
                step5()
                break
            else:
                vk.messages.send(user_id=event.object.from_id, random_id=0, message='Увы, но код неверен этот! Не жульничал ли ты?')


def step5():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            text1 = event.object.text.lower()
            if text1 == "да!":
                vk.messages.send(user_id=event.object.from_id, random_id=0, message='На встречу мечте отправляйся своей и по ссылке ты пройди поскорей - https://vk.com/id557333673?w=wall557333673_2')
                vk.messages.send(user_id="37916557", random_id=0, message='Глеб добрался до морзянки, надо проверить QR')
                break






while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            usertext = event.object.text.lower()
            if usertext == "начать":
                vk.messages.send(user_id=event.object.from_id, random_id=0, message='Друг, ты действительно умен, стоишь ты у ворот кремнем, но чтобы их преодолеть придется много попотеть. Вводи же код скорее ты, чтоб счастья море обрести! ')
                step1()

            else: vk.messages.send(user_id=event.object.from_id, random_id=0, message='Я не понимаю')
