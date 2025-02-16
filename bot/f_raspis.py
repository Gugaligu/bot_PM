import datetime
from datetime import date
from datetime import timedelta
import requests
import sqlite3
db = sqlite3.connect("../data/db.db")
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)

weather_token="94eaed681c7d9c4ada968813098d55fc"

def weat():
    weather_array=weather_array1
    if time>time2:
        tim2(0)
        tim()
        we()
        print(weather_array)
        return weather_array
    else:
        tim()
        print("access")
        return weather_array

def tim():
    global time
    time = datetime.datetime.now()
tim()
def tim2(flag):
    global time2
    if flag==1:
        time2 = datetime.datetime.now()+timedelta(minutes=1)
    else:
        time2 = datetime.datetime.now()+timedelta(hours=1)
    print(time2)
tim2(0)

def get_weather():
    try:
        print("погодка1")
        try:
            r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?lat=52.720388&lon=58.665662&appid={weather_token}&units=metric", timeout=1)
        except requests.exceptions.ReadTimeout:
            tim2(1)
            print("ошибка погоды")
            totallistday = weather_array1
            return totallistday
        print("погодка2")
        data = r.json()
        totallistday = []
        totallistday.append([data["list"][1]['dt_txt'], int(data["list"][2]["main"]["temp"]),
                             smiles(data["list"][1]["weather"][-1]['main'], data["list"][1]["clouds"]["all"])])
        for day in data["list"]:
            if day["dt_txt"][-8:-6] == "09":
                temp = int(day["main"]["temp"])
                time = day["dt_txt"]
                proc = day["clouds"]["all"]
                weather = smiles(day["weather"][-1]['main'], proc)
                totallistday.append([time, temp, weather])
        print(totallistday)
        if totallistday[0][0][8:10] == totallistday[1][0][8:10]:
            totallistday.pop(0)
        print(totallistday)
        return totallistday

    except requests.exceptions.ConnectionError:
        tim2(1)
        print("ошибка погоды")
        totallistday = weather_array1
        return totallistday


def smiles(weather,proc):
    smile={
        "Thunderstorm":"🌩️",
        "Drizzle": "🌦️",
        "Rain": "🌧️",
        "Snow": "🌨️",
        "Clear": "☀️",
        "Clouds": "☁️",
        "Mist": "🌫️",
        "Smoke": "🌫️",
        "Haze": "🌫️",
        "Dust": "🌫️",
        "Fog": "🌫️",
        "Sand": "🌫️",
        "Ash": "🌫️",
        "Squall": "💨",
        "Tornado": "🌪️"
    }
    if weather=="Clouds":
        if proc>=85:
            return "☁️"
        elif proc<=25:
            return "🌤️"
        elif proc>25 and proc<=50:
            return "⛅"
        else:
            return "🌥️"
    return smile.get(weather)
def we():
    global weather_array1
    weather_array1 = get_weather()
    return weather_array1
weather_array1=[]
we()






def flevel_admin(tg_id):
    cursor = db.cursor()
    res = cursor.execute("""SELECT admin From user WHERE tg_id=(?)""", (tg_id,)).fetchone()
    if res==None:
        return 0
    return res[0]


def c_spisok(c):
    c=int(c)
    rezi = []
    if c < 42 and c > 4:
        rezi = [c - 4, c - 3, c - 2, c - 1, c + 1, c + 2, c + 3, c + 4]
    elif c >= 42:
        kol_prob = abs(41 - c)
        rezi = [c - 4, c - 3, c - 2, c - 1, ]
        for d in range(1, 46 - c):
            rezi.append(c + d)
        for b in range(8 - len(rezi)):
            rezi.append("-")
    elif c <= 4:
        for d in range(5 - c):
            rezi.append("-")
        if c == 4:
            rezi = rezi + [c - 3, c - 2, c - 1]
        if c == 3:
            rezi = rezi + [c - 2, c - 1]
        if c == 2:
            rezi = rezi + [c - 1]
        rezi = rezi + [c + 1, c + 2, c + 3, c + 4]
    return rezi
def level_dly_menu(level,c):
    rezi=list(map(str,c_spisok(c)))
    if level>1:
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="<-", callback_data=("<-"+str(c))),
                                                        InlineKeyboardButton(text="изменить",callback_data="изменить"),
                                                        InlineKeyboardButton(text="->", callback_data=(">-"+str(c)))],
                                                     [InlineKeyboardButton(text=rezi[0], callback_data="рас"+rezi[0]),
                                                      InlineKeyboardButton(text=rezi[1], callback_data="рас"+rezi[1]),
                                                      InlineKeyboardButton(text=rezi[2], callback_data="рас"+rezi[2]),
                                                      InlineKeyboardButton(text=rezi[3], callback_data="рас"+rezi[3]),
                                                      InlineKeyboardButton(text=rezi[4], callback_data="рас"+rezi[4]),
                                                      InlineKeyboardButton(text=rezi[5], callback_data="рас"+rezi[5]),
                                                      InlineKeyboardButton(text=rezi[6], callback_data="рас"+rezi[6]),
                                                      InlineKeyboardButton(text=rezi[7], callback_data="рас"+rezi[7])],
                                                     [InlineKeyboardButton(text="вопросы❔",callback_data="vopr_v_raspis")],
                                                        [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="<-", callback_data=("<-" + str(c))),
                              InlineKeyboardButton(text="вопросы❔",callback_data="vopr_v_raspis"),
                              InlineKeyboardButton(text="->", callback_data=(">-" + str(c)))],
                              [InlineKeyboardButton(text=rezi[0], callback_data="рас"+rezi[0]),
                              InlineKeyboardButton(text=rezi[1], callback_data="рас"+rezi[1]),
                              InlineKeyboardButton(text=rezi[2], callback_data="рас"+rezi[2]),
                              InlineKeyboardButton(text=rezi[3], callback_data="рас"+rezi[3]),
                              InlineKeyboardButton(text=rezi[4], callback_data="рас"+rezi[4]),
                              InlineKeyboardButton(text=rezi[5], callback_data="рас"+rezi[5]),
                              InlineKeyboardButton(text=rezi[6], callback_data="рас"+rezi[6]),
                              InlineKeyboardButton(text=rezi[7], callback_data="рас"+rezi[7])],
                              [InlineKeyboardButton(text="Отмена↩️",callback_data="menu")]])

def vivod_ras(ras):
    rez= f"""<blockquote><b><u>ПОНЕДЕЛЬНИК                           {ras[0][6]}</u>
8:00-9:20    | {ras[0][3]}
9:35-10:55  | {ras[1][3]}
11:10-12:30| {ras[2][3]}
13:30-14:50| {ras[3][3]}
15:05-16:25| {ras[4][3]}</b></blockquote>
<blockquote><b><u>ВТОРНИК                                      {ras[5][6]}</u>
8:00-9:20    | {ras[5][3]}
9:35-10:55  | {ras[6][3]}
11:10-12:30| {ras[7][3]}
13:30-14:50| {ras[8][3]}
15:05-16:25| {ras[9][3]}</b></blockquote>
<blockquote><b><u>СРЕДА                                           {ras[10][6]}</u>
8:00-9:20    | {ras[10][3]}
9:35-10:55  | {ras[11][3]}
11:10-12:30| {ras[12][3]}
13:30-14:50| {ras[13][3]}
15:05-16:25| {ras[14][3]}</b></blockquote>
<blockquote><b><u>ЧЕТВЕРГ                                       {ras[15][6]}</u>
8:00-9:20    | {ras[15][3]}
9:35-10:55  | {ras[16][3]}
11:10-12:30| {ras[17][3]}
13:30-14:50| {ras[18][3]}
15:05-16:25| {ras[19][3]}</b></blockquote>
<blockquote><b><u>ПЯТНИЦА                                     {ras[20][6]}</u>
8:00-9:20    | {ras[20][3]}
9:35-10:55  | {ras[21][3]}
11:10-12:30| {ras[22][3]}
13:30-14:50| {ras[23][3]}
15:05-16:25| {ras[24][3]}</b></blockquote>
<blockquote><b><u>СУББОТА                                      {ras[25][6]}</u>
8:00-9:20    | {ras[25][3]}
9:35-10:55  | {ras[26][3]}
11:10-12:30| {ras[27][3]}</b></blockquote>
    РАСПИСАНИЕ {ras[0][1]} НЕДЕЛИ
"""
    cho=weat()
    if cho is not None:
        if len(cho)>4:
            for wether in cho:
                if wether[0][0:10] in rez:
                    index=rez.find(str(wether[0][0:10]))
                    print(wether)
                    if wether[1]>9:
                        otnimi=13
                    elif wether[1]<=9:
                        otnimi = 12
                    else:
                        otnimi=0
                    if  wether[1]<0:
                        znak=""
                    else:
                        znak = "+"
                    rez2 = rez[:index-otnimi]+znak+str(wether[1])+wether[2]+rez[index-1:]
                    rez=rez2
    return rez


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
    mass2 = []
    for i in mass1:
        text = i[i.find("[") + 1:i.find("<")].replace(" ", "")
        mass2 = text.split(",")
        if "+" in mass2[-1]:
            mass2.append(mass2[3].split("+"))
            mass2.pop(3)
            index = []
            for tire in mass2[-1]:
                if "-" in str(tire):
                    proiti = tire.split("-")
                    for mnogo in range(int(proiti[0]), int(proiti[1]) + 1):
                        mass2[-1].append(str(mnogo))
                    index.append(tire)
            mass_prom = [x for x in mass2[-1] if x not in index]
            mass2.pop(-1)
            mass2.append(mass_prom)
            print(mass2)




        elif "-" in text:
            if len(mass2) > 1:
                mass2.append(mass2[3].split("-"))
                mass2.pop(3)
                for nedel in range(int(mass2[3][0]), int(mass2[3][1]) + 1):
                    if str(nedel) not in mass2[-1]:
                        mass2[-1].append(str(nedel))
                  
        if len(mass2[-1]) > 0:
            print(mass2)
            if isinstance(mass2[-1], list):
                for nedel in mass2[-1]:
                    cursor = db.cursor()
                    res = cursor.execute(f"""UPDATE {grope} SET para=(?)
                                             WHERE grope=(?) and
                                             nedel=(?) and
                                             day=(?) and
                                             nomerpar=(?)""",
                                         (str(mass2[0]), str(gr), int(nedel), str(mass2[2]), int(mass2[1])))
            elif isinstance(mass2[-1], str):
                print(type(mass2), mass2)
                nedel = mass2[-1]
                cursor = db.cursor()
                res = cursor.execute(f"""UPDATE {grope} SET para=(?)
                                                                     WHERE grope=(?) and
                                                                     nedel=(?) and
                                                                     day=(?) and
                                                                     nomerpar=(?)""",
                                     (str(mass2[0]), str(gr), int(nedel), str(mass2[2]), int(mass2[1])))
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
