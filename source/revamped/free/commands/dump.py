from discord.ext import commands
from .utilities import *


class DumpCog(commands.Cog, name="Dump commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="alldump",
        usage="<channel>",
        description="Dump all from a channel"
    )
    async def alldump(self, luna, channel: discord.TextChannel):

        if not files.file_exist(
                f"data/dumping/all/{channel.guild.name}/{channel.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/all/{channel.guild.name}/{channel.name}",
                documents=False
            )
        try:
            prints.event(
                f"Dumping all from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nEvent\n\nDumping all from {channel.mention} ({channel.guild.name})...```"
            )
            async for message in channel.history(limit=None):
                if message.attachments:
                    for attachment in message.attachments:
                        r = requests.get(attachment.url, stream=True)
                        open(
                            f'data/dumping/all/{channel.guild.name}/{channel.name}/{attachment.filename}', 'wb'
                        ).write(
                            r.content
                        )
            prints.message(
                f"Dumped all from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nInfo\n\nDumped all from {channel.mention} ({channel.guild.name})```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="imgdump",
        usage="<channel>",
        description="Dump images from a channel"
    )
    async def imgdump(self, luna, channel: discord.TextChannel):

        if not files.file_exist(
                f"data/dumping/images/{channel.guild.name}/{channel.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/images/{channel.guild.name}/{channel.name}",
                documents=False
            )
        try:
            prints.event(
                f"Dumping images from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nEvent\n\nDumping images from {channel.mention} ({channel.guild.name})...```"
            )
            async for message in channel.history(limit=None):
                if message.attachments:
                    for attachment in message.attachments:
                        if attachment.url.endswith(".png") or attachment.url.endswith(
                                ".jpg"
                        ) or attachment.url.endswith(".jpeg") or attachment.url.endswith(".gif"):
                            r = requests.get(attachment.url, stream=True)
                            open(
                                f'data/dumping/images/{channel.guild.name}/{channel.name}/{attachment.filename}', 'wb'
                            ).write(
                                r.content
                            )
            prints.message(
                f"Dumped images from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nInfo\n\nDumped images from {channel.mention} ({channel.guild.name})```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="audiodump",
        usage="<channel>",
        description="Dump audio from a channel"
    )
    async def audiodump(self, luna, channel: discord.TextChannel):

        if not files.file_exist(
                f"data/dumping/audio/{channel.guild.name}/{channel.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/audio/{channel.guild.name}/{channel.name}",
                documents=False
            )
        try:
            prints.event(
                f"Dumping audio from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nEvent\n\nDumping audio from {channel.mention} ({channel.guild.name})...```"
            )
            async for message in channel.history(limit=None):
                if message.attachments:
                    for attachment in message.attachments:
                        if attachment.url.endswith(".mp3"):
                            r = requests.get(attachment.url, stream=True)
                            open(
                                f'data/dumping/audio/{channel.guild.name}/{channel.name}/{attachment.filename}', 'wb'
                            ).write(
                                r.content
                            )
            prints.message(
                f"Dumped audio from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nInfo\n\nDumped audio from {channel.mention} ({channel.guild.name})```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="videodump",
        usage="<channel>",
        description="Dump videos from a channel"
    )
    async def videodump(self, luna, channel: discord.TextChannel):

        if not files.file_exist(
                f"data/dumping/videos/{channel.guild.name}/{channel.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/videos/{channel.guild.name}/{channel.name}",
                documents=False
            )
        try:
            prints.event(
                f"Dumping videos from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nEvent\n\nDumping videos from {channel.mention} ({channel.guild.name})...```"
            )
            async for message in channel.history(limit=None):
                if message.attachments:
                    for attachment in message.attachments:
                        if attachment.url.endswith(
                                ".mp4"
                        ) or attachment.url.endswith(".mov"):
                            r = requests.get(attachment.url, stream=True)
                            open(
                                f'data/dumping/videos/{channel.guild.name}/{channel.name}/{attachment.filename}', 'wb'
                            ).write(
                                r.content
                            )
            prints.message(
                f"Dumped videos from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nInfo\n\nDumped videos from {channel.mention} ({channel.guild.name})```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="textdump",
        usage="<channel>",
        description="Dump text from a channel"
    )
    async def textdump(self, luna, channel: discord.TextChannel):

        if not files.file_exist(
                f"data/dumping/text/{channel.guild.name}/{channel.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/text/{channel.guild.name}/{channel.name}",
                documents=False
            )
        try:
            prints.event(
                f"Dumping text from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nEvent\n\nDumping last 1000 messages from {channel.mention} ({channel.guild.name})...```"
            )
            text = ""
            async for message in channel.history(limit=1000):
                text += f"{message.author.name}#{message.author.discriminator}: {message.content}\n"
            open(
                f'data/dumping/text/{channel.guild.name}/{channel.name}/{channel.name}.txt', 'w', encoding='utf-8'
            ).write(text)
            prints.message(
                f"Dumped text from {channel.name} ({channel.guild.name})"
            )
            await message_builder(
                luna, title="Dumping",
                description=f"```\nInfo\n\nDumped last 1000 messages from {channel.mention} ({channel.guild.name})```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="emojidump",
        usage="<guild>",
        description="Dump all emojis from a guild"
    )
    async def emojidump(self, luna, guild: discord.Guild):

        if not files.file_exist(
                f"data/dumping/emojis/{guild.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/emojis/{guild.name}", documents=False
            )
        try:
            prints.event(f"Dumping emojis from {guild.name}")
            await message_builder(
                luna, title="Dumping",
                description=f"```\nEvent\n\nDumping emojis from {guild.name}...```"
            )
            for emoji in guild.emojis:
                url = str(emoji.url)
                name = str(emoji.name)
                r = requests.get(url, stream=True)
                if '.png' in url:
                    open(

                        f'data/dumping/emojis/{guild.name}/{name}.png', 'wb'
                    ).write(
                        r.content
                    )
                elif '.gif' in url:
                    open(
                        f'data/dumping/emojis/{guild.name}/{name}.gif', 'wb'
                    ).write(
                        r.content
                    )
            prints.message(f"Dumped emojis from {guild.name}")
            await message_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped emojis from {guild.name}```")
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="emojidownload",
        usage="<guild> <emoji>",
        description="Download a emoji"
    )
    async def emojidownload(self, luna, guild: discord.Guild, emoji: discord.Emoji):

        if not files.file_exist(
                f"data/dumping/emojis/{guild.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/emojis/{guild.name}", documents=False
            )
        try:
            prints.event(f"Downloading emoji from {guild.name}")
            await message_builder(
                luna, title="Downloading",
                description=f"```\nEvent\n\nDownloading emoji from {guild.name}...```"
            )
            url = str(emoji.url)
            name = str(emoji.name)
            r = requests.get(url, stream=True)
            if '.png' in url:
                open(

                    f'data/emojis/{guild.name}/{name}.png', 'wb'
                ).write(
                    r.content
                )
            elif '.gif' in url:
                open(

                    f'data/emojis/{guild.name}/{name}.gif', 'wb'
                ).write(
                    r.content
                )
            prints.message(f"Downloaded emoji from {guild.name}")
            await message_builder(
                luna, title="Downloading",
                description=f"```\nInfo\n\nDownloaded emoji from {guild.name}```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="avatardump",
        usage="<guild>",
        description="Dump avatars from a guild"
    )
    async def avatardump(self, luna, guild: discord.Guild):

        if not files.file_exist(
                f"data/dumping/avatars/{guild.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/avatars/{guild.name}", documents=False
            )
        try:
            prints.event(f"Dumping avatars from {guild.name}")
            await message_builder(
                luna, title="Dumping",
                description=f"```\nEvent\n\nDumping avatars from {guild.name}...```"
            )
            for member in guild.members:
                url = str(member.avatar_url)
                name = str(member.name)
                r = requests.get(url, stream=True)
                if '.png' in url:
                    open(

                        f'data/dumping/avatars/{guild.name}/{name}.png', 'wb'
                    ).write(
                        r.content
                    )
                elif '.gif' in url:
                    open(

                        f'data/dumping/avatars/{guild.name}/{name}.gif', 'wb'
                    ).write(
                        r.content
                    )
            prints.message(f"Dumped avatars from {guild.name}")
            await message_builder(
                luna, title="Dumping",
                description=f"```\nInfo\n\nDumped avatars from {guild.name}```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="channeldump",
        usage="<guild>",
        description="Dump channels from a guild"
    )
    async def channelnamesdump(self, luna, guild: discord.Guild):

        if not files.file_exist(
                f"data/dumping/channels/{guild.name}",
                documents=False
        ):
            files.create_folder(
                f"data/dumping/channels/{guild.name}", documents=False
            )
        try:
            prints.event(f"Dumping channel names from {guild.name}")
            await message_builder(
                luna, title="Dumping",
                description=f"```\nEvent\n\nDumping channel names from {guild.name}...```"
            )
            for channel in guild.channels:
                name = str(channel.name)
                with open(f'data/dumping/channels/{guild.name}/{name}.txt', 'w') as f:
                    f.write(name)
            prints.message(f"Dumped channel names from {guild.name}")
            await message_builder(
                luna, title="Dumping",
                description=f"```\nInfo\n\nDumped channel names from {guild.name}```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")
