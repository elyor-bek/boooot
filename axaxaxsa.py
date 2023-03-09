from qwerqerqwerqweqwerqwerqwerqwerqwerwewqrwrerewre import get_date
from random import randint
from aiogram import Router, Dispatcher
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
from aiogram import Bot
from aiogram.types.dice import DiceEmoji
from aiogram import F
from aiogram.types import ContentType
from aiogram.filters import Text
from aiogram.filters.command import Command 
from asyncio import run, sleep
from aiogram.types import Poll, PollAnswer
from abc import ABC,abstractclassmethod
from xixi import my_token
#from asyncio import run
City=InlineKeyboardMarkup(
    inline_keyboard= [
    [ 
    InlineKeyboardButton(text="Tashkent",callback_data="Tashkent"),
    InlineKeyboardButton(text="Fergana",callback_data="Fergana"),
    InlineKeyboardButton(text="Andijon",callback_data="Andijon"),
    ],
    [
    InlineKeyboardButton(text="Namangan",callback_data="Namangan"),
    InlineKeyboardButton(text="Qashqadaryo",callback_data="Qashqadaryo"),
    InlineKeyboardButton(text="Sirdaryo",callback_data="Sirdaryo"),
    ],
    [
    InlineKeyboardButton(text="Surhondaryo",callback_data="Termez"),
    InlineKeyboardButton(text="Samarqand",callback_data="Samarqand"),
    InlineKeyboardButton(text="Xorazm",callback_data="Urgench"),
    ],
    [
    InlineKeyboardButton(text="Buxoro",callback_data="Buxoro"),
    InlineKeyboardButton(text="Navoiy",callback_data="Navoiy"),
    InlineKeyboardButton(text="Jizzax",callback_data="Jizzax"),
    ],
    [
    InlineKeyboardButton(text="Qoraqolpog'iston",callback_data="Karakalpakstan"),
    ],
    ],
)
great=Router()
@great.message(Command(commands=["start"]))
async def great_message(msg:Message,bot:Bot):
    await msg.answer("Bu 12 viloyat ob-havo ma'lumoti boti",reply_markup=City)

@great.callback_query()
async def get_weather(call:CallbackQuery):
    city=call.data
    print(city)
    weather=get_date(city)
    await call.answer(f"{weather} in C")

async def start():
    dp=Dispatcher()
    kb=Bot(my_token)#token
    dp.include_router(great)
    try:
        await dp.start_polling(kb)
    except Exception as f:
        await kb.session.close()
if __name__=="__main__":
    run(start())