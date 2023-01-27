TRIGGERS = []

def trigger_message(event, trigger, **params):
        if event.userid > 0:
                event.message_send(trigger.text_out, **params)
    
class Trigger:
        __slots__ = ('text_in', 'text_out', 'func', 'func_params')
        
        def __init__(self, text_in, text_out, func, params):
            self.text_in = text_in
            self.text_out = text_out
            self.func = func
            self.func_params = params


def AddTrig(text_in, text_out ='', func=trigger_message, **params):
        TRIGGERS.append(Trigger(text_in.lower(), text_out, func, params))
        
def ListenTriggers(event, upd):
        if len(event.splited) == 1:
                for trigger in TRIGGERS:
                        if trigger.text_in == event.splited[0]:
                                trigger.func(event, trigger, **trigger.func_params)
                    
HandleEvent("MSG", ListenTriggers)

AddTrig ("км", "Кто меня звал? \nПиши 'км  команды' для помощи")

#AddTrig("что", "Я тебя люблю ❤️")