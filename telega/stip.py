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
TOKEN_API = "7503899100:AAEcNx9fksbRf2pjOfIRLXf6ZtaLT0fb6BU"
bot1 = Bot(TOKEN_API)
stipend = Router()


@stipend.callback_query(F.data=="стипендия")
async def stip(callback: CallbackQuery):
    await callback.answer("вы выбрали дней до стипендии")
    await callback.message.edit_text(fstep_day(),reply_markup=kBackmebu)

def fstep_day():
    #ищю дней до стипы
    t = date.today()
    tstr = str(t)
    if int(tstr[-2:]) <= 25:
        stip = date.fromisoformat(tstr[:-2] + "25")
    else:
        if int(tstr[5:-3]) + 1 < 10:
            stip = date.fromisoformat(tstr[:5] + "0" + str(int(tstr[5:-3]) + 1) + "-25")
        else:
            stip = date.fromisoformat(tstr[:5] + str(int(tstr[5:-3]) + 1) + "-25")
    daystip=(stip - t).days
    if date.weekday(stip)==5:
        daystip+=2
    elif date.weekday(stip)==6:
        daystip+=1

    dney=""
    if daystip in [1,21,31]:
        dney="день"
    elif daystip in [2,3,4,22,23,24,32]:
        dney="дня"
    else:
        dney="дней"

    if daystip>20:
        com="                           (⊙︿⊙ )"
    elif daystip<=20 and daystip>=10:
        com="                           ༼☯﹏☯༽"
    elif daystip<10 and daystip>4:
        com = "                         (っ╥╯﹏╰╥c)"
    else:
        com = "                         (づ｡◕‿‿◕｡)づ"
    stroke=(f"ㅤㅤㅤㅤДо стипендии {daystip} {dney}!\n"
            f"===============↓↓↓===============\n"
                            +com)
    return stroke

kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти↩️",callback_data="menu")]])
