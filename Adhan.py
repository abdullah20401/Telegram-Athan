import json
from datetime import datetime
import requests
import time
import telebot

egypt = 1
karachi_shafi = 2
karachi_hanafi = 3
icna = 4
muslim_world_league = 5
ummalqura = 6
fixedisha = 7

city = 'chicago'

url = "https://muslimsalat.com/{}/daily/{}.json?key=EnterApiKey".format(city, icna)

urlapi = 'https://api.telegram.org/botEnterApiKey/getUpdates'



hijri_dates = 'http://api.aladhan.com/v1/gToH?'

bot = telebot.TeleBot('EnterApiKey')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalamu alaikum this bot will give you a notification when its prayer time to get prayer timings just type in /fajr /zuhr /asr /maghrib /isha or you can get the current time by typing /time you can also get the hijri calendar date by typing in /date or or can get the day /day or you can get the month /month or the year /year you can also get the /weekday if you need help use this command /help")
#    bot.send_video(chat_id=update.message.chat_id, video=open('2019_05_26_18_37_18.mp4', 'rb'), supports_streaming=True)
@bot.message_handler(commands=['help', 'Help', 'HELP'])
def send_welcome(message):
    bot.reply_to(message, "Assalamu alaikum this bot will give you a notification when its prayer time to get prayer timings just type in /fajr /zuhr /asr /maghrib /isha or you can get the current time by typing /time you can also get the hijri calendar date by typing in /date or you can get the day /day or you can get the month /month or the year /year you can also get the /weekday for further help contact me at chicagoprayerbot@yahoo.com")


@bot.message_handler(commands=['fajr', 'Fajr'])
def s(message):
    bot.reply_to(message, requests.get(url).json()['items'][0]['fajr'].upper())

@bot.message_handler(commands=['zuhr', 'dhuhr', 'duhr', 'Zuhr', 'Dhuhr'])
def se(message):
    bot.reply_to(message, requests.get(url).json()['items'][0]['dhuhr'].upper())

@bot.message_handler(commands=['asr', 'Asr'])
def s(message):
    bot.reply_to(message, requests.get(url).json()['items'][0]['asr'].upper())

@bot.message_handler(commands=['maghrib', 'Maghrib'])
def s(message):
    bot.reply_to(message, requests.get(url).json()['items'][0]['maghrib'].upper())

@bot.message_handler(commands=['isha', 'Isha'])
def s(message):
    bot.reply_to(message, requests.get(url).json()['items'][0]['isha'].upper())

@bot.message_handler(commands=['time', 'Time'])
def s(message):
    bot.reply_to(message, time.strftime("%I:%M %p", time.localtime()))

@bot.message_handler(commands=['date', 'Date', 'DATE'])
def azan(message):
	bot.reply_to(message, requests.get(hijri_dates).json()['data']['hijri']['date'])

@bot.message_handler(commands=['month', 'Month', 'MONTH'])
def month(message):
	bot.reply_to(message, requests.get(hijri_dates).json()['data']['hijri']['month'].get('en') + '   ' + requests.get(hijri_dates).json()['data']['hijri']['month'].get('ar'))

@bot.message_handler(commands=['weekday', 'Weekday', 'WEEKDAY'])
def weekday(message):
	bot.reply_to(message, requests.get(hijri_dates).json()['data']['hijri']['weekday']['en'] + '   ' + requests.get(hijri_dates).json()['data']['hijri']['weekday']['ar'])

@bot.message_handler(commands=['year', 'Year', 'YEAR'])
def year(message):
	bot.reply_to(message, requests.get(hijri_dates).json()['data']['hijri']['year'])

@bot.message_handler(commands=['day', 'Day', 'DAY'])
def day(message):
	bot.reply_to(message, requests.get(hijri_dates).json()['data']['hijri']['day'])

@bot.message_handler(commands=['commands', 'Commands', 'COMMANDS', 'command', 'Command', 'COMMAND'])
def day(message):
    bot.reply_to(message, '/start, /help /fajr, /zuhr, /asr, /maghrib, /isha, /time, /date, /day, /month, /weekday')


bot.polling()
