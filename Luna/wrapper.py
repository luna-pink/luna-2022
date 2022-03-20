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

def statuscon():
    startup_status = files.json(
        f"Luna/config.json", "startup_status", documents=True
    )
    if startup_status == "dnd":
        statuscon = Status.dnd
    elif startup_status == "idle":
        statuscon = discord.Status.idle
    elif startup_status == "invisible" or startup_status == "offline":
        statuscon = Status.offline
    else:
        statuscon = Status.online
    return statuscon


class Bot(commands.Bot):
    __slots__ = ('ready', 'extensions', 'scheduler')

    def __init__(self, key: str, status="online") -> None:
        """
        It initializes the bot with the given key and status

        :param key: The token for your bot
        :type key: str
        :param status: The status that the bot will appear with, defaults to online (optional)
        """
        self.ready = False
        self.extensions = [p.stem for p in Path(__file__).parent.glob('**/*.py') if p.stem != '__init__']
        self.scheduler = AsyncIOScheduler()
        self.scheduler.configure(timezone=utc)
        self.key = key
        self.stat = status

        # if self.stat == "dnd":
        #     statuscon = discord.Status.dnd
        # elif self.stat == "idle":
        #     statuscon = discord.Status.idle
        # elif self.stat == "invisible" or self.stat == "offline":
        #     statuscon = discord.Status.offline
        # else:
        #     statuscon = discord.Status.online

        super().__init__(
            command_prefix=get_prefix(),
            case_insensitive=True,
            self_bot=True,
            help_command=None
        )

        if not self.key == "Jgy67HUXLH":
            print("Invalid key")
            os._exit(0)

    def run(self, token: str, reconnect=True) -> None:
        """
        Run the bot using the provided token

        :param token: The token for the bot
        :type token: str
        :param reconnect: If True, the bot will automatically reconnect if it is disconnected, defaults to True (optional)
        """
        super().run(token, reconnect=reconnect)

    async def close(self) -> None:
        """
        Wait 2 seconds, then shut down the scheduler
        """
        time.sleep(2)
        self.scheduler.shutdown()
        await super().close()

    async def on_ready(self) -> None:
        """
        This function is called when the bot is ready to receive and send messages
        :return: Nothing.
        """
        if self.ready:
            return

        # startup_status = files.json(
        #     f"Luna/config.json", "startup_status", documents=True
        # )
        #
        # if startup_status == "dnd":
        #     payload = {'status': "dnd"}
        # elif startup_status == "idle":
        #     payload = {'status': "idle"}
        # elif startup_status == "invisible" or startup_status == "offline":
        #     payload = {'status': "invisible"}
        # else:
        #     payload = {'status': "online"}
        #
        # requests.patch(
        #     f'https://discordapp.com/api/{api_version}/users/@me/settings',
        #     json=payload,
        #     headers={
        #         'authorization': user_token,
        #         'user-agent': 'Mozilla/5.0'
        #     }
        # )

        self.scheduler.start()
        self.ready = True

    async def on_message(self, message: discord.Message) -> None:
        """
        It's a coroutine that takes a message as an argument and then processes commands

        :param message: discord.Message - The message that was sent
        :type message: discord.Message
        :return: Nothing.
        """
        if message.author.bot:
            return

        await self.process_commands(message)

    async def process_commands(self, message: discord.Message) -> None:
        """
        It takes a message, checks if it's a command, and if it is, invokes the command

        :param message: The message that was sent by the user
        :type message: discord.Message
        """
        ctx = await self.get_context(message, cls=commands.Context)

        await self.invoke(ctx)
