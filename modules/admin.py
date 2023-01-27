import json
import requests
import os
import platform
import sys
import subprocess


def test(event):
    users = 147111159
    if event.userid == users:
        command = event.args
        pipe = os.popen(command) 
        event.message_send (pipe.read())
    else:
        event.message_send ("Недостаточно прав, придурок")
        
def test1(event):
    users = 147111159
    if event.userid == users:
        event.message_send (str(exec(event.args))) 
    else:
        event.message_send ('Недостаточно прав для выполнения команды.')

def py(event):
    users = 147111159
    if event.userid == users:
        event.message_send (str(eval(event.args))) 
    else:
        event.message_send ('Недостаточно прав для выполнения команды.')

def kick(event):
    fwd_msg = GetForwardMsg(event)
    ret = fwd_msg[0]['from_id']
    e = event.peer_id - 2000000000
    m = event.bot.method("messages.removeChatUser", chat_id = e, member_id = ret)
    users = 147111159
    if event.userid == users:
        event.message_send('Участник исключен.')
    else:
        event.message_send ('Недостаточно прав для выполнения команды.')    
    

HandleCmd ('exec', 0, test1)
HandleCmd ('е', 0, test)
HandleCmd('п', 0, py)
HandleCmd('кик', 0, kick)