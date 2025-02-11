import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)
import sqlite3

db = sqlite3.connect("db.db")

TOKEN_API = "7503899100:AAEcNx9fksbRf2pjOfIRLXf6ZtaLT0fb6BU"
bot1 = Bot(TOKEN_API)
menu = Router()



def fkmenu(id_tg):
    level = flevel_admin(id_tg)
    if level == 1:
        return kmenu
    elif level == 2:
        return kadmin_menu
    elif level == 3:
        return kadmin_menu_ss
    else:
        return kreg





@menu.callback_query(F.data=="menu")
async def back(callback: CallbackQuery,state:FSMContext):
    await state.clear()
    level = flevel_admin(callback.message.chat.id)
    if level == 1:
        await callback.message.edit_text(
            fmenu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kmenu)
    elif level == 2:
        await callback.message.edit_text(
            fmenu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kadmin_menu)
    elif level == 3:
        await callback.message.edit_text(
            fmenu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kadmin_menu_ss)
    else:
        await callback.message.edit_text("ㅤㅤЗарегистрируйтесь\n"
                                         "===========↓===========",
                                         reply_markup=kreg)

def flevel_admin(id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT admin From user WHERE tg_id=(?)""", (id,)).fetchone()
    if res==None:
        return 0
    return res[0]

def fmenu(id,first_name,username):
    cursor = db.cursor()
    res = cursor.execute("""SELECT * From user WHERE tg_id=(?)""", (id,)).fetchone()
    return "Пользователь👤\n" \
           f"Имя:{res[2]}\n" \
           f"Имя в тг:{first_name}({username})\n" \
           f"группа:{res[4]}\n" \
           f"статус:{fnazvanie_admina(res[1])}\n" \
           f"====================\n" \
           f"ㅤㅤМеню функций"

def fnazvanie_admina(id):
    level=flevel_admin(id)
    if level == 0:
        return "не зарегистрирован"
    elif level==1:
        return "ученик"
    elif level == 2:
        return "староста"
    elif level==3:
        return "создатель"
    else:
        return "нет такого"

kreg = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="регистрация",callback_data="reg")]])

kmenu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="расписание🗓",callback_data="расписание")],
                                              [InlineKeyboardButton(text="дней до стипендии💸",callback_data="стипендия")],
                                                [InlineKeyboardButton(text="gpt4",url='https://t.me/GPT4Telegrambot')],
                                                [InlineKeyboardButton(text="настройки",callback_data="настройки учасника")],
                                              # [InlineKeyboardButton(text="полезные документы📁",callback_data="документы")]
                                              ])

kadmin_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="расписание🗓",callback_data="расписание")],
                                              [InlineKeyboardButton(text="дней до стипендии💸",callback_data="стипендия")],
                                                [InlineKeyboardButton(text="gpt4",url='https://t.me/GPT4Telegrambot')],
                                              # [InlineKeyboardButton(text="полезные документы📁",callback_data="документы")],
                                              [InlineKeyboardButton(text="Меню Админа👤",callback_data="Меню Админа")]])

kadmin_menu_ss = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="расписание🗓",callback_data="расписание")],
                                              [InlineKeyboardButton(text="дней до стипендии💸",callback_data="стипендия")],
                                                [InlineKeyboardButton(text="gpt4",url='https://t.me/GPT4Telegrambot')],
                                              # [InlineKeyboardButton(text="полезные документы📁",callback_data="документы")],
                                              [InlineKeyboardButton(text="Меню Админа SS👤",callback_data="Меню Админа SS")]])
