import discord
from discord.ext import commands
import time
import main as luna
import os
import requests
import socket


class NettoolCog(commands.Cog, name="Nettool commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "ping",
					usage="",
					description = "Display the latency")
	async def ping(self, ctx):
		await ctx.message.delete()

		if luna.mode() == 2:
			before = time.monotonic()
			sent = await ctx.send(f"```ini\n[ Latency ]\n\nPinging...\n\n[ {luna.footervar()} ]```")
			ping = (time.monotonic() - before) * 100
			await sent.edit(content=f"```ini\n[ Latency ]\n\nAPI Latency\n{int(ping)}ms\n\n[ {luna.footervar()} ]```")
		if luna.mode() == 3:
			before = time.monotonic()
			sent = await ctx.send(f"> **Latency**\n> \n> Pinging...\n> \n> {luna.footervar()}")
			ping = (time.monotonic() - before) * 100
			await sent.edit(content=f"> **Latency**\n> \n> API Latency\n> {int(ping)}ms\n> \n> {luna.footervar()}")
		else:
			embed = discord.Embed(title="Latency", url=luna.titleurlvar(), description=f"Pinging...", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			before = time.monotonic()
			sent = await ctx.send(embed=embed)
			ping = (time.monotonic() - before) * 100
			embed = discord.Embed(title="Latency", url=luna.titleurlvar(), description=f"**API Latency**\n{int(ping)}ms", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await sent.edit(embed=embed)

	@commands.command(name = "ip",
						usage="",
						description = "Display information about given ip")
	async def ip(self, ctx, ip:str):
		await ctx.message.delete()
		if ip is None:
			await ctx.send("Please specify a IP address")
			return
		else:
			try:
				with requests.session() as ses:
					resp = ses.get(f'https://ipinfo.io/{ip}/json')
					if "Wrong ip" in resp.text:
						await ctx.send("Invalid IP address")
						return
					else:
						try:
							j = resp.json()
							embed = discord.Embed(title=f"IP: {ip}", url=luna.titleurlvar(), description=f'**City**\n{j["city"]}\n\n**Region**\n{j["region"]}\n\n**Country**\n{j["country"]}\n\n**Coordinates**\n{j["loc"]}\n\n**Postal**\n{j["postal"]}\n\n**Timezone**\n{j["timezone"]}\n\n**Organization**\n{j["org"]}', color=luna.hexcolorvar())
							embed.set_thumbnail(url=luna.imagevar())
							embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
							embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
							embed.set_image(url=luna.largeimagevar())
							await luna.send(ctx, embed)
						except discord.HTTPException:
							await ctx.send(
								f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
			except Exception as e:
				await ctx.send(f"Error: {e}")				

	@commands.command(name="tcpping", usage="<ip> <port>", description="Checks if the host is online by connecting to the port")
	async def tcpping(self, ctx, ip, port):
		await ctx.message.delete()
		if ip is None:
			await ctx.send("Please specify a IP address")
			return
		if port is None:
			await ctx.send("Please specify a port")
			return
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.3)
		try:
			sock.connect((ip, int(port)))
		except:
			embed = discord.Embed(title="__TCP-Ping__", description=f"**Status:** Offline\n**IP:** {ip}\n**Port:** {port}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="__TCP-Ping__", description=f"**Status:** Online\n**IP:** {ip}\n**Port:** {port}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name="portscan", usage="<ip>", description="Checks for common open ports")
	async def portscan(self, ctx, ip):
		await ctx.message.delete()
		if ip is None:
			await ctx.send("Please specify a IP address")
			return
		ports = ["10","12","13","14","16","17","18","20","21","22","23","25","40","42","45","47","48","50","53","80","81","110","139","389","443","445","996","1433","1521","1723","3066","3072","3306","3389","5900","8080","8181","65530","65535"]
		open_ports = []
		for port in ports:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.2)
			try:
				sock.connect((ip, int(port)))
			except:
				pass
			else:
				sock.close()
				open_ports.append(port)

		embed = discord.Embed(title="Port Scanner", description=f'**IP:** {ip}\n**Ports Checked:** {",".join(ports)}\n**Open Ports:** {",".join(open_ports)}', color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)


	@commands.command(name="resolve", usage="<url>", description="Gets the urls/website's host IP")
	async def resolve(self, ctx, url):
		await ctx.message.delete()
		import socket
		new_url = ""
		if url is None:
			await ctx.send("Please specify a URL")
			return
		if url.startswith("https://"):
			new_url = url.replace("https://", "")
		elif url.contains("http://"):
			new_url = url.replace("http://", "")
		
		try:
			ip = socket.gethostbyname(new_url)
		except:
			await ctx.send("URL is invalid")
			return
		embed = discord.Embed(title="Host Resolver", description=f"**URL:** {url}\n**IP:** {ip}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name="scrapeproxies", usage="", aliases=['proxyscrape', 'scrapeproxy'],description="Scrape for proxies")
	async def scrapeproxies(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title="Scrapeproxies", description=f"Saved all scraped proxies in data/proxies.", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)
		if not os.path.exists('data/proxies'):
			os.makedirs('data/proxies')
		file = open("data/proxies/http.txt", "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open("data/proxies/https.txt", "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open("data/proxies/socks4.txt", "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open("Proxies/socks5.txt", "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")




def setup(bot:commands.Bot):
	bot.add_cog(NettoolCog(bot))