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

    dney=""
    if daystip in [1,21,31]:
        dney="день"
    elif daystip in [2,3,4,22,23,24]:
        dney="дня"
    else:
        dney="дней"

    if daystip>20:
        com="ㅤㅤㅤЕще очинь долго((( ТРЭШ"
    elif daystip<=20 and daystip>=10:
        com="ㅤЕще примерно пол месяца УЖАС :("
    elif daystip<10 and daystip>4:
        com = "Еще примерно недельку протянуть Ура!!!!"
    else:
        com = "ㅤㅤ   Уже совсем скоро!!!"
    stroke=(f"ㅤㅤㅤㅤДо стипендии {daystip} {dney}!\n"
            f"===============↓↓↓===============\n"
                            +com)
    return stroke

kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти",callback_data="menu")]])