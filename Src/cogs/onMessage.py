from logging import exception
import discord
import sys
import os
import main as luna
import asyncio
import json
import re
import datetime
import requests
import time
import httpx
import playsound
import dhooks

from discord.ext import commands
from datetime import datetime
from win10toast import ToastNotifier 
from colorama import init

import pyPrivnote as pn

init()

toaster = ToastNotifier()

class bcolors:
    RESET = '\033[0m'
    EVENT = '\033[94m'
    INFO = '\033[96m'
    ERROR = '\033[31m'
    SNIPERLOG = '\033[35m'

SelfbotLog = "Selfbot" # 35 Magenta
SniperLog = "Sniper" # 35 Magenta

cooldown = []

def file_exist(file_name):
    return os.path.exists(file_name)

class OnMessage(commands.Cog, name="on message"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	# ///////////////////////////////////////////////////////////////
	# Afk
        
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return
		sniped_start_time = time.time()
		try:
			if luna.nitro_sniper() == "on" and 'https://discord.gift/' in message.content:
				elapsed_snipe = '%.3fs' % (time.time() - sniped_start_time)
				code = re.search("discord.gift/(.*)", message.content).group(1)
				if len(code) >= 16:
					async with httpx.AsyncClient() as client:
						start_time = time.time()
						if luna.nitro_sniper_api() == "v6":
							result = await client.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': luna.token, 'user-agent': 'Mozilla/5.0'})
						elif luna.nitro_sniper_api() == "v7":
							result = await client.post(f'https://discordapp.com/api/v7/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': luna.token, 'user-agent': 'Mozilla/5.0'})
						elif luna.nitro_sniper_api() == "v8":
							result = await client.post(f'https://discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': luna.token, 'user-agent': 'Mozilla/5.0'})
						elif luna.nitro_sniper_api() == "v9":
							result = await client.post(f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': luna.token, 'user-agent': 'Mozilla/5.0'})
						else:
							result = await client.post(f'https://canary.discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': luna.token, 'user-agent': 'Mozilla/5.0'})
						elapsed = '%.3fs' % (time.time() - start_time)
					status = 'Ratelimit'
					ping = False
					redeemedping = False
					if 'This gift has been redeemed already' in str(result.content):
						status = 'Nitro already redeemed'
						ping = False
					elif 'nitro' in str(result.content):
						status = 'Nitro successfully redeemed'
						redeemedping = True
					elif 'Unknown Gift Code' in str(result.content):
						status = 'Unknown gift code'
						ping = False

					datetime.now(tz=None)
					dateTimeObj = datetime.now()
					timestampStr = dateTimeObj.strftime("%H:%M")

					print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Author  | {message.author}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Code    | {code}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Status  | {status}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Elapsed Times"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Sniped  | {elapsed_snipe}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | API     | {elapsed}"
						"\n")

					if luna.nitrotoast() == "on" and luna.alltoasts() == "on" and redeemedping and sys.platform == "win32":
						try:
							toaster.show_toast(luna.toasttitle(), f"Successfully redeemed a Nitro code!\nServer: {message.guild}\nChannel: {message.channel}\nAuthor: {message.author}", icon_path="data/resources/luna.ico", duration=5, threaded=True)
						except Exception:
							pass
		except Exception as e:
			luna.printerror(e)


		if file_exist('./data/giveawayjoiner.json'):
			pass
		else:
			data = {
                "giveawayjoiner": "on",
                "delay_in_minutes": "1",
                "giveaway_blocked_words": ["ban", "kick", "selfbot", "self bot", "test", "check"],
                "giveaway_server_joiner": "on"
            }
			with open("data/giveawayjoiner.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		with open("data/giveawayjoiner.json", "r") as f:
			data = json.load(f)
		giveawayjoiner = data.get('giveawayjoiner')
		delay_in_minutes = int(data.get('delay_in_minutes'))
		giveaway_blocked_words = data.get('giveaway_blocked_words')
		giveaway_server_joiner = data.get('giveaway_server_joiner')
		if giveawayjoiner == "on" and message.author.bot:
			elapsed_snipe = '%.3fs' % (time.time() - sniped_start_time)
			custom_giveaway_bot_ids = []
			custom_giveaway_bot_reactions = []
			try:
				if os.path.exists('data/giveawaybots.json'):
					with open("data/giveawaybots.json", "r", encoding="utf-8") as jsonFile:
						data = json.load(jsonFile)
                            
					for key, value in data.items():
						try:
							custom_giveaway_bot_ids.append(int(key))
							custom_giveaway_bot_reactions.append(str(value))
						except Exception:
							pass
			except Exception:
				pass

			if ((("giveaway" in str(message.content).lower()) and (int(message.author.id) in custom_giveaway_bot_ids) and ("cancelled" not in str(message.content).lower()) and ("mention" not in str(message.content).lower()) and ("specify" not in str(message.content).lower()) and ("congratulations" not in str(message.content).lower()))):
				found_something_blacklisted = 0
				for blocked_word in giveaway_blocked_words:
					if str(blocked_word).lower() in str(message.content).lower():
						datetime.now(tz=None)
						dateTimeObj = datetime.now()
						timestampStr = dateTimeObj.strftime("%H:%M")
						print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Skipped giveaway"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Reason  | Backlisted word: {blocked_word}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
							"\n")
						found_something_blacklisted = 1

				try:
					for embed in message.embeds:
						embed_dict = embed.to_dict()
						for blocked_word in giveaway_blocked_words:
							try:
								found = re.findall(blocked_word, str(embed_dict).lower())[0]
								if found:
									datetime.now(tz=None)
									dateTimeObj = datetime.now()
									timestampStr = dateTimeObj.strftime("%H:%M")
									print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Skipped giveaway"
										f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Reason  | Backlisted word: {blocked_word}"
										f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
										f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
										"\n")
									found_something_blacklisted = 1
									break
							except:
								pass
                                        
							if found_something_blacklisted > 0:
								break
				except:
					pass
						
				if found_something_blacklisted == 0:
					try:
						embeds = message.embeds
						joined_server = 'None'
						giveaway_prize = None
						try:
							for embed in embeds:
								giveaway_prize = embed.to_dict()['author']['name']
						except Exception:
							for embed in embeds:
								giveaway_prize = embed.to_dict()['title']
						if giveaway_server_joiner == "on":
							try:
								for embed in embeds:
									embed_dict = embed.to_dict()
									code = re.findall(r"\w[a-z]*\W*\w[a-z]+\.\w[g]*\W\S*", str(embed_dict['description']))[0].replace(")", "").replace("https://discord.gg/", "")
									async with httpx.AsyncClient() as client:
										await client.post(f'https://canary.discord.com/api/v8/invites/{code}', headers={'authorization': luna.token, 'user-agent': 'Mozilla/5.0'})
										joined_server = f'discord.gg/{code}'
										await asyncio.sleep(5)
							except Exception:
								pass
						else:
							pass
						datetime.now(tz=None)
						dateTimeObj = datetime.now()
						timestampStr = dateTimeObj.strftime("%H:%M")
						print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Giveaway found"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Prize   | {giveaway_prize}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Joining | In {delay_in_minutes} minute/s!"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Invite  | Joined discord: {joined_server}"
							"\n")
					except Exception as e:
						print(e)
						return
							
					await asyncio.sleep(delay_in_minutes * 60)

					try:
						if int(message.author.id) in custom_giveaway_bot_ids:
							index = custom_giveaway_bot_ids.index(int(message.author.id))
							try:
								await message.add_reaction(custom_giveaway_bot_reactions[index])
							except Exception as e:
								luna.printerror(e)
								return
							datetime.now(tz=None)
							dateTimeObj = datetime.now()
							timestampStr = dateTimeObj.strftime("%H:%M")
							print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Joined giveaway"
								f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
								f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
								f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Prize   | {giveaway_prize}"
								"\n")
					except Exception:
						pass
		#///////////////////////////////////////////////////////////////
		# Copy Member

		if luna.copycat is not None and luna.copycat.id == message.author.id:
			await message.channel.send(chr(173) + message.content)

		# ///////////////////////////////////////////////////////////////
		# Share command
		with open('./config.json') as f:
			config = json.load(f)
		prefix = config.get('prefix')
		with open('data/sharing.json') as f:
			slot = json.load(f)
		share = slot.get('share')
		user_id = slot.get('user_id')

		if share == "on":
			if message.author.id == user_id:
				if f"{prefix}help" in message.content:
					luna.printsharedcommand("help")
					if luna.mode() == 2:
						sent = await message.channel.send(f"```ini\n[ {luna.titlevar()} ]\n\n{luna.descriptionvar()}[ {prefix}help ] » Show all shared commands\n\n[ {luna.footervar()} ]```")
						await asyncio.sleep(luna.deletetimer())
						await sent.delete()
					else:
						embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"{luna.descriptionvar()}**{prefix}help** » Show all shared commands", color=luna.hexcolorvar())
						embed.set_thumbnail(url=luna.imagevar())
						embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
						embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
						embed.set_image(url=luna.largeimagevar())
						sent = await message.channel.send(embed=embed)
						await asyncio.sleep(luna.deletetimer())
						await sent.delete()
			else:
				pass

		# ///////////////////////////////////////////////////////////////
		# AFK System

		if luna.afk_stat == 1:

			with open("config.json", "r") as f:
				config = json.load(f)
				afkmessage = config.get('afkmessage')
				if afkmessage == "":
					afkmessage = "This is an autoresponse message! User is now AFK.."
			if message.guild is None and not isinstance(message.channel, discord.GroupChannel):
				if message.author == self.bot.user:
					return
					
				if luna.mode() == 2:
					sent = await message.channel.send(f"```ini\n[ I am AFK ]\n\n{afkmessage}\n\n[ {luna.footervar()} ]```")
				else:
					embed = discord.Embed(title="I am AFK", url=luna.titleurlvar(), description=f"{afkmessage}", color=luna.hexcolorvar())
					embed.set_thumbnail(url=luna.imagevar())
					embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
					embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
					embed.set_image(url=luna.largeimagevar())
					sent = await message.channel.send(embed=embed)

				if luna.afk_stat == 0:
					luna.afk_stat = 1
					await asyncio.sleep(30)
					luna.afk_stat = 0
				elif luna.afk_stat == 1:
					luna.afk_stat = 0
					await asyncio.sleep(30)
					luna.afk_stat = 1
				await sent.delete()

		# ///////////////////////////////////////////////////////////////
		# Mention

		mention = f'<@!{self.bot.user.id}>'
		if mention in message.content:
			if message.author == self.bot.user:
				return
			else:
				print("")
				luna.printsniper("You have been mentioned.")
				luna.printsniper(f"Server  | {message.guild}")
				luna.printsniper(f"Channel | {message.channel}")
				luna.printsniper(f"Author  | {message.author}")
				print("")
			
			#///////////////////////////////////////////////////////////////
			# Selfbot Detection - Embed

		if message.author.bot == False:
			if message.author == self.bot.user:
				pass
			else:
				embeds = message.embeds
				for embed in embeds:
					global cooldown
					if embed is not None and cooldown.count(message.author.id) == 0 and not ("https://" or "http://" or "cdn.discordapp.com" or ".png" or ".gif" or "www.") in message.content:
						cooldown.append(message.author.id)
						try:
							if luna.selfbottoast() == "on" and luna.alltoasts() == "on":
								toaster.show_toast(luna.toasttitle(), f"Selfbot Detected.\nServer:  {message.guild}\nChannel: {message.channel}\nAuthor:  {message.author}", icon_path="data/resources/luna.ico", duration=5, threaded=True)
						except Exception:
							pass
						datetime.now(tz=None)
						dateTimeObj = datetime.now()
						timestampStr = dateTimeObj.strftime("%H:%M")
						print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SelfbotLog}{bcolors.RESET} | Selfbot Detected."
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SelfbotLog}{bcolors.RESET} | Server  | {message.guild}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SelfbotLog}{bcolors.RESET} | Channel | {message.channel}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SelfbotLog}{bcolors.RESET} | Author  | {message.author}"
							"\n")
						await asyncio.sleep(120)
						cooldown.remove(message.author.id)
					else:
						pass

			# Selfbot Detection - Code block

	

	# 		# ///////////////////////////////////////////////////////////////
	# 		# Snipers

	# 		with open('./config.json') as f:
	# 			config = json.load(f)
	# 		token = config.get('token')
	# 		startup_status = config.get('startup_status')

	# 		headers1 = {
	# 			'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
	# 			'Content-Type': 'application/json',
	# 			'Authorization': token,
	# 		}

	# 		if startup_status == "dnd":
	# 			statusbot = "dnd"
	# 		elif startup_status == "idle":
	# 			statusbot = "idle"
	# 		else:
	# 			statusbot = "online"

	# 		request = requests.Session()

	# 		def GiveawayData():
	# 			print("")
	# 			main.printsniper(f"Server  | {message.guild}")
	# 			main.printsniper(f"Channel | {message.channel}")
	# 			print("")

	# 		def SlotBotData(status):
	# 			print("")
	# 			main.printsniper(f"Server  | {message.guild}")
	# 			main.printsniper(f"Channel | {message.channel}")
	# 			main.printsniper(f"Status  | {status}")
	# 			print("")

	# 		def NitroData(elapsed, code, status):
	# 			print("")
	# 			main.printsniper(f"Server  | {message.guild}")
	# 			main.printsniper(f"Channel | {message.channel}")
	# 			main.printsniper(f"Author  | {message.author}")
	# 			main.printsniper(f"Code    | {code}")
	# 			main.printsniper(f"Status  | {status}")
	# 			main.printsniper("Elapsed Times")
	# 			main.printsniper(f"Sniped  | {elapsed}ms")
	# 			print("")
	# 			setting1 = {
	# 				'status': f"{statusbot}",
	# 				"custom_status": {"text": "Charge [⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀]"}
	# 			}
	# 			request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers1, json=setting1, timeout=10)
	# 			time.sleep(1)
	# 			setting1 = {
	# 				'status': f"{statusbot}",
	# 				"custom_status": {"text": "Charge [##⠀⠀⠀⠀⠀⠀⠀⠀]"}
	# 			}
	# 			request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers1, json=setting1, timeout=10)
	# 			time.sleep(1)
	# 			setting1 = {
	# 				'status': f"{statusbot}",
	# 				"custom_status": {"text": "Charge [####⠀⠀⠀⠀⠀⠀]"}
	# 			}
	# 			request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers1, json=setting1, timeout=10)
	# 			time.sleep(1)
	# 			setting1 = {
	# 				'status': f"{statusbot}",
	# 				"custom_status": {"text": "Charge [######⠀⠀⠀⠀]"}
	# 			}
	# 			request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers1, json=setting1, timeout=10)
	# 			time.sleep(1)
	# 			setting1 = {
	# 				'status': f"{statusbot}",
	# 				"custom_status": {"text": "Charge [########⠀⠀]"}
	# 			}
	# 			request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers1, json=setting1, timeout=10)
	# 			time.sleep(1)
	# 			setting1 = {
	# 				'status': f"{statusbot}",
	# 				"custom_status": {"text": "Charge [##########]"}
	# 			}
	# 			request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers1, json=setting1, timeout=10)

	# 		def PrivnoteData(code, elapsed, status, link):
	# 			print("")
	# 			main.printsniper(f"Server  | {message.guild}")
	# 			main.printsniper(f"Channel | {message.channel}")
	# 			main.printsniper(f"Author  | {message.author}")
	# 			main.printsniper(f"Link    | {link}")
	# 			main.printsniper(f"Status  | {status}")
	# 			main.printsniper(f"Content | Saved in data/themes/{code}.txt")
	# 			main.printsniper("Elapsed Times")
	# 			main.printsniper(f"Sniped  | {elapsed}ms")
	# 			print("")

	# 		if 'https://discord.gift/' in message.content:
	# 			with open("data/nitro.json") as f:
	# 				nitrosn = json.load(f)
	# 			nitro_sniper = nitrosn.get('nitrosniper')
	# 			if nitro_sniper == "on":
	# 				if message.author == self.bot.user:
	# 					pass
	# 				else:
	# 					start = datetime.now()
	# 					code = re.search("discord.gift/(.*)", message.content).group(1)
	# 					token = config.get('token')

	# 					headers = {'Authorization': token}

	# 					r = requests.post(
	# 						f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
	# 						headers=headers,
	# 					).text

	# 					if 'This gift has been redeemed already.' in r:
	# 						elapsed = datetime.now() - start
	# 						elapsed = f'{elapsed.microseconds}'
	# 						elapsed = elapsed[:-3]
	# 						status = "Nitro already redeemed"
	# 						NitroData(elapsed, code, status)

	# 					elif 'subscription_plan' in r:
	# 						elapsed = datetime.now() - start
	# 						elapsed = f'{elapsed.microseconds}'
	# 						elapsed = elapsed[:-3]
	# 						status = "Nitro successfully redeemed"
	# 						NitroData(elapsed, code, status)

	# 					elif 'Unknown Gift Code' in r:
	# 						elapsed = datetime.now() - start
	# 						elapsed = f'{elapsed.microseconds}'
	# 						elapsed = elapsed[:-3]
	# 						status = "Unknown gift code"
	# 						NitroData(elapsed, code, status)

	# 			else:
	# 				return

	# 		if 'Someone just dropped' in message.content:
	# 			with open("data/slotbot.json") as f:
	# 				slot = json.load(f)
	# 			slotbot_sniper = slot.get('slotbotsniper')
	# 			if slotbot_sniper == "on":
	# 				if message.author.id == 346353957029019648:
	# 					try:
	# 						await message.channel.send('~grab')
	# 					except discord.errors.Forbidden:
	# 						status = "SlotBot couldnt grab"
	# 						SlotBotData(status)
	# 					status = "Slotbot grabbed"
	# 					SlotBotData(status)
	# 				else:
	# 					return

	# 		if 'GIVEAWAY' in message.content:
	# 			with open("data/giveawayjoiner.json") as f:
	# 				slot = json.load(f)
	# 			giveaway_sniper = slot.get('giveawayjoiner')
	# 			delay_in_minutes = int(slot.get('delay_in_minutes'))
	# 			if giveaway_sniper == "on":
	# 				if message.author.id == 294882584201003009:
	# 					try:
	# 						main.printsniper(f"Giveaway found, reacting in {delay_in_minutes} minute/s")
	# 						GiveawayData()
	# 						delay_in_minutes_calc = delay_in_minutes * 60
	# 						await asyncio.sleep(delay_in_minutes_calc)
	# 						await message.add_reaction("🎉")
	# 					except discord.errors.Forbidden:
	# 						main.printsniper("Couldnt react on giveaway")
	# 						GiveawayData()
	# 					GiveawayData()
	# 					main.printsniper("Giveaway Sniped")
	# 			else:
	# 				return

	# 		if f'Congratulations <@{self.bot.user.id}>' in message.content:
	# 			with open("data/giveawayjoiner.json") as f:
	# 				slot = json.load(f)
	# 			giveaway_sniper = slot.get('giveawayjoiner')
	# 			if giveaway_sniper == "on":
	# 				if message.author.id == 294882584201003009:
	# 					main.printsniper("Giveaway Won")
	# 					GiveawayData()
	# 			else:
	# 				return

	# 		if 'privnote.com' in message.content:
	# 			with open("data/privnote.json") as f:
	# 				slot = json.load(f)
	# 			privnote_sniper = slot.get('privnotesniper')
	# 			if privnote_sniper == "on":
	# 				start = datetime.now()
	# 				code = re.search('privnote.com/(.*)', message.content).group(1)
	# 				link = 'https://privnote.com/' + code
	# 				try:
	# 					note_text = pn.read_note(link)
	# 					elapsed = datetime.now() - start
	# 					elapsed = f'{elapsed.microseconds}'
	# 					elapsed = elapsed[:-3]
	# 				except Exception:
	# 					status = "Privnote already sniped"
	# 					PrivnoteData(code, elapsed, status, link)
	# 				with open(f'data/privnote/{code}.txt', 'a+') as f:
	# 					status = "Privnote sniped"
	# 					PrivnoteData(code, elapsed, status, link)
	# 					f.write(note_text)
	# 			else:
	# 				return
			
	# 		else:
	# 			return


def setup(bot):
	bot.add_cog(OnMessage(bot))
