import datetime
import sqlite3
db = sqlite3.connect("../data/db.db")
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)

def flevel_admin(tg_id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT admin From user WHERE tg_id=(?)""", (tg_id,)).fetchone()
    if res==None:
        return 0
    return res[0]


def level_dly_menu(level,c):
    if level>1:
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="<-", callback_data=("<-"+str(c))),
                                                        InlineKeyboardButton(text="изменить",callback_data="изменить"),
                                                        InlineKeyboardButton(text="->", callback_data=(">-"+str(c)))],
                                                     [InlineKeyboardButton(text="вопросы❔",callback_data="vopr_v_raspis")],
                                                        [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="<-", callback_data=("<-" + str(c))),
                              InlineKeyboardButton(text="Отмена↩️",callback_data="menu"),
                              InlineKeyboardButton(text="->", callback_data=(">-" + str(c)))],
                                [InlineKeyboardButton(text="вопросы❔",callback_data="vopr_v_raspis")]])

def vivod_ras(ras):
    return f"""--------------ПОНЕДЕЛЬНИК--------------
8:00-9:20    | {ras[0][3]}
9:35-10:55  | {ras[1][3]}
11:10-12:30| {ras[2][3]}
13:30-14:50| {ras[3][3]}
15:05-16:25| {ras[4][3]}
-------------------ВТОРНИК-------------------
8:00-9:20    | {ras[5][3]}
9:35-10:55  | {ras[6][3]}
11:10-12:30| {ras[7][3]}
13:30-14:50| {ras[8][3]}
15:05-16:25| {ras[9][3]}
----------------------СРЕДА----------------------
8:00-9:20    | {ras[10][3]}
9:35-10:55  | {ras[11][3]}
11:10-12:30| {ras[12][3]}
13:30-14:50| {ras[13][3]}
15:05-16:25| {ras[14][3]}
---------------------ЧЕТВЕРГ---------------------
8:00-9:20    | {ras[15][3]}
9:35-10:55  | {ras[16][3]}
11:10-12:30| {ras[17][3]}
13:30-14:50| {ras[18][3]}
15:05-16:25| {ras[19][3]}
-------------------ПЯТНИЦА-------------------
8:00-9:20    | {ras[20][3]}
9:35-10:55  | {ras[21][3]}
11:10-12:30| {ras[22][3]}
13:30-14:50| {ras[23][3]}
15:05-16:25| {ras[24][3]}
-------------------СУББОТА-------------------
8:00-9:20    | {ras[25][3]}
9:35-10:55  | {ras[26][3]}
11:10-12:30| {ras[27][3]}
    РАСПИСАНИЕ {ras[0][1]} НЕДЕЛИ
"""
def raspisne(id_tg):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={id_tg}").fetchone())[0]
    gr=grope
    grope += "_rasp"
    cursor = db.cursor()
    res1 = cursor.execute(f"""Select * FROM {grope} WHERE grope=(?) and nedel=(?)""", (gr,kakaya_shas_nedel(gr,id_tg),)).fetchall()
    if kakaya_shas_nedel(gr,id_tg) == None:
        cursor = db.cursor()
        res = cursor.execute(f"""Select * FROM {grope} WHERE grope=(?)""",
                              (gr,)).fetchone()
        if res!=None:
            return "zero"
        else:
            return res1

    return res1

def raspisnie_strelochki(id_tg,znach):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={id_tg}").fetchone())[0]
    gr=grope
    grope += "_rasp"
    cursor = db.cursor()
    res1 = cursor.execute(f"""Select * FROM {grope} WHERE grope=(?) and nedel=(?)""", (gr,znach,)).fetchall()
    return res1

def kakaya_shas_nedel(gr,id_tg):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={id_tg}").fetchone())[0]
    grope += "_rasp"
    cursor = db.cursor()
    res1 = cursor.execute(f"""Select nedel FROM {grope} WHERE grope=(?) and data=(?)""", (str(gr),str(datetime.date.today()),)).fetchone()
    if res1!=None:
        return res1[0]
    return res1

def del_in_groupe(id_tg):
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={id_tg}").fetchone())[0]
    gr=grope
    grope += "_rasp"
    cursor = db.cursor()
    res1 = cursor.execute(f"""delete FROM {grope} WHERE grope=(?)""", (gr,))
    db.commit()


def gen_ned(text,id_tg):#создать расписание
    cursor = db.cursor()
    grope1 = (cursor.execute(f"Select grope FROM user where tg_id={id_tg}").fetchone())[0]
    grope1 += "_rasp"
    text.lower()
    text = text[text.find("(") + 1:text.find(")")]
    mass = text.split("-")
    y=int(mass[0])
    m=int(mass[1])
    d=int(mass[2])
    gr=grope(str(id_tg))
    #делаем дату начала с откатом до понедельника чтобы выводилось
    data_nach = datetime.date(y,m,d) - datetime.timedelta(days=n_day(datetime.date(y,m,d)))
    ned = 1
    for i in range(315):
        vosk = 5
        data_for = data_nach + datetime.timedelta(days=i)
        if str(t_day(n_day(data_for)))=="воскресенье":
            vosk=1

        if t_day(n_day(data_for))=="понедельник" and i>1:
            ned+=1

        for nomerpar in range(vosk):
            nomerpar+=1
            cursor = db.cursor()
            res = cursor.execute(f"""Insert into {grope1}(nedel,day,grope,nomerpar,data) VALUES((?),(?),(?),(?),(?))""",
                                  (int(ned),str(t_day(n_day(data_for))),gr,int(nomerpar),str(data_for)))
            db.commit()

















def dobavit_paru(text,id_tg):#UPDATE данные в таблице
    cursor = db.cursor()
    grope = (cursor.execute(f"Select grope FROM user where tg_id={id_tg}").fetchone())[0]
    gr=grope
    grope += "_rasp"
    text.lower()
    text = text[text.find("["):]
    text = text.replace("]", "<>")
    mass1 = text.split(">")
    for i in mass1:
        text = i[i.find("[") + 1:i.find("<")].replace(" ", "")
        mass2 = text.split(",")
        if "-" in text:
            if len(mass2) > 1:
                mass2.append(mass2[3].split("-"))
                mass2.pop(3)
                for nedel in range(int(mass2[3][0]), int(mass2[3][1]) + 1):
                    cursor = db.cursor()
                    res = cursor.execute(f"""UPDATE {grope} SET para=(?)
                                                                     WHERE grope=(?) and
                                                                     nedel=(?) and
                                                                     day=(?) and
                                                                     nomerpar=(?)""",
                                     (mass2[0], gr, nedel, mass2[2], mass2[1]))
                db.commit()
        else:
            if len(mass2)>1:
                cursor = db.cursor()
                res = cursor.execute(f"""UPDATE {grope} SET para=(?)
                                                                             WHERE grope=(?) and
                                                                             nedel=(?) and
                                                                             day=(?) and
                                                                             nomerpar=(?)""",
                                 (mass2[0], gr, mass2[3], mass2[2], mass2[1]))

                db.commit()












def n_day(data):#индекс дня недели
    #ввести дату
    vesti_datu=data

    #делает номер
    day_nomber=datetime.date.weekday(vesti_datu)

    #вывод номер
    return day_nomber
def t_day(nomer):#расшифровка индекса
    text={
        0: "понедельник",
        1: "вторник",
        2: "среда",
        3: "четверг",
        4: "пятница",
        5: "суббота",
        6: "воскресенье"
    }
    return text.get(nomer)

def grope(id_tg):
    cursor = db.cursor()
    res = cursor.execute("""SELECT grope From user WHERE tg_id=(?)""", (id_tg,)).fetchone()
    return res[0]