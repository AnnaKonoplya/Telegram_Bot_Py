import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5792872337:AAEoqqKZOjRbiERc9HeT_H7TT-ectr2q7vo')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я бот для получения цитат и афоризмов из русских источников. Введите /quote, чтобы получить случайную цитату.')

@bot.message_handler(commands=['quote'])
def send_quote(message):
    response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=ru')
    soup = BeautifulSoup(response.text, 'html.parser')
    quote = soup.get_text()
    bot.reply_to(message, quote)

bot.polling()
