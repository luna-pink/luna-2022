from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', aliases=['commands'])
    async def help(self, ctx):
        await ctx.send(
            '```\n'
            'Luna Help\n'
            '\n'
            'help - Shows this message\n'
            'ping - Pong!\n'
            '```'
            )
