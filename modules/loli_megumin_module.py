#Модуль для показа лоли и некололи с группы Бота Мегумин
#Версия: 1.0
#Авторы: https://vk.com/edwardfuchs
#Git: None
import requests
import random



#Настройка
text_loli = "Вот тебе лолька.<br>Её номер {num}/{all}<br>"
text_nekololi = "Вот тебе некололька.<br>Её номер {num}/{all}<br>"
text_feet = "Ножки. <br>{num} из {all}<br>"
text_ass = "Жжжжёпа. <br>{num} из {all}<br>"
text_ada = "Ада <3 {num} из {all}"
#Получение токена страницы
def get_bot(event):
    bot = None
    if event.bot.is_group():
        bot = event.bot.getBot("page")
        #для старой версии ядра
        if bot == None:
            bot = event.bot.getBot(0)
    else:
        bot = event.bot
    return bot
    
    
def get_count(bot, owner_id, album_id):
    res = bot.method("photos.get", owner_id = owner_id, album_id = album_id, count = 0)
    if "response" not in res:
        return
    count = res['response']['count']
    return count
    

def get_photo(bot, owner_id, album_id, num):
    res = bot.method("photos.get", owner_id = owner_id, album_id = album_id, count = 1, offset = num)
    if "response" not in res:
        return
    photoid = str(res['response']['items'][0]['id'])
    return f'photo{owner_id}_{photoid}'


def loli(event):
    bot = get_bot(event)
    if not bot:
        event.message_send('Для работы необходим токен страницы')
        return
    #кол. фото в альбоме
    count = get_count(bot, "-169151978", "262529122")
    if not count:
        event.message_send(f'Не удалось получить кол. фото.')
        return
    num = random.randint(0,count-1)
    #получаем фото
    photo = get_photo(bot, "-169151978", "262529122", num)
    if not photo:
        event.message_send(f'Не удалось получить фото.')
        return
    #text_loli = text_loli.replace("{num}", str(num+1))
    #text_loli = text_loli.replace("{all}", str(count))
    text = text_loli.replace("{num}", str(num+1)).replace("{all}", str(count))
    #Отправляем
    event.message_send(text, attachment=photo)
    
    
def nekololi(event):
    bot = get_bot(event)
    if not bot:
        event.message_send('Для работы необходим токен страницы')
        return
    #кол. фото в альбоме
    count = get_count(bot, "-169151978", "257528235")
    if not count:
        event.message_send(f'Не удалось получить кол. фото.')
        return
    num = random.randint(0,count-1)
    #получаем фото
    photo = get_photo(bot, "-169151978", "257528235", num)
    if not photo:
        event.message_send(f'Не удалось получить фото.')
        return
    text = text_nekololi.replace("{num}", str(num+1)).replace("{all}", str(count))
    #Отправляем
    event.message_send(text, attachment=photo)


def feet(event):
    bot = get_bot(event)
    if not bot:
        event.message_send('Для работы необходим токен страницы')
        return
    #кол. фото в альбоме
    count = get_count(bot, "-168678399", "255309889")
    if not count:
        event.message_send(f'Не удалось получить кол. фото.')
        return
    num = random.randint(0,count-1)
    #получаем фото
    photo = get_photo(bot, "-168678399", "255309889" , num)
    if not photo:
        event.message_send(f'Не удалось получить фото.')
        return
    text = text_feet.replace("{num}", str(num+1)).replace("{all}", str(count))
    #Отправляем
    event.message_send(text, attachment=photo)
    
def ass (event):
    bot = get_bot(event)
    if not bot:
        event.message_send('Для работы необходим токен страницы')
        return
    #кол. фото в альбоме
    count = get_count(bot, "-99451607", "219045867"  )
    if not count:
        event.message_send(f'Не удалось получить кол. фото.')
        return
    num = random.randint(0,count-1)
    #получаем фото
    photo = get_photo(bot, "-99451607", "219045867", num)
    if not photo:
        event.message_send(f'Не удалось получить фото.')
        return
    text = text_ass.replace("{num}", str(num+1)).replace("{all}", str(count))
    #Отправляем
    event.message_send(text, attachment=photo)

def ada (event):

    bot = get_bot(event)

    if not bot:
        event.message_send('Для работы необходим токен страницы')
        return
    #кол. фото в альбоме
    count = get_count(bot, "-441911", "264644543" )
    if not count:
        event.message_send(f'Не удалось получить кол. фото.')
        return
    num = random.randint(0,count-1)
    #получаем фото
    photo = get_photo(bot, "-441911", "264644543", num)
    if not photo:
        event.message_send(f'Не удалось получить фото.')
        return
    text = text_ada.replace("{num}", str(num+1)).replace("{all}", str(count))
    #Отправляем
    event.message_send(text, attachment=photo)
    
HandleCmd('лоли', 0, loli)
HandleCmd('некололи', 0, nekololi)
HandleCmd('жопы', 0,ass)
HandleCmd ('ада', 0, ada)