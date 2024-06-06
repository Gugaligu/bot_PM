import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import keyboard as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import func
import f_raspis
from aiogram import Bot

raspis=Router()

class raspisanie(StatesGroup):
    text=State()


@raspis.callback_query(F.data=="расписание")
async def rasp(callback: CallbackQuery):
    ras=f_raspis.raspisne(callback.message.chat.id)
    await callback.answer("вы выбрали раписание")
    await callback.message.edit_text(
f"""РАСПИСАНИЕ {ras[0][1]} НЕДЕЛИ
---------ПОНЕДЕЛЬНИК---------
1){ras[0][3]}
2){ras[1][3]}
3){ras[2][3]}
4){ras[3][3]}
5){ras[4][3]}
--------------ВТОРНИК--------------
1){ras[5][3]}
2){ras[6][3]}
3){ras[7][3]}
4){ras[8][3]}
5){ras[9][3]}
-----------------СРЕДА-----------------
1){ras[5][3]}
2){ras[6][3]}
3){ras[7][3]}
4){ras[8][3]}
5){ras[9][3]}
----------------ЧЕТВЕРГ----------------
1){ras[5][3]}
2){ras[6][3]}
3){ras[7][3]}
4){ras[8][3]}
5){ras[9][3]}
--------------ПЯТНИЦА--------------
1){ras[5][3]}
2){ras[6][3]}
3){ras[7][3]}
4){ras[8][3]}
5){ras[9][3]}
--------------СУББОТА--------------
1){ras[5][3]}
2){ras[6][3]}
3){ras[7][3]}
""",reply_markup=kb.raspis_menu)
    print(f_raspis.raspisne(callback.message.chat.id))










@raspis.callback_query(F.data == "изменить")
async def rasp(callback: CallbackQuery):
    await callback.answer("изменить")
    await callback.message.edit_text('выберите пункт', reply_markup=kb.izmenit)






@raspis.callback_query(F.data == "создать расписание")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.answer("изменить")
    await callback.message.edit_text('''введите дату 1 недели 
в скобках через тире
    Пример:(2023-09-01)''', reply_markup=kb.sozdat_rasp)
    await state.set_state(raspisanie.text)

@raspis.message(raspisanie.text)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(text=message.text)
        await asyncio.sleep(5)
        await message.delete()

@raspis.callback_query(F.data=="пров созд")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    if func.level_admin(callback.message.chat.id)<2:
        await state.clear()
        await callback.message.edit_text("нужен уровень выше", reply_markup=kb.Backmebu)
    else:
        await callback.message.edit_text("создано", reply_markup=kb.Backmebu)
        f_raspis.gen_ned(data["text"],callback.message.chat.id)
        await state.clear()















@raspis.callback_query(F.data == "изменить расписание")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.answer("изменить")
    await callback.message.edit_text("""
`понедельник`
`вторник`
`среда`
`четверг`
`пятница`
`суббота`
`воскресенье`

Пример ввода(можно копировать)

`одна.                        
(дискретка,1,понедельник,27-38)`

`одна.
(дискретка,1,понедельник,27)`
                                    
`несколько.
(дискретка,1,понедельник,27-38)
(мат анализ,2,понедельник,27-38)
(История,3,понедельник,27-38)
(английский,4,понедельник,27-38)`""",parse_mode='Markdown', reply_markup=kb.izmen_rasp)
    await state.set_state(raspisanie.text)

@raspis.message(raspisanie.text)
async def reg_name(message: Message, state:FSMContext):
        await state.update_data(text=message.text)
        await asyncio.sleep(5)
        await message.delete()

@raspis.callback_query(F.data=="пров изменение")
async def Admin(callback: CallbackQuery,state:FSMContext):
    data = await state.get_data()
    await callback.message.edit_text("изменено", reply_markup=kb.Backmebu)
    f_raspis.dobavit_paru(data["text"],callback.message.chat.id)
    await state.clear()













@raspis.callback_query(F.data == "удалить расписание")
async def rasp(callback: CallbackQuery,state:FSMContext):
    await callback.answer("изменить")
    await callback.message.edit_text('введите....', reply_markup=kb.del_raspis)




