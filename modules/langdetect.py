def message(data):
	return [data['response']['items'][0]['reply_message']] if not data['response']['items'][0]['fwd_messages'] else data['response']['items'][0]['fwd_messages']
	
def GetForwardMsg(event):
	if hasattr(event, 'page_pid'):
		return message(event.bot.getBot('page').method('messages.getById', message_ids=event.message_id))
	elif event.bot.is_group():
		return event.updates['object']['fwd_messages'] 
	else:
		return message(event.bot.method('messages.getById', message_ids=event.message_id))

def GetAttachment(event):
	if hasattr(event, 'page_pid'):
		return event.bot.getBot('page').method('messages.getById', message_ids=event.message_id)['response']['items'][0]['fwd_messages']
	elif event.bot.is_group():
		return event.updates['object']['attachments']
	else:
		return event.bot.method('messages.getById', message_ids=event.message_id)['response']['items'][0]['attachments']


SET_GLOBAL('GetForwardMsg', GetForwardMsg)
SET_GLOBAL('GetAttachment', GetAttachment) 