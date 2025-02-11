import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
import f_admin

TOKEN_API = "7503899100:AAEcNx9fksbRf2pjOfIRLXf6ZtaLT0fb6BU"
bot1 = Bot(TOKEN_API)
admin = Router()

class del_chel(StatesGroup):
    number=State()
class admin_sdelat(StatesGroup):
    number = State()
class name_sdelat(StatesGroup):
    number = State()
    name = State()
class otpr(StatesGroup):
    text = State()


@admin.callback_query(F.data=="настройки учасника")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text("выберите", reply_markup=kudalakk)

@admin.callback_query(F.data=="запрос удаления")
async def Admin(callback: CallbackQuery):
    name=f_admin.fname_in_db2(callback.message.chat.id)
    print(name)
    tg_id_admin=f_admin.find_admin(callback.message.chat.id)
    print(tg_id_admin)
    await bot1.send_message(chat_id=tg_id_admin, text=f"удалить {name} |{callback.message.chat.id}|?", reply_markup=kudalakkprov)
    await callback.message.edit_text("запрос отправлен одному из старост", reply_markup=kBackmebu)

@admin.callback_query(F.data=="разрешить удаление акка")
async def Admin(callback: CallbackQuery):
    text=callback.message.text
    tg_id=text[text.find("|")+1:text.rfind("|")]
    print(tg_id)
    f_admin.fdel_in_groupe2(tg_id)
    await callback.message.edit_text("удален", reply_markup=udal_soob)




@admin.callback_query(F.data=="Меню Админа")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text("Меню Админа", reply_markup=kfunckadmin)



@admin.callback_query(F.data=="Меню Админа SS")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text("Меню Админа SS ранга", reply_markup=kfunckadmin_SS)


@admin.callback_query(F.data=="отпр меседж")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await callback.message.edit_text("отправьте текст", reply_markup=kotpr_ss)
    await state.set_state(otpr.text)



@admin.message(otpr.text)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(text=message.text)
        await asyncio.sleep(5)
        await message.delete()

@admin.callback_query(F.data=="отпр меседж пров")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await callback.message.edit_text("отправлено", reply_markup=kBackmebu)
    data = await state.get_data()
    for id in f_admin.getallid():
        print(id[0],data["text"])
        await bot1.send_message(chat_id=id[0], text=data["text"], reply_markup=udal_soob)







@admin.callback_query(F.data=="посмотреть группы")
async def Admin(callback: CallbackQuery):
    c="список групп\n"
    for i in f_admin.posmotr_group():
        c+=i[0]+"\n"
    await callback.message.edit_text(c, reply_markup=kBackmebu)

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
    await callback.message.edit_text(f_admin.fadmin_vision_grope(callback.message.chat.id) + '\nотправьте номер',
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
        await callback.message.edit_text("отправьте номер!",reply_markup = kBackmebu)
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
    await callback.message.edit_text(f_admin.fadmin_vision() + '\nотправьте номер',
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
        await callback.message.edit_text("отправьте номер!",reply_markup = kBackmebu)
    elif f_admin.flevel_admin(callback.message.chat.id)<= f_admin.flevel_admin(f_admin.fpo_id_tg_id(data["number"])):
        await state.clear()
        await callback.message.edit_text("его уровень выше или равен твоему!", reply_markup=kBackmebu)
    else:
        await callback.message.edit_text("ученик удален", reply_markup=kBackmebu)
        f_admin.fdel_in_groupe(f_admin.fpo_id_tg_id(data["number"]), data["number"])
        await state.clear()




@admin.callback_query(F.data=="добавить старосту")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(admin_sdelat.number)
    await callback.message.edit_text(f_admin.fadmin_vision_grope(callback.message.chat.id) + '\nотправьте номер(не выдавайте детям!)',
                                     reply_markup = ksdelat_adminom_user)

@admin.message(admin_sdelat.number)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(number=message.text)
        await asyncio.sleep(5)
        await message.delete()

@admin.callback_query(F.data=="сделать старостой пров")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    adming=f_admin.grope(callback.message.chat.id)
    userg=f_admin.grope(f_admin.fpo_id_tg_id(data["number"]))
    userlvl=f_admin.flevel_admin(f_admin.fpo_id_tg_id(data["number"]))
    if data["number"].isdigit() and userlvl==1:
        if adming==userg:
            await callback.message.edit_text("статус выдан", reply_markup=kBackmebu)
            f_admin.fsdelat_adminom(data["number"])
            await bot1.send_message(f_admin.fpo_id_tg_id(data["number"]), 'вы стали старостой!',reply_markup=udal_soob)
            await state.clear()
        else:
            await callback.message.edit_text("этот номер не в вашей группе", reply_markup=kBackmebu)
    else:
        await state.clear()
        await callback.message.edit_text("ошибка! отправьте номер или этот человек уже староста",reply_markup = kBackmebu)



@admin.callback_query(F.data=="изменить имя")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(name_sdelat.number)
    await callback.message.edit_text(f_admin.fadmin_vision_grope(callback.message.chat.id) + '\nотправьте номер',
                                     reply_markup = ksdelat_name_user1)

@admin.message(name_sdelat.number)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(number=message.text)
        await asyncio.sleep(5)
        await message.delete()

@admin.callback_query(F.data=="изменить имя пров1")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    adming=f_admin.grope(callback.message.chat.id)
    userg=f_admin.grope(f_admin.fpo_id_tg_id(data["number"]))
    userlvl=f_admin.flevel_admin(f_admin.fpo_id_tg_id(data["number"]))
    await state.set_state(name_sdelat.name)
    if data["number"].isdigit() and userlvl==1:
        if adming==userg:
            await callback.message.edit_text("""отправьте новое имя\n1)желательно до 11 символов\n2)имя может быть занято так-что пишите с фамилией
            Например:Абобикс В.""", reply_markup=ksdelat_name_user2)
        else:
            await callback.message.edit_text("этот номер не в вашей группе", reply_markup=kBackmebu)
    else:
        await state.clear()
        await callback.message.edit_text("ошибка! отправьте номер или этот человек староста",reply_markup = kBackmebu)

@admin.message(name_sdelat.name)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(name=message.text)
        await asyncio.sleep(5)
        await message.delete()

@admin.callback_query(F.data=="изменить имя пров2")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if f_admin.fname_in_db(str(data["name"])) and len(str(data["name"]))<15:
        await bot1.send_message(chat_id=str(f_admin.fpo_id_tg_id(data["number"])),
                                text=f'изменить имя на({data["name"]})?\n|{data["number"]}|',
                                reply_markup=izmen_ime)
        await callback.message.edit_text(text="заявка отправлена пользователю",reply_markup=kBackmebu)
    else:
        await callback.message.edit_text(data["name"] + "-это имя занято или слишком большое",
                                         reply_markup=kBackmebu)
    await state.clear()

@admin.callback_query(F.data=="разрешить изменить")
async def Admin(callback: CallbackQuery,state:FSMContext):
    t=callback.message.text
    name = t[t.find("(") + 1:t.find(")")]
    number = t[t.find("|") + 1:t.rfind("|")]
    f_admin.fupdatename(name,number)
    await callback.message.edit_text(text="имя сохранено", reply_markup=udal_soob)


@admin.callback_query(F.data=="сделать админом")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(admin_sdelat.number)
    await callback.message.edit_text(f_admin.fadmin_vision() + '\nотправьте номер (пример:10)',
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
        await bot1.send_message(f_admin.fpo_id_tg_id(data["number"]), 'вы стали старостой!',reply_markup=udal_soob)
        await state.clear()
    else:
        await state.clear()
        await callback.message.edit_text("отправьте номер!",reply_markup = kBackmebu)


@admin.callback_query(F.data == "убрать сообщение")
async def reg_grope(callback: CallbackQuery):
    await callback.message.delete()


izmen_ime=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="разрешить✅",callback_data="разрешить изменить")],
                                                 [InlineKeyboardButton(text="запретить❌",callback_data="запретить prow sozd")]])

kBackmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="назад ↩️", callback_data="menu")]])

ksdelat_adminom_user_ss=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="сделать админом пров")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])

ksdelat_adminom_user=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="сделать старостой пров")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])

kdelete_user_ss=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="удалитьss")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])

kdelete_user=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="удалить")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])

kfunckadmin=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="группа",callback_data="группа")],
                                              [InlineKeyboardButton(text="все участники бота",callback_data="все участники бота")],
                                               [InlineKeyboardButton(text="добавить старосту",callback_data="добавить старосту")],
                                                [InlineKeyboardButton(text="изменить имя",callback_data="изменить имя")],
                                              [InlineKeyboardButton(text="удалить из группы",callback_data="удалить из группы")],
                                              [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])

kfunckadmin_SS=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="все участники бота",callback_data="все участники бота")],
                                              [InlineKeyboardButton(text="удалить ученика",callback_data="удалить ученика")],
                                              [InlineKeyboardButton(text="посмотреть группы",callback_data="посмотреть группы")],
                                              [InlineKeyboardButton(text="сделать админом",callback_data="сделать админом")],
                                            [InlineKeyboardButton(text="отправить меседж",callback_data="отпр меседж")],
                                              [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])

ksdelat_name_user1=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="изменить имя пров1")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])
ksdelat_name_user2=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="изменить имя пров2")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])
kotpr_ss=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="отпр меседж пров")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])

udal_soob=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="убрать сообщение❌",callback_data="убрать сообщение")]])



kudalakk=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="удалить аккаунт?",callback_data="запрос удаления")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])

kudalakkprov=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="удалить✅",callback_data="разрешить удаление акка")],
                                                 [InlineKeyboardButton(text="не удалять❌",callback_data="запретить prow sozd")]])


knastroiki=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="выйти из группы\n(удалить аккаунт)",callback_data="выйти из группы")],
                                                  [InlineKeyboardButton(text="назад ↩️",callback_data="menu")]])
