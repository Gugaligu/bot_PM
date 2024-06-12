import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
import sqlite3
import menu
db = sqlite3.connect("../data/db.db")

TOKEN_API = "6662629827:AAHoIxMjnrbtSLX2W7Pw3ARqbAjf_xq8QbI"
bot1 = Bot(TOKEN_API)
registration = Router()

class registrationclass(StatesGroup):
    name=State()
    grope=State()

@registration.message(CommandStart())
async def Start(message: Message):
    if fprov_registration(message.chat.id):
        await message.answer(
            fmenu(message.chat.id, message.chat.first_name, message.chat.username),
            reply_markup=menu.fkmenu(message.chat.id))
    else:
        await message.answer("ㅤㅤЗарегистрируйтесь\n"
                             "===========↓===========",
                             reply_markup=kreg)
    await message.delete()

@registration.callback_query(F.data=="reg")
async def Filterr(callback: CallbackQuery,state:FSMContext):
    await state.set_state(registrationclass.name)
    await callback.message.edit_text("отправьте свое имя\n"
                                     "1)желательно до 11 символов\n"
                                     "2)имя может быть занято так-что пишите с фамилией\n\n"
                                     "Например:Абобикс В.\n\n"
                                     "(сообщение будет сохранено и удалено, не пугайтесь!)",
                                     reply_markup=kreg_name)

@registration.message(registrationclass.name)
async def freg_name(message: Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(registrationclass.grope)
    await asyncio.sleep(5)
    await message.delete()

@registration.callback_query(F.data=="reg_name")
async def Filterr(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    await callback.message.edit_text("Здравствуйте "+data["name"]+"\nвыберите группу",reply_markup=kgrope)
    await state.set_state(registrationclass.grope)

@registration.callback_query(registrationclass.grope)
async def reg_grope(callback: CallbackQuery, state: FSMContext):
    await state.update_data(grope=callback.data)
    data = await state.get_data()
    if fname_in_db(str(data["name"])):
        fregistration(callback.message.chat.id,data["name"],data["grope"])

        await callback.message.edit_text(
            fmenu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=menu.fkmenu(callback.message.chat.id))


    else:
        await callback.message.edit_text(data["name"]+"-это имя занято или слишком большое",
            reply_markup=kBackmebu)
    await state.clear()


def fmenu(id,first_name,username):
    cursor = db.cursor()
    res = cursor.execute("""SELECT * From user WHERE tg_id=(?)""", (id,)).fetchone()
    return "Пользователь\n" \
           f"Имя:{res[2]}\n" \
           f"Имя в тг:{first_name}({username})\n" \
           f"группа:{res[4]}\n" \
           f"Админ:{fnazvanie_admina(res[1])}\n" \
           f"====================\n" \
           f"ㅤㅤМеню функций"
def fprov_registration(id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT tg_id From user WHERE tg_id=(?)""", (id,)).fetchone()
    return res != None
def flevel_admin(id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT admin From user WHERE tg_id=(?)""", (id,)).fetchone()
    if res==None:
        return 0
    return res[0]

def fname_in_db(name):
    cursor = db.cursor()
    res = cursor.execute("""SELECT name From user WHERE name=(?)""", (name,)).fetchone()
    if res==None:
        return True
    else:
        return False

def fregistration(id, name, grope):
    cursor = db.cursor()
    res = cursor.execute("""INSERT INTO user(tg_id,name,grope) VALUES((?),(?),(?))""", (id,name,grope,))
    db.commit()
    pass
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

kreg_name = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="проверить имя",callback_data="reg_name")],
                                                 [InlineKeyboardButton(text="back",callback_data="menu")]])

kgrope = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="ПМ",callback_data="PM")]])

kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти",callback_data="menu")]])
