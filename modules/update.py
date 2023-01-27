import importlib
import os

def update_cmds(event):
    GET_GLOBAL('HANDLERS').clear()
    GET_GLOBAL('CMDS').clear()
 
    for module in os.listdir(MODULES_PATH):
        if module[-3:] == '.py':
            importlib.reload(__import__(module[:-3]))
    users = 147111159
    if event.userid == users:
        event.message_send('Обновлено✅ ')
    else:
        event.message_send ('Недостаточно прав')
HandleCmd('обновись', 3, update_cmds)
HandleCmd('о', 3, update_cmds)