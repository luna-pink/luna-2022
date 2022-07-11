import asyncio
import platform
import typing

import aiohttp
import httpx
import psutil
from discord.ext import commands
from discord.ext.commands import has_permissions

from .utilities import *


class UtilsCog(commands.Cog, name="Util commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="pcspecs",
        usage="",
        aliases=['pc', 'specs'],
        description="Show your pc specs"
    )
    async def pcspecs(self, luna):

        uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        cpufreq = psutil.cpu_freq()
        cores = "".join(f"\n{f'Core{str(i)}':17} » {percentage}%" for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)))

        svmem = psutil.virtual_memory()
        partitions = psutil.disk_partitions()
        disk_io = psutil.disk_io_counters()
        partition_info = ""
        for partition in partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            partition_info += f"{'Device':17} » {partition.device}\n" \
                              f"{'Mountpoint':17} » {partition.mountpoint}\n" \
                              f"{'System Type':17} » {partition.fstype}\n" \
                              f"{'Total Size':17} » {get_size(partition_usage.total)}\n" \
                              f"{'Used':17} » {get_size(partition_usage.used)}\n" \
                              f"{'Free':17} » {get_size(partition_usage.free)}\n" \
                              f"{'Percentage':17} » {get_size(partition_usage.percent)}%\n" \
                              f"{'Total Read':17} » {get_size(disk_io.read_bytes)}\n" \
                              f"{'Total Write':17} » {get_size(disk_io.write_bytes)}\n\n"
        net_io = psutil.net_io_counters()
        await message_builder(
            luna, title="PC Specs",
            description=f"```\nGeneral\n\n"
                        f"{'System':17} » {uname.system}\n"
                        f"{'Node':17} » {uname.node}\n"
                        f"{'Release':17} » {uname.release}\n"
                        f"{'Version':17} » {uname.version}\n"
                        f"{'Machine':17} » {uname.machine}\n"
                        f"{'Processor':17} » {uname.processor}\n```"
                        f"```\nCPU Information\n\n"
                        f"{'Physical Cores':17} » {psutil.cpu_count(logical=False)}\n"
                        f"{'Total Cores':17} » {psutil.cpu_count(logical=True)}\n"
                        f"{'Max Frequency':17} » {cpufreq.max:.2f}Mhz\n"
                        f"{'Min Frequency':17} » {cpufreq.min:.2f}Mhz\n"
                        f"{'Current Frequency':17} » {cpufreq.current:.2f}Mhz\n\n"
                        f"Current Usage{cores}\n```"
                        f"```\nMemory Information\n\n"
                        f"{'Total':17} » {get_size(svmem.total)}\n"
                        f"{'Available':17} » {get_size(svmem.available)}\n"
                        f"{'Used':17} » {get_size(svmem.used)}\n"
                        f"{'Percentage':17} » {get_size(svmem.percent)}%\n```"
                        f"```\nDisk Information\n\n"
                        f"{partition_info}\n```"
                        f"```\nNetwork\n\n"
                        f"{'Bytes Sent':17} » {get_size(net_io.bytes_sent)}\n"
                        f"{'Bytes Received':17} » {get_size(net_io.bytes_recv)}\n```"
                        f"```\nBoot Time\n\n"
                        f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n```"
        )

    @commands.command(
        name="addgc",
        usage="<user_id>",
        description="Add a user to a groupchannel"
    )
    async def addgc(self, luna, user_id):

        if isinstance(luna.message.channel, discord.GroupChannel):
            user = await self.bot.fetch_user(user_id)
            await luna.message.channel.add_recipients(user)
        else:
            await error_builder(luna, description="```\nThis command can only be used in a groupchannel\n```")

    @commands.command(
        name="kickgc",
        usage="",
        description="Kick all from a groupchannel"
    )
    async def kickgc(self, luna):

        if isinstance(luna.message.channel, discord.GroupChannel):
            for recipient in luna.message.channel.recipients:
                await luna.message.channel.remove_recipients(recipient)
        else:
            await error_builder(luna, description="```\nThis command can only be used in a groupchannel\n```")

    @commands.command(
        name="leavegc",
        usage="",
        description="Leave a groupchannel"
    )
    async def leavegc(self, luna):

        if isinstance(luna.message.channel, discord.GroupChannel):
            await luna.message.channel.leave()
        else:
            await error_builder(luna, description="```\nThis command can only be used in a groupchannel\n```")

    @commands.command(
        name="serverjoiner",
        aliases=['joinservers', 'jservers',
                 'joinserver', 'joininvites'],
        usage="",
        description="Join all invites in data/invites.txt"
    )
    async def serverjoiner(self, luna):

        if configs.risk_mode() == "on":
            if os.stat(
                    "data/invites.txt"
            ).st_size == 0:
                await message_builder(luna, title="Server Joiner", description=f"```\ninvites.txt is empty...```")
                return
            else:
                with open("data/invites.txt", "r") as file:
                    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
                    line_count = len(nonempty_lines)
                await message_builder(
                    luna, title="Server Joiner",
                    description=f"```\nFound {line_count} invites in invites.txt\nJoining provided invites...```"
                )
                with open("data/invites.txt", "r+") as f:
                    for line in f:
                        invite = line.strip("\n")
                        invite = invite.replace(
                            'https://discord.gg/',
                            ''
                        ).replace(
                            'https://discord.com/invite/',
                            ''
                        ).replace(
                            'Put the invites of the servers you want to join here one after another',
                            ''
                        )
                        try:
                            async with httpx.AsyncClient() as client:
                                await client.post(
                                    f'https://discord.com/api/{api_version}/invites/{invite}',
                                    headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'}
                                )
                                prints.event(f"Joined {invite}")
                                await asyncio.sleep(0.5)
                        except Exception as e:
                            prints.error(f"Failed to join {invite}")
                            prints.error(e)
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="proxyserverjoiner", usage="",
        description="Join all invites in data/invites.txt using proxies"
    )
    async def proxyserverjoiner(self, luna):

        proxies = open(
            "data/raiding/proxies.txt", 'r'
        )
        proxylist = []
        for p, _proxy in enumerate(proxies):
            proxy = _proxy.split('\n')[0]
            proxylist.append(proxy)
        if configs.risk_mode() == "on":
            if os.stat("data/invites.txt").st_size == 0:
                await message_builder(luna, title="Server Joiner", description=f"```\ninvites.txt is empty...```")
                return
            else:
                with open(
                    "data/invites.txt", "r"
                ) as file:
                    nonempty_lines = [line.strip("\n")
                                      for line in file if line != "\n"]
                    line_count = len(nonempty_lines)
                await message_builder(
                    luna, title="Server Joiner",
                    description=f"```\nFound {line_count} invites in invites.txt\nJoining provided invites...```"
                )
                with open("data/invites.txt", "r+") as f:
                    for line in f:
                        invite = line.strip("\n")
                        invite = invite.replace(
                            'https://discord.gg/',
                            ''
                        ).replace(
                            'https://discord.com/invite/',
                            ''
                        ).replace(
                            'Put the invites of the servers you want to join here one after another',
                            ''
                        )
                        try:
                            async with httpx.AsyncClient() as client:
                                await client.post(
                                    f'https://discord.com/api/{api_version}/invites/{invite}',
                                    headers={
                                        'authorization': user_token, 'user-agent': 'Mozilla/5.0'
                                    },
                                    proxies={'http://': f'http://{proxylist[p]}'}
                                )
                                prints.event(f"Joined {invite}")
                                await asyncio.sleep(0.5)
                        except Exception as e:
                            prints.error(f"Failed to join {invite}")
                            prints.error(e)
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="countdown",
        usage="<number>",
        description="Create a countdown"
    )
    async def countdown(self, luna, number: int):

        for count in range(number, 0, -1):
            await luna.send(count)
            await asyncio.sleep(1)

    @commands.command(
        name="countup",
        usage="<number>",
        description="Create a countup"
    )
    async def countup(self, luna, number: int):

        for count in range(number):
            await luna.send(count)
            await asyncio.sleep(1)

    @commands.command(
        name="emojis",
        usage="",
        description="List all emojis"
    )
    async def emojis(self, luna):

        server = luna.message.guild
        emojis = [e.name for e in server.emojis]
        emojis = '\n'.join(emojis)
        await message_builder(luna, title="Emojis", description=f"```\n{emojis}```")

    @commands.command(
        name="addemoji",
        usage="<emoji_name> <image_url>",
        description="Add an emoji"
    )
    @has_permissions(manage_emojis=True)
    async def addemoji(self, luna, emoji_name, image_url=None):

        if luna.message.attachments:
            image = await luna.message.attachments[0].read()
        elif image_url:
            async with aiohttp.ClientSession() as session:
                async with session.get(image_url) as resp:
                    image = await resp.read()
        await luna.guild.create_custom_emoji(name=emoji_name, image=image)
        embed = discord.Embed(
            title="Emoji Added",

            description=f"{emoji_name}"
        )
        embed.set_thumbnail(url=image_url)
        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="editemoji",
        usage="<emoji> <new_name>",
        description="Edit an emoji"
    )
    @has_permissions(manage_emojis=True)
    async def editemoji(self, luna, emoji: discord.Emoji, new_name):

        oldname = emoji.name
        await emoji.edit(name=new_name)
        embed = discord.Embed(
            title="Emoji Edited",

            description=f"{oldname} to {new_name}"
        )
        embed.set_thumbnail(url=emoji.url)
        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="delemoji",
        usage="<emoji>",
        description="Delete an emoji"
    )
    @has_permissions(manage_emojis=True)
    async def delemoji(self, luna, emoji: discord.Emoji):

        name = emoji.name
        emojiurl = emoji.url
        await emoji.delete()
        embed = discord.Embed(
            title="Emoji Deleted",

            description=f"{name}"
        )
        embed.set_thumbnail(url=emojiurl)
        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="stealemoji",
        aliases=['stealemojis'],
        usage="<guild_id>",
        description="Steal all emojis from a guild"
    )
    @has_permissions(manage_emojis=True)
    async def stealemoji(self, luna, guild_id):

        if not os.path.exists('data/emojis'):
            os.makedirs('data/emojis')
        guild_id = int(guild_id)
        try:
            _ = self.bot.get_guild(guild_id)
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")
            return

    @commands.command(
        name='playing',
        usage="<text>",
        description="Change your activity to playing"
    )
    async def playing(self, luna, *, status: str):
        try:
            await self.bot.change_presence(activity=discord.Game(name=status))
            await message_builder(luna, title="Status Changed", description=f"```Status changed to » Playing {status}```")
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name='streaming',
        usage="<text>",
        description="Change your activity to streaming"
    )
    async def streaming(self, luna, *, status: str):
        try:
            await self.bot.change_presence(activity=discord.Streaming(name=status, url=configs.stream_url()))
            await message_builder(luna, title="Status Changed", description=f"```Status changed to » Streaming {status}```")
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name='listening',
        usage="<text>",
        description="Change your activity to listening"
    )
    async def listening(self, luna, *, status: str):
        try:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
            await message_builder(luna, title="Status Changed", description=f"```Status changed to » Listening to {status}```")
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name='watching',
        usage="<text>",
        description="Change your activity to watching"
    )
    async def watching(self, luna, *, status: str = None):
        try:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
            await message_builder(luna, title="Status Changed", description=f"```Status changed to » Watching {status}```")
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name='stopactivity',
        usage="",
        aliases=['stopplaying', 'stopstreaming', 'stoplistening', 'stopwatching'],
        description="Stop your activity"
    )
    async def stopactivity(self, luna):
        try:
            await self.bot.change_presence(activity=None)
            await message_builder(luna, title="Status Changed", description="```Status changed to » Nothing```")
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="clean",
        usage="<amount>",
        description="Clean your messages"
    )
    async def clean(self, luna, amount: int):

        try:
            await luna.channel.purge(limit=amount, before=luna.message, check=is_me)
        except BaseException:
            try:
                await asyncio.sleep(1)
                async for message in luna.message.channel.history(limit=amount):
                    if message.author == self.bot.user:
                        await message.delete()
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
                return

    @commands.command(
        name="textreact",
        aliases=['treact'],
        usage="<amount>",
        description="Text as reaction"
    )
    async def textreact(self, luna, messageNo: typing.Optional[int] = 1, *, text):

        text = iter(text.lower())
        emotes = {
            "a": "🇦",
            "b": "🇧",
            "c": "🇨",
            "d": "🇩",
            "e": "🇪",
            "f": "🇫",
            "g": "🇬",
            "h": "🇭",
            "i": "🇮",
            "j": "🇯",
            "k": "🇰",
            "l": "🇱",
            "m": "🇲",
            "n": "🇳",
            "o": "🇴",
            "p": "🇵",
            "q": "🇶",
            "r": "🇷",
            "s": "🇸",
            "t": "🇹",
            "u": "🇺",
            "v": "🇻",
            "w": "🇼",
            "x": "🇽",
            "y": "🇾",
            "z": "🇿",
        }
        for i, m in enumerate(await luna.channel.history(limit=100).flatten()):
            if messageNo == i:
                for c in text:
                    await m.add_reaction(f"{emotes[c]}")
                break

    @commands.command(
        name="afk",
        usage="<on/off>",
        description="AFK mode on/off"
    )
    async def afk(self, luna, mode: str = None):
        global afk_status
        if mode in {"on", "off"}:
            prints.message(f"AFK Mode » {color.print_gradient(f'{mode}')}")
            afk_status = 1 if mode == "on" else 0
            await message_builder(luna, description=f"```\nAFK Mode » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="invisiblenick",
        usage="",
        description="Make your nickname invisible"
    )
    async def invisiblenick(self, luna):
        try:
            name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
            await luna.message.author.edit(nick=name)
        except Exception as e:
            await luna.send(f"Error: {e}")

    @commands.command(
        name="hypesquad",
        usage="<bravery/brilliance/balance>",
        description="Change Hypesquad house"
    )
    async def hypesquad(self, luna, house: str):
        request = requests.session()
        headers = {
            'Authorization': user_token,
            'Content-Type': 'application/json'
        }

        if house == "bravery":
            payload = {'house_id': 1}
        elif house == "brilliance":
            payload = {'house_id': 2}
        elif house == "balance":
            payload = {'house_id': 3}

        try:
            request.post(
                'https://discord.com/api/{api_version}/hypesquad/online',
                headers=headers, json=payload
            )
            prints.message(f"Successfully set your hypesquad house to {house}")
            embed = discord.Embed(
                title="Hypesquad",

                description=f"```\nSuccessfully set your hypesquad house to {house}```",

            )

            embed.set_footer(
                text=theme.footer(),

            )

            await send(luna, embed)
        except BaseException:
            await error_builder(luna, description=f"```\nFailed to set your hypesquad house```")

    @commands.command(
        name="acceptfriends",
        usage="",
        description="Accept friend requests"
    )
    async def acceptfriends(self, luna):

        for relationship in self.bot.user.relationships:
            if relationship == discord.RelationshipType.incoming_request:
                with contextlib.suppress(Exception):
                    await relationship.accept()
                    prints.message(f"Accepted {relationship}")

    @commands.command(
        name="ignorefriends",
        usage="",
        description="Delete friend requests"
    )
    async def ignorefriends(self, luna):

        for relationship in self.bot.user.relationships:
            if relationship is discord.RelationshipType.incoming_request:
                relationship.delete()
                prints.message(f"Deleted {relationship}")

    @commands.command(
        name="delfriends",
        usage="",
        description="Delete all friends"
    )
    async def delfriends(self, luna):

        for relationship in self.bot.user.relationships:
            if relationship is discord.RelationshipType.friend:
                with contextlib.suppress(Exception):
                    await relationship.delete()
                    prints.message(f"Deleted {relationship}")

    @commands.command(
        name="clearblocked",
        usage="",
        description="Delete blocked friends"
    )
    async def clearblocked(self, luna):

        for relationship in self.bot.user.relationships:
            if relationship is discord.RelationshipType.blocked:
                with contextlib.suppress(Exception):
                    await relationship.delete()
                    prints.message(f"Deleted {relationship}")

    @commands.command(
        name="leaveservers",
        usage="",
        description="Leave all servers"
    )
    async def leaveservers(self, luna):

        with contextlib.suppress(BaseException):
            guilds = requests.get(
                'https://discord.com/api/{api_version}/users/@me/guilds',
                headers={
                    'authorization': user_token,
                    'user-agent': 'Mozilla/5.0'
                }
            ).json()
            for guild in range(len(guilds)):
                guild_id = guilds[guild]['id']
                requests.delete(
                    f'https://discord.com/api/{api_version}/users/@me/guilds/{guild_id}',
                    headers={
                        'authorization': user_token,
                        'user-agent': 'Mozilla/5.0'
                    }
                )
                prints.message(f"Left {guild}")

