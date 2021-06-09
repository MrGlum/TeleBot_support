import random
from logging import info
import telebot
from telebot import types

TOKEN = "1703341423:AAHTHYo3j7wj56VBJBojMrbAm2WGXWOFZt4"
bot = telebot.TeleBot(TOKEN)
tasks = 'C:\\Users\\pashencev.alexandr\\Documents\\Чикаго\\Инструкция по Приложению\\PDF\\10. Задачи.pdf'

answer = ["Справка", "Информация", "Отдых", "Злые языки"]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in ("Привет", "привет"):
        bot.send_message(
            message.chat.id, "Привет! Ты можешь задать вопрос прямо в чате, если тебе нужна справка напиши /info. Если не помогло напиши /help")
    
    elif message.text == "Как создавать задачу?":
        bot.send_document(message.chat.id, open(tasks, 'rb'))

#@bot.message_handler(commands=[help, info])
#def get_commands_message(message):
#    if message.text == "/help":
#        user_probl = message.user.id
#        bot.send_message(message.user.id, reply_to_message_id='/help')
#        bot.send_message(message.chat.id, user_probl)
#    elif message.text == "/info":
#        bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)
