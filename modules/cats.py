import requests


def cat(event):
    req = requests.get('https://aws.random.cat/meow').json() 
    f = open ('temp/hentai.jpg', 'wb') 
    pic = requests.get(req['file']).content 
    f.write(pic)
    f.close()
    event.bot.upload_files([{'data': 'temp/hentai.jpg', 'type': 'photo'}],event.peer_id, message='Мяу.') 
     
def waifu(event):
    req = requests.get('https://api.waifu.pics/sfw/waifu').json()
    f = open ('temp/waifu.jpg', 'wb') 
    pic = requests.get(req['url']).content 
    f.write(pic)
    f.close()
    event.bot.upload_files([{'data': 'temp/waifu.jpg', 'type': 'photo'}],event.peer_id, message='Держи.')
def hent(event):
    req = requests.get('https://api.waifu.pics/nsfw/waifu').json()
    
    f = open ('temp/hentai.jpg', 'wb') 
    pic = requests.get(req['url']).content 
    f.write(pic)
    f.close()
    event.bot.upload_files([{'data': 'temp/hentai.jpg', 'type': 'photo'}],event.peer_id, message='Держи.') 

def trap(event):
    req = requests.get('https://api.waifu.pics/nsfw/trap').json()
    f = open ('temp/trap.jpg', 'wb') 
    pic = requests.get(req['url']).content 
    f.write(pic)
    f.close()
    event.bot.upload_files([{'data': 'temp/trap.jpg', 'type': 'photo'}],event.peer_id, message='Держи.')
def coffee(event):
    req = requests.get('https://coffee.alexflipnote.dev/random.json').json()
    f = open ('temp/coffee.jpg', 'wb') 
    pic = requests.get(req['file']).content 
    f.write(pic)
    f.close()
    event.bot.upload_files([{'data': 'temp/coffee.jpg', 'type': 'photo'}],event.peer_id, message='Доброе утро)')
def food(event):
    req = requests.get('https://foodish-api.herokuapp.com/api/').json()
    f = open ('temp/food.jpg', 'wb') 
    pic = requests.get(req['image']).content 
    f.write(pic)
    f.close()
    event.bot.upload_files([{'data': 'temp/food.jpg', 'type': 'photo'}],event.peer_id, message='Приятного Аппетита! ')

HandleCmd('кофе', 0, coffee)    
HandleCmd('котики', 0, cat  )
HandleCmd ('вайфу', 0, waifu)
HandleCmd ('хентай', 0, hent)
HandleCmd ('трап', 0, trap)
HandleCmd ('еда' , 0, food )