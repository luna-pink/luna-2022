from discord.ext import commands


class OnReadyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user)
        print(self.bot.user.id)
        print('------')