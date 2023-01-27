from asyncio import Handle
from time import strftime
import requests
import random
from datetime import datetime, date, time
import re

def idnf(event):
    m = event.bot.method("users.get", user_ids = event.args, fields = 'city, bdate, last_seen, sex, followers_count, country, online, is_closed, photo_id, domain, relation, counters, first_name_acc,last_name_acc')

    
    #Исключения
    if 'v' in m:
        raise Exception('пользователь не найден')
    if 'deactivated'in m['response'][0]:
        raise Exception ('пользователь удален')
    rel = "Неизвестно"

    #Проверка закрыт ли профиль
    close = m['response'][0]['is_closed']
    if m['response'][0]['is_closed'] == False:
       close = 'открыт'
    else:
        close = 'закрыт'
    
    #Имя Фамилия    
    name = 'Неизвестно'
    if 'first_name' in m['response'][0]:
        name = m["response"][0]['first_name']
    fname = 'Неизвестно'
    if 'last_name' in m['response'][0]:
        fname = m["response"][0]['last_name']

    #Id
    idd = 'Неизвестно'
    if 'id' in m['response'][0]:
        idd = m['response'][0]['id']
    domain = m['response'][0]['domain']

    #Дата рождения    
    dat = "Неизвестно"
    if 'bdate' in m['response'][0]:
        dat = str(m["response"][0]["bdate"])
    
    #Город, Страна
    cit = 'Неизвестно'
    if 'city' in m['response'][0]:
        cit = m["response"][0]["city"]["title"]  
    country = 'Неизвестно'
    if 'country' in m['response'][0]:
        country = m["response"][0]['country']['title']

    #Время последенего посещения
    seen = 'Неизвестно'
    if 'last_seen' in m['response'][0]: 
        seen = datetime.fromtimestamp(m['response'][0]['last_seen']['time']).strftime('%H:%M %d.%m.%Y')
    else:    
        seen= 'Неизвестно'
     
    #Время регистрации
    r = requests.get('https://vk.com/foaf.php?id='+str(idd)+'')
    p = re.compile(r'<ya:created dc:date="([^"]*)"')  
    t = p.findall(r.text)[0].strip('T')[0:16]
    n = re.sub(r'[^0-9-:]',' ', t)

    #Пол
    sex = m['response'][0]['sex']
    if m['response'][0]['sex'] == 1:
        sex = "Женский"
    elif m['response'][0]['sex'] == 2:
        sex = "Мужской"
    else:
        sex = "Неизвестно"

    #Количество друзей
    fcount = 'Неизвестно'
    if 'followers_count'in m['response'][0]:
        fcount = m['response'][0]['followers_count']
    
    #Количество подписчиков
    f_count = m['response'][0]['counters']['friends']

    #Статус
    online = ''
    if m['response'][0]['online'] == 1:
        online = 'Онлайн'
    else:
        online = 'Оффлайн'
      
    
    #Семейное положения
    if 'relation' in m['response'][0]:
        rel = m['response'][0]['relation']
    rel_id = "Неизвестно"
    if rel == 3 and m['response'][0]['sex'] == 1:
        rel = "Помолвлена с"
    if rel == 3 and m['response'][0]['sex'] == 2:
        rel = "Помолвлен с"
    if rel == 4 and m['response'][0]['sex'] == 1:
        rel = "Замужем за "
    if rel == 4 and m['response'][0]['sex'] == 2:
        rel = "Женат на" 
    if rel == 5:
        rel = "Всё сложно"
    if rel == 6:
        rel = "В активном поиске"
    if rel == 7 and m['response'][0]['sex'] == 1:
        rel = "Влюблена в"
    if rel == 7 and m['response'][0]['sex'] == 2:
        rel = "Влюблен в"
    if 'relation_partner' in m['response'][0]:
        rel_id = "@id"+str(m['response'][0]['relation_partner']['id'])+"("+m['response'][0]['relation_partner']['first_name']+" "+m['response'][0]['relation_partner']["last_name"]+")"

    #Фото
    if 'photo_id' in m['response'][0]:
        photo = 'photo' + str(m['response'][0]['photo_id'])
    else:
        photo = ""


    t = (f"""[Профиль {close}]
{name} {fname}
id: {idd}(@{domain})
Дата рождения: {dat}
Город: {country}, {cit}
Дата посещения: {seen}
Дата регистрации: {n}
Пол: {sex}
Кол-во друзей: {f_count}
Семейное положение: {rel} {rel_id}
Подписчики: {fcount}
Статус: {online}
""")
    event.message_send (t, attachment = photo )

HandleCmd('ид', 0, idnf)
HandleCmd('id',0, idnf)