from asyncio import Handle
from time import strftime
import requests
import random
from datetime import datetime, date, time
import re

def dick(event):
    event.message_send("конец, член, мальчик, достоинство, крайняя плоть, детородный орган, хрен, мужской член, мужское достоинство, шишка, причинное место, мужской половой орган, болт, хобби, нефритовый стержень, хер, пожарник, мужской орган, сморчок, уд, кила, пипетка, убивец, ванька-встанька, двадцать первый палец, жила подпупная, фалл, пинус, писюн, семяпровод, мехирь, мотовило, балун, торчило, причиндал, кукан, пипка, сюнька, самочерный, елдык, щекотун")

def who(event):
    m = event.bot.method ("messages.getConversationMembers", peer_id = event.peer_id)
    r = random.choice (m['response']['profiles'])
    event.message_send(f"""Я думаю, что {event.args} у нас @id{r['id']}({r['first_name']} {r['last_name']})""")

def who_acc(event):
    m = event.bot.method ("messages.getConversationMembers", peer_id = event.peer_id, fields = 'first_name_acc, last_name_acc')
    r = random.choice (m['response']['profiles'])
    event.message_send(f"""Я думаю, что {event.args} @id{r['id']}({r['first_name_acc']} {r['last_name_acc']})""")

def bottle(event):
    m = event.bot.method ("messages.getConversationMembers", peer_id = event.peer_id)
    r = random.choice (m['response']['profiles'])
    name ="("+r['first_name']+" "+r['last_name']+")"
    
    w1 = ['На бутылку у нас присядет','Счастливым обладателем бутылки в анусе становится']
    w2 = ['Хех, бутылки закончились\nСядет на баночку у нас','Похоже бутылок не осталось.\nНо есть банки.\nПрисядет'] 
    rnd = random.randint(1,3)
    if rnd == 1:
        event.message_send (random.choice(w2)+" "+"@id"+str(r['id']) +name, attachment='photo147111159_457260164')
    else:
        event.message_send (random.choice(w1)+" "+"@id"+str(r['id'])+name, attachment='photo147111159_457260165')
    #second = ("Хех, бутылки кончились.\nОстались банки.\aПрошу, присаживайся, " +" "+r['first_name']+" "+r['last_name']+"\n""Смотри чтобы не лопнула", attachment = "photo147111159_457260166")

def cmds(event):
    cmd = f'''
    Основные команды:
    мyзыкa: поиск музыки по запросу
    видеo: поиск видео по запросу
    доки: поиск документов по запросу
    порно: поиск прона по запросу
    погодa: погода
    инфa: вероятность чего-то
    кто/кого: выбирает случайного участника
    цитата: цитирует сообщение
    курс: курс некоторых валют
    ид: информация о пользователе
    скажи: озвучивает сообщение
    данет: случайный выбор да или нет + гиф
    бутылка: набутыливает случайного участника
    осу [ваш никнейм]: показывает статистику профиля osu! (STD)
    мания [ваш никней]: показывает статистику профиля osu! (Mania)
    гатари: показывает статистику профиля osu!gatari (Mania) (WIP)
    когда: случайная дата
    вики: поиск в Wikipeida
    
    Изображения:
    r34/34: поиск по тегам на rule34
    ада: случайный арт Ады Вонг
    лоли/некололи: показывает лолю
    котики: все же любят котиков, верно?
    трап: рандомный аниме трап
    вайфу: рандомная вайфу
    хентай: рандомная хентай пикча
    еда: рандомное блюдо(временно не работает)
    кофе: пикча кофе?

    Команды Администратора:
    exec: Динамическое выполнение кода
    e: Выполнение команды внутри Linux
    п: Выполнение команды внутри ядра бота
    кик: Исключение выбранного участника
    '''
    event.message_send(f'{cmd}')

def skin(event):
    event.message_send ('https://drive.google.com/file/d/1hK4pOYHCHVOorf8vRaNGI77IJtdk1gPD/view?usp=share_link')
    
def info(event):
    event.message_send('Вероятность того, что {} составляет {}%'.format(event.args, random.randint(0, 146)))

def rand(event):
    yesno = requests.get ("https://yesno.wtf/api").json()
    picture = yesno['image']
    answ = yesno["answer"]
    if answ == 'yes':
        answ = "Да" 
    if answ == 'no':
        answ = "Нет"
    f = open ('temp/yesno.gif', 'wb') 
    pic = requests.get(picture).content 
    f.write(pic)
    f.close()
    event.bot.upload_files([{'data': 'temp/yesno.gif', 'type': 'doc'}], event.peer_id, message= answ) 
    
def when (event):
    time = ['января','февраля','декабря','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
    #time = ['февраля']
    date = random.randint(1,31)
    date_feb = random.randint(1,28)
    year = random.randint(2022, 2066)
    if 'февраля' in time:
        event.message_send (f'''Я думаю, что {event.args} {str(date_feb)} {random.choice(time)} {str(year)} года''')
    else:
        event.message_send (f'''Я думаю, что {event.args} {str(date)} {random.choice(time)} {str(year)} года''')

HandleCmd('хуй', 0, dick)
HandleCmd('команды', 0, cmds)
HandleCmd('помощь', 0, cmds)
HandleCmd('инфа', 0, info)
HandleCmd('скин', 0, skin)
HandleCmd('кто', 0, who)
HandleCmd('кого',0, who_acc)
HandleCmd('бутылка', 0, bottle)
HandleCmd ('данет', 0, rand)
HandleCmd ('когда', 0, when)