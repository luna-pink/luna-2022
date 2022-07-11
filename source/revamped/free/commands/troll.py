import asyncio

from discord.ext import commands
from .utilities import *


class TrollCog(commands.Cog, name="Troll commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="ghostping",
        usage="<@member>",
        aliases=['gp'],
        description="Ghostping someone"
    )
    async def ghostping(self, luna):
        try:
            await luna.message.delete()
        except BaseException:
            pass

    @commands.command(
        name="empty",
        usage="",
        description="Sends a empty message"
    )
    async def empty(self, luna):

        await luna.send("​")

    @commands.command(
        name="copy",
        usage="<@member>",
        aliases=['copycat'],
        description="Copy every message a member"
    )
    async def copy(self, luna, member: discord.User):

        global copycat
        copycat = member
        if configs.mode() == 2:
            sent = await luna.send(f"```ini\n[ {theme.title()} ]\n\nNow copying {copycat}\n\n[ {theme.footer()} ]```")
            await asyncio.sleep(configs.delete_timer())
            await sent.delete()
        else:
            embed = discord.Embed(
                title=theme.title(),

                description=f"Now copying {copycat}",

            )

            embed.set_footer(
                text=theme.footer(),

            )

            sent = await send(luna, embed)
            await asyncio.sleep(configs.delete_timer())
            await sent.delete()

    @commands.command(
        name="stopcopy",
        usage="",
        aliases=['stopcopycat'],
        description="Stop copying a member"
    )
    async def stopcopy(self, luna):

        global copycat
        if copycat is None:
            if configs.mode() == 2:
                sent = await luna.send(
                    f"```ini\n[ {theme.title()} ]\n\nNo one was getting copied\n\n[ {theme.footer()} ]```"
                )
                await asyncio.sleep(configs.delete_timer())
                await sent.delete()
            else:
                embed = discord.Embed(
                    title=theme.title(),

                    description=f"No one was getting copied",

                )

                embed.set_footer(
                    text=theme.footer(),

                )

                sent = await send(luna, embed)
                await asyncio.sleep(configs.delete_timer())
                await sent.delete()
            return

        if configs.mode() == 2:
            sent = await luna.send(
                f"```ini\n[ {theme.title()} ]\n\nStopped copying {copycat}\n\n[ {theme.footer()} ]```"
            )
            copycat = None
            await asyncio.sleep(configs.delete_timer())
            await sent.delete()
        else:
            embed = discord.Embed(
                title=theme.title(),

                description=f"Stopped copying {copycat}",

            )

            embed.set_footer(
                text=theme.footer(),

            )

            sent = await send(luna, embed)
            copycat = None
            await asyncio.sleep(configs.delete_timer())
            await sent.delete()

    @commands.command(
        name="fakenitro",
        usage="[amount]",
        description="Generate fake nitro links"
    )
    async def fakenitro(self, luna, amount: int = None):

        try:
            if amount is None:
                await luna.send(Nitro())
            else:
                for each in range(0, amount):
                    await luna.send(Nitro())
        except Exception as e:
            await luna.send(f"Error: {e}")

    @commands.command(
        name="trollnitro",
        usage="",
        description="Send a used nitro link"
    )
    async def trollnitro(self, luna):

        await luna.send("https://discord.gift/6PWNmA6NTuRkejaP")

    @commands.command(
        name="mreact",
        usage="",
        description="Mass reacts on last message"
    )
    async def mreact(self, luna):
        await luna.message.delete()
        messages = await luna.message.channel.history(limit=1).flatten()
        for message in messages:
            await message.add_reaction("😂")
            await message.add_reaction("😡")
            await message.add_reaction("🤯")
            await message.add_reaction("👍")
            await message.add_reaction("👎")
            await message.add_reaction("💯")
            await message.add_reaction("🍑")
            await message.add_reaction("❗")
            await message.add_reaction("🥳")
            await message.add_reaction("👏")
            await message.add_reaction("🔞")
            await message.add_reaction("🇫")
            await message.add_reaction("🥇")
            await message.add_reaction("🤔")
            await message.add_reaction("💀")
            await message.add_reaction("❤️")

    @commands.command(
        name="fakenuke",
        usage="",
        description="Fakenuke"
    )
    async def fakenuke(self, luna):

        message = await luna.send(content=':bomb: :bomb: Nuking this server in 5 :rotating_light:')
        await asyncio.sleep(1)
        await message.edit(content='0')
        await asyncio.sleep(1)
        await message.edit(content='1')
        await asyncio.sleep(1)
        await message.edit(content='2')
        await asyncio.sleep(1)
        await message.edit(content='3')
        await asyncio.sleep(1)
        await message.edit(content='4')
        await asyncio.sleep(1)
        await message.edit(content='This server will be destoyed now')
        await asyncio.sleep(1)
        await message.edit(content=':bomb:')
        await asyncio.sleep(1)
        await message.edit(content=':boom:')
        await asyncio.sleep(1)
        await message.edit(content='Shouldn\'t have even created it ig')
        await asyncio.sleep(1)
        await message.edit(content=':bomb: :bomb:')
        await asyncio.sleep(1)
        await message.edit(content=':boom: :boom:')
        await asyncio.sleep(1)
        await message.edit(content='You will wish you never lived to know about discord')
        await asyncio.sleep(1)
        await message.edit(content=':bomb: :bomb: :bomb:')
        await asyncio.sleep(1)
        await message.edit(content=':boom: :boom: :boom:')
        await asyncio.sleep(1)
        await message.edit(content='There it comes...')
        await asyncio.sleep(1)
        await message.edit(content='https://giphy.com/gifs/rick-roll-lgcUUCXgC8mEo')

    @commands.command(
        name="banroulette",
        usage="",
        description="Ban roulette"
    )
    async def banroulette(self, luna):
        """
        Get a random user from the server and ban them
        """

        user = random.choice(luna.message.guild.members)
        if user == luna.user:
            return
        try:
            await user.ban()
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")
        await message_builder(luna, "Ban Roulette", f"{user} has been banned")
