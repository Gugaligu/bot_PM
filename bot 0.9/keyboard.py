from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/start")],
                                     [KeyboardButton(text="menu")]],
                                        resize_keyboard=True)
menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="расписание",callback_data="расписание")],
                                              [InlineKeyboardButton(text="дней до стипендии",callback_data="стипендия")],
                                              [InlineKeyboardButton(text="ивенты",callback_data="ивенты")],
                                              [InlineKeyboardButton(text="полезные документы",callback_data="документы")]])
Backmebu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="back",callback_data="back1")]])

reg = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="регистрация",callback_data="reg")]])

reg_name = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="проверить имя",callback_data="reg_name")],
                                                 [InlineKeyboardButton(text="back",callback_data="back1")]])

grope = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="ПМ",callback_data="PM")]])

pust = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="....",callback_data=".")]])
#группы
admin_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="расписание",callback_data="расписание")],
                                              [InlineKeyboardButton(text="дней до стипендии",callback_data="стипендия")],
                                              [InlineKeyboardButton(text="ивенты",callback_data="ивенты")],
                                              [InlineKeyboardButton(text="полезные документы",callback_data="документы")],
                                              [InlineKeyboardButton(text="Меню Админа",callback_data="Меню Админа")]])

admin_menu_ss = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="расписание",callback_data="расписание")],
                                              [InlineKeyboardButton(text="дней до стипендии",callback_data="стипендия")],
                                              [InlineKeyboardButton(text="ивенты",callback_data="ивенты")],
                                              [InlineKeyboardButton(text="полезные документы",callback_data="документы")],
                                              [InlineKeyboardButton(text="Меню Админа SS",callback_data="Меню Админа SS")]])

funckadmin=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="группа",callback_data="группа")],
                                              [InlineKeyboardButton(text="все участники бота",callback_data="все участники бота")],
                                              [InlineKeyboardButton(text="удалить из группы",callback_data="удалить из группы")],
                                              [InlineKeyboardButton(text="back",callback_data="back1")]])

funckadmin_SS=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="все участники бота",callback_data="все участники бота")],
                                              [InlineKeyboardButton(text="удалить ученика",callback_data="удалить ученика")],
                                              [InlineKeyboardButton(text="сделать админом",callback_data="сделать админом")],
                                              [InlineKeyboardButton(text="back",callback_data="back1")]])

delete_user=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="удалить")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="back1")]])

delete_user_ss=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="удалитьss")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="back1")]])

sdelat_adminom_user_ss=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="сделать админом пров")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="back1")]])

raspis_menu=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="<-",callback_data="<-"),InlineKeyboardButton(text="изменить",callback_data="изменить"),InlineKeyboardButton(text="->",callback_data="->")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="back1")]])

izmenit=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="создать расписание",callback_data="создать расписание")],
                                                    [InlineKeyboardButton(text="изменить расписание",callback_data="изменить расписание")],
                                                    [InlineKeyboardButton(text="удалить расписание",callback_data="удалить расписание")],
                                                        [InlineKeyboardButton(text="Отмена",callback_data="back1")]])

sozdat_rasp=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="пров созд")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="back1")]])

izmen_rasp=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="пров изменение")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="back1")]])

del_raspis=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проверить Ввод",callback_data="пров удаление")],
                                                  [InlineKeyboardButton(text="Отмена",callback_data="back1")]])
