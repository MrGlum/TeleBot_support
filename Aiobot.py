from typing import Text

from aiogram.bot.api import compose_data
from aiogram.types import chat, message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
import logging


API_TOKEN = config.TOKEN

logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%d.%m.%Y %H:%M:%S',
)

logging.info('Hello')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

vopros_otvet = { "вопрос1": "ответ1",
                "вопрос2": "ответ2"}

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/info", description="Краткая справка"),
        BotCommand(command="/help", description="Позвать кожанного")
    ]
    await bot.set_my_commands(commands)

# @dp.message_handler(commands="start")
# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["С пюрешкой", "Без пюрешки"]
#     keyboard.add(*buttons)
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)

# @dp.message_handler(Text(equals="С пюрешкой"))
# async def with_puree(message: types.Message):
#     await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())


#@dp.message_handler(commands=['start', "start@My_best_aw_bot"], content_types=["Привет", "Привет@My_best_aw_bot"])
#async def send_welcome(message: types.Message):
#    await message.reply("Привет! Ты можешь задать вопрос прямо в чате, если тебе нужна справка напиши /info.\nЕсли не помогло напиши /help")


@dp.message_handler(commands=['info', "info@My_best_aw_bot"])
async def send_info(message: types.Message):
    await message.reply("Это справочный бот который сможет ответить на самые часто задаваемые вопросы:\n/start для начала диалога\nБот реагирет на все вопросы в чате, просто задай вопрос.\nТак же ты можешь вести диалог в привате, просто задай вопрос боту в ЛС.\nЕсли не помогло напиши /help")


@dp.message_handler(commands=['help', "help@My_best_aw_bot"])
async def send_help(message: types.Message):
    voprositel = "Привет, " + \
        str(message.from_user.first_name) + \
        ", с тобой скоро свяжется специалист!"
    await message.reply(voprositel)
    await message.forward(config.helper_user, message)

# @dp.message_handler()
# async def SuperMegaBrain(message: types.message):
#     for hit in vopros_otvet.keys():
#         if message.text == hit:
#             await message.reply(vopros_otvet.values(hit))
#         else:
#             await message.reply("Не понятно!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    