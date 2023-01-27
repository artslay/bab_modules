import requests 

#STD
def osu(event):
    url = "https://osu.ppy.sh/api/get_user"
    api = "2de8729119015d4f3aed90f9f6a1a3464c95e982"
    o = requests.get (url, params ={
        "k" :api,
        "u" : event.args
    }).json()
    
    b = requests.get ("https://osu.ppy.sh/api/get_user_best", params= {
        "k" : api, 
        "u" : event.args, 
        "limit" : 10
    }).json()
    beatmap = b[0]['beatmap_id']
    t = requests.get ("https://osu.ppy.sh/api/get_beatmaps", params= {
        "k" : api, 
        "b" : beatmap
    }).json()
    b_diff = t[0]["version"]
    b_artist = t[0]["artist"]
    b_star = t[0]["difficultyrating"]
    b_name = t[0]["title"]
    beatmap_pp = b[0]['pp']
    
    nickname = o[0]['username']
    pp = o[0]['pp_raw' ]
    rank = o[0]['pp_rank']
    country_rank =o[0]['pp_country_rank']
    join = o[0]['join_date']
    country = o[0]['country']
    lvl = o[0]['level']
    playcount = o[0]['playcount']
    acc = round(float(o[0]['accuracy']))
    pp_recent = b[0]['rank']
    mods = b[0]['enabled_mods']
    if mods == '64':
        mods = 'DT'
    if mods == '0':
        mods == 'NoMod'
    try:
        b_diff, b_artist, b_star_, b_name, beatmap_pp, nickname, pp, rank, country_rank, join, country, lvl, playcount, acc, pp_recent, mods
    except:
        event.message_send (f""" Информация о пользователе: {nickname}
Дата регистрации: {join}
Страна: {country}
Топ страны: # {country_rank}
Топ мира: # {rank}
PP: {pp}
Уровень: {round(float(lvl),2)} 
Общая точность: {acc}%
Плейкаунт: {playcount}

Топ скоров:
#1 {b_artist} - {b_name}[{b_diff}] - {pp_recent} ранк
{round(float(b_star), 2)}✩, получено {beatmap_pp}pp [{mods}]
  """)

#Последний скор
def last(event):
    api = "2de8729119015d4f3aed90f9f6a1a3464c95e982"
    l = requests.get ("https://osu.ppy.sh/api/get_user_recent", params= {
      "k" : api, 
      "u" : event.args, 
      "limit" : "1"
    }).json()
    event.message_send (l[0]["rank"])

#osu!mania
def osu_mania(event):
    url = "https://osu.ppy.sh/api/get_user"
    api = "2de8729119015d4f3aed90f9f6a1a3464c95e982"
    o = requests.get (url, params ={
        "k" :api,
        "m" : 3,
        "u" : event.args
    }).json()

    b = requests.get("https://osu.ppy.sh/api/get_user_best", params={
        "k": api,
        "u": event.args,
        'm': 3,
        "limit": 10
    }).json()
    beatmap = b[0]['beatmap_id']
    t = requests.get("https://osu.ppy.sh/api/get_beatmaps", params={
        "k": api,
        "b": beatmap
    }).json()
    b_diff = t[0]["version"]
    b_artist = t[0]["artist"]
    b_star = t[0]["difficultyrating"]
    b_name = t[0]["title"]
    beatmap_pp = b[0]['pp']

    nickname = o[0]['username']
    pp = o[0]['pp_raw']
    rank = o[0]['pp_rank']
    country_rank = o[0]['pp_country_rank']
    join = o[0]['join_date']
    country = o[0]['country']
    lvl = o[0]['level']
    playcount = o[0]['playcount']
    acc = round(float(o[0]['accuracy']))
    pp_recent = b[0]['rank']
    mods = b[0]['enabled_mods']
    if mods == '64':
        mods = 'DT'
    if mods == '0':
        mods == 'NoMod'
    event.message_send (f""" Информация о пользователе: {nickname}
Дата регистрации: {join}
Страна: {country}
Топ страны: #{country_rank}
Топ мира: #{rank}
PP: {pp}
Уровень: {lvl} 
Общая точность: {acc}%
Плейкаунт: {playcount}

Топ скоров:
#1 {b_artist} - {b_name}[{b_diff}] - {pp_recent} ранк
{round(float(b_star), 2)}✩, получено {beatmap_pp}pp [{mods}]
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


HandleCmd ("гатари", 0, gatari)
HandleCmd ("г", 0, gatari)
HandleCmd ("осу", 0, osu)
HandleCmd ("мания", 0, osu_mania)
HandleCmd ("л", 0, last)