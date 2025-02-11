import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from datetime import date
import menu

TOKEN_API = "7503899100:AAEcNx9fksbRf2pjOfIRLXf6ZtaLT0fb6BU"
bot1 = Bot(TOKEN_API)
docki = Router()


@docki.callback_query(F.data=="документы")
async def dock(callback: CallbackQuery):
    await callback.answer("вы выбрали полезные документы")
    await callback.message.edit_text("полезных документов пока не загружено!")
    await callback.message.edit_reply_markup(reply_markup=kBackmebu)


kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти↩️", callback_data="menu")]])