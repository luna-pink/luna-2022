from discord.ext import commands


class PingCog(commands.Cog, name="Nettool commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", aliases=["pong"])
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(PingCog(bot))
    print("Ping command loaded.")
