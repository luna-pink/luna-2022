import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, NotOwner
import time
import main as luna
import asyncio

class OnMember(commands.Cog, name="on member events"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_member_join(self, member):
		if luna.antiraid is True and member.bot:
			try:
				guild = member.guild
				async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
					if member.guild.id in luna.whitelisted_users.keys() and i.user.id in luna.whitelisted_users[
							member.guild.id].keys():
						return
					else:
						await guild.ban(member, reason="Lolicon Anti-Raid")
						await guild.ban(i.user, reason="Lolicon Anti-Raid")
			except Exception as e:
				print(e)

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		if luna.antiraid is True:
			try:
				guild = member.guild
				async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
					if guild.id in luna.whitelisted_users.keys() and i.user.id in luna.whitelisted_users[
							guild.id].keys() and i.user.id is not self.bot.user.id:
						print('not banned')
					else:
						print('banned')
						await guild.ban(i.user, reason="Lolicon Anti-Raid")
			except Exception as e:
				print(e)


def setup(bot):
	bot.add_cog(OnMember(bot))
