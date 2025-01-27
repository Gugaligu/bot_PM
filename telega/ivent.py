import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)
from datetime import date
import menu
TOKEN_API = "6662629827:AAHoIxMjnrbtSLX2W7Pw3ARqbAjf_xq8QbI"
bot1 = Bot(TOKEN_API)
event = Router()

@event.callback_query(F.data=="ивенты")
async def ivent(callback: CallbackQuery):
    await callback.answer("вы выбрали ивенты")
    await callback.message.edit_text("Ивентов пока нет(")
    await callback.message.edit_reply_markup(reply_markup=kBackmebu)

kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти↩️",callback_data="menu")]])