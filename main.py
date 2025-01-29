import telebot
from telebot import types
from telegram import ParseMode
# Подключенная библиотека с изображениями и описаниями карт
import tarodata
import random

TOKEN = 'TOKEN'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Случайный выбор')
    key2 = types.KeyboardButton('Поиск карты')
    markup.add(key1, key2)
    bot.send_message(message.chat.id, 'Привет! Я телеграм-бот, который присылает случайную карту таро высших арканов и ее описание. Нажимай на кнопку внизу или пиши /info для получения информации!', reply_markup=markup)

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Данный telegram-bot создан в развлекательных целях и предоставляет информацию об высших арканах карт таро. Изображения и описания взяты из игры Cyberpunk 2077 производства CD PROJECT RED. Чтобы выбрать случайную карту, нажми кнопку "Случайный выбор". Чтобы найти информацию о конкретной карте, пиши "Поиск карты"')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет! Выбирай внизу, что тебя интересует!')
    elif message.text == 'Случайный выбор':
        random_c(message)
    elif message.text == 'Поиск карты':
        markup = types.InlineKeyboardMarkup(row_width=3)
        fool = types.InlineKeyboardButton(text='Шут', callback_data='fool')
        mag = types.InlineKeyboardButton(text='Маг', callback_data='mag')
        priest = types.InlineKeyboardButton(text='Жрица', callback_data='priest')
        empress = types.InlineKeyboardButton(text='Императрица', callback_data='empress')
        emperor = types.InlineKeyboardButton(text='Император', callback_data='emperor')
        priest1 = types.InlineKeyboardButton(text='Жрец', callback_data='priest1')
        lovers = types.InlineKeyboardButton(text='Влюбленные', callback_data='lovers')
        chariot = types.InlineKeyboardButton(text='Колесница', callback_data='chariot')
        force = types.InlineKeyboardButton(text='Сила', callback_data='force')
        hermit = types.InlineKeyboardButton(text='Отшельник', callback_data='hermit')
        fortune = types.InlineKeyboardButton(text='Колесо Фортуны', callback_data='fortune')
        justice = types.InlineKeyboardButton(text='Справедливость', callback_data='justice')
        hanged = types.InlineKeyboardButton(text='Повешенный', callback_data='hanged')
        death = types.InlineKeyboardButton(text='Смерть', callback_data='death')
        moderation = types.InlineKeyboardButton(text='Умеренность', callback_data='moderation')
        devil = types.InlineKeyboardButton(text='Дьявол', callback_data='devil')
        tower = types.InlineKeyboardButton(text='Башня', callback_data='tower')
        star = types.InlineKeyboardButton(text='Звезда', callback_data='star')
        moon = types.InlineKeyboardButton(text='Луна', callback_data='moon')
        sun = types.InlineKeyboardButton(text='Солнце', callback_data='sun')
        trial = types.InlineKeyboardButton(text='Суд', callback_data='trial')
        peace = types.InlineKeyboardButton(text='Мир', callback_data='peace')
        markup.add(fool, mag, priest, empress, emperor, priest1, lovers, chariot, force, hermit, fortune, justice, hanged, death, moderation, devil, tower, star, moon, sun, trial, peace)
        bot.send_message(message.chat.id, 'О какой карте хотите найти информацию?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю. Напиши /info или /start.')

# Функция генерации случайной карты
def random_c(message):
    pic1 = list(tarodata.data_c.get('pic'))
    pic2 = random.choice(pic1)
    number = pic1.index(pic2)
    name1 = tarodata.data_c.get('name')
    name2 = name1[number]
    info1 = tarodata.data_c.get('info')
    info2 = info1[number]
    img = open(pic2, 'rb')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, f'<b>{name2}</b>', parse_mode='html')
    bot.send_message(message.chat.id, info2, parse_mode='html')

# Функция показа конкретной выбранной карты
def tarocard(message, i):
    picture = tarodata.data_c.get('pic')
    picture1 = picture[i]
    img = open(picture1, 'rb')
    bot.send_photo(message.chat.id, img)
    name = tarodata.data_c.get('name')
    name1 = name[i]
    info = tarodata.data_c.get('info')
    info1 = info[i]
    bot.send_message(message.chat.id, f'<b>{name1}</b>', parse_mode='html')
    bot.send_message(message.chat.id, info1, parse_mode='html')

# Возврат информации от нажатия кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'fool':
        tarocard(call.message, 0)
    elif call.data == 'mag':
        tarocard(call.message, 1)
    elif call.data == 'priest':
        tarocard(call.message, 2)
    elif call.data == 'empress':
        tarocard(call.message, 3)
    elif call.data == 'emperor':
        tarocard(call.message, 4)
    elif call.data == 'priest1':
        tarocard(call.message, 5)
    elif call.data == 'lovers':
        tarocard(call.message, 6)
    elif call.data == 'chariot':
        tarocard(call.message, 7)
    elif call.data == 'force':
        tarocard(call.message, 8)
    elif call.data == 'hermit':
        tarocard(call.message, 9)
    elif call.data == 'fortune':
        tarocard(call.message, 10)
    elif call.data == 'justice':
        tarocard(call.message, 11)
    elif call.data == 'hanged':
        tarocard(call.message, 12)
    elif call.data == 'death':
        tarocard(call.message, 13)
    elif call.data == 'moderation':
        tarocard(call.message, 14)
    elif call.data == 'devil':
        tarocard(call.message, 15)
    elif call.data == 'tower':
        tarocard(call.message, 16)
    elif call.data == 'star':
        tarocard(call.message, 17)
    elif call.data == 'moon':
        tarocard(call.message, 18)
    elif call.data == 'sun':
        tarocard(call.message, 19)
    elif call.data == 'trial':
        tarocard(call.message, 20)
    elif call.data == 'peace':
        tarocard(call.message, 21)

    bot.answer_callback_query(callback_query_id=call.id)

bot.polling(none_stop=True, interval=0)
