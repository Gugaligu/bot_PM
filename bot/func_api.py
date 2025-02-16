
import sqlite3

db = sqlite3.connect("../data/db.db", check_same_thread=False)
def gettr_all_grope():
    grope_mass=[]
    cursor = db.cursor()
    grope_bd = cursor.execute("SELECT gr from spisokgrop;").fetchall()
    if len(grope_bd)==0:
        grope_mass.append("групп нет")
    else:
        for groppa in grope_bd:
            grope_mass.append(groppa[0])
    return grope_mass
def json_rasp(grope):
    mass_gr_aply=gettr_all_grope()
    if grope in mass_gr_aply:
        cursor = db.cursor()
        json={
        grope:{

            }
        }
        all = cursor.execute(f"SELECT day,para FROM {grope}_rasp;").fetchall()
        c = 0
        if len(all)==0:
            return "error"
        for i in range(1,46):
            pn = []
            vt = []
            sr = []
            ch = []
            pt = []
            sb = []
            for a in range(6):
                for b in range(5):
                    if 'понедельник'==all[c][0]:
                        pn.append(all[c][1])
                    elif 'вторник'==all[c][0]:
                        vt.append(all[c][1])
                    elif 'среда'==all[c][0]:
                        sr.append(all[c][1])
                    elif 'четверг' == all[c][0]:
                        ch.append(all[c][1])
                    elif 'пятница' == all[c][0]:
                        pt.append(all[c][1])
                    elif 'суббота' == all[c][0]:
                        sb.append(all[c][1])
                    else:raise "eblan"
                    c+=1
            c+=1
            json[grope][str(i)]={
                "PN":pn,
                "VT":vt,
                "SR":sr,
                "CH":ch,
                "PT":pt,
                "SB":sb,
            }
        return json
    else:
        return "error"

def redact(grope,red=False):
    mass_gr_aply=gettr_all_grope()
    if grope in mass_gr_aply:
        cursor = db.cursor()
        json = {
            grope: {
                "понедельник":{1:{},2:{},3:{},4:{},5:{}},
                "вторник":{1:{},2:{},3:{},4:{},5:{}},
                "среда":{1:{},2:{},3:{},4:{},5:{}},
                "четверг":{1:{},2:{},3:{},4:{},5:{}},
                "пятница":{1:{},2:{},3:{},4:{},5:{}},
                "суббота":{1:{},2:{},3:{},4:{},5:{}}
            }
        }

        all = cursor.execute(f"SELECT nedel,day,nomerpar,para FROM {grope}_rasp;").fetchall()
        for data in all:
            day=data[1]
            if day=="воскресенье":
                continue
            nedel = data[0]
            nomer=data[2]
            para=data[3]
            if para==' ':
                continue
            tmp_js=json[grope][day][nomer]
            if para in json[grope][day][nomer] and para.replace(" ","")!="":
                tmp_js[para].append(nedel)
            else:
                tmp_js[para]=[]
                tmp_js[para].append(nedel)

    else:
        return "error"
    if red==True:
        json=tmp_redact(json,grope)
    return json
def tmp_redact(json,grope):
    json_redact={
        grope:{
            "понедельник": {1: [], 2: [], 3: [], 4: [], 5: []},
            "вторник": {1: [], 2: [], 3: [], 4: [], 5: []},
            "среда": {1: [], 2: [], 3: [], 4: [], 5: []},
            "четверг": {1: [], 2: [], 3: [], 4: [], 5: []},
            "пятница": {1: [], 2: [], 3: [], 4: [], 5: []},
            "суббота": {1: [], 2: [], 3: [], 4: [], 5: []}
        }
    }
    for day, value in json[grope].items():
        for nomer, value1 in json[grope][day].items():
            for para, nedel in json[grope][day][nomer].items():
                    # =======================================================
                    stroke=""
                    cash=-100
                    block=True
                    for i in range(len(nedel)):
                        try:
                            if nedel[i]+1==nedel[i+1]:
                                if block==False:
                                    ...
                                else:
                                    block=False
                                    stroke+=f"{str(nedel[i])}-"
                            else:
                                block=True
                                stroke += f"{str(nedel[i])},"
                        except IndexError:
                            stroke += f"{str(nedel[i])},"
                    #=========================================================
                    stroke=f"{para}({stroke[:-1]})"
                    json_redact[grope][day][nomer].append(stroke)
    return json_redact