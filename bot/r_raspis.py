import asyncio
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
import f_raspis
import datetime

raspis=Router()
time = datetime.datetime.now()
class raspisanie(StatesGroup):
    text=State()


@raspis.callback_query(F.data=="расписание")
async def rasp(callback: CallbackQuery):
    ras= f_raspis.raspisne(callback.message.chat.id)
    c=0
    if ras=="zero":
        await callback.message.edit_text("лето! (расписание станет доступно в сентябре)", reply_markup=kkBackmebu)
    elif len(ras)!=0:
        await callback.answer("вы выбрали раписание")
        c=str(ras[0][1])
        level = f_raspis.flevel_admin(callback.message.chat.id)
        raspis_menu_strelka = f_raspis.level_dly_menu(level, c)
        await callback.message.edit_text(f_raspis.vivod_ras(ras), reply_markup=raspis_menu_strelka,parse_mode='HTML')
    else:
        await callback.message.edit_text(f"расписания {f_raspis.grope(callback.message.chat.id)} несуществует создайте его", reply_markup=ksozdat_ras1)






@raspis.callback_query(F.data[:3].in_({"рас"}))
async def rasp(callback: CallbackQuery):
    c=callback.data[3:]
    ras = f_raspis.raspisnie_strelochki(callback.message.chat.id, c)
    level = f_raspis.flevel_admin(callback.message.chat.id)
    raspis_menu_strelka = f_raspis.level_dly_menu(level, c)
    if len(ras) != 0:
        await callback.message.edit_text(f_raspis.vivod_ras(ras), reply_markup=raspis_menu_strelka,parse_mode='HTML')
    elif c < 1 and callback.data[:-2] == "<-" or callback.data[:-2] == "<":
        await callback.message.edit_text("такой недели нет", reply_markup=kBackmebu)
    elif c > 45 and callback.data[:-2] == ">-" or callback.data[:-2] == ">":
        await callback.message.edit_text("такой недели нет", reply_markup=kBackmebu)
    else:
        await callback.message.edit_text(
            f"расписания {f_raspis.grope(callback.message.chat.id)} несуществует создайте его",
            reply_markup=ksozdat_ras1)
    await asyncio.sleep(1)












#<-
@raspis.callback_query(F.data[:-2].in_({'<-', '<', '>-', '>'}))
async def rasp(callback: CallbackQuery):
    print(callback.data)
    if callback.data[:-2]=="<-":
        c=int(callback.data[-2:])-1
    elif callback.data[:-2]=="<":
        c = int(callback.data[-1]) - 1
    elif callback.data[:-2]==">-":
        c = int(callback.data[-2:]) + 1
    elif callback.data[:-2]==">":
        c = int(callback.data[-1]) + 1
    else:
        c=""
        await callback.message.edit_text("чтото пошло нетак",reply_markup=kBackmebu)
    ras= f_raspis.raspisnie_strelochki(callback.message.chat.id, c)
    level = f_raspis.flevel_admin(callback.message.chat.id)
    raspis_menu_strelka= f_raspis.level_dly_menu(level, c)
    if len(ras) != 0:
        await callback.message.edit_text(f_raspis.vivod_ras(ras), reply_markup=raspis_menu_strelka,parse_mode='HTML')
    elif c<1 and callback.data[:-2]=="<-" or callback.data[:-2]=="<":
        await callback.message.edit_text("такой недели нет", reply_markup=kBackmebu)
    elif c > 45 and callback.data[:-2]==">-" or callback.data[:-2]==">":
        await callback.message.edit_text("такой недели нет",reply_markup=kBackmebu)
    else:
        await callback.message.edit_text(
                f"расписания {f_raspis.grope(callback.message.chat.id)} несуществует создайте его",
                reply_markup=ksozdat_ras1)
    await asyncio.sleep(1)


























@raspis.callback_query(F.data == "изменить")
async def rasp(callback: CallbackQuery):
    await callback.answer("изменить")
    await callback.message.edit_text('выберите пункт', reply_markup=kizmenit)






@raspis.callback_query(F.data == "создать расписание нач")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.answer("изменить")
    await callback.message.edit_text('''отправьте дату 1 недели 
в скобках через тире (нужно быть администратором)
    Пример:(2023-09-01)''', reply_markup=ksozdat_ras2)
    await state.set_state(raspisanie.text)

@raspis.message(raspisanie.text)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(text=message.text)
        await asyncio.sleep(5)
        await message.delete()

@raspis.callback_query(F.data == "Автоматическое создание")
async def Admin(callback: CallbackQuery,state:FSMContext):
    c = 0
    year_fix = datetime.date.today().year
    if datetime.date.today().month < 6:
        year_fix -= 1

    if f_raspis.t_day(datetime.date(year_fix, 9, 1).weekday()) == "воскресенье":
        c = 1
    if datetime.date.today().month > 6:
        d = datetime.date(datetime.date.today().year, 9, 1 + c)
    else:
        d = datetime.date(datetime.date.today().year - 1, 9, 1 + c)

    await state.update_data(text="("+str(d)+")")
    data = await state.get_data()
    if f_raspis.flevel_admin(callback.message.chat.id)<2:
        await state.clear()
        await callback.message.edit_text("нужен уровень выше", reply_markup=kBackmebu)
    else:
        await callback.message.edit_text("создано", reply_markup=kBackmebu)
        f_raspis.gen_ned(data["text"], callback.message.chat.id)
        await state.clear()

@raspis.callback_query(F.data=="пров созд")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if f_raspis.flevel_admin(callback.message.chat.id)<2:
        await state.clear()
        await callback.message.edit_text("нужен уровень выше", reply_markup=kBackmebu)
    else:
        await callback.message.edit_text("создано", reply_markup=kBackmebu)
        f_raspis.gen_ned(data["text"], callback.message.chat.id)
        await state.clear()















@raspis.callback_query(F.data == "изменить расписание")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.answer("изменить")
    await callback.message.edit_text("""
cайт для упрощенного создания:https://gugaligu.github.io/raspisanie.github.io/

Пример ввода(можно копировать. Каждое изменение писать в квадратных скобках,вместо запятых нужно ставить+)

`понедельник`
`вторник`
`среда`
`четверг`
`пятница`
`суббота`
`воскресенье`

  название, номер, день, неделя
`[дискретка,1,понедельник,25-32+34+35+37-39]`


отправьте сообщение""",parse_mode='Markdown', reply_markup=kizmen_rasp)
    await state.set_state(raspisanie.text)

@raspis.message(raspisanie.text)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(text=message.text)
        await asyncio.sleep(5)
        await message.delete()

@raspis.callback_query(F.data=="пров изменение")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    await callback.message.edit_text("изменено", reply_markup=kBackmebu)
    f_raspis.dobavit_paru(data["text"], callback.message.chat.id)
    await state.clear()












@raspis.callback_query(F.data == "удалить расписание")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.answer("изменить")
    await callback.message.edit_text('вы уверены?', reply_markup=kdel_raspis)
@raspis.callback_query(F.data == "пров удаление")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.answer("изменить")
    await callback.message.edit_text('расписание удалено', reply_markup=kBackmebu)
    f_raspis.del_in_groupe(callback.message.chat.id)


kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти↩️", callback_data="menu")]])

ksozdat_ras1=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="создать расписание➕",callback_data="создать расписание нач")],
                                                  [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])

ksozdat_ras2=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод✅",callback_data="пров созд")],
                                                    [InlineKeyboardButton(text="Автоматическое создание",callback_data="Автоматическое создание")],
                                                  [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])

kdel_raspis=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="УДАЛИТЬ🗑",callback_data="пров удаление")],
                                                  [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])

kizmen_rasp=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод✅",callback_data="пров изменение")],
                                                [types.InlineKeyboardButton(text="сайт для создания",web_app=WebAppInfo(url="https://gugaligu.github.io/raspisanie.github.io/"))],
                                                  [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])

kizmenit=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="изменить расписание🗓",callback_data="изменить расписание")],
                                                    [InlineKeyboardButton(text="удалить расписание🗑",callback_data="удалить расписание")],
                                                        [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])
kkBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="удалить расписание🗑",callback_data="удалить расписание")],[InlineKeyboardButton(text="Выйти↩️", callback_data="menu")]])
