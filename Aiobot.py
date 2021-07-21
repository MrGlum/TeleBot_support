from typing import Text
from aiogram.utils.callback_data import CallbackData
from gtts import gTTS
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from contextlib import suppress
from aiogram.utils.exceptions import MessageNotModified, PhotoAsInputFileRequired


import config
import logging
import datetime
import requests
import json

API_TOKEN = config.TOKEN
user_data = {}

logging.basicConfig(
    level=logging.DEBUG,
    filename=f"logi\mylog{datetime.date.today()}.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%d.%m.%Y %H:%M:%S',
)

logging.info('Hello')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

vopros_otvet = {"хай": "хеллоу",
                "алло": "По лбу не дало?",
                "ну чо зайчики?": "чишотакое",
                "как вы?": "Уж получше твоего, старый!",
                "йоу нигга": "WOZZZZZZZAAAAAAAAAAA",
                "ну чо как дела": "пока не родила"}

# fabnum - префикс, action - название аргумента, которым будем передавать значение
callback_tema = CallbackData("fabnum", "action")


def weather_info(city):
    wa = config.WeatherAPI
    city = city.split()[1]
    pogoda = requests.get(
        f"https://api.weatherbit.io/v2.0/current?city={city}&lang=ru&key={wa}")
    j_otvet = json.dumps(pogoda)
    answer = (f'Погода в {city}: {j_otvet}')
    return answer


def get_keyboard_fab():
    buttons = [
        types.InlineKeyboardButton(
            text="МТ", callback_data=callback_tema.new(action="one_button")),
        types.InlineKeyboardButton(
            text="Супервайзер", callback_data=callback_tema.new(action="two_button")),
        types.InlineKeyboardButton(
            text="Аналитик", callback_data=callback_tema.new(action="three_button")),
        types.InlineKeyboardButton(
            text="Статистика", callback_data=callback_tema.new(action="finish"))
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def update_num_text_fab(message: types.Message, new_value: int):
    with suppress(MessageNotModified):
        await message.edit_text(f"Вы выбрали тему: {new_value} раз.", reply_markup=get_keyboard_fab())


@dp.message_handler(commands="go")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Выберите тему по которой вам необходима помощь:", reply_markup=get_keyboard_fab())


@dp.callback_query_handler(callback_tema.filter(action=["two_button", "one_button", "three_button"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, 0)
    action = callback_data["action"]
    if action == "two_button":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text_fab(call.message, user_value + 1)
    elif action == "one_button":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text_fab(call.message, user_value + 1)
    elif action == "three_button":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text_fab(call.message, user_value + 1)
    await call.answer()


@dp.callback_query_handler(callback_tema.filter(action=["finish"]))
async def callbacks_num_finish_fab(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    await call.message.edit_text(f"Ты ткнул по кнопочкам: {user_value} раз")
    await call.answer()


@dp.message_handler(commands=['start', "start@My_best_aw_bot"])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Ты можешь задать вопрос прямо в чате, если тебе нужна справка напиши /info.\nЕсли не помогло напиши /help")


@dp.message_handler(commands=['info', "info@My_best_aw_bot"])
async def send_info(message: types.Message):
    await message.reply("Это справочный бот который сможет ответить на самые часто задаваемые вопросы:\nДля для поиска нужной подсказки напиши /go в чате или в личном сообщении боту.\nЧтобы задать вопрос специалисту, напиши /help в начале сообщения.")


@dp.message_handler(commands=[])
@dp.callback_query_handler(callback_tema.filter(action=['Погода', 'погода']))
async def pogodaka(call: types.Message):
    await call.answer("Введите Ваш город:")
    await call.reply(weather_info(call.text))


@dp.message_handler(commands=['help', "help@My_best_aw_bot"])
async def send_help(message: types.Message):
    voprositel = "Привет, " + \
        str(message.from_user.first_name) + \
        ", с тобой скоро свяжется специалист!"
    await message.reply(voprositel)
    await message.forward(config.helper_user, message)


@dp.message_handler()
async def SuperMegaBrain(message: types.Message):
    if message.text.lower() in vopros_otvet.keys():
        await message.reply(vopros_otvet[message.text.lower()])
    elif message.text.lower() == 'виталя':
        await message.answer(str(message))
    else:
        await message.reply_voice(voice=gTTS(message.text, lang='ru'))
        gTTS(message.text, lang='ru').save('Jim.ogg')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
