import requests
import re

def wiki(event):
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles='+event.args+'&redirects=1&utf8=1&exintro=1'
    url1 = 'https://ru.wikipedia.org/w/api.php?action=opensearch&format=json&search='+event.args+'&utf8=1'
    r = requests.get (url).json()
    p = requests.get(url1).json()
    try:
        for w in r['query']['pages']:
            t = r['query']['pages'][w]['extract']
            event.message_send('Поиск по запросу'+' '+event.args+' '+'в Wikipedia:\n'+re.sub (r'\<[^>]*\>', '', t)+'\nПохожие запросы: '+', '.join(p[1]))
    except:
        event.message_send('По запросу '+event.args+', ничего не найдено!')
HandleCmd('вики', 0, wiki)