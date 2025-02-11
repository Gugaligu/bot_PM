import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from datetime import date
import menu
from datetime import date
import sqlite3
db = sqlite3.connect("db.db")

def getallid():
    cursor = db.cursor()
    res1 = cursor.execute("SELECT  tg_id   FROM    user;").fetchall()
    return res1

def posmotr_group():
    cursor = db.cursor()
    res1 = cursor.execute("SELECT gr FROM spisokgrop;").fetchall()
    return res1

def fsdelat_adminom(nomer):
    cursor = db.cursor()
    res = cursor.execute("""UPDATE user SET admin='2' WHERE id=(?)""", (nomer,))
    db.commit()

def fdel_in_groupe(id,nomer):
    cursor = db.cursor()
    res1 = cursor.execute("""SELECT grope From user WHERE grope=(?)""", (grope(id),)).fetchone()
    cursor = db.cursor()
    res2 = cursor.execute("""SELECT grope From user WHERE id=(?)""", (nomer,)).fetchone()
    if res1[0]==res2[0] and (res2=="создатель" or res2=="староста"):
        cursor = db.cursor()
        res1 = cursor.execute("""delete FROM user WHERE id=(?)""", (nomer,))
        db.commit()
    return
def fdel_in_groupe2(tg_id):
    cursor = db.cursor()
    res1 = cursor.execute("""delete FROM user WHERE tg_id=(?)""", (tg_id,))
    db.commit()
def fpo_id_tg_id(id):
    cursor = db.cursor()
    res1 = cursor.execute("""SELECT tg_id From user WHERE id=(?)""", (id,)).fetchone()
    return res1[0]
def fname_in_db(name):
    cursor = db.cursor()
    res = cursor.execute("""SELECT name From user WHERE name=(?)""", (name,)).fetchone()
    if res==None:
        return True
    else:
        return False
def fname_in_db2(tg_id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT name From user WHERE tg_id=(?)""", (tg_id,)).fetchone()
    return res[0]


def find_admin(tg_id):
    cursor = db.cursor()
    grope = cursor.execute("""SELECT grope From user WHERE tg_id=(?)""", (tg_id,)).fetchone()
    print(grope)
    cursor = db.cursor()
    res = cursor.execute("""SELECT tg_id From user WHERE grope=(?) and admin=(?)""", (grope[0],2,)).fetchone()
    print(res)
    return res[0]


def fupdatename(name,number):
    cursor = db.cursor()
    res = cursor.execute("""UPDATE user SET name=(?) WHERE id=(?)""", (name,number))
    db.commit()


def flevel_admin(id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT admin From user WHERE tg_id=(?)""", (id,)).fetchone()
    if res==None:
        return 0
    return res[0]


def fadmin_vision_grope(id):
    g=grope(id)
    cursor = db.cursor()
    res = cursor.execute("""SELECT id,name,admin,grope From user WHERE grope=(?)""", (g,)).fetchall()
    stroke=f"Группа {g}\n(При некоректном отображении переверните телефон)\n\n"
    m0,m1,m2 = 2,3,5
    for i in res:
        m0=max(m0,len(str(i[0])))
        m1=max(m1,len(str(i[1])))
        m2=max(m2,len(nazvanie_admina(i[2])))
    stroke += "№" + "  "*(m0-2)+"     "
    stroke += "имя" + "  "*(m1-3)+"     "
    stroke += "админ" + "  "*(m2-5)+"     "
    stroke += "группа\n"
    for i in res:
        stroke+= str(i[0])+"  "*(m0-len(str(i[0])))+"     "
        stroke+= str(i[1])+"  "*(m1-len(str(i[1])))+"     "
        stroke+= str(nazvanie_admina(i[2]))+"  "*(m2-len(nazvanie_admina(i[2])))+"     "
        stroke+= str(i[3])
        stroke+= "\n"
    return stroke

def fadmin_vision():
    cursor = db.cursor()
    res = cursor.execute("""SELECT id,name,admin,grope From user""").fetchall()
    stroke="(При некоректном отображении переверните телефон)\n"
    m0,m1,m2 = 2,3,5
    for i in res:
        m0=max(m0,len(str(i[0])))
        m1=max(m1,len(str(i[1])))
        m2=max(m2,len(nazvanie_admina(i[2])))
    stroke += "№" + "  "*(m0-2)+"     "
    stroke += "имя" + "  "*(m1-3)+"     "
    stroke += "админ" + "  "*(m2-5)+"     "
    stroke += "группа\n"
    for i in res:
        stroke+= str(i[0])+"  "*(m0-len(str(i[0])))+"     "
        stroke+= str(i[1])+"  "*(m1-len(str(i[1])))+"     "
        stroke+= str(nazvanie_admina(i[2]))+"  "*(m2-len(nazvanie_admina(i[2])))+"     "
        stroke+= str(i[3])
        stroke+= "\n"
    return stroke
def grope(id_tg):
    cursor = db.cursor()
    res = cursor.execute("""SELECT grope From user WHERE tg_id=(?)""", (id_tg,)).fetchone()
    return res[0]
def nazvanie_admina(uroven):
    if uroven == 0:
        return "не зарегистрирован"
    elif uroven==1:
        return "ученик"
    elif uroven == 2:
        return "староста"
    elif uroven==3:
        return "создатель"
    else:
        return "нет такого"