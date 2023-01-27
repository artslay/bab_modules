import requests

def audio(event):
    url = "http://api.voicerss.org/"
    api ="49f4b58b962b4547949521a0dd704c51"
    r = requests.get (url, params={
        "key": api, 
        "src": event.args, 
        "hl" : "ru-ru",
        "v" : "Marina", 
        "f" : "48khz_16bit_mono", 
        "r" : "1"
    })

    f = open('audio.mp3','wb')
    f.write(r.content)
    f.close
    
    l = event.bot.method ("docs.getMessagesUploadServer", type = "audio_message")
    url = l['response']['upload_url']
    files = {'file': ('audio.mp3', open('audio.mp3', 'rb'))}
    p = requests.post (url, files = files).json()
    s = event.bot.method ('docs.save', file = p['file'])
    audio = "doc"+str(s['response']['audio_message']['owner_id']) +"_"+str(s['response']['audio_message']['id'])
    
    #event.message_send (audio)
    event.message_send ("" , attachment = ""+audio+"") 
    
def bla(event): 
    r = requests.post(
        "https://yandex.ru/lab/api/yalm/text3",
        json={"query": event.args, "intro": 1, "filter": 1},
    ).json()
    event.message_send (r["query"] + r['text'])
    
HandleCmd ("скажи", 0, audio)
HandleCmd ("бла", 0, bla)