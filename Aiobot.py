from aiogram.bot.api import compose_data
from aiogram.types import chat, message
import config
import all_que

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.TOKEN

# Configure logging
# logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

vopros = all_que.otvet


@dp.message_handler(commands=['start', 'help', "info", "info@My_best_aw_bot", "help@My_best_aw_bot", "start@My_best_aw_bot"])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Ты можешь задать вопрос прямо в чате, если тебе нужна справка напиши /info.\nЕсли не помогло напиши /help")
    await message.forward(125939380, message)


@dp.message_handler()
async def TEST_1(message: types.Message):
    otvetik = compose_data(vopros)
    await message.answer(str(otvetik[1]))


# @dp.message_handler()
# async def SuperMegaBrain(message: types.message):
#    for message in vopros.keys():
#        if message == vopros.keys():
#            await message.answer(map(str,vopros.values(message.text)))
#        else:
#            await message.answer("Не понятно!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
