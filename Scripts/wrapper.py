from pathlib import Path
import time

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from pytz import utc

from Functions.files import *


def get_prefix():
    prefix = files.json("Luna/config.json", "prefix", documents=True)
    return prefix


class Bot(commands.Bot):
    __slots__ = ('ready', 'extensions', 'scheduler')

    def __init__(self, key: str) -> None:
        """_summary_

        Args:
            key (str): _description_
        """
        self.ready = False
        self.extensions = [p.stem for p in Path(__file__).parent.glob('**/*.py') if p.stem != '__init__']
        self.scheduler = AsyncIOScheduler()
        self.scheduler.configure(timezone=utc)
        self.key = key

        super().__init__(
            command_prefix=get_prefix(),
            status=discord.Status.online,
            case_insensitive=True,
            self_bot=True,
            help_command=None
        )

        if not self.key == "Jgy67HUXLH":
            print("Invalid key")
            os._exit(0)

    def run(self, token: str, reconnect=True) -> None:
        """_summary_

        Args:
            token (str): _description_
            reconnect (bool, optional): _description_. Defaults to True.
        """
        super().run(token, reconnect=reconnect)

    async def close(self) -> None:
        time.sleep(2)
        self.scheduler.shutdown()
        await super().close()

    async def on_ready(self) -> None:
        if self.ready:
            return

        self.scheduler.start()
        self.ready = True

    async def on_message(self, message: discord.Message) -> None:
        """_summary_

        Args:
            message (discord.Message): _description_
        """
        if message.author.bot:
            return

        await self.process_commands(message)

    async def process_commands(self, message: discord.Message) -> None:
        """_summary_

        Args:
            message (discord.Message): _description_
        """
        ctx = await self.get_context(message, cls=commands.Context)

        await self.invoke(ctx)
