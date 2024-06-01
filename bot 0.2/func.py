from datetime import date
import sqlite3
db = sqlite3.connect("../data/db.db")

def step_day():
    #ищю дней до стипы
    t = date.today()
    tstr = str(t)
    if int(tstr[-2:]) <= 25:
        stip = date.fromisoformat(tstr[:-2] + "25")
    else:
        if int(tstr[5:-3]) + 1 < 10:
            stip = date.fromisoformat(tstr[:5] + "0" + str(int(tstr[5:-3]) + 1) + "-25")
        else:
            stip = date.fromisoformat(tstr[:5] + str(int(tstr[5:-3]) + 1) + "-25")
    daystip=(stip - t).days

    dney=""
    if daystip in [1,21,31]:
        dney="день"
    elif daystip in [2,3,4,22,23,24]:
        dney="дня"
    else:
        dney="дней"

    if daystip>20:
        com="ㅤㅤㅤЕще очинь долго((( ТРЭШ"
    elif daystip<=20 and daystip>=10:
        com="ㅤЕще примерно пол месяца УЖАС :("
    elif daystip<10 and daystip>4:
        com = "Еще примерно недельку протянуть Ура!!!!"
    else:
        com = "ㅤㅤУже совсем скоро!!!"
    stroke=(f"ㅤㅤㅤㅤДо стипендии {daystip} {dney}!\n"
            f"===============↓↓↓===============\n"
                            +com)
    return stroke
def registration(id, name, grope):
    cursor = db.cursor()
    res = cursor.execute("""INSERT INTO user(tg_id,name,grope) VALUES((?),(?),(?))""", (id,name,grope,))
    print(res)
    db.commit()
    pass
def prov_registration(id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT tg_id From user WHERE tg_id=(?)""", (id,)).fetchone()
    print(res)
    return res != None
def menu(id,first_name,username):
    cursor = db.cursor()
    res = cursor.execute("""SELECT * From user WHERE tg_id=(?)""", (id,)).fetchone()
    return "Пользователь\n" \
           f"Имя:{res[2]}\n" \
           f"Имя в тг:{first_name}({username})\n" \
           f"группа:{res[4]}\n" \
           f"Админ:{nazvanie_admina(res[1])}\n" \
           f"====================\n" \
           f"ㅤㅤМеню функций"
def nazvanie_admina(id):
    level=level_admin(id)
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
def nazvanie_admina2(uroven):
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

def name_in_db(name):
    cursor = db.cursor()
    res = cursor.execute("""SELECT name From user WHERE name=(?)""", (name,)).fetchone()
    print(res)
    if res==None:
        return True
    else:
        return False


def level_admin(id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT admin From user WHERE tg_id=(?)""", (id,)).fetchone()
    print(res)
    if res==None:
        return 0
    return res[0]

def grope(id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT grope From user WHERE tg_id=(?)""", (id,)).fetchone()
    return res[0]
def admin_vision_grope(id):
    g=grope(id)
    cursor = db.cursor()
    res = cursor.execute("""SELECT id,name,admin,grope From user WHERE grope=(?)""", (g,)).fetchall()
    stroke=f"Группа {g}\n\n"
    m0,m1,m2 = 2,3,5
    for i in res:
        m0=max(m0,len(str(i[0])))
        m1=max(m1,len(str(i[1])))
        m2=max(m2,len(nazvanie_admina2(i[2])))
    stroke += "№" + "  "*(m0-2)+"     "
    stroke += "имя" + "  "*(m1-3)+"     "
    stroke += "админ" + "  "*(m2-5)+"     "
    stroke += "группа\n"
    for i in res:
        stroke+= str(i[0])+"  "*(m0-len(str(i[0])))+"     "
        stroke+= str(i[1])+"  "*(m1-len(str(i[1])))+"     "
        stroke+= str(nazvanie_admina2(i[2]))+"  "*(m2-len(nazvanie_admina2(i[2])))+"     "
        stroke+= str(i[3])
        stroke+= "\n"
    return stroke
def admin_vision():
    cursor = db.cursor()
    res = cursor.execute("""SELECT id,name,admin,grope From user""").fetchall()
    stroke="(При некоректном отображении переверните телефон)\n"
    m0,m1,m2 = 2,3,5
    for i in res:
        m0=max(m0,len(str(i[0])))
        m1=max(m1,len(str(i[1])))
        m2=max(m2,len(nazvanie_admina2(i[2])))
    stroke += "№" + "  "*(m0-2)+"     "
    stroke += "имя" + "  "*(m1-3)+"     "
    stroke += "админ" + "  "*(m2-5)+"     "
    stroke += "группа\n"
    for i in res:
        stroke+= str(i[0])+"  "*(m0-len(str(i[0])))+"     "
        stroke+= str(i[1])+"  "*(m1-len(str(i[1])))+"     "
        stroke+= str(nazvanie_admina2(i[2]))+"  "*(m2-len(nazvanie_admina2(i[2])))+"     "
        stroke+= str(i[3])
        stroke+= "\n"
    return stroke
def del_in_groupe(id,nomer):
    cursor = db.cursor()
    res1 = cursor.execute("""SELECT grope From user WHERE grope=(?)""", (grope(id),)).fetchone()
    cursor = db.cursor()
    res2 = cursor.execute("""SELECT grope From user WHERE id=(?)""", (nomer,)).fetchone()
    if res1[0]==res2[0] and (res2!="супер" or res2!="да"):
        cursor = db.cursor()
        res1 = cursor.execute("""delete FROM user WHERE id=(?)""", (nomer,))
        db.commit()
    return
def sdelat_adminom(nomer):
    cursor = db.cursor()
    res = cursor.execute("""UPDATE user SET admin='2' WHERE id=(?)""", (nomer,))
    db.commit()

def rename(id,nomer,text):
    cursor = db.cursor()
    res1 = cursor.execute("""SELECT grope From user WHERE grope=(?)""", (grope(id),)).fetchone()
    cursor = db.cursor()
    res2 = cursor.execute("""SELECT grope From user WHERE id=(?)""", (nomer,)).fetchone()
    if res1[0]==res2[0]:
        cursor = db.cursor()
        res1 = cursor.execute("""UPDATE user SET name=() WHERE id=(?)""", (text,nomer,))
        db.commit()
def po_id_tg_id(id):
    cursor = db.cursor()
    res1 = cursor.execute("""SELECT tg_id From user WHERE id=(?)""", (id,)).fetchone()
    return res1[0]