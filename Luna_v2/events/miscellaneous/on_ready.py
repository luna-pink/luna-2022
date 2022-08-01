from discord.ext import commands
from luna import log
import dearpygui.dearpygui as dpg


class OnReadyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log('info', f'Logged in as\n{self.bot.user}\n{self.bot.user.id}')
        dpg.set_value('status', f"Logged in as {self.bot.user}")
