from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"logged in: {self.bot.user}")
        for command in self.bot.commands:
            print(f"{command}")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

def setup(bot):
    bot.add_cog(help(bot))