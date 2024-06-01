#pylint:disable=W0611
import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from medo import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
stopuser = {}
token='6618438873:AAG7GZaSrz9Gvosz0DCpm8COM8-9ZakTMbQ'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=7197902508
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝙵𝚁𝙴𝙴'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝙵𝚁𝙴𝙴",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝙵𝚁𝙴𝙴':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
			keyboard.add(contact_button)
			random_number = random.randint(2, 8)
			photo_url = f'https://t.me/MEDO_MODY0/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 {BL}</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
	
		username = message.from_user.first_name
		random_number = random.randint(2, 8)
		photo_url = f'https://t.me/MEDO_MODY0/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙾𝚁 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙲𝙷𝙴𝙲𝙺 𝙸𝚃''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝙵𝚁𝙴𝙴'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝚃𝙷𝙴𝚂𝙴 𝙰𝙴𝚆 𝙱𝙾𝚃 𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂
━━━━━━━━━━━━
 𝙱𝚁𝙰𝙸𝙽𝚃𝙴𝙴 𝙰𝚄𝚃𝙷 > <code>/chk number|mm|yy|cvc</code>
𝚂𝚃𝙰𝚃𝚄𝚂 𝙾𝙽𝙻𝙸𝙽𝙴 ✅
━━━━━━━━━━━━
 3𝙳 𝙻𝙾𝙾𝙺𝚄𝙿 > <code>/vbv number|mm|yy|cvc</code>
𝙾𝙽𝙻𝙸𝙽𝙴 ✅
━━━━━━━━━━━━
 𝚂𝚃𝚁𝙸𝙿𝙴 𝙲𝙷𝙰𝚁𝙶𝙴 > <code>/str number|mm|yy|cvc</code>  𝙾𝙵𝙵𝙻𝙸𝙽𝙴 ❌
━━━━━━━━━━━━
 𝚂𝚃𝚁𝙸𝙿𝚁 𝙰𝚄𝚃𝙷 > <code>/au number|mm|yy|cvc</code> 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 ❌
━━━━━━━━━━━━
𝚆𝙴 𝚆𝙸𝙻𝙻 𝙱𝙴 𝙰𝙳𝙳𝙸𝙽𝙶 𝚂𝙾𝙼𝙴 𝙶𝙰𝚃𝙴𝚆𝙰𝚈𝚂 𝙰𝙽𝙳 𝚃𝙾𝙾𝙻𝚂 𝚂𝙾𝙾𝙽 </b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝙵𝚁𝙴𝙴'
		if BL == '𝙵𝚁𝙴𝙴':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝙵𝚁𝙴𝙴",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 {BL}</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 {BL}</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝚈𝙾𝚄 𝙲𝙰𝙽𝙽𝙾𝚃 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃 𝙱𝙴𝙲𝙰𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 𝙷𝙰𝚂 𝙴𝚇𝙿𝙸𝚁𝙴𝙳</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝙵𝚁𝙴𝙴'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"​​​​🇪🇬 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 𝙰𝚄𝚃𝙷  🇪🇬",callback_data='br')
		sw = types.InlineKeyboardButton(text=f" ♡ 𝚂𝚃𝚁𝙸𝙿𝙴 𝙲𝙷𝙰𝚁𝙶𝙴 ♡",callback_data='str')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝙲𝙷𝙾𝙾𝚂𝙴 𝚃𝙷𝙴  𝙶𝙰𝚃𝙴𝚆𝙰𝚈 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe charge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝚂𝚃𝙾𝙿𝙿𝙴𝙳 ✅\n𝙱𝙾𝚃 𝙱𝚈 ➜ @Xx_so1om_Xx')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(st(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝚂𝚃𝙰𝚃𝚄𝚂 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙲𝙷𝙰𝚁𝙶𝙴 ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝙲𝙲𝙽 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝙳𝙴𝙲𝙻𝙸𝙽𝙴𝙳 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙸𝙽𝚂𝚄𝙵𝙵 𝙸𝙲𝙸𝙴𝙽𝚃 𝙵𝚄𝙽𝙳𝚂 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝚃𝙾𝚃𝙰𝙻 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝚂𝚃𝙾𝙿 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃 𝚆𝙷𝙸𝙻𝙴 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂 𝙰𝚁𝙴 𝙱𝙴𝙸𝙽𝙶 𝙲𝙷𝙴𝙲𝙺 𝙰𝚃 𝚃𝙷𝙴 𝙶𝙰𝚃𝙴𝚆𝙰𝚈 {gate} 𝙱𝙾𝚃 𝙱𝚈@Xx_so1om_Xx''', reply_markup=mes)
					
					msg=f'''<b>𝙲𝙷𝙰𝚁𝙶𝙴 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 :  @Xx_so1om_Xx
Taken {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
					msgc=f'''<b>𝙲𝙽𝙽 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
Taken {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
					msgf=f'''<b>𝙸𝙽𝚂𝚄𝙵𝙵 𝙸𝙲𝙸𝙴𝙽𝚃 𝙵𝚄𝙽𝙳𝚂 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
					if 'success' in last:
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝙱𝙴𝙴𝙽 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳 ✅\n𝙱𝙾𝚃 𝙱𝚈 ➜ @Xx_so1om_Xx')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝚂𝚃𝙾𝙿𝙿𝙴𝙳 ✅\n𝙱𝙾𝚃 𝙱𝚈 ➜ @Xx_so1om_Xx')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝚂𝚃𝙰𝚃𝚄𝚂 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝙲𝙲𝙽 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝙳𝙴𝙲𝙻𝙸𝙽𝙴𝙳 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝚁𝙸𝚂𝙺 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝚃𝙾𝚃𝙰𝙻 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝚂𝚃𝙾𝙿 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃 𝚆𝙷𝙸𝙻𝙴 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂 𝙰𝚁𝙴 𝙱𝙴𝙸𝙽𝙶 𝙲𝙷𝙴𝙲𝙺 𝙰𝚃 𝚃𝙷𝙴 𝙶𝙰𝚃𝙴𝚆𝙰𝚈 {gate} 𝙱𝙾𝚃 𝙱𝚈 @Xx_so1om_Xx''', reply_markup=mes)
					
					msg=f'''<b>𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳✅
			
𝙲𝙰𝚁𝙳 ➼ <code>{cc}</code>
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 ➼ {last}
𝙶𝙴𝚃𝙴𝚆𝙰𝚈 ➼ {gate}		
𝙸𝙽𝙵𝙾 ➼ {card_type} - {brand}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 ➼ {country} - {country_flag} 
𝙱​​𝙸𝙽 ➼ {cc[:6]}
𝙸𝚂𝚂𝚄𝙴𝚁 ➼ {bank}
𝚃𝙸𝙼𝙴 ➼ {"{:.1f}".format(execution_time)}
𝙱𝙾𝚈 𝙱𝚈: @Xx_so1om_Xx</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(4)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝙱𝙴𝙴𝙽  𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳 ✅\n 𝙱𝙾𝚃 𝙱𝚈 ➜ @Xx_so1om_Xx')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.au') or message.text.lower().startswith('/au'))
def respond_to_vbv(message):
	gate='stripe Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝙵𝚁𝙴𝙴",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝙵𝚁𝙴𝙴'
	if BL == '𝙵𝚁𝙴𝙴':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆  {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆  {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝚈𝙾𝚄 𝙲𝙰𝙽𝙽𝙾𝚃 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃 𝙱𝙴𝙲𝙰𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 𝙷𝙰𝚂 𝙴𝚇𝙿𝙸𝚁𝙴𝙳</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝙵𝚁𝙴𝙴'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(scc(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳✅ 
- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
Taken {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	msgd=f'''<b>𝙳𝙴𝙲𝙻𝙸𝙽𝙴𝙳 ❌
			- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
Taken {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='Braintree Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝙵𝚁𝙴𝙴",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝙵𝚁𝙴𝙴'
	if BL == '𝙵𝚁𝙴𝙴':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 
 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 
 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝚈𝙾𝚄 𝙲𝙰𝙽𝙽𝙾𝚃 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃 𝙱𝙴𝙲𝙰𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 𝙷𝙰𝚂 𝙴𝚇𝙿𝙸𝚁𝙴𝙳</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝙵𝚁𝙴𝙴'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
𝚃𝙰𝙺𝙴𝙽 {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	msgd=f'''<b>𝙳𝙴𝙲𝙻𝙸𝙽𝙴𝙳 ❌
			- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
𝚃𝙰𝙺𝙴𝙽 {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	gate='stripe charge'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝙵𝚁𝙴𝙴",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝙵𝚁𝙴𝙴'
	if BL == '𝙵𝚁𝙴𝙴':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝚈𝙾𝚄 𝙲𝙰𝙽𝙽𝙾𝚃 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃 𝙱𝙴𝙲𝙰𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 𝙷𝙰𝚂 𝙴𝚇𝙿𝙸𝚁𝙴𝙳</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝙵𝚁𝙴𝙴'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(st(cc))
	except Exception as e:
		last='Error'
		print(e)
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msgd=f'''<b>𝚁𝙴𝙶𝙴𝙲𝚃𝙴𝙳 ❌
- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
𝚃𝙰𝙺𝙴𝙽 {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	msg=f'''<b>𝙲𝙷𝙰𝚁𝙶𝙴 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
𝚃𝙰𝙺𝙴𝙽 {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	msgc=f'''<b>𝙲𝙽𝙽 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx'
𝚃𝙰𝙺𝙴𝙽 {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	msgf=f'''<b>𝙸𝙽𝚂𝚄𝙵𝙵 𝙸𝙲𝙸𝙴𝙽𝚃 𝙵𝚄𝙽𝙳𝚂 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
𝚃𝙰𝙺𝙴𝙽 {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	if 'success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "funds" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgf)
	elif "card's security" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgc)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>𝙼𝙴𝙳𝙾 𝚅𝙸𝙿 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝙳 ✅
𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 𝙴𝚇𝙿𝙸𝚁𝙴𝚂𝚅➜  {timer}
𝚃𝚈𝙿 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='SOLOM-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝚅𝙸𝙿'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝙽𝙴𝚆 𝙺𝙴𝚈 𝙲𝚁𝙴𝙰𝚃𝙴𝙳 🚀
		
𝙿𝙻𝙰𝙽 ➜ {plan}
𝙴𝚇𝙿𝙸𝚁𝙴𝚂 𝙸𝙽 ➜ {ig}
𝙺𝙴𝚈 ➜ <code>{pas}</code>
		
𝚄𝚂𝙴 /redeem [𝙺𝙴𝚈]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3D Lookup'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝙵𝚁𝙴𝙴",
  "timer": "none",
			}
		}
		BL='𝙵𝚁𝙴𝙴'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝙵𝚁𝙴𝙴':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙷𝙴𝙻𝙻𝙾 {name}
𝚃𝙷𝙸𝚂 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻 𝙰𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙴𝙴 
𝙸𝙵 𝚈𝙾𝚄  𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴 𝙸𝚃, 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰 𝚆𝙴𝙴𝙺𝙸𝙻𝚈 𝙾𝚁 𝙼𝙾𝙽𝚃𝙷𝙻𝚈 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 

𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝙹𝙾𝙱 𝙸𝚂 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝙲𝙰𝚁𝙳𝚂 

𝙱𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽:

𝙴𝙶𝚈𝙿𝚃
1 𝙳𝙰𝚈 ➜ 30 𝙴𝙶
1 𝚆𝙴𝙴𝙺 ➜ 200 𝙴𝙶
1 𝙼𝙾𝙽𝚃𝙷 ➜ 500 𝙴𝙶

𝙸𝚁𝙰𝚀
1 𝙳𝙰𝚈 ➜ 1$ 𝙰𝚂𝙸𝙰
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝙰𝚂𝙸𝙰 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝙰𝚂𝙸𝙰

𝚆𝙾𝚁𝙻𝙳 𝚆𝙸𝙳𝙴 ➜ 𝚄𝚂𝙳𝚃
1 𝙳𝙰𝚈 ➜ 1$ 𝚄𝚂𝙳𝚃
1 𝚆𝙴𝙴𝙺 ➜ 5$ 𝚄𝚂𝙳𝚃 
1 𝙼𝙾𝙽𝚃𝙷 ➜ 18$ 𝚄𝚂𝙳𝚃 

𝙲𝙻𝙸𝙲𝙺 /cmds 𝚃𝙾 𝚅𝙸𝙴𝚆 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 

𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝙽 𝙽𝙾𝚆 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝙾𝚆𝙽𝙴𝚁  ✨", url="https://t.me/Xx_so1om_Xx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝚈𝙾𝚄 𝙲𝙰𝙽𝙽𝙾𝚃 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃 𝙱𝙴𝙲𝙰𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙿𝚃𝙸𝙾𝙽 𝙷𝙰𝚂 𝙴𝚇𝙿𝙸𝚁𝙴𝙳</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝙵𝚁𝙴𝙴'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝚈𝙾𝚄 𝙲𝙰𝚁𝙳𝚂...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		response = requests.post(
		f'https://rimuruchkbot.alwaysdata.net/vbv.php?bin={cc}')
		last=(response.json()['result'])
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝙿𝙰𝚂𝚂𝙴𝙳 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
𝚃𝙰𝙺𝙴𝙽 {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	msgd=f'''<b>𝚁𝙴𝙶𝙴𝙲𝚃𝙴𝙳 ❌
- - - - - - - - - - - - - - - - - - - - - - -
𝙲𝙲 -> <code>{cc}</code>
𝙶𝙰𝚃𝙴𝚆𝙰𝚈 -> {gate}
𝚁𝙴𝚂𝙿𝙾𝙽𝚂𝙴 -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
𝙱𝙸𝙽 -> {cc[:6]}
𝙱𝙸𝙽 𝙸𝙽𝙵𝙾 -> {card_type} - {brand}
𝙱𝙰𝙽𝙺 -> {bank}
𝙲𝙾𝚄𝙽𝚃𝚁𝚈 -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
𝙳𝙴𝚅 : @Xx_so1om_Xx
𝚃𝙰𝙺𝙴𝙽 {"{:.1f}".format(execution_time)} 𝚂𝙴𝙲𝙾𝚄𝙽𝙳𝚂 .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")