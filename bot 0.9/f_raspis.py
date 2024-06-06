import datetime
import sqlite3
db = sqlite3.connect("../data/db.db")



def raspisne(id_tg):
    gr = grope(id_tg)
    cursor = db.cursor()
    res1 = cursor.execute("""Select * FROM raspisanie WHERE grope=(?) and nedel=(?)""", (gr,kakaya_shas_nedel(gr),)).fetchall()
    return res1

def kakaya_shas_nedel(gr):
    cursor = db.cursor()
    res1 = cursor.execute("""Select nedel FROM raspisanie WHERE grope=(?) and data=(?)""", (str(gr),str(datetime.date.today()),)).fetchone()
    print(datetime.date.today())
    if res1!=None:
        return res1[0]
    return res1

def del_in_groupe(id_tg):
    gr=grope(id_tg)
    cursor = db.cursor()
    res1 = cursor.execute("""delete FROM raspisanie WHERE grope=(?)""", (gr,))
    db.commit()
    print("ошибка")
    return


def gen_ned(text,id_tg):#создать расписание
    text.lower()
    text = text[text.find("(") + 1:text.find(")")]
    mass = text.split("-")
    y=int(mass[0])
    m=int(mass[1])
    d=int(mass[2])
    gr=grope(id_tg)
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
            res = cursor.execute("""Insert into raspisanie(nedel,day,grope,nomerpar,data) VALUES((?),(?),(?),(?),(?))""",
                                  (int(ned),str(t_day(n_day(data_for))),gr,int(nomerpar),str(data_for)))
            db.commit()

















def dobavit_paru(text,id_tg):#UPDATE данные в таблице
    gr = grope(id_tg)
    text.lower()
    if "одна" in text:
        text=text[text.find("(")+1:text.find(")")].replace(" ","")
        mass=text.split(",")
        if "-" in text:
            mass.append(mass[3].split("-"))
            mass.pop(3)
            for nedel in range(int(mass[3][0]),int(mass[3][1])+1):
                print(mass[0],gr,nedel,mass[2],mass[1])
                cursor = db.cursor()
                res = cursor.execute("""UPDATE raspisanie SET para=(?) 
                                         WHERE grope=(?) and 
                                             nedel=(?) and 
                                             day=(?) and 
                                             nomerpar=(?)""",(mass[0],gr,nedel,mass[2],mass[1]))
            db.commit()
        else:
            cursor = db.cursor()
            res = cursor.execute("""UPDATE raspisanie SET para=(?) 
                                                         WHERE grope=(?) and 
                                                         nedel=(?) and 
                                                         day=(?) and 
                                                         nomerpar=(?)""", (mass[0], gr, mass[3], mass[2], mass[1]))
            db.commit()
    elif "несколько":
        text=text[text.find("("):]
        mass1=text.split("\n")
        for i in mass1:
            text = i[i.find("(") + 1:i.find(")")].replace(" ", "")
            mass2 = text.split(",")
            if "-" in text:
                mass2.append(mass2[3].split("-"))
                mass2.pop(3)
                for nedel in range(int(mass2[3][0]), int(mass2[3][1]) + 1):
                    print(mass2[0], gr, nedel, mass2[2], mass2[1])
                    cursor = db.cursor()
                    res = cursor.execute("""UPDATE raspisanie SET para=(?)
                                                     WHERE grope=(?) and
                                                     nedel=(?) and
                                                     day=(?) and
                                                     nomerpar=(?)""", (mass2[0], gr, nedel, mass2[2], mass2[1]))
                db.commit()
            else:
                cursor = db.cursor()
                res = cursor.execute("""UPDATE raspisanie SET para=(?)
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