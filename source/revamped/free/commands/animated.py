import asyncio

import itertools
from discord.ext import commands

from .utilities import *


class AnimatedCog(commands.Cog, name="Animated commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="animguild",
        usage="[name]",
        description="Animates the guild name"
    )
    async def animguild(self, luna, *, name: str = None):

        global cyclename
        global start_animation
        if name is not None and len(name) <= 3 and configs.error_log() == "console":
            prints.error(
                "Invalid name length, needs to be over 3 characters long"
            )
        elif name is not None and len(name) <= 3 and configs.error_log() != "console":
            await error_builder(
                luna,
                description=f"```\nInvalid name length, needs to be over 3 characters long```"
            )

        else:
            embed = discord.Embed(
                title="Animguild",
                description=f"```\nAnimating: {name}```",

            )

            embed.set_footer(
                text=theme.footer(),

            )

            await send(luna, embed)
            name = luna.guild.name.lower()
            cyclename = name
            length = len(name)
            start_animation = True
            while start_animation:
                for x in range(length):
                    time.sleep(0.5)
                    letter = cyclename[x]
                    first_part = cyclename[:x]
                    second_part = cyclename[x + 1:]
                    new_data = first_part + second_part
                    if letter == letter.upper():
                        await luna.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
                    else:
                        await luna.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])

    @commands.command(
        name="stopanimguild",
        usage="",
        description="Stops the guild animation"
    )
    async def stopanimguild(self, luna):

        global start_animation
        start_animation = False
        embed = discord.Embed(
            title="Animguild",
            description="```\nStopped the animation```"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="cyclenick",
        usage="<name>",
        description="Animates the nickname"
    )
    async def cyclenick(self, luna, *, text):

        embed = discord.Embed(
            title="Cyclenick",
            description=f"```\nAnimating: {text}```"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)
        global cycling
        cycling = True
        while cycling:
            name = ""
            for letter in text:
                name = name + letter
                await luna.message.author.edit(nick=name)

    @commands.command(
        name="stopcyclenick",
        usage="",
        description="Stops the nickname animation"
    )
    async def stopcyclenick(self, luna):

        global cycling
        cycling = False
        embed = discord.Embed(
            title="Cyclenick",
            description="```\nStopped the animation```"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="cyclegroup",
        usage="<name>",
        description="Animates the group name"
    )
    async def cyclegroup(self, luna, *, text):

        embed = discord.Embed(
            title="Cyclegroup",
            description=f"```\nAnimating: {text}```"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)
        global cycling_group
        cycling_group = True
        while cycling:
            name = ""
            for letter in text:
                name = name + letter
                await luna.message.channel.edit(name=name)

    @commands.command(
        name="stopcyclegroup",
        usage="",
        description="Stops the group animation"
    )
    async def stopcyclegroup(self, luna):

        global cycling_group
        cycling_group = False
        embed = discord.Embed(
            title="Cyclegroup",
            description="```\nStopped the animation```"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="virus",
        usage="[@member] <virus>",
        description="Animated virus message"
    )
    async def virus(self, luna, user: discord.Member = None, *, virus: str = "trojan"):
        user = user or luna.author
        start = await luna.send(f"{luna.author.mention} has started to spread {virus}")
        animation_list = (
            f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected {virus}-virus.exe into {user.name}``",
        )
        for i in animation_list:
            await asyncio.sleep(1.5)
            await start.edit(content=i)

    @commands.command(
        name="cathi",
        usage="[text]",
        description="Cute cat animation"
    )
    async def cathi(self, luna, *, text: str = "Hi..."):
        start = await luna.send("A package arrived!")
        animation_list = (
            """ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""",
            f"""ຸ 　　　{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""",
        )
        for _, cat in itertools.product(range(3), animation_list):
            await asyncio.sleep(2)
            await start.edit(content=cat)

    @commands.command(
        name="flop",
        usage="",
        description="Flop animation"
    )
    async def flop(self, luna):
        start = await luna.send(f"{luna.author.mention} has started to flop")
        animation_list = (
            "(   ° - °) (' - '   )",
            "(\\\\° - °)\\ (' - '   )",
            "(—°□°)— (' - '   )",
            "(╯°□°)╯(' - '   )",
            "(╯°□°)╯︵(\\\\ .o.)\\",
        )
        for i in animation_list:
            await asyncio.sleep(2)
            await start.edit(content=i)

    @commands.command(
        name="poof",
        usage="",
        description="Poof animation"
    )
    async def poof(self, luna):
        start = await luna.send(f"{luna.author.mention} has started to poof")
        animation_list = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
        for i in animation_list:
            await asyncio.sleep(2)
            await start.edit(content=i)

    @commands.command(
        name="boom",
        usage="",
        description="Boom animation"
    )
    async def boom(self, luna):
        start = await luna.send(f"{luna.author.mention} has started to boom")
        animation_list = (
            "```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
            "💣",
            "💥",
        )
        for i in animation_list:
            await asyncio.sleep(2)
            await start.edit(content=i)

    @commands.command(
        name="tableflip",
        usage="",
        description="Tableflip animation"
    )
    async def tableflip(self, luna):
        start = await luna.send(f"{luna.author.mention} is flipping the table")
        animation_list = (
            "`(\\°-°)\\  ┬─┬`",
            "`(\\°□°)\\  ┬─┬`",
            "`(-°□°)-  ┬─┬`",
            "`(╯°□°)╯    ]`",
            "`(╯°□°)╯     ┻━┻`",
            "`(╯°□°)╯       [`",
            "`(╯°□°)╯          ┬─┬`",
            "`(╯°□°)╯                 ]`",
            "`(╯°□°)╯                  ┻━┻`",
            "`(╯°□°)╯                         [`",
            "`(\\°-°)\\                               ┬─┬`",
        )
        for i in animation_list:
            await asyncio.sleep(2)
            await start.edit(content=i)

    @commands.command(
        name="unflip",
        usage="",
        description="Unflip animation"
    )
    async def tableflip(self, luna):
        start = await luna.send(f"{luna.author.mention} is unflipping the table")
        animation_list = (
            "`(\\°-°)\\  ┻━┻`",
            "`(\\°□°)\\  ┻━┻`",
            "`(-°□°)-  ┻━┻`",
            "`(-°□°)-  ]`",
            "`(\\°-°)\\  ┬─┬`",
        )
        for i in animation_list:
            await asyncio.sleep(2)
            await start.edit(content=i)

    @commands.command(
        name="warning",
        usage="",
        description="System overload animation"
    )
    async def warning(self, luna):
        start = await luna.send(f"{luna.author.mention} is getting a warning")
        animation_list = (
            "`LOAD !! WARNING !! SYSTEM OVER`",
            "`OAD !! WARNING !! SYSTEM OVERL`",
            "`AD !! WARNING !! SYSTEM OVERLO`",
            "`D !! WARNING !! SYSTEM OVERLOA`",
            "`! WARNING !! SYSTEM OVERLOAD !`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`ARNING !! SYSTEM OVERLOAD !! W`",
            "`RNING !! SYSTEM OVERLOAD !! WA`",
            "`NING !! SYSTEM OVERLOAD !! WAR`",
            "`ING !! SYSTEM OVERLOAD !! WARN`",
            "`NG !! SYSTEM OVERLOAD !! WARNI`",
            "`G !! SYSTEM OVERLOAD !! WARNIN`",
            "`!! SYSTEM OVERLOAD !! WARNING`",
            "`! SYSTEM OVERLOAD !! WARNING !`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
            "`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
            "`CTRL + R FOR MANUAL OVERRIDE..`",
        )
        for i in animation_list:
            await asyncio.sleep(2)
            await start.edit(content=i)
