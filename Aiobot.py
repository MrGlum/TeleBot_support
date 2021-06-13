from aiogram.bot.api import compose_data
from aiogram.types import chat, message
import config
import all_que
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.TOKEN

logging.basicConfig(
    level=logging.DEBUG, 
    filename = "mylog.log", 
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", 
    datefmt='%H:%M:%S',
    )

logging.info('Hello')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

vopros = all_que.otvet


@dp.message_handler(commands=['start', "info", "info@My_best_aw_bot", "start@My_best_aw_bot"])
async def send_info(message: types.Message):
    await message.reply("Привет! Ты можешь задать вопрос прямо в чате, если тебе нужна справка напиши /info.\nЕсли не помогло напиши /help")
#    await message.forward(125939380, message)

@dp.message_handler(commands=['help', "help@My_best_aw_bot"])
async def send_help(message: types.Message):
    voprositel = "Привет, " + str(message.from_user.first_name) + " с тобой скоро свяжутся!"
    await message.reply(voprositel)
    await message.forward(125939380, message)

# @dp.message_handler()
# async def SuperMegaBrain(message: types.message):
#    for message in vopros.keys():
#        if message == vopros.keys():
#            await message.answer(map(str,vopros.values(message.text)))
#        else:
#            await message.answer("Не понятно!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
