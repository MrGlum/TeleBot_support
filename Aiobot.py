from aiogram.bot.api import compose_data
from aiogram.types import chat, message
import config
import all_que
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.TOKEN

logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)

logging.info('Hello')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

vopros_otvet = { "вопрос1": "ответ1",
                "вопрос2": "ответ2"}


@dp.message_handler(commands=['start', "Привет", "Привет@My_best_aw_bot", "start@My_best_aw_bot"])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Ты можешь задать вопрос прямо в чате, если тебе нужна справка напиши /info.\nЕсли не помогло напиши /help")


@dp.message_handler(commands=['info', "info@My_best_aw_bot"])
async def send_info(message: types.Message):
    await message.reply("Это справочный бот который сможет ответить на самые часто задаваемые вопросы:\n/start для начала диалога\nБот реагирет на все вопросы в чате, просто задай вопрос.\nТак же ты можешь вести диалог в привате, просто задай вопрос боту в ЛС.\nЕсли не помогло напиши /help")


@dp.message_handler(commands=['help', "help@My_best_aw_bot"])
async def send_help(message: types.Message):
    voprositel = "Привет, " + \
        str(message.from_user.first_name) + \
        ", с тобой скоро свяжется специалист!"
    await message.reply(voprositel)
    await message.forward(125939380, message)

@dp.message_handler()
async def SuperMegaBrain(message: types.message):
    for message in vopros_otvet.keys():
        if message == vopros_otvet.keys():
            await message.answer(map(str,vopros_otvet.values(message.text)))
        else:
            await message.answer("Не понятно!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
