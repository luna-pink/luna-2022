from discord.ext import commands
from .utilities import *


class BackupsCog(commands.Cog, name="Backup commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="backupserver",
        usage="[guild_id]",
        aliases=["cloneserver"],
        description="Backup the server"
    )
    async def backupserver(self, luna, guild_id: int = None):

        if guild_id is None:
            guild = luna.guild
        else:
            guild = self.bot.get_guild(guild_id)
        server_name = guild.name.encode("utf-8").decode("utf-8")
        new_guild = await self.bot.create_guild(server_name)
        await message_builder(luna, description=f"```\nCloning {guild.name}```")
        prints.message(f"Created new guild")
        new_guild_default_channels = await new_guild.fetch_channels()
        for channel in new_guild_default_channels:
            await channel.delete()

        for channel in guild.channels:
            if str(channel.type).lower() == "category":
                try:
                    channel.name = channel.name.encode("utf-8").decode("utf-8")
                    await new_guild.create_category(
                        channel.name, overwrites=channel.overwrites,
                        position=channel.position
                    )
                    prints.message(f"Created new category » {channel.name}")
                except Exception as e:
                    prints.error(e)
                    pass

        for channel in guild.voice_channels:
            try:
                cat = ""
                for category in new_guild.categories:
                    if channel.category.name == category.name:
                        cat = category
                channel.name = channel.name.encode("utf-8").decode("utf-8")
                await new_guild.create_voice_channel(
                    channel.name, category=cat, overwrites=channel.overwrites,
                    nsfw=channel.nsfw, position=channel.position
                )
                prints.message(f"Created new voice channel » {channel.name}")
            except Exception as e:
                prints.error(e)
                pass

        for channel in guild.stage_channels:
            try:
                cat = ""
                for category in new_guild.categories:
                    if channel.category.name == category.name:
                        cat = category
                channel.name = channel.name.encode("utf-8").decode("utf-8")
                await new_guild.create_stage_channel(
                    channel.name, category=cat, overwrites=channel.overwrites,
                    topic=channel.topic, slowmode_delay=channel.slowmode_delay,
                    nsfw=channel.nsfw, position=channel.position
                )
                prints.message(f"Created new stage channel » {channel.name}")
            except Exception as e:
                prints.error(e)
                pass

        for channel in guild.text_channels:
            try:
                cat = ""
                for category in new_guild.categories:
                    if channel.category.name == category.name:
                        cat = category
                channel.name = channel.name.encode("utf-8").decode("utf-8")
                await new_guild.create_text_channel(
                    channel.name, category=cat, overwrites=channel.overwrites,
                    topic=channel.topic, slowmode_delay=channel.slowmode_delay,
                    nsfw=channel.nsfw, position=channel.position
                )
                prints.message(f"Created new text channel » {channel.name}")
            except Exception as e:
                prints.error(e)
                pass

        for role in guild.roles[::-1]:
            if role.name != "@everyone":
                try:
                    role.name = role.name.encode("utf-8").decode("utf-8")
                    await new_guild.create_role(
                        name=role.name, color=role.color, permissions=role.permissions,
                        hoist=role.hoist, mentionable=role.mentionable
                    )
                    prints.message(f"Created new role » {role.name}")
                except Exception as e:
                    prints.error(e)
                    pass

        await message_builder(luna, description=f"```\nCloned {luna.guild.name}```")

    @commands.command(
        name="friendsbackup",
        usage="",
        description="Backup your friendslist"
    )
    async def friendsbackup(self, luna):

        prints.event("Backing up friendslist...")
        friendsamount = 0
        blockedamount = 0
        friendslist = ""
        blockedlist = ""
        for friend in self.bot.user.friends:
            friendslist += f"{friend.name}#{friend.discriminator}\n"
            friendsamount += 1
        file = open(
            "data/backup/friends.txt", "w", encoding='utf-8'
        )
        file.write(friendslist)
        file.close()
        for block in self.bot.user.blocked:
            blockedlist += f"{block.name}#{block.discriminator}\n"
            blockedamount += 1
        file = open(
            "data/backup/blocked.txt", "w", encoding='utf-8'
        )
        file.write(blockedlist)
        file.close()
        prints.message(
            f"Friendslist backed up. Friends » {friendsamount} Blocked » {blockedamount}"
        )
        await message_builder(
            luna,
            description=f"```\nBacked up {friendsamount} friends in Documents/data/backup/friends.txt\nBacked up {blockedamount} blocked users in Documents/data/backup/blocked.txt```"
        )