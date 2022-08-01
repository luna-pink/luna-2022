import asyncio

from discord.ext import commands
from .utilities import *


class FunCog(commands.Cog, name="Fun commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="impersonate",
        usage="<@member> <message>",
        description="Make them send your message"
    )
    async def impersonate(self, luna, user: discord.User, *, message: str):

        webhook = await luna.channel.create_webhook(name=user.name)
        await webhook.send(message, username=user.name, avatar_url=user.avatar_url)
        await webhook.delete()

    @commands.command(
        name="shoot",
        usage="<@member>",
        description="Shoot up someone"
    )
    async def shoot(self, luna, user: discord.Member):

        await message_builder(
            luna, description=f"{user.mention},  got shot up!",
            large_image="https://media1.tenor.com/images/cfb7817a23645120d4baba2dcb9205e0/tenor.gif", footer="None"
        )

    @commands.command(
        name="feed",
        usage="<@member>",
        description="Feed someone"
    )
    async def feed(self, luna, user: discord.Member):

        r = requests.get("https://nekos.life/api/v2/img/feed").json()
        await message_builder(
            luna, description=f"{luna.author.mention} feeds {user.mention}",
            large_image=str(r['url']), footer="None"
        )

    @commands.command(
        name="bite",
        usage="<@member>",
        description="Bite someone"
    )
    async def bite(self, luna, user: discord.Member):

        gif_list = [
            "https://c.tenor.com/MKjNSLL4dGoAAAAC/bite-cute.gif",
            "https://c.tenor.com/aKzAQ_cFsFEAAAAC/arms-bite.gif",
            "https://c.tenor.com/4j3hMz-dUz0AAAAC/anime-love.gif",
            "https://c.tenor.com/TX6YHUnHJk4AAAAC/mao-amatsuka-gj-bu.gif"]
        await message_builder(
            luna, description=f"{user.mention} got bitten by {luna.author.mention}!",
            large_image=random.choice(gif_list), footer="None"
        )

    @commands.command(
        name="kiss",
        usage="<@member>",
        description="Kiss someone"
    )
    async def kiss(self, luna, user: discord.Member):

        r = requests.get("https://nekos.life/api/v2/img/kiss").json()
        await message_builder(
            luna, description=f"{user.mention} got kissed by {luna.author.mention}!",
            large_image=str(r['url']), footer="None"
        )

    @commands.command(
        name="hug",
        usage="<@member>",
        description="Hug someone"
    )
    async def hug(self, luna, user: discord.Member):

        r = requests.get("https://nekos.life/api/v2/img/hug").json()
        await message_builder(
            luna, description=f"{user.mention} got hugged by {luna.author.mention}!",
            large_image=str(r['url']), footer="None"
        )

    @commands.command(
        name="pat",
        usage="<@member>",
        description="Pat someone"
    )
    async def pat(self, luna, user: discord.Member):

        r = requests.get("https://nekos.life/api/v2/img/pat").json()
        await message_builder(luna, description=f"{luna.author.mention} pats {user.mention}", large_image=str(r['url']), footer="None")

    @commands.command(
        name="slap",
        usage="<@member>",
        description="Slap someone"
    )
    async def slap(self, luna, user: discord.Member):

        r = requests.get("https://nekos.life/api/v2/img/slap").json()
        await message_builder(
            luna, description=f"{luna.author.mention} slapped {user.mention}",
            large_image=str(r['url']), footer="None"
        )

    @commands.command(
        name="tickle",
        usage="<@member>",
        description="Tickle someone"
    )
    async def tickle(self, luna, user: discord.Member):

        r = requests.get("https://nekos.life/api/v2/img/tickle").json()
        await message_builder(
            luna, description=f"{luna.author.mention} tickles {user.mention}",
            large_image=str(r['url']), footer="None"
        )

    @commands.command(
        name="fml",
        usage="",
        description="Fuck my life"
    )
    async def fml(self, luna):

        request = requests.get(
            'https://react.flawcra.cc/api/generation.php?type=fml'
        )
        data = request.json()
        text = data['text']
        await message_builder(luna, description=f"```\n{text}\n```")

    @commands.command(
        name="gay",
        usage="[@member]",
        description="Gay rate somebody"
    )
    async def gay(self, luna, user: discord.Member = None):

        if user is None:
            user = luna.author
        number = random.randint(1, 100)
        await message_builder(luna, title=f"{user}'s Gay Rate", description=f"{number}% Gay 🏳️‍🌈")

    @commands.command(
        name="iq",
        usage="[@member]",
        description="Somebody's IQ"
    )
    async def iq(self, luna, user: discord.Member = None):

        if user is None:
            user = luna.author
        number = random.randint(1, 120)
        special = "\n\nQuite low, isn't it?" if number < 20 else ""
        await message_builder(luna, title=f"{user}'s IQ", description=f"{number}{special}")

    @commands.command(
        name="love",
        usage="<@member> [@member]",
        description="Love rate"
    )
    async def love(self, luna, user1: discord.Member, user2: discord.Member = None):

        if user2 is None:
            user2 = luna.author
        number = random.randint(1, 100)
        breakup = random.randint(1, 100)
        kids = random.randint(1, 100)
        embed = discord.Embed(
            title=f"{user1} ❤️ {user2}",
            description=f"{number}% fitted!\n{kids}% chance of them having kids!\n{breakup}% chance of them breaking up!"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="coronatest",
        usage="<@member>",
        description="Test somebody for Corona"
    )
    async def coronatest(self, luna, user: discord.Member = None):

        member = luna.author if user is None else user
        random.seed((member.id * 6) / 2)
        percent = random.randint(0, 100)
        embed = discord.Embed(
            title=f"{user}'s Corona Test",
            description=f'```\n{percent}% positive!\n``````\nResult\n\nOverall » {"Positive" if (percent > 50) else "Negative"}```'
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="8ball",
        usage="<question>",
        description="Ask 8 Ball!"
    )
    async def _8ball(self, luna, *, question: str):

        responses = [
            'That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'That is a definite yes!',
            'Maybe',
            'There is a good chance'
        ]
        answer = random.choice(responses)
        embed = discord.Embed(
            title="8 Ball",
            description=f"```\nQuestion\n\n{question}\n``````\nAnswer\n\n{answer}\n```"
        )
        embed.set_thumbnail(
            url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png"
        )
        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="slot",
        usage="",
        aliases=['slots'],
        description="Play slots"
    )
    async def slot(self, luna):

        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**------------------\n| {a} | {b} | {c} |\n------------------\n\n{luna.author.name}**,"
        if a == b == c:
            embed = discord.Embed(
                title="Slot Machine",
                description=f"{slotmachine} All matchings, you won!",

            )
        elif (a == b) or (a == c) or (b == c):
            embed = discord.Embed(
                title="Slot Machine",
                description=f"{slotmachine} 2 in a row, you won!",

            )
        else:
            embed = discord.Embed(
                title="Slot Machine",
                description=f"{slotmachine} No match, you lost!",

            )

        embed.set_footer(
            text=theme.footer(),

        )
        await send(luna, embed)

    @commands.command(
        name="dadjoke",
        usage="",
        description="Dad jokes"
    )
    async def dadjoke(self, luna):

        request = requests.get(
            'https://icanhazdadjoke.com/',
            headers={
                'accept': 'application/json'
            }
        )
        data = request.json()
        joke = data['joke']
        embed = discord.Embed(
            title=theme.title(),

            description=f'```\n{joke}\n```'
        )
        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="joke",
        usage="",
        description="Random jokes"
    )
    async def dadjoke(self, luna):

        request = requests.get(
            'http://www.official-joke-api.appspot.com/random_joke'
        )
        data = request.json()
        setup = data['setup']
        punchline = data['punchline']
        embed = discord.Embed(
            title=theme.title(),

            description=f'```\nSetup\n\n{setup}\n``````\nPunchline\n\n{punchline}\n```'
        )
        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="coinflip",
        usage="",
        description="Flip a coin"
    )
    async def coinflip(self, luna):

        lista = ['head', 'tails']
        coin = random.choice(lista)
        try:
            if coin == 'head':
                await message_builder(luna, title="Head")
            else:
                await message_builder(luna, title="Tails")
        except discord.HTTPException:
            if coin == 'head':
                await luna.send("```\nCoinflip » Head```")
            else:
                await luna.send("```\nCoinflip » Tails```")

    @commands.command(
        name="prntsc",
        usage="",
        description="Send a random prnt.sc"
    )
    async def prntsc(self, luna):

        await luna.send(Randprntsc())

    @commands.command(
        name="farmer",
        usage="",
        description="Dank Memer farmer"
    )
    async def farmer(self, luna):

        global farming
        farming = True
        while farming:
            await luna.send("pls beg")
            await asyncio.sleep(3)
            await luna.send("pls deposit all")
            await asyncio.sleep(42)

    @commands.command(
        name="afarmer",
        usage="",
        description="Advanced Dank Memer farmer"
    )
    async def afarmer(self, luna):

        global farming
        farming = True
        while farming:
            await luna.send("pls beg")
            await asyncio.sleep(3)
            await luna.send("pls deposit all")
            await asyncio.sleep(3)
            await luna.send("pls postmeme")
            await asyncio.sleep(3)
            await luna.send("n")
            await asyncio.sleep(3)
            await luna.send("pls fish")
            await asyncio.sleep(33)

    @commands.command(
        name="cfarmer",
        usage="",
        description="Advanced Dank Memer farmer"
    )
    async def cfarmer(self, luna):

        global farming
        farming = True
        while farming:
            await luna.send("pls hunt")
            await asyncio.sleep(5)
            await luna.send("pls search")
            await asyncio.sleep(5)
            await luna.send("pls fish")
            await asyncio.sleep(10)
            await luna.send("pls beg")
            await asyncio.sleep(20)
            await luna.send("pls pm")
            await asyncio.sleep(16)
            await luna.send("pls beg")
            await asyncio.sleep(5)
            await luna.send("pls dep all")
            await asyncio.sleep(15)

    @commands.command(
        name="stopfarmer",
        usage="",
        description="Stops the Dank Memer farmer"
    )
    async def stopfarmer(self, luna):

        global farming
        farming = False
        await message_builder(luna, description="Stopped farming")
