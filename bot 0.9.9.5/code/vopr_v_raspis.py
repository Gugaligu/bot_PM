import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
import sqlite3
db = sqlite3.connect("../data/db.db")

TOKEN_API = "6662629827:AAHoIxMjnrbtSLX2W7Pw3ARqbAjf_xq8QbI"
bot1 = Bot(TOKEN_API)
voprosik = Router()

class voprstate(StatesGroup):
    nedel = State()
    days = State()
    urok = State()
    count_vopr = State()

@voprosik.callback_query(F.data=="создать вопросы vopr")
async def rasp(callback: CallbackQuery,state:FSMContext):
    t=callback.message.text
    await state.set_state(voprstate.nedel)
    print(t[-9:-7])
    await state.update_data(nedel=t[-9:-7])
    await callback.message.edit_text("выберите день", reply_markup=day)

@voprosik.callback_query(F.data.in_({"понедельник vopr", "вторник vopr","среда vopr", "четверг vopr", "пятница vopr","суббота vopr"}))
async def rasp(callback: CallbackQuery,state:FSMContext):
    t=callback.data
    print(t[:-5])
    await state.set_state(voprstate.days)
    await state.update_data(days=t[:-5])
    date1 = await state.get_data()
    await callback.message.edit_text("выберите urok", reply_markup=fgen_spisok_para(callback.message.chat.id,date1["nedel"],date1["days"]))

@voprosik.callback_query(F.data[0]=="#")
async def rasp(callback: CallbackQuery,state:FSMContext):
    t=callback.data[1:]
    await state.set_state(voprstate.urok)
    print(t)
    await state.update_data(urok=t)
    await callback.message.edit_text("отправьте количество вопросов", reply_markup=pr_colvo_vopr)
    await state.set_state(voprstate.count_vopr)

@voprosik.message(voprstate.count_vopr)
async def freg_name(message: Message, state:FSMContext):
    await state.update_data(name=message.text)
    await asyncio.sleep(5)
    await message.delete()

@voprosik.callback_query(F.data=="pr_colvo")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.message.edit_text("недоделал", reply_markup=kBackmebu)







# @vopr.callback_query(F.data=="вопросы vopr")
# async def rasp(callback: CallbackQuery):
#     await callback.message.edit_text("выберите вопросы", reply_markup=gen_vopr)

def fgen_spisok_para(tg_id,nedel,days):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={tg_id}").fetchone())[0]
    cursor = db.cursor()
    print(grope, nedel, days)
    res = cursor.execute(f"Select para FROM raspisanie WHERE (grope='{grope}' and nedel={nedel} and day='{days}')").fetchall()
    print(res)
    c = []
    for g in res:
        c.append([InlineKeyboardButton(text=g[0], callback_data="#"+g[0])])
    c.append([InlineKeyboardButton(text="Отмена", callback_data="menu")])
    print(c)
    gen_urok = InlineKeyboardMarkup(inline_keyboard=c)
    return gen_urok

day = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="понедельник",callback_data="понедельник vopr")],
                                            [InlineKeyboardButton(text="вторник",callback_data="вторник vopr")],
                                            [InlineKeyboardButton(text="среда",callback_data="среда vopr")],
                                            [InlineKeyboardButton(text="четверг",callback_data="четверг vopr")],
                                            [InlineKeyboardButton(text="пятница",callback_data="пятница vopr")],
                                            [InlineKeyboardButton(text="суббота",callback_data="суббота vopr")],
                                            [InlineKeyboardButton(text="Отмена",callback_data="menu")]])
kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти", callback_data="menu")]])
pr_colvo_vopr = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="проверить", callback_data="pr_colvo")],
                                            [InlineKeyboardButton(text="Отмена",callback_data="menu")]])