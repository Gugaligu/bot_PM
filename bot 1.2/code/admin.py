import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
import f_admin

TOKEN_API = "6662629827:AAHoIxMjnrbtSLX2W7Pw3ARqbAjf_xq8QbI"
bot1 = Bot(TOKEN_API)
admin = Router()

class del_chel(StatesGroup):
    number=State()
class admin_sdelat(StatesGroup):
    number = State()

@admin.callback_query(F.data=="Меню Админа")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text("Меню Админа", reply_markup=kfunckadmin)



@admin.callback_query(F.data=="Меню Админа SS")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text("Меню Админа SS ранга", reply_markup=kfunckadmin_SS)

@admin.callback_query(F.data=="группа")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text(f_admin.fadmin_vision_grope(callback.message.chat.id),
                                     reply_markup = kBackmebu)
@admin.callback_query(F.data=="все участники бота")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text(f_admin.fadmin_vision(),
                                     reply_markup = kBackmebu)






















@admin.callback_query(F.data=="удалить из группы")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(del_chel.number)
    await callback.message.edit_text(f_admin.fadmin_vision_grope(callback.message.chat.id) + '\nвведите номер',
                                     reply_markup = kdelete_user)
@admin.message(del_chel.number)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(number=message.text)
        await asyncio.sleep(5)
        await message.delete()

@admin.callback_query(F.data=="удалить")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if not(data["number"].isdigit()):
        await state.clear()
        await callback.message.edit_text("введите номер!",reply_markup = kBackmebu)
    elif f_admin.flevel_admin(callback.message.chat.id)<= f_admin.flevel_admin(f_admin.fpo_id_tg_id(data["number"])):
        await state.clear()
        await callback.message.edit_text("его уровень выше или равен твоему!", reply_markup=kBackmebu)
    else:
        await callback.message.edit_text("ученик удален", reply_markup=kBackmebu)
        f_admin.fdel_in_groupe(callback.message.chat.id, data["number"])
        await state.clear()
























@admin.callback_query(F.data=="удалить ученика")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(del_chel.number)
    await callback.message.edit_text(f_admin.fadmin_vision() + '\nвведите номер',
                                     reply_markup = kdelete_user_ss)
@admin.message(del_chel.number)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(number=message.text)
        await asyncio.sleep(5)
        await message.delete()

@admin.callback_query(F.data=="удалитьss")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if not(data["number"].isdigit()):
        await state.clear()
        await callback.message.edit_text("введите номер!",reply_markup = kBackmebu)
    elif f_admin.flevel_admin(callback.message.chat.id)<= f_admin.flevel_admin(f_admin.fpo_id_tg_id(data["number"])):
        await state.clear()
        await callback.message.edit_text("его уровень выше или равен твоему!", reply_markup=kBackmebu)
    else:
        await callback.message.edit_text("ученик удален", reply_markup=kBackmebu)
        f_admin.fdel_in_groupe(f_admin.fpo_id_tg_id(data["number"]), data["number"])
        await state.clear()













@admin.callback_query(F.data=="сделать админом")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(admin_sdelat.number)
    await callback.message.edit_text(f_admin.fadmin_vision() + '\nвведите номер',
                                     reply_markup = ksdelat_adminom_user_ss)

@admin.message(admin_sdelat.number)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(number=message.text)
        await asyncio.sleep(5)
        await message.delete()

@admin.callback_query(F.data=="сделать админом пров")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if data["number"].isdigit():
        await callback.message.edit_text("статус выдан", reply_markup=kBackmebu)
        f_admin.fsdelat_adminom(data["number"])
        await bot1.send_message(f_admin.fpo_id_tg_id(data["number"]), 'вы стали админом!',reply_markup=udal_soob)
        await state.clear()
    else:
        await state.clear()
        await callback.message.edit_text("введите номер!",reply_markup = kBackmebu)


@admin.callback_query(F.data == "убрать сообщение")
async def reg_grope(callback: CallbackQuery):
    await callback.message.delete()




kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти", callback_data="menu")]])

ksdelat_adminom_user_ss=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="сделать админом пров")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="menu")]])

kdelete_user_ss=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="удалитьss")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="menu")]])

kdelete_user=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="удалить")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="menu")]])

kfunckadmin=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="группа",callback_data="группа")],
                                              [InlineKeyboardButton(text="все участники бота",callback_data="все участники бота")],
                                              [InlineKeyboardButton(text="удалить из группы",callback_data="удалить из группы")],
                                              [InlineKeyboardButton(text="back",callback_data="menu")]])

kfunckadmin_SS=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="все участники бота",callback_data="все участники бота")],
                                              [InlineKeyboardButton(text="удалить ученика",callback_data="удалить ученика")],
                                              [InlineKeyboardButton(text="сделать админом",callback_data="сделать админом")],
                                              [InlineKeyboardButton(text="back",callback_data="menu")]])

udal_soob=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="убрать сообщение",callback_data="убрать сообщение")]])