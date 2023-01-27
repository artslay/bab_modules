import json
import requests
import random

def r34(event):
    url = 'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index'
    try:
        r = requests.get(url, params = {
        'limit' : 100,
        'tags' : event.args,
        'json' : 1
        }).json()
        f = open ('temp/yande.jpg', 'wb')
        rand = random.choice(r)
        pic = requests.get(rand['sample_url']).content
        tags = rand['tags'] 
        f.write(pic)
        f.close()

        event.bot.upload_files([{'data': 'temp/yande.jpg', 'type': 'photo'}],event.peer_id, message = f"""Поиск по r34:
        Тэги: {tags}""")
    except:
        event.message_send('По тегам: '+event.args+', ничего не найдено!')

HandleCmd ('r34', 0, r34)
HandleCmd ('34', 0, r34)
