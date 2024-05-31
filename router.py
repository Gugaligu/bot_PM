import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import keyboard as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import func
from datetime import date
from aiogram import Bot
TOKEN_API = "6662629827:AAHoIxMjnrbtSLX2W7Pw3ARqbAjf_xq8QbI"
bot1 = Bot(TOKEN_API)

router = Router()



class registrationclass(StatesGroup):
    name=State()
    grope=State()
class del_chel(StatesGroup):
    number=State()
class admin_sdelat(StatesGroup):
    number = State()



#/start бота
@router.message(CommandStart())
async def Start(message: Message):
    if func.prov_registration(message.chat.id):
        level = func.level_admin(message.chat.id)
        if level == 1:
            print(message)
            await message.answer(
                func.menu(message.chat.id, message.chat.first_name, message.chat.username),
                reply_markup=kb.menu)
        elif level == 2:
            await message.answer(
                func.menu(message.chat.id, message.chat.first_name, message.chat.username),
                reply_markup=kb.admin_menu)
        elif level == 3:
            await message.answer(
                func.menu(message.chat.id, message.chat.first_name, message.chat.username),
                reply_markup=kb.admin_menu_ss)
        else:
            await message.message.answer("вы не зарегистрированы\n"
                                             "или не имеете прав (/start)")
    else:
        await message.answer("ㅤㅤЗарегистрируйтесь\n"
                             "===========↓===========",
                             reply_markup=kb.reg)
    await message.delete()

@router.callback_query(F.data=="reg")
async def Filterr(callback: CallbackQuery,state:FSMContext):
    await state.set_state(registrationclass.name)
    await callback.answer("1 этап")
    print(callback.message.message_id)
    await callback.message.edit_text("Отправьте сообщение с именем")
    await callback.message.edit_reply_markup(reply_markup=kb.pust)
    await asyncio.sleep(15)
    await callback.message.delete()

@router.message(registrationclass.name)
async def reg_name(message: Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(registrationclass.grope)
    await message.delete()
    await message.answer("выбери группу",reply_markup=kb.grope)

#ЧТО БЛЯТЬ?
@router.callback_query(registrationclass.grope)
async def reg_grope(callback: CallbackQuery, state: FSMContext):
    await state.update_data(grope=callback.data)
    data = await state.get_data()
    func.registration(callback.message.chat.id,data["name"],data["grope"])
    await state.clear()
    await asyncio.sleep(1)
    level = func.level_admin(callback.message.chat.id)
    if level == 1:
        await callback.message.edit_text(
            func.menu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kb.menu)
    elif level == 2:
        await callback.message.edit_text(
            func.menu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kb.admin_menu)
    elif level == 3:
        await callback.message.edit_text(
            func.menu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kb.admin_menu_ss)
    else:
        await callback.message.edit_text("вы не зарегистрированы\n"
                                         "или не имеете прав (/start)")

@router.callback_query(F.data=="Меню Админа")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text("Меню Админа", reply_markup=kb.funckadmin)

@router.callback_query(F.data=="Меню Админа SS")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text("Меню Админа SS ранга", reply_markup=kb.funckadmin_SS)

@router.callback_query(F.data=="группа")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text(func.admin_vision_grope(callback.message.chat.id),
                                     reply_markup = kb.Backmebu)
@router.callback_query(F.data=="все участники бота")
async def Admin(callback: CallbackQuery):
    await callback.message.edit_text(func.admin_vision(),
                                     reply_markup = kb.Backmebu)

@router.callback_query(F.data=="удалить из группы")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(del_chel.number)
    await callback.message.edit_text(func.admin_vision_grope(callback.message.chat.id)+'\nвведите номер',
                                     reply_markup = kb.delete_user)
@router.message(del_chel.number)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(number=message.text)
        await asyncio.sleep(5)
        await message.delete()

@router.callback_query(F.data=="удалить")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if not(data["number"].isdigit()):
        await state.clear()
        await callback.message.edit_text("введите номер!",reply_markup = kb.Backmebu)
    elif func.level_admin(callback.message.chat.id)<=func.level_admin(func.po_id_tg_id(data["number"])):
        await state.clear()
        await callback.message.edit_text("его уровень выше или равен твоему!", reply_markup=kb.Backmebu)
    else:
        await callback.message.edit_text("ученик удален", reply_markup=kb.Backmebu)
        func.del_in_groupe(callback.message.chat.id,data["number"])
        await state.clear()

@router.callback_query(F.data=="удалить ученика")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(del_chel.number)
    await callback.message.edit_text(func.admin_vision()+'\nвведите номер',
                                     reply_markup = kb.delete_user)
@router.message(del_chel.number)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(number=message.text)
        await asyncio.sleep(5)
        await message.delete()

@router.callback_query(F.data=="удалить ученика")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if not(data["number"].isdigit()):
        await state.clear()
        await callback.message.edit_text("введите номер!",reply_markup = kb.Backmebu)
    elif func.level_admin(callback.message.chat.id)<=func.level_admin(func.po_id_tg_id(data["number"])):
        await state.clear()
        await callback.message.edit_text("его уровень выше или равен твоему!", reply_markup=kb.Backmebu)
    else:
        await callback.message.edit_text("ученик удален", reply_markup=kb.Backmebu)
        func.del_in_groupe(func.po_id_tg_id(data["number"]),data["number"])
        await state.clear()

@router.callback_query(F.data=="сделать админом")
async def Admin(callback: CallbackQuery,state:FSMContext):
    await state.set_state(admin_sdelat.number)
    await callback.message.edit_text(func.admin_vision()+'\nвведите номер',
                                     reply_markup = kb.sdelat_adminom_user)

@router.message(admin_sdelat.number)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(number=message.text)
        await asyncio.sleep(5)
        await message.delete()

@router.callback_query(F.data=="сделать админом пров")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if data["number"].isdigit():
        await callback.message.edit_text("статус выдан", reply_markup=kb.Backmebu)
        func.sdelat_adminom(data["number"])
        await bot1.send_message(func.po_id_tg_id(data["number"]),'вы стали админом!')
        await asyncio.sleep(5)
        await callback.message.delete()
        await state.clear()
    else:
        await state.clear()
        await callback.message.edit_text("введите номер!",reply_markup = kb.Backmebu)


#выбор расписания в меню
@router.callback_query(F.data=="расписание")
async def rasp(callback: CallbackQuery):
    await callback.answer("вы выбрали раписание")
    await callback.message.edit_text("Расписание пар\n"
                                     "-----------------------------------------------\n"
                                     "Понедельник\n"
                                     "  1)История до 38 недели\n"
                                     "  2)Алгебра\n"
                                     "-----------------------------------------------\n"
                                     "Вторник\n"
                                     "  1)Дискретка\n"
                                     "  2)Б.Ж\n"
                                     "  3)История\n"
                                     "  4)Английский\n"
                                     "-----------------------------------------------\n"
                                     "Среда\n"
                                     "  1)История до 38 недели\n"
                                     "  2)Б.Ж\n"
                                     "  3)Программирование\n"
                                     "-----------------------------------------------\n"
                                     "Четверг\n"
                                     "  1)Дискретка\n"
                                     "  2)Русский\n"
                                     "  3)Мат. Анализ\n"
                                     "-----------------------------------------------\n"
                                     "Пятница\n"
                                     "  1)ЭВМ\n"
                                     "  2)Мат. Анализ\n"
                                     "  3)Информатика\n"
                                     "-----------------------------------------------\n"
                                     "Суббота\n"
                                     "  прошли уже\n"
                                     "-----------------------------------------------\n"
                                     "Воскресенье\n"
                                     "  нету")
    await callback.message.edit_reply_markup(reply_markup=kb.Backmebu)

#выбор стипендии в меню
@router.callback_query(F.data=="стипендия")
async def stip(callback: CallbackQuery):
    await callback.answer("вы выбрали дней до стипендии")
    await callback.message.edit_text(func.step_day(),reply_markup=kb.Backmebu)

#выбор ивентов в меню
@router.callback_query(F.data=="ивенты")
async def ivent(callback: CallbackQuery):
    await callback.answer("вы выбрали ивенты")
    await callback.message.edit_text("Ивентов пока нет(")
    await callback.message.edit_reply_markup(reply_markup=kb.Backmebu)

#выбор полезных документов в меню
@router.callback_query(F.data=="документы")
async def dock(callback: CallbackQuery):
    await callback.answer("вы выбрали полезные документы")
    await callback.message.edit_text("полезных документов пока не загружено!")
    await callback.message.edit_reply_markup(reply_markup=kb.Backmebu)

#возврат к меню
@router.callback_query(F.data=="back1")
async def back(callback: CallbackQuery):
    await callback.answer("Back")
    level = func.level_admin(callback.message.chat.id)
    if level == 1:
        await callback.message.edit_text(
            func.menu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kb.menu)
    elif level == 2:
        await callback.message.edit_text(
            func.menu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kb.admin_menu)
    elif level == 3:
        await callback.message.edit_text(
            func.menu(callback.message.chat.id, callback.message.chat.first_name, callback.message.chat.username),
            reply_markup=kb.admin_menu_ss)
    else:
        await callback.message.edit_text("вы не зарегистрированы\n"
                                         "или не имеете прав (/start)")
