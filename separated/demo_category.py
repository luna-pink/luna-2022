from discord.ext import commands


class democategory(commands.Cog, name="Nettool commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="test")
    async def ping(self, ctx):
        await ctx.send("Pong!")
