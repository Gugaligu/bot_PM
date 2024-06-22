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
class set_grop(StatesGroup):
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
    await callback.message.edit_text("Здравствуйте "+data["name"]+"\nвыберите группу или создайте(заявка будет рассматривается)",
                                     reply_markup=fgen_spisok_grop())
    await state.set_state(registrationclass.grope)
    print(callback.message.chat.id)

@registration.callback_query(registrationclass.grope)
async def reg_grope(callback: CallbackQuery, state: FSMContext):
    if callback.data!="+ДОБ ГРУППУ":
        await state.update_data(grope=callback.data)
        data = await state.get_data()
        if fname_in_db(str(data["name"])):
            fregistration(callback.message.chat.id, data["name"], data["grope"])

            await callback.message.edit_text(
                fmenu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
                reply_markup=menu.fkmenu(callback.message.chat.id))
        else:
            await callback.message.edit_text(data["name"] + "-это имя занято или слишком большое",
                                             reply_markup=kBackmebu)
        await state.clear()
    else:
        await state.clear()
        await state.set_state(set_grop.grope)
        await callback.message.edit_text("введите название группы в скобках\nпример:(PM)", reply_markup=sozd_grop)



@registration.message(set_grop.grope)
async def freg_name(message: Message, state: FSMContext):
    await state.update_data(grope=message.text)
    await asyncio.sleep(5)
    await message.delete()

@registration.callback_query(F.data=="отправить на проверку")
async def reg_grope(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data["grope"])
    if (")" in data["grope"]) and ("(" in data["grope"]):
        await callback.message.edit_text("заявка отправлена на рассмотрение и будет принята в течении дня\n(минимально час) вам прийдет уведомление",reply_markup=kBackmebu)
        await bot1.send_message(chat_id="1442714637", text=f'создать группу{data["grope"]} от {callback.message.chat.username} id#{callback.message.chat.id}#',reply_markup=prow_sozd)
    else:
        await callback.message.edit_text("В СКОБКАХ ГРУППУ!",reply_markup=kBackmebu)
    await state.clear()


@registration.callback_query(F.data=="разрешить prow sozd")
async def reg_grope(callback: CallbackQuery):
    t=callback.message.text
    fsozdat_gr_po_razr(t[t.find("(")+1:t.find(")")])
    c = callback.message.text
    ct=c[c.find("#")+1:c.rfind("#")]
    await bot1.send_message(chat_id=str(ct),
                            text=f'группа создана!',
                            reply_markup=udal_soob)
    await callback.message.delete()

@registration.callback_query(F.data == "запретить prow sozd")
async def reg_grope(callback: CallbackQuery):
    await callback.message.delete()

@registration.callback_query(F.data == "убрать сообщение")
async def reg_grope(callback: CallbackQuery):
    await callback.message.delete()

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

def fgen_spisok_grop():
    cursor = db.cursor()
    res = cursor.execute("Select gr FROM spisokgrop").fetchall()
    print(res)
    c = []
    for g in res:
        c.append([InlineKeyboardButton(text=g[0], callback_data=g[0])])
    c.append([InlineKeyboardButton(text="+", callback_data="+ДОБ ГРУППУ")])
    print(c)
    kgrope = InlineKeyboardMarkup(inline_keyboard=c)
    return kgrope

def fsozdat_gr_po_razr(grope):
    cursor = db.cursor()
    res = cursor.execute(f"""INSERT INTO spisokgrop(gr) VALUES("{grope}")""")
    cursor = db.cursor()
    res1 = cursor.execute(f"""CREATE TABLE {grope}_rasp (
                                            id       INTEGER PRIMARY KEY AUTOINCREMENT,
                                            nedel    INTEGER NOT NULL,
                                            day      TEXT    NOT NULL,
                                            para     TEXT    NOT NULL
                                                                     DEFAULT [ ],
                                            grope    TEXT    NOT NULL,
                                            nomerpar INTEGER NOT NULL,
                                            data     TEXT    NOT NULL
                                                                        );""")
    cursor = db.cursor()
    res2 = cursor.execute(f"""CREATE TABLE {grope}_vopr (
                                            id       INTEGER PRIMARY KEY AUTOINCREMENT,
                                            get_data INTEGER NOT NULL,
                                            urok     TEXT    NOT NULL,
                                            vopros   INTEGER,
                                            chelovec TEXT,
                                            photo    TEXT    NOT NULL,
                                            grope    TEXT    NOT NULL
                                                                        );""")
    db.commit()

kreg = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="регистрация",callback_data="reg")]])

kreg_name = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="проверить имя",callback_data="reg_name")],
                                                 [InlineKeyboardButton(text="Назад",callback_data="menu")]])

kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти",callback_data="menu")]])

sozd_grop = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="отправить на проверку",callback_data="отправить на проверку")],
                                                 [InlineKeyboardButton(text="back",callback_data="menu")]])
prow_sozd= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="разрешить",callback_data="разрешить prow sozd")],
                                                 [InlineKeyboardButton(text="запретить",callback_data="запретить prow sozd")]])
udal_soob=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="убрать сообщение",callback_data="убрать сообщение")]])