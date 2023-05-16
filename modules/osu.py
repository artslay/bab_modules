from urllib import request
import requests 
import json
import sqlite3

def db_create(event):
    con = sqlite3.connect('users1.db')
    con.execute('''CREATE TABLE users 
                    (osu_id TEXT PRIMARY KEY, 
                    vk_id TEXT, 
                    mode TEXT)''')
    event.message_send("готово")
    con.close()

def link(event):
    api = "YOUR API"
    username = event.args
    response = requests.get(f'https://osu.ppy.sh/api/get_user?k={api}&u={username}')
    data = response.json()
    if not data or len(event.args) == 0:
        raise Exception (f'''пользователь {username} не найден!''')
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor1 = con.cursor()
    cursor2 = con.cursor()
    input = (event.args, event.userid, 'osu')
    id = (event.args, event.userid)
    idd = (event.userid)
    info = cursor.execute('SELECT * FROM users WHERE vk_id=?', (idd,)).fetchone()
    if info is None:
        cursor.execute('INSERT INTO users (osu_id, vk_id, mode) VALUES (?, ?, ?)', input)
        con.commit()
    else:
        cursor1.execute("UPDATE users SET osu_id=? WHERE vk_id=?", (id))
        con.commit()
    cursor2.execute('SELECT osu_id FROM users WHERE vk_id='+(str(idd)))
    name = cursor2.fetchone()
    j = (''.join(name))
    event.message_send('Аккаунт прикреплён к профилю '+j)

def mode_change(event):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor1 = con.cursor()
    id = (event.args, event.userid)
    idd = str(event.userid)
    cursor.execute("UPDATE users SET mode=? WHERE vk_id=?", (id))
    info = cursor1.execute('SELECT * FROM users WHERE vk_id=?', (idd,)).fetchone()
    if info is None:
        raise Exception('Пользователь не найден!\nНеобходимо привязать ник командой [о линк]')
    if 'mania' in event.args or 'osu' in event.args:
        con.commit()
        event.message_send("Режим игры был изменен на " + event.args)
    else:
        event.message_send(f'''Необходимо указать режим игры!
[о м mania] или [о м osu]''')

def asd(event):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor1 = con.cursor()
    id = str(event.userid)
    cursor.execute('SELECT osu_id FROM users WHERE vk_id='+id)
    cursor1.execute('SELECT mode FROM users WHERE vk_id='+id)
    name = cursor.fetchone()
    mode = cursor1.fetchone()
    j = (''.join(name))
    jj = (''.join(mode))
    event.message_send(f'''Текущий никнейм осу который привязан к странице:
    {j}
    Выбранный режим: {jj}''')

#STD
def osu(event):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor1 = con.cursor()
    cursor2 = con.cursor()
    id = str(event.userid)
    cursor.execute('SELECT osu_id FROM users WHERE vk_id='+id)
    cursor1.execute('SELECT mode FROM users WHERE vk_id='+id)
    name = cursor.fetchone()
    mode = cursor1.fetchone()
    info = cursor2.execute('SELECT * FROM users WHERE vk_id=?', (id,)).fetchone()
    if info is None:
        raise Exception('Пользователь не найден!\nНеобходимо привязать ник командой [о линк]')
    j = (''.join(name))
    jj = (''.join(mode))
    namee = str(j)
    modee = str(jj)
    if 'osu' in modee:
        modee = 0
    else:
        modee = 3
    url = "https://osu.ppy.sh/api/get_user"
    api = "YOUR API"
    o = requests.get (url, params ={
        "k" : api,
        "m" : modee,
        "u" : namee
    }).json()
    avatar_id = o[0]['user_id']
    avatar = 'http://s.ppy.sh/a/'+avatar_id+''
    b = requests.get ("https://osu.ppy.sh/api/get_user_best", params= {
        "k" : api,
        "m" : modee,
        "u" : namee

    }).json()
    beatmap = b[0]['beatmap_id']
    t = requests.get ("https://osu.ppy.sh/api/get_beatmaps", params= {
        "k" : api, 
        "b" : beatmap
    }).json()
    beatmap1 = b[1]['beatmap_id']
    t1 = requests.get ("https://osu.ppy.sh/api/get_beatmaps", params= {
        "k" : api,
        "b" : beatmap1
    }).json()
    beatmap2 = b[2]['beatmap_id']
    t2 = requests.get ("https://osu.ppy.sh/api/get_beatmaps", params= {
        "k" : api,
        "b" : beatmap2
    }).json()

    #Топ 1
    b_diff = t[0]["version"]
    b_artist = t[0]["artist"]
    b_star = t[0]["difficultyrating"]
    b_name = t[0]["title"]
    b_pp = b[0]['pp']
    pp_recent = b[0]['rank']
    date = b[0]['date']

    #Топ 2
    b1_diff = t1[0]["version"]
    b1_artist = t1[0]["artist"]
    b1_star = t1[0]["difficultyrating"]
    b1_name = t1[0]["title"]
    b1_pp = b[1]['pp']
    pp1_recent = b[1]['rank']

    #Топ 3
    b2_diff = t2[0]["version"]
    b2_artist = t2[0]["artist"]
    b2_star = t2[0]["difficultyrating"]
    b2_name = t2[0]["title"]
    b2_pp = b[2]['pp']
    pp2_recent = b[2]['rank']

    #Остальное
    nickname = o[0]['username']
    pp = o[0]['pp_raw' ]
    rank = o[0]['pp_rank']
    country_rank =o[0]['pp_country_rank']
    join = o[0]['join_date']
    country = o[0]['country']
    lvl = o[0]['level']
    playcount = o[0]['playcount']
    acc = o[0]['accuracy']
    acc_conv = round(float(acc), 2)

    #Моды   
    mods = b[0]['enabled_mods']
    if mods == '0':
        mods = 'NM'
    if mods == '16':
        mods = 'HR'
    if mods == '64':
        mods = 'DT'
    if mods == '8':
        mods = 'HD'
    if mods == '72':
        mods = 'HDDT'
    if mods == '80':
       mods = 'DTHR'
    if mods == '24':
        mods = 'HDHR'
    if mods == '256':
        mods = 'HT'    
    if mods == '576':
        mods = 'NC'
    if mods == '88':
        mods = 'HDDTHR'
    if mods == '520':
        mods = 'NCHD'
    mods1 = b[1]['enabled_mods']
    if mods1 == '0':
        mods1 = 'NM'
    if mods1 == '16':
        mods1 = 'HR'
    if mods1 == '64':
        mods1 = 'DT'
    if mods1 == '8':
        mods1 = 'HD'
    if mods1 == '72':
        mods1 = 'HDDT'
    if mods1 == '80':
       mods1 = 'DTHR'
    if mods1 == '24':
        mods1 = 'HDHR'
    if mods1 == '256':
        mods1 = 'HT'    
    if mods1 == '576':
        mods1 = 'NC'
    if mods1 == '88':
        mods1 = 'HDDTHR'
    if mods1 == '520':
        mods1 = 'NCHD'
    mods2 = b[2]['enabled_mods']
    if mods2 == '0':
        mods2 = 'NM'
    if mods2 == '16':
        mods2 = 'HR'
    if mods2 == '64':
        mods2 = 'DT'
    if mods2 == '8':
        mods2 = 'HD'
    if mods2 == '72':
        mods2 = 'HDDT'
    if mods2 == '80':
       mods2 = 'DTHR'   
    if mods2 == '24':
        mods2 = 'HDHR'
    if mods2 == '256':
        mods2 = 'HT'    
    if mods2 == '576':
        mods2 = 'NC'
    if mods2 == '88':
        mods2 = 'HDDTHR'
    if mods2 == '520':
        mods2 = 'NCHD'

    #Ответ
    event.message_send (f""" Информация о пользователе: {nickname} {modee} 

Дата регистрации: {join}
Страна: {country}

Топ страны: #{country_rank}
Топ мира: #{rank}

PP: {pp}
Уровень: {round(float(lvl),2)} 
Плейкаунт: {playcount}
Общая точность: {acc_conv}%

Топ скоров:
-------------------------------------------------------
#1 {b_artist} - {b_name} [{b_diff}] - {pp_recent} ранк
{round(float(b_star), 2)}✩, получено {b_pp}pp [{mods}]
-------------------------------------------------------
#2 {b1_artist} - {b1_name} [{b1_diff}] - {pp1_recent} ранк
{round(float(b1_star), 2)}✩, получено {b1_pp}pp [{mods1}]
-------------------------------------------------------
#3 {b2_artist} - {b2_name} [{b2_diff}] - {pp2_recent} ранк
{round(float(b2_star), 2)}✩, получено {b2_pp}pp [{mods2}] 
-------------------------------------------------------
  """)

#osu!gatari
def gatari(event):
    url = ('https://api.gatari.pw/user/stats')
    r = requests.get(url, params={
        "u" : event.args,
        "mode" : 3}).json()
    url_1 = 'https://api.gatari.pw/users/get'
    o = requests.get(url_1, params={
        "u" : event.args,
        "mode" : 3}).json()

    pp = r['stats']['pp']
    nickname = o['users'][0]['username']
    c_rank = r['stats']['country_rank']
    rank = r['stats']['rank']
    playcount = r['stats']['playcount']
    playtime = r['stats']['playtime']
        
    event.message_send(f""" Информация о пользователе: {nickname} (Gatari)(Mania)
 PP: {pp}
 Топ страны: #{c_rank}
 Топ мира: #{rank}
 Плейкаунт: {playcount} {playtime}

    """)
    
def osu_v2(event):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor1 = con.cursor()
    cursor2 = con.cursor()
    id = str(event.userid)
    cursor.execute('SELECT osu_id FROM users WHERE vk_id='+id)
    cursor1.execute('SELECT mode FROM users WHERE vk_id='+id)
    info = cursor2.execute('SELECT * FROM users WHERE vk_id=?', (id,)).fetchone()
    if info is None:
        raise Exception ('Пользователь не найден!\nНеобходимо привязать ник командой [о линк]')
    name = cursor.fetchone()
    mode = cursor1.fetchone()
    j = (''.join(name))
    jj = (''.join(mode))
    namee = str(j)
    modee = str(jj)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "client_id" : 'YOUR ID',
        "client_secret" : "YOUR SECRET",
        "grant_type" : "client_credentials",
        "scope" : "public"
    }
    url = 'https://osu.ppy.sh/oauth/token'
    r = requests.post (url, json=payload, headers=headers).json()
    token = (r["access_token"])
    headers1 = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + token + ""
    }

    url1 = 'https://osu.ppy.sh/api/v2/users/'+namee+'/'+modee+''
    r1 = requests.get(url1, headers=headers1).json()
    id_nick = str(r1['id'])
    url2 = 'https://osu.ppy.sh/api/v2/users/'+id_nick+'/scores/recent'
    r2 = requests.get(url2, headers=headers1).json()
    if not r2:
        raise Exception(f'''у игрока {namee} нет последних игр за 24 часа!''')
    name1 = r1['username']
    acc = r2[0]['accuracy']
    acc1 = acc*100
    acc_r = round(acc1, 2)
    combo = r2[0]['max_combo']
    mods = r2[0]['mods']
    if not mods:
        mods = 'NoMod'
    pp = r2[0]['pp']
    rank = r2[0]['rank']
    stat = r2[0]['statistics']
    count_300 = stat['count_300']
    count_100 = stat['count_100']
    count_50 = stat['count_50']
    count_miss = stat['count_miss']
    star = r2[0]['beatmap']['difficulty_rating']
    diff_name = r2[0]['beatmap']['version']
    status = r2[0]['beatmap']['status']
    star_str = str(star)

    creator = r2[0]['beatmapset']['creator']
    title = r2[0]['beatmapset']['title']
    artist = r2[0]['beatmapset']['artist']
   

    f = f = open('temp/osu.json', 'wb')
    data = json.dumps(r2)
    b = bytes(data, 'utf-8')
    f.write(b)
    f.close()

    f1 = open('temp/cover.jpg', 'wb')
    pic = requests.get(r2[0]['beatmapset']['covers']['cover']).content
    f1.write(pic)
    f1.close()
    
    event.bot.upload_files([{'data' : 'temp/cover.jpg', 'type' : 'photo'}], event.peer_id ,message = f'''Последний скор игрока {name1}:
    
    {artist} - {title} [{diff_name}] by {creator} <{status}>
    Сложность: {star_str}✩
    Моды: {mods}
    Акка: {acc_r}%
    Ранк: {rank}
    Комба: {combo}x
    Статы: {count_300}x / {count_100}x / {count_50}x / Miss: {count_miss}x
    Пепе: {pp} pp
    ''')


HandleCmd ("гатари", 0, gatari)
HandleCmd ("г", 0, gatari)

HandleCmd ("с", 0, osu)
HandleCmd ("стата", 0, osu)

HandleCmd ("ласт", 0, osu_v2)
HandleCmd ("л", 0, osu_v2)

HandleCmd ("link", 0, link)
HandleCmd ("линк", 0, link)

HandleCmd ("ник", 0, asd)
HandleCmd ("дб", 0, db_create)
HandleCmd ("м", 0, mode_change)

