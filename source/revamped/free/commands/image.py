import urllib

from discord.ext import commands
from .utilities import *


class ImageCog(commands.Cog, name="Image commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    # ///////////////////////////////////////////////////////////////
    # Avatar commands

    @commands.command(
        name="avatar",
        usage="[@member]",
        aliases=["av"],
        description="Send the avatar"
    )
    async def avatar(self, luna, user: discord.Member = None):

        if user is None:
            user = luna.author
        await message_builder(luna, description=f"```\n{user}'s avatar\n```", large_image=user.avatar_url)

    @commands.command(
        name="avatart",
        usage="<@member> <text>",
        asliases=["avt"],
        description="Send the avatar with text"
    )
    async def avatart(self, luna, user: discord.Member, *, text: str):

        await message_builder(luna, description=f"```\n{text}\n```", large_image=user.avatar_url)

    @commands.command(
        name="searchav",
        usage="<@member>",
        description="Search link of the avatar"
    )
    async def searchav(self, luna, user: discord.Member = None):

        if user is None:
            user = luna.author
        await message_builder(luna, description=f"```\nSearch link for {user}'s avatar\n``````\nGoogle search URL\n\nhttps://images.google.com/searchbyimage?image_url={user.avatar_url}\n```")

    @commands.command(
        name="linkav",
        usage="<@member>",
        description="Link of the avatar"
    )
    async def linkav(self, luna, member: discord.Member):

        embed = discord.Embed(
            title=f"Link for {member}'s avatar",
            description=f"{member.avatar_url}"
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="stealav",
        usage="<@member>",
        description="Steal the avatar"
    )
    async def stealav(self, luna, user: discord.Member):

        url = user.avatar_url
        prefix = files.json("data/config.json", "prefix", documents=False)
        if configs.password() == "password-here":
            await error_builder(luna, f"```\nYou didn't configurate your password yet, use {prefix}password <password>\n```")
        else:
            configs.password()
            with open('PFP-1.png', 'wb') as f:
                r = requests.get(url, stream=True)
                for block in r.iter_content(1024):
                    if not block:
                        break
                    f.write(block)
        try:
            with open('PFP-1.png', 'rb') as f:
                await self.bot.user.edit(password=configs.password(), avatar=f.read())
            await message_builder(luna, description=f"```\nStole {user}'s avatar\n```", large_image=user.avatar_url)
        except discord.HTTPException as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="setavatar",
        usage="<url>",
        description="Set your avatar"
    )
    async def setavatar(self, luna, url: str):
        prefix = files.json("data/config.json", "prefix", documents=False)
        if configs.password() == "password-here":
            await error_builder(luna, f"```\nYou didn't configurate your password yet, use {prefix}password <password>\n```")
        else:
            configs.password()
            with open('PFP-1.png', 'wb') as f:
                r = requests.get(url, stream=True)
                for block in r.iter_content(1024):
                    if not block:
                        break
                    f.write(block)
        try:
            with open('PFP-1.png', 'rb') as f:
                await self.bot.user.edit(password=configs.password(), avatar=f.read())
            await message_builder(luna, description=f"```\nChanged avatar\n```")
        except discord.HTTPException as e:
            await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="invisav",
        usage="",
        description="Invisible avatar"
    )
    async def invisav(self, luna):
        prefix = files.json("data/config.json", "prefix", documents=False)
        url = "https://gauginggadgets.com/wp-content/uploads/2020/07/InvisibleProfileImage.png"
        if configs.password() == "password-here":
            await error_builder(luna, f"```\nYou didn't configurate your password yet, use {prefix}password <password>\n```")
        else:
            configs.password()
            with open('PFP-1.png', 'wb') as f:
                r = requests.get(url, stream=True)
                for block in r.iter_content(1024):
                    if not block:
                        break
                    f.write(block)
        try:
            with open('PFP-1.png', 'rb') as f:
                await self.bot.user.edit(password=configs.password(), avatar=f.read())
            await message_builder(luna, description=f"```\nChanged to an invisible avatar\n```")
        except discord.HTTPException as e:
            await error_builder(luna, description=f"```{e}```")

    # ///////////////////////////////////////////////////////////////
    # Fun image commands

    @commands.command(
        name="dog",
        usage="",
        description="Send a random dog"
    )
    async def dog(self, luna):

        r = requests.get("https://dog.ceo/api/breeds/image/random").json()
        embed = discord.Embed(title=theme.title())
        embed.set_footer(text=theme.footer())

        embed.set_image(url=str(r['message']))
        await send(luna, embed)

    @commands.command(
        name="fox",
        usage="",
        description="Send a random fox"
    )
    async def fox(self, luna):

        r = requests.get('https://randomfox.ca/floof/').json()
        embed = discord.Embed(title=theme.title())
        embed.set_footer(text=theme.footer())

        embed.set_image(url=str(r['image']))
        await send(luna, embed)

    @commands.command(
        name="cat",
        usage="",
        description="Send a random cat"
    )
    async def cat(self, luna):

        r = requests.get("https://api.thecatapi.com/v1/images/search").json()
        embed = discord.Embed(title=theme.title())
        embed.set_footer(text=theme.footer())

        embed.set_image(url=str(r[0]["url"]))
        await send(luna, embed)

    @commands.command(
        name="sadcat",
        usage="",
        description="Send a random sad cat"
    )
    async def sadcat(self, luna):

        r = requests.get("https://api.alexflipnote.dev/sadcat").json()
        embed = discord.Embed(title=theme.title())
        embed.set_footer(text=theme.footer())

        embed.set_image(url=str(r['file']))
        await send(luna, embed)

    @commands.command(
        name="waifu",
        usage="",
        description="Send a random waifu"
    )
    async def waifu(self, luna):

        r = requests.get("https://nekos.life/api/v2/img/waifu").json()
        embed = discord.Embed(title=theme.title())
        embed.set_footer(text=theme.footer())

        embed.set_image(url=str(r['url']))
        await send(luna, embed)

    # ///////////////////////////////////////////////////////////////
    # Image commands

    @commands.command(
        name="wallpaper",
        usage="",
        description="Send a random anime wallpaper"
    )
    async def wallpaper(self, luna):

        r = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
        embed = discord.Embed(title=theme.title())
        embed.set_footer(text=theme.footer())

        embed.set_image(url=str(r['url']))
        await send(luna, embed)

    @commands.command(
        name="wide",
        usage="<@member>",
        description="Wide profile picture"
    )
    async def wide(self, luna, user: discord.User):

        embed = discord.Embed(title=theme.title())
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/wide?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)

    @commands.command(
        name="trumptweet",
        usage="<text>",
        description="Create a Trump tweet"
    )
    async def trumptweet(self, luna, *, text: str):

        request = requests.get(
            f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={urllib.parse.quote(text)}'
        )
        data = request.json()
        link = data['message']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="bidentweet",
        usage="<text>",
        description="Create a Biden tweet"
    )
    async def bidentweet(self, luna, *, text: str):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f'https://api.popcat.xyz/biden?text={str(urllib.parse.quote(text))}'
        )
        await send(luna, embed)

    @commands.command(
        name="tweet",
        usage="<name> <text>",
        description="Create a tweet"
    )
    async def tweet(self, luna, name, *, text: str):

        request = requests.get(
            f'https://nekobot.xyz/api/imagegen?type=tweet&username={name}&text={urllib.parse.quote(text)}'
        )
        data = request.json()
        link = data['message']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="supreme",
        usage="<text>",
        description="Custom supreme logo"
    )
    async def supreme(self, luna, *, text: str):

        request = requests.get(
            f'https://react.flawcra.cc/api/generation.php?type=supreme&text={str(urllib.parse.quote(text))}'
        ).json()[
            'url']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=f'{request}')
        await send(luna, embed)

    @commands.command(
        name="changemymind",
        usage="<text>",
        description="Changemymind meme"
    )
    async def changemymind(self, luna, *, text: str):

        request = requests.get(
            f'https://nekobot.xyz/api/imagegen?type=changemymind&text={urllib.parse.quote(text)}'
        )
        data = request.json()
        link = data['message']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="phcomment",
        aliases=['pornhubcomment'],
        usage="<@member> <text>",
        description="Pornhub comment"
    )
    async def phcomment(self, luna, user: discord.User, *, text: str):

        image_url = str(user.avatar_url).replace(".webp", ".png")
        request = requests.get(
            f'https://nekobot.xyz/api/imagegen?type=phcomment&image={image_url}&username={urllib.parse.quote(user.name)}&text={urllib.parse.quote(text)}'
        )
        data = request.json()
        link = data['message']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="clyde",
        usage="<text>",
        description="Custom Clyde message"
    )
    async def clyde(self, luna, *, text: str):

        request = requests.get(
            f'https://nekobot.xyz/api/imagegen?type=clyde&text={urllib.parse.quote(text)}'
        )
        data = request.json()
        link = data['message']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="pikachu",
        usage="<text>",
        description="Surprised Pikachu"
    )
    async def pikachu(self, luna, *, text: str):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://api.popcat.xyz/pikachu?text={urllib.parse.quote(str(text))}"
        )
        await send(luna, embed)

    @commands.command(
        name="stonks",
        usage="<@member>",
        description="Stonks!"
    )
    async def stonks(self, luna, user: discord.User):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)

    @commands.command(
        name="notstonks",
        usage="<@member>",
        description="Notstonks!"
    )
    async def notstonks(self, luna, user: discord.User):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}&notstonks=true"
        )
        await send(luna, embed)

    @commands.command(
        name="emergencymeeting",
        usage="<text>",
        description="Emergency meeting!"
    )
    async def emergencymeeting(self, luna, *, text):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/emergencymeeting?text={urllib.parse.quote(text)}"
        )
        await send(luna, embed)

    @commands.command(
        name="eject",
        usage="<true/false> <color> <@member>",
        description="Among Us"
    )
    async def eject(self, luna, impostor: bool, crewmate: str, user: discord.User):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/ejected?name={urllib.parse.quote(user.name)}&impostor={impostor}&crewmate={crewmate}"
        )
        await send(luna, embed)

    @commands.command(
        name="drip",
        usage="<@member>",
        description="Drip meme"
    )
    async def drip(self, luna, user: discord.User):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/drip?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)

    @commands.command(
        name="gun",
        usage="<@member>",
        description="Gun meme"
    )
    async def gun(self, luna, user: discord.User):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://api.popcat.xyz/gun?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)

    @commands.command(
        name="ad",
        usage="<@member>",
        description="Make yourself an ad"
    )
    async def ad(self, luna, user: discord.User):

        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://api.popcat.xyz/ad?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)


class ImageCog2(commands.Cog, name="Image commands 2"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="alert",
        usage="<text>",
        description="Iphone alert"
    )
    async def alert(self, luna, *, text: str):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://api.popcat.xyz/alert?text={urllib.parse.quote(str(text))}"
        )
        await send(luna, embed)

    @commands.command(
        name="caution",
        usage="<text>",
        description="Caution image"
    )
    async def caution(self, luna, *, text: str):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://api.popcat.xyz/caution?text={urllib.parse.quote(str(text))}"
        )
        await send(luna, embed)

    @commands.command(
        name="distractedbf",
        usage="<@boyfriend> <@woman> <@girlfriend>",
        description="Distracted boyfriend meme"
    )
    async def distractedbf(self, luna, boyfriend: discord.User, woman: discord.User, girlfriend: discord.User):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/distractedbf?boyfriend={urllib.parse.quote(str(boyfriend.avatar_url).replace('webp', 'png'))}&woman={urllib.parse.quote(str(woman.avatar_url).replace('webp', 'png'))}&girlfriend={urllib.parse.quote(str(girlfriend.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)

    @commands.command(
        name="icanmilkyou",
        usage="<@member1> <@member2>",
        description="ICanMilkYou"
    )
    async def icanmilkyou(self, luna, user1: discord.User, user2: discord.User):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/icanmilkyou?user1={urllib.parse.quote(str(user1.avatar_url))}&user2={urllib.parse.quote(str(user2.avatar_url))}"
        )
        await send(luna, embed)

    @commands.command(
        name="heaven",
        usage="<@member>",
        description="Heaven meme"
    )
    async def heaven(self, luna, user: discord.User):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/heaven?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)

    @commands.command(
        name="dockofshame",
        usage="<@member>",
        description="Heaven meme"
    )
    async def dockofshame(self, luna, user: discord.User):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/dockofshame?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)

    @commands.command(
        name="firsttime",
        usage="<@member>",
        description="First time? meme"
    )
    async def firsttime(self, luna, user: discord.User):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://vacefron.nl/api/firsttime?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}"
        )
        await send(luna, embed)

    @commands.command(
        name="trash",
        usage="<@member>",
        description="Trash meme"
    )
    async def trash(self, luna, user: discord.User):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f'https://api.no-api-key.com/api/v2/trash?image={str(user.avatar_url).replace(".webp", ".png")}'
        )
        await send(luna, embed)

    @commands.command(
        name="simp",
        usage="<@member>",
        description="Simp card"
    )
    async def simp(self, luna, user: discord.User):
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f'https://api.no-api-key.com/api/v2/simpcard?image={str(user.avatar_url).replace(".webp", ".png")}'
        )
        await send(luna, embed)

    @commands.command(
        name="wanted",
        usage="<@member>",
        description="Wanted"
    )
    async def wanted(self, luna, user: discord.User):
        request = requests.get(
            f'https://react.flawcra.cc/api/generation.php?type=wanted&url={str(user.avatar_url).replace(".webp", ".png")}'
        )
        data = request.json()
        link = data['url']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="wasted",
        usage="<@member>",
        description="GTA Wasted"
    )
    async def wasted(self, luna, user: discord.User):
        request = requests.get(
            f'https://react.flawcra.cc/api/generation.php?type=wasted&url={str(user.avatar_url).replace(".webp", ".png")}'
        )
        data = request.json()
        link = data['url']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="continued",
        usage="<@member>",
        description="To be continued"
    )
    async def continued(self, luna, user: discord.User):
        request = requests.get(
            f'https://react.flawcra.cc/api/generation.php?type=tobecontinued&url={str(user.avatar_url).replace(".webp", ".png")}'
        )
        data = request.json()
        link = data['url']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="drake",
        usage="<no, yes>",
        description="Drake yes and no meme"
    )
    async def drake(self, luna, *, text: str):
        try:
            text = text.split(', ')
            text1 = text[0]
            text2 = text[1]
            embed = discord.Embed(
                title=theme.title()
            )
            embed.set_footer(text=theme.footer())

            embed.set_image(
                url=f'https://api.popcat.xyz/drake?text1={str(urllib.parse.quote(text1))}&text2={str(urllib.parse.quote(text2))}'
            )
            await send(luna, embed)
        except BaseException:
            prefix = files.json("data/config.json", "prefix", documents=False)
            await error_builder(luna, f"```Example: {prefix}drake Paid Selfbots, Luna\nThe space between the comma and the two words is required.```")

    @commands.command(
        name="takemymoney",
        usage="<text1, text2>",
        description="Take my money"
    )
    async def takemymoney(self, luna, *, text: str):
        text = text.split(', ')
        text1 = text[0]
        text2 = text[1]
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(
            url=f"https://api.memegen.link/images/money/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png"
        )
        await send(luna, embed)

    @commands.command(
        name="pornhub",
        usage="<text1, text2>",
        description="PornHub logo"
    )
    async def pornhub(self, luna, *, text: str):
        text = text.split(', ')
        text1 = text[0]
        text2 = text[1]
        request = requests.get(
            f'https://react.flawcra.cc/api/generation.php?type=phlogo&text={str(urllib.parse.quote(text1))}&text2={str(urllib.parse.quote(text2))}'
        )
        data = request.json()
        link = data['url']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)

    @commands.command(
        name="recaptcha",
        usage="<text>",
        description="reCAPTCHA"
    )
    async def recaptcha(self, luna, *, text: str):
        request = requests.get(
            f'https://react.flawcra.cc/api/generation.php?type=captcha&text={str(urllib.parse.quote(text))}'
        )
        data = request.json()
        link = data['url']
        embed = discord.Embed(
            title=theme.title()
        )
        embed.set_footer(text=theme.footer())

        embed.set_image(url=link)
        await send(luna, embed)