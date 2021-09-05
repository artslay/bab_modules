def idnf(event):
    m = event.bot.method("users.get", user_ids = event.args, fields = 'city, bdate, last_seen, sex, followers_count, country, online, is_closed, photo_id')
     #= event.bot.method("users.get", user_ids = event.userid, fields = 'city, bdate, last_seen, sex, followers_count')
    if 'v' in m:
        raise Exception('пользователь не найден')
    if 'deactivated'in m['response'][0]:
        raise Exception ('пользователь удален')
        
        #raise Exception ("неверный id")
        
    seen = 'Неизвестно'
    if 'last_seen' in m['response'][0]: 
        seen = datetime.fromtimestamp(m['response'][0]['last_seen']['time']).strftime('%H:%m %d.%m.%Y')
    else:    
        seen= 'Неизвестно' 
        
    close = m['response'][0]['is_closed']
    if m['response'][0]['is_closed'] == False:
       close = 'открыт'
    else:
        close = 'закрыт'
        
    cit = 'Неизвестно'
    if 'city' in m['response'][0]:
        cit = m["response"][0]["city"]["title"]
        
    country = 'Неизвестно'
    if 'country' in m['response'][0]:
        country = m["response"][0]['country']['title']
        
    dat = "Неизвестно"
    if 'bdate' in m['response'][0]:
        dat = m["response"][0]["bdate"]
        
    sex = m['response'][0]['sex']
    if m['response'][0]['sex'] == 1:
        sex = "Женский"
    elif m['response'][0]['sex'] == 2:
        sex = "Мужской"
    else:
        sex = "Неизвестно"
        
    name = 'Неизвестно'
    if 'first_name' in m['response'][0]:
        name = m["response"][0]['first_name']
    fname = 'Неизвестно'
    if 'last_name' in m['response'][0]:
        fname = m["response"][0]['last_name']
    idd = 'Неизвестно'
    if 'id' in m['response'][0]:
        idd = m['response'][0]['id']
        
    p = re.compile(r'<ya:created dc:date="([^"]*)"')
    r = requests.get('https://vk.com/foaf.php?id='+str(idd)+'')
    t = p.findall(r.text)[0]
    
    
    fcount = 'Неизвестно'
    if 'followers_count'in m['response'][0]:
        fcount = m['response'][0]['followers_count']
    online = ''
    if m['response'][0]['online'] == 1:
        online = 'Онлайн'
    else:
        online = 'Оффлайн'
    if 'photo_id' in m['response'][0]:
        photo = 'photo' + str(m['response'][0]['photo_id'])
    else:
        photo = ""
    
    
    t = (f"""[Профиль {close}]
{name} {fname}
id: {idd}
Дата рождения: {dat}
Город: {country}, {cit}
Дата посещения: {seen}
Дата регистрации: {t}
Пол: {sex}
Подписчики: {fcount}
Статус: {online}""")
    event.message_send (t, attachment = photo )

HandleCmd('id',0, idnf)
HandleCmd('ид', 0, idnf)