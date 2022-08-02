from discord.ext import commands


class RaidCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join')
    async def join(self, ctx):
        await ctx.send()
