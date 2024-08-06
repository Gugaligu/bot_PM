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
    photo_id = State()

class voprvibral(StatesGroup):
    vopr= State()
    urok= State()
class voprdelete(StatesGroup):
    vopr= State()
    urok= State()


@voprosik.callback_query(F.data=="vopr_v_raspis")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.message.edit_text("выберите",reply_markup=vopr_v_raspis(flevel_admin(callback.message.chat.id)))
    t = callback.message.text
    await state.set_state(voprstate.nedel)
    await state.update_data(nedel=t[-9:-7])

@voprosik.callback_query(F.data=="создать вопросы vopr")
async def rasp(callback: CallbackQuery,state:FSMContext):
    if count_vopr_in_table(callback.message.chat.id)<=3000:
        await callback.message.edit_text(f"выберите день\n"
        f"Ваше доступное количество вопросов({count_vopr_in_table(callback.message.chat.id)} из 3000)", reply_markup=day)
    else:
        await callback.message.edit_text("удалите вопросы лимит превышен",reply_markup=kBackmebu)


@voprosik.callback_query(F.data.in_({"понедельник vopr", "вторник vopr","среда vopr", "четверг vopr", "пятница vopr","суббота vopr"}))
async def rasp(callback: CallbackQuery,state:FSMContext):
    t=callback.data
    print(t[:-5])
    await state.set_state(voprstate.days)
    await state.update_data(days=t[:-5])
    date1 = await state.get_data()
    await callback.message.edit_text("выберите урок", reply_markup=fgen_spisok_para(callback.message.chat.id,date1["nedel"],date1["days"]))

@voprosik.callback_query(F.data[0]=="#")
async def rasp(callback: CallbackQuery,state:FSMContext):
    t=callback.data[1:]
    await state.set_state(voprstate.urok)
    print(t)
    await state.update_data(urok=t)
    await callback.message.edit_text("отправьте количество вопросов(меньше 120)", reply_markup=pr_colvo_vopr)
    await state.set_state(voprstate.count_vopr)

@voprosik.message(voprstate.count_vopr)
async def freg_name(message: Message, state:FSMContext):
    await state.update_data(count_vopr=message.text)
    await asyncio.sleep(5)
    await message.delete()

@voprosik.callback_query(F.data=="pr_colvo")
async def rasp(callback: CallbackQuery,state:FSMContext):
    date1 = await state.get_data()
    if int(date1["count_vopr"])<=120:
        await callback.message.edit_text("отправьте фото вопросов", reply_markup=prov_photo)
        await state.set_state(voprstate.photo_id)
    else:
        await callback.message.edit_text("слишком большое число вопросов", reply_markup=kBackmebu)
@voprosik.message(voprstate.photo_id)
async def freg_name(message: Message, state:FSMContext):
    p=(str(message.photo[-1])[9:])
    p1=p[:p.find("'")]
    await state.update_data(photo_id=p1)
    print(p1)
    await asyncio.sleep(5)
    await message.delete()




@voprosik.callback_query(F.data=="pr_photo")
async def rasp(callback: CallbackQuery,state:FSMContext):
    date1 = await state.get_data()
    await callback.message.edit_text(f"создано\nнеделя {date1['nedel']},\nурок {date1['urok']},\nкол-во вопросов {date1['count_vopr']}", reply_markup=kBackmebu)
    sozdat_vopr(date1['nedel'],date1['urok'],date1['count_vopr'],date1['photo_id'],callback.message.chat.id)
# разнообразие обеспечивается количеством вопросов тоесть к уроку приписывать количество каждый может забрать
# хоть все вопросы но только 1 раз не(1:Артем,Артем,Артем.....)
# генерируем кнопки(номера вопросов при нажатии повторно бронь анулируется)

@voprosik.callback_query(F.data[0]=="?")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.answer(callback.data[1:])
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={callback.message.chat.id}").fetchone())[0]
    grope += "_vopr"
    cursor = db.cursor()
    photo_ = cursor.execute(f"""SELECT photo From {grope} WHERE urok=(?)""", (str(callback.data[1:]),)).fetchone()
    cursor = db.cursor()
    caption_ = cursor.execute(f"""SELECT vopros,chelovec From {grope} WHERE urok=(?)""", (str(callback.data[1:]),)).fetchall()
    cap="список:\n"
    for vopr in caption_:
        cap+=f"{vopr[0]}:{vopr[1]}\n"
    cap+="\nвыберите:"
    cap=cap.replace("None","")
    await callback.message.answer_photo(photo=photo_[0],
                                        reply_markup=vibor_vopr(callback.data[1:],callback.message.chat.id),
                                        caption=cap
                    )
    await state.clear()
    await state.set_state(voprvibral.urok)
    await state.update_data(urok=callback.data[1:])
    await state.set_state(voprvibral.vopr)

@voprosik.callback_query(voprvibral.vopr)
async def rasp(callback: CallbackQuery,state:FSMContext):
    date1 = await state.get_data()
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={callback.message.chat.id}").fetchone())[0]
    grope += "_vopr"
    cursor = db.cursor()
    vibral = cursor.execute(f"""SELECT chelovec From {grope} WHERE vopros=(?) and urok=(?)""", (int(callback.data),str(date1["urok"]),)).fetchone()
    cursor = db.cursor()
    name = cursor.execute("""SELECT name From user WHERE tg_id=(?)""", (int(callback.message.chat.id),)).fetchone()
    #вытащил из массивов
    name2 = name[0]
    vibral2 = vibral[0]
    if vibral2==None:
        vibral2=""
    print(vibral[0],name)
    # он выбирал уже?
    if name2 in vibral2:
        #удалил из списка
        nameminus=vibral2.replace((name2+", "),"")
        cursor = db.cursor()
        udal = cursor.execute(f"""UPDATE {grope} SET chelovec=(?) WHERE vopros=(?) and urok=(?)""",
                              (nameminus,int(callback.data),str(date1["urok"]),)).fetchone()
        db.commit()
    else:
        #добавил в список
        nameplus = vibral2+name2+", "
        cursor = db.cursor()
        dobav = cursor.execute(f"""UPDATE {grope} SET chelovec=(?) WHERE vopros=(?) and urok=(?)""",
                              (nameplus, int(callback.data), str(date1["urok"]),)).fetchone()
        db.commit()
    # обновляю список
    cursor = db.cursor()
    caption_ = cursor.execute(f"""SELECT vopros,chelovec From {grope} WHERE urok=(?)""",
                              (str(date1["urok"]),)).fetchall()
    cap = "список:\n"
    print(caption_)
    for vopr in caption_:
        cap += f"{vopr[0]}:{vopr[1]}\n"
    cap += "\nвыберите:"
    cap = cap.replace("None", "")
    print(cap)
    await callback.message.edit_caption(caption=cap,reply_markup=vibor_vopr(date1["urok"],callback.message.chat.id))



@voprosik.callback_query(F.data=="вопросы vopr")
async def rasp(callback: CallbackQuery):
    await callback.message.edit_text("выберите вопросы", reply_markup=gen_sozdanie_voprosi(callback.message.chat.id))

@voprosik.callback_query(F.data == "убрать сообщение")
async def reg_grope(callback: CallbackQuery):
    await callback.message.delete()

@voprosik.callback_query(F.data == "удалить вопрос")
async def reg_grope(callback: CallbackQuery,state:FSMContext):
    await state.set_state(voprdelete.urok)
    await callback.message.edit_text("выберите вопросы которые нужно удалить",
                                     reply_markup=gen_sozdanie_voprosi_delete(callback.message.chat.id))

@voprosik.callback_query(voprdelete.urok)
async def reg_grope(callback: CallbackQuery,state:FSMContext):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={callback.message.chat.id}").fetchone())[0]
    grope += "_vopr"
    cursor = db.cursor()
    res1 = cursor.execute(f"""delete FROM {grope} WHERE urok=(?)""", (callback.data,))
    db.commit()
    await callback.message.edit_text("вопрос удален",
                                     reply_markup=kBackmebu)
    await state.clear()












def flevel_admin(tg_id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT admin From user WHERE tg_id=(?)""", (tg_id,)).fetchone()
    if res==None:
        return 0
    return res[0]


def vopr_v_raspis(level):
    if level>1:
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="вопросы❔",callback_data="вопросы vopr")],
                                                     [InlineKeyboardButton(text="создать вопросы➕",callback_data="создать вопросы vopr")],
                                                     [InlineKeyboardButton(text="удалить вопросы🗑",callback_data="удалить вопрос")],
                                                        [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="вопросы❔",callback_data="вопросы vopr")],
                             [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])


def fgen_spisok_para(tg_id,nedel,days):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={tg_id}").fetchone())[0]
    grope1 = grope+"_rasp"
    cursor = db.cursor()
    print(grope, nedel, days)
    res = cursor.execute(f"Select para FROM {grope1} WHERE grope='{grope}' and nedel={nedel} and day='{days}'").fetchall()
    print(res)
    c = []
    for g in res:
        c.append([InlineKeyboardButton(text=g[0], callback_data="#"+g[0])])
    c.append([InlineKeyboardButton(text="Отмена↩️", callback_data="menu")])
    print(c)
    gen_urok = InlineKeyboardMarkup(inline_keyboard=c)
    return gen_urok


def gen_sozdanie_voprosi_delete(tg_id):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={tg_id}").fetchone())[0]
    grope += "_vopr"
    cursor = db.cursor()
    res = cursor.execute(f"Select get_data,urok FROM {grope}").fetchall()
    c = []
    b=[]
    for g in res:
        if g[1] in b:
            continue
        b.append(g[1])
        c.append([InlineKeyboardButton(text=f"{g[0]} неделя {g[1]}", callback_data=g[1])])
    c.append([InlineKeyboardButton(text="Отмена↩️", callback_data="menu")])
    gen_vopr = InlineKeyboardMarkup(inline_keyboard=c)
    return gen_vopr
def gen_sozdanie_voprosi(tg_id):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={tg_id}").fetchone())[0]
    grope += "_vopr"
    cursor = db.cursor()
    res = cursor.execute(f"Select get_data,urok FROM {grope}").fetchall()
    c = []
    b=[]
    for g in res:
        if g[1] in b:
            continue
        b.append(g[1])
        c.append([InlineKeyboardButton(text=f"{g[0]} неделя {g[1]}", callback_data="?"+g[1])])
    c.append([InlineKeyboardButton(text="Отмена↩️", callback_data="menu")])
    gen_vopr = InlineKeyboardMarkup(inline_keyboard=c)
    return gen_vopr
def sozdat_vopr(nedel,urok,count,photo,tg_id):
    cursor = db.cursor()
    grope = cursor.execute("""SELECT grope From user WHERE tg_id=(?)""", (tg_id,)).fetchone()[0]
    cursor = db.cursor()
    grope2 = (cursor.execute(f"Select grope FROM user where tg_id={tg_id}").fetchone())[0]
    grope2 += "_vopr"
    urok= f"{urok} {str(count)} вопросов"
    for i in range(int(count)):
        print(i)
        i+=1
        cursor = db.cursor()
        res = cursor.execute(f"""INSERT INTO {grope2}(get_data,urok,vopros,photo,grope) VALUES((?),(?),(?),(?),(?))""",
                             (int(nedel),str(urok),i,str(photo),str(grope),))

    db.commit()
    pass
def count_vopr_in_table(tg_id):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={tg_id}").fetchone())[0]
    grope += "_vopr"
    cursor = db.cursor()
    count = cursor.execute(f"""SELECT COUNT (*) FROM {grope}""").fetchone()
    return count[0]


def vibor_vopr(urok,tg_id):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={tg_id}").fetchone())[0]
    grope+="_vopr"
    cursor = db.cursor()
    vop = cursor.execute(f"Select vopros FROM {grope} where urok=(?)",(str(urok),)).fetchall()
    c = []
    b =[]
    re=0
    for g in vop:
        re+=1
        b.append((InlineKeyboardButton(text=str(g[0]), callback_data=str(g[0]))))
        if re==5:
            c.append(b)
            b=[]
            re=0
    c.append([InlineKeyboardButton(text="убрать сообщение❌",callback_data="убрать сообщение")])
    vibor_vopr = InlineKeyboardMarkup(inline_keyboard=c)
    return vibor_vopr



day = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="понедельник",callback_data="понедельник vopr")],
                                            [InlineKeyboardButton(text="вторник",callback_data="вторник vopr")],
                                            [InlineKeyboardButton(text="среда",callback_data="среда vopr")],
                                            [InlineKeyboardButton(text="четверг",callback_data="четверг vopr")],
                                            [InlineKeyboardButton(text="пятница",callback_data="пятница vopr")],
                                            [InlineKeyboardButton(text="суббота",callback_data="суббота vopr")],
                                            [InlineKeyboardButton(text="Отмена",callback_data="menu")]])
kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти↩️", callback_data="menu")]])
pr_colvo_vopr = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="проверить✅", callback_data="pr_colvo")],
                                            [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])
prov_photo = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="проверить✅", callback_data="pr_photo")],
                                            [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])