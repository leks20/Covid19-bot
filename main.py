import os

import COVID19Py
from dotenv import load_dotenv
import requests
import telebot
from telebot import apihelper, types

load_dotenv()
token = os.getenv('teleram_token')

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot(token)
apihelper.proxy = {'https': 'socks5://66.42.43.209:1080'}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Россия')
    btn3 = types.KeyboardButton('Украина')
    btn4 = types.KeyboardButton('Беларусь')
    btn5 = types.KeyboardButton('Италия')
    btn6 = types.KeyboardButton('США')
    btn7 = types.KeyboardButton('Франция')
    btn8 = types.KeyboardButton('Япония')
    btn9 = types.KeyboardButton('Германия')
    btn10 = types.KeyboardButton('Казахстан')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    text = f"<b>Привет {message.from_user.first_name}!</b>\nВыбери страну"
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "казахстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
