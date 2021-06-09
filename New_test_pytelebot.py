import random
import logging
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)
tasks = 'C:\\Users\\pashencev.alexandr\\Documents\\Чикаго\\Инструкция по Приложению\\PDF\\10. Задачи.pdf'

answer = ["Справка", "Информация", "Отдых"]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in ("Привет", "привет"):
        bot.send_message(
            message.chat.id, "Привет! Ты можешь задать вопрос прямо в чате, если тебе нужна справка напиши /info. Если не помогло напиши /help")
    
    elif message.text in ("как создавать задачу?", "Не могу создать задачу", "как сделать задачу", "задачи не работают"):
        bot.send_document(message.chat.id, open(tasks, 'rb'))

    elif message.text in ["/help", "/help@My_best_aw_bot"]:
    #    bot.forward_message(message.chat.id, message.from_user.id, message.id)
    #    problem_chel = [message.from_user.id, 'очень нужна помощь!']
    #    for i in problem_chel:
        bot.forward_message(125939380, from_chat_id=message.chat.id , message_id=message.from_user.id)
        bot.send_message(message.chat.id, "Ожидайте, с вами свяжутся!")
    
    elif message.text in ["/info", "/info@My_best_aw_bot"]:
        bot.send_message(message.chat.id, random.choice(answer))




bot.polling(none_stop=True, interval=0)
