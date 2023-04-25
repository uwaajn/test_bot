import telebot # импорт библиотеки для работы Python с Telegram ботами
import re
import requests
from bs4 import BeautifulSoup
import os



mybot = telebot.TeleBot('6026532140:AAFSDrDcF5ARezc0FzhqxU9hBULtFh7q3Bo') # ключ для бота
@mybot.message_handler(content_types=['text']) # бот "ловит" текстовые сообщения типа "текст"



def echo_message(message): # функция, на вход сообщение
    if (re.findall(r'^[0-9a-zA-Z]+[.][0-9a-zA-Z]{2,4}[/][\w]', message.text)): # проверяем по шаблону, что пользователь отправил ссылку
        mybot.send_message(message.from_user.id, message.text)

        response = requests.get('https://' + message.text) # идёт обращение на сайт, ('https://' +) для успешного обращения

        soup = BeautifulSoup(response.text, 'lxml') # "забрали" сайт в XML
        text_site = soup.text # удаление от XML

        f = open('C:\\text_site.txt', 'w', encoding='utf-8') # открытие файла в режиме записи
        f.write(text_site) # запись текста с сайта в файл
        mybot.send_document(message.from_user.id, open('C:\\text_site.txt', 'r', encoding='utf-8'))


mybot.polling(none_stop=True, interval=0)                   # "опрос" работы бота без перерырыва (интервал 0)
mybot.echo_message                                           # применение функции бота
