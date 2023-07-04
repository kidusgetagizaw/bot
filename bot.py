import telebot
import time
import mysql.connector


TOKEN='6323409890:AAHwUHsxAsD3zSzGazHTaR8-osC1ShJEh9E'
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','START'])
def start(message):
  bot.send_message(message.from_user.id,'hello user this is created by kidus geta')

@bot.message_handler(func = lambda message: True)
def Telegram_bots(message):
    bot.send_message(message.from_user.id,message.text)
bot.infinity_polling()
