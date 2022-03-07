from doctest import debug_script
from pathlib import Path
import time

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from pytz import utc

# token = 'mfa.RKXALnKQEhlV9SOfFKbyMbNvDzaRW3sjuunOQijDmbI6WfXB0wRgKOOdEKqzy8hoNXxhUHF-jQdz1Xpj6Zyh'

class Bot(commands.Bot):
    """
    This is the code that will be executed when the bot is started.
    """
    __slots__ = ('ready', 'extensions', 'scheduler')
    
    def __init__(self) -> None:
        self.ready = False
        self.extensions = [p.stem for p in Path(__file__).parent.glob('**/*.py') if p.stem != '__init__']
        self.scheduler = AsyncIOScheduler()
        self.scheduler.configure(timezone=utc)
        
        super().__init__(
            command_prefix='.',
            status=discord.Status.online,
            case_insensitive=True,
            self_bot=True,
            help_command=None
        )
        
    def run(self, token: str, reconnect=True) -> None:
        """
        Tell the bot to start running. Reconnect is enabled by default.
        """
        # print("Running bot...")
        super().run(token, reconnect=reconnect)
        
    async def close(self) -> None:
        # print("Closing bot...")
        time.sleep(2)
        self.scheduler.shutdown()
        await super().close()
        
    # async def on_connect(self) -> None:
    #     print(f"Bot connected! DWSP: {self.ws.latency * 1000:.0f}ms")
        
    # async def on_disconnect(self) -> None:
    #     print("Bot disconnected!")
        
    async def on_ready(self) -> None:
        if self.ready:
            return
        
        self.scheduler.start()
        # print(f"Scheduler started ({len(self.scheduler.get_jobs())} jobs)")
        
        # print(f"Bot is ready! Connected to: {self.user}")
        self.ready = True
        
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot or isinstance(message.channel, discord.DMChannel):
            return
        
        await self.process_commands(message)

    async def process_commands(self, message: discord.Message) -> None:
        ctx = await self.get_context(message, cls=commands.Context)
        
        if ctx.command is None:
            return
        
        await self.invoke(ctx)

# bot = Bot()
        
# class Help(commands.Cog):
#     __slots__ = ()
        
#     @commands.command(name='help', 
#                       help="View the help menu", 
#                       usage="")
#     async def command_help(self, ctx: commands.Context) -> None:
#         await ctx.message.delete()
#         await ctx.send(f"Hi")
        
# bot.add_cog(Help(bot))
    
# if __name__ == '__main__':
#     bot.run()