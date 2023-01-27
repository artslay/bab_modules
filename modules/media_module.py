#Если ваш бот группа, необходим токен страницы, иначе поиск работать не будет. Группам такая возможность не доступна

import requests
import random


def music(event):
    if event.bot.is_group():
        bot = event.bot.getBot('0')
    else:
        bot = event.bot

    if not bot:
        return event.message_send('Для работы необходим токен страницы')
    
    info = []
    param = (('v', '5.81'), ('q',event.args),('count','300'),('sort','2'),('access_token',event.bot.token))
    res = requests.post('https://api.vk.com/method/audio.search', data=param).json()
    if (res['response']['count'] != 0 ):
        for j in range(10):
            item = random.randint(0, len(res['response']['items'])-1)
                
            if 'audio'+str(res['response']['items'][item]['owner_id'])+'_'+str(res['response']['items'][item]['id']) in info:
                continue
            info.append('audio'+str(res['response']['items'][item]['owner_id'])+'_'+str(res['response']['items'][item]['id']))

    if len(info) < 10:
        param = (('v', '5.81'), ('q',event.args),('count','300'),('sort','0'),('access_token',event.bot.token))
        res = requests.post('https://api.vk.com/method/audio.search', data=param).json()
        if (res['response']['count'] != 0 ):
            for j in range(10):
                item = random.randint(0, len(res['response']['items'])-1)
                
                if 'audio'+str(res['response']['items'][item]['owner_id'])+'_'+str(res['response']['items'][item]['id']) in info:
                    continue
                info.append('audio'+str(res['response']['items'][item]['owner_id'])+'_'+str(res['response']['items'][item]['id']))

    if len(info) >0:
        event.message_send('Музыка по запросу '+event.args, attachment=','.join(info))
    else:
        event.message_send('Музыка по запросу '+event.args+' не найдена')

def docs(event):
    if event.bot.is_group():

        bot = event.bot.getBot('0')
    else:
        bot = event.bot

    if not bot:
        return event.message_send('Для работы необходим токен страницы')
    
    info = []
    param = (('v', '5.81'), ('q',event.args),('count','300'),('sort','2'),('access_token',event.bot.token))
    res = requests.post('https://api.vk.com/method/docs.search', data=param).json()
    if (res['response']['count'] != 0 ):
        for j in range(10):
            item = random.randint(0, len(res['response']['items'])-1)
                
            if 'audio'+str(res['response']['items'][item]['owner_id'])+'_'+str(res['response']['items'][item]['id']) in info:
                continue
            info.append('doc'+str(res['response']['items'][item]['owner_id'])+'_'+str(res['response']['items'][item]['id']))

    if len(info) < 10:
        param = (('v', '5.81'), ('q',event.args),('count','300'),('sort','0'),('access_token',event.bot.token))
        res = requests.post('https://api.vk.com/method/docs.search', data=param).json()
        if (res['response']['count'] != 0 ):
            for j in range(10):
                item = random.randint(0, len(res['response']['items'])-1)
                
                if 'doc'+str(res['response']['items'][item]['owner_id'])+'_'+str(res['response']['items'][item]['id']) in info:
                    continue
                info.append('doc'+str(res['response']['items'][item]['owner_id'])+'_'+str(res['response']['items'][item]['id']))

    if len(info) >0:
        event.message_send('Доки по запросу '+event.args, attachment=','.join(info))
    else:
        event.message_send('Доки по запросу '+event.args+' не найдены')



def video(event):

    if event.bot.is_group():
        bot = event.bot.getBot('0')
    else:
        bot = event.bot

    if not bot:
        return event.message_send('Для работы необходим токен страницы')
        
    param = (('v', '5.81'), ('q',event.args),('count','200'),('adult','0'),('access_token',event.bot.token))
    res = requests.post('https://api.vk.com/method/video.search', data=param).json()
    info = []

    if (len(res['response']['items']) != 0):
        for k in range(len(res['response']['items'])):
            for i in range(10):
                itm = random.randint( 0, len(res['response']['items'])-1)
                title = res['response']['items'][itm]['title'].lower()

                info.append('video'+str(res['response']['items'][itm]['owner_id'])+'_'+str(res['response']['items'][itm]['id']))

        event.message_send('Видео по запросу '+event.args+'(Всего: {})'.format(len(res['response']['items']))+':',attachment=",".join(info))
    else:
        event.message_send('Видео по запросу '+event.args+ ' не найдено')
    

def porn(event):

    if event.bot.is_group():
        bot = event.bot.getBot('0')
    else:
        bot = event.bot

    if not bot:
        return event.message_send('Для работы необходим токен страницы')
        
    param = (('v', '5.81'), ('q',event.args),('count','200'),('adult','1'),('access_token',event.bot.token))
    res = requests.post('https://api.vk.com/method/video.search', data=param).json()
    info = []

    if (len(res['response']['items']) != 0):
        for k in range(len(res['response']['items'])):
            for i in range(10):
                itm = random.randint( 0, len(res['response']['items'])-1)
                title = res['response']['items'][itm]['title'].lower()

                info.append('video'+str(res['response']['items'][itm]['owner_id'])+'_'+str(res['response']['items'][itm]['id']))

        event.message_send('Порно по запросу '+event.args+'(Всего: {})'.format(len(res['response']['items']))+':',attachment=",".join(info))
    else:
        event.message_send('Порнуха '+event.args+ ' не найдена')
     

HandleCmd('музыка', 0, music)
HandleCmd('видео' , 0, video)
HandleCmd('порно', 0, porn)
HandleCmd ('доки', 0, docs)