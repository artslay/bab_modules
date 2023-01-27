from PIL import Image, ImageFile, ImageDraw, ImageFont
ImageFile.LOAD_TRUNCATED_IMAGES = True
import textwrap
import requests
import datetime
import time
import re 



def prepare_mask(size, antialias = 2):
	mask = Image.new('L', (size[0] * antialias, size[1] * antialias), 0)
	ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
	return mask.resize(size, Image.ANTIALIAS)

def crop(im, s):
	w, h = im.size
	k = w / s[0] - h / s[1]
	if k > 0: im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
	elif k < 0: im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
	return im.resize(s, Image.ANTIALIAS)

def quote(event):
# 	try:
		fwd_msg = GetForwardMsg(event)
		date = fwd_msg[0]['date'] 
		ret = fwd_msg[0]['from_id']
		text = ''

		if ret > 0:
			ret = event.bot.method('users.get', **{'user_ids': ret, 'fields': 'photo_max'})
			user = ret['response'][0]['first_name'] + ' ' + ret['response'][0]['last_name']
		else:
			ret = event.bot.method('groups.getById', **{'group_ids': ret*(-1), 'fields': 'photo_max'})
			user = ret['response'][0]['name']

		rsize = (700, 400)
		f = ImageFont.truetype('Files/Fonts/12.ttf', 30)
		fs = ImageFont.truetype('Files/Fonts/12.ttf',20)
		fss = ImageFont.truetype('Files/Fonts/12.ttf', 15)
		res = Image.new("RGB", rsize, color=(0, 0, 0))
		tex = Image.new("RGB", rsize, color=(0, 0, 0))
		draw = ImageDraw.Draw(tex)

		if len(text) > 70:
			font = fss
		else:
			font = f

		sidth = int(draw.textsize(" ", font=font)[0])

		width, height = 0, 0

		for line in [l['text'] for l in fwd_msg]:
			for word in line.split():
				word_width = len(word) * sidth
		
				if width + word_width >= rsize[0] - 500:
					width = 0
					text += "\n"
		
				width += sidth + word_width
				text += word + " "
	
			width = 0
			text += "\n"
	
		text = text[:-1]
		a = re.findall(r'\[A-Z0-9]+\|.+?\]', text)
		for i in a:
			b = i.split('|')[1][:-1]
			text = text.replace(i,b)
		width, height = draw.multiline_textsize(text, font=font)
		draw.multiline_text((0, 0), text, font=font)

		y = rsize[1] // 2 - height // 2
		x = 300 + (rsize[0] - 370 - width) // 2

		res.paste(tex, (x, y))

		if y <= 10:  
			#event.message_send("")

		    if height < 110:
			    height = 110
			    y = rsize[1] // 2 - height // 2

		size = (200, 200)
		url = ret['response'][0]['photo_max']
		avatar = requests.get(url, stream=True).raw
		txt = Image.new('RGBA', res.size, (255, 255, 255, 0))
		im = Image.open(avatar).convert("RGBA")
		im = crop(im, size) 
		im.putalpha(prepare_mask(size, 2))
		draw = ImageDraw.Draw(res)
		dt = time.strftime("%d.%m.%Y", time.localtime(date))
		if False:#detect(user) == 'ja':
			font = ImageFont.truetype('Files/Fonts/12.ttf', 24)
			draw.multiline_text((25, 310), f"\n  {user}\n  {dt}", font=font)
		else:
			draw.multiline_text((25, 310), f"\n  {user}\n  {dt}", font=fs)
		res.paste(im, (25, 100), im)
		res.save('tmp/quote.png')
		event.bot.upload_files([{'data': 'tmp/quote.png', 'type': 'photo'}], event.peer_id, message='#Цитата')
	    
	    #except Exception as e:
		    #event.message_send("Укажите цитируемое сообщение({})".format(e))

HandleCmd('цитата', 0, quote)