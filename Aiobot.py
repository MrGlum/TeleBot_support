from aiogram.types import message
import config
import logging
import all_que

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.TOKEN
vopros = all_que.voprosy
# Configure logging
# logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help', "info", "info@My_best_aw_bot", "help@My_best_aw_bot", "start@My_best_aw_bot", ])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Ты можешь задать вопрос прямо в чате, если тебе нужна справка напиши /info.\nЕсли не помогло напиши /help")
    await message.forward(125939380, message)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.message_handler()
async def SuperMegaBrain(messge: types.Message):
    if message in vopros:
        await message.answer(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
