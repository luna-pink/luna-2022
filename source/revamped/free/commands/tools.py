import re
from subprocess import call

import qrcode
from discord.ext import commands
from gtts import gTTS

from .utilities import *


class ToolsCog(commands.Cog, name="Tools commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="note",
        aliases=['newnote'],
        usage="<name> <text>",
        description="Create a note"
    )
    async def note(self, luna, name: str, *, text: str):

        if files.file_exist(f"data/notes/{name}.txt", documents=False):
            if configs.error_log() == "console":
                prints.error(
                    f"A note already exists with the name » {color.print_gradient(name)}"
                )
            else:
                await error_builder(luna, description=f"```\nA note already exists with the name » {name}```")
        else:
            file = open(
                f"data/notes/{name}.txt", 'wb'
            )
            file.write(str(text))
            file.close()
            prints.message(f"Created note » {color.print_gradient(name)}")
            embed = discord.Embed(
                title=theme.title(),
                description=f"```\nCreated note » {name}```"
            )

            embed.set_footer(
                text=theme.footer(),

            )

            await send(luna, embed)

    @commands.command(
        name="editnote",
        usage="<name> <name>",
        description="Edit the note name"
    )
    async def editnote(self, luna, name: str, themename: str):

        if not files.file_exist(f"data/notes/{name}.txt", documents=False):
            if configs.error_log() == "console":
                prints.error(
                    f"No note exists with the name » {color.print_gradient(name)}"
                )
            else:
                await error_builder(luna, description=f"```\nNo note exists with the name » {name}```")
        else:
            os.rename(
                f"data/notes/{name}.txt", f"data/notes/{themename}.txt"
            )
            prints.message(
                f"Edited note {name} to » {color.print_gradient(themename)}"
            )
            embed = discord.Embed(
                title=theme.title(),
                description=f"```\nEdited \"note\" {name} to » {themename}```"
            )

            embed.set_footer(
                text=theme.footer(),

            )

            await send(luna, embed)

    @commands.command(
        name="delnote",
        usage="<name>",
        description="Delete a note"
    )
    async def delnote(self, luna, name: str):

        if files.file_exist(f"data/notes/{name}.txt", documents=False):
            os.remove(
                f"data/notes/{name}.txt"
            )
            prints.message(f"Deleted note » {color.print_gradient(name)}")

            embed = discord.Embed(
                title=theme.title(),
                description=f"```\nDeleted note » {name}```"
            )

            embed.set_footer(
                text=theme.footer(),

            )

            await send(luna, embed)
        else:
            if configs.error_log() == "console":
                prints.error(f"There is no note called » {color.print_gradient(name)}")
            else:
                await error_builder(luna, description=f"```\nThere is no note called » {name}```")

    @commands.command(
        name="sendnote",
        usage="<name>",
        description="Send the note"
    )
    async def sendnote(self, luna, name: str):

        if not files.file_exist(f"data/notes/{name}.txt", documents=False):
            if configs.error_log() == "console":
                prints.error(
                    f"No note exists with the name » {color.print_gradient(name)}"
                )
            else:
                await error_builder(luna, description=f"```\nNo note exists with the name » {name}```")
        else:
            if name.endswith('.txt'):
                name = name[:-4]
            await luna.send(file=discord.File(f"data/notes/{name}.txt"))

    @commands.command(
        name="shownote",
        usage="<name>",
        description="Send the content of the note"
    )
    async def shownote(self, luna, name: str):

        if not files.file_exist(f"data/notes/{name}.txt", documents=False):
            if configs.error_log() == "console":
                prints.error(
                    f"No note exists with the name » {color.print_gradient(name)}"
                )
            else:
                await error_builder(luna, description=f"```\nNo note exists with the name » {name}```")
        else:
            file = open(
                f"data/notes/{name}.txt", "r"
            )
            file_data = file.read()
            if file_data == "":
                if configs.error_log() == "console":
                    prints.error(f"The note is empty")
                else:
                    await error_builder(luna, description=f"```\nThe note is empty```")
            else:
                embed = discord.Embed(
                    title="Notes",
                    description=f"```\nContent of {name}.txt ↴\n\n{str(file_data)}```",

                )

                embed.set_footer(
                    text=theme.footer(),

                )

                await send(luna, embed)

    @commands.command(
        name="notes",
        usage="",
        description="Show all notes"
    )
    async def notes(self, luna):

        path_to_text = "data/notes"
        text_files = [pos_txt for pos_txt in os.listdir(
            path_to_text
        ) if pos_txt.endswith('.txt')]
        prefix = files.json("data/config.json", "prefix", documents=False)

        if not text_files:
            stringedit = "None"
        else:
            string = f"{text_files}"
            stringedit = string.replace(
                ',',
                f"\n{prefix}shownote"
            ).replace(
                "'",
                ""
            ).replace(
                '[',
                f"{prefix}shownote "
            ).replace(
                ']',
                ""
            ).replace(
                '.txt',
                ""
            )

        embed = discord.Embed(
            title="Notes",
            description=f"{theme.description()}```\n"
                        f"Note control\n\n"
                        f"{prefix}note <name> <text> » Create a note\n"
                        f"{prefix}editnote <name> <name> » Edit note name\n"
                        f"{prefix}delnote <name>   » Delete a note\n"
                        f"{prefix}sendnote <name>  » Send the note\n```"
                        f"```\nAvailable notes\n\n{stringedit}```"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="tokencheck",
        usage="",
        description="Check the tokens.txt"
    )
    async def tokencheck(self, luna):

        file = open(
            "data/raiding/tokens.txt", "r"
        )
        nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
        file.close()

        if os.stat("data/raiding/tokens.txt").st_size == 0:
            await message_builder(luna, title="Token Check", description="```\ntokens.txt is empty...```")
            return

        await message_builder(luna, title="Token Check", description="```\nChecking tokens...```")

        valid_tokens = []
        success = 0
        failed = 0

        with open("data/raiding/tokens.txt", "r+") as f:
            for line in f:
                token = line.strip("\n")
                headers = {
                    'Content-Type': 'application/json',
                    'authorization': token
                }
                url = f"https://discord.com/api/v6/users/@me/library"
                request = requests.get(url, headers=headers)
                if request.status_code == 200:
                    valid_tokens.append(token)
                    success += 1
                else:
                    failed += 1
                    pass

        with open("data/raiding/tokens.txt", "w+") as f:
            for i in valid_tokens:
                f.write(i + "\n")
        await message_builder(
            luna, title="Token Check",
            description="```\nSuccessfully checked all tokens and removed invalid ones.\n``````\nValid tokens » " + str(success) + "\nInvalid tokens » " + str(failed) + "```"
        )

    @commands.command(
        name="tokeninfo",
        usage="<token>",
        description="Check the token for information"
    )
    async def tokeninfo(self, luna, token: str):

        headers = {"Authorization": token, "Content-Type": "application/json"}
        res = requests.get(f"https://discord.com/api/{api_version}/users/@me", headers=headers)
        cc_digits = {"american express": "3", "visa": "4", "mastercard": "5"}
        languages = {
            "da": "Danish, Denmark",
            "de": "German, Germany",
            "en-GB": "English, United Kingdom",
            "en-US": "English, United States",
            "es-ES": "Spanish, Spain",
            "fr": "French, France",
            "hr": "Croatian, Croatia",
            "lt": "Lithuanian, Lithuania",
            "hu": "Hungarian, Hungary",
            "nl": "Dutch, Netherlands",
            "no": "Norwegian, Norway",
            "pl": "Polish, Poland",
            "pt-BR": "Portuguese, Brazilian, Brazil",
            "ro": "Romanian, Romania",
            "fi": "Finnish, Finland",
            "sv-SE": "Swedish, Sweden",
            "vi": "Vietnamese, Vietnam",
            "tr": "Turkish, Turkey",
            "cs": "Czech, Czechia, Czech Republic",
            "el": "Greek, Greece",
            "bg": "Bulgarian, Bulgaria",
            "ru": "Russian, Russia",
            "uk": "Ukranian, Ukraine",
            "th": "Thai, Thailand",
            "zh-CN": "Chinese, China",
            "ja": "Japanese",
            "zh-TW": "Chinese, Taiwan",
            "ko": "Korean, Korea",
        }
        if res.status_code == 200:
            res_json = res.json()
            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json["id"]
            avatar_id = res_json["avatar"]
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif"
            phone_number = res_json["phone"]
            email = res_json["email"]
            mfa_enabled = res_json["mfa_enabled"]
            flags = res_json["flags"]
            locale = res_json["locale"]
            verified = res_json["verified"]
            language = languages.get(locale)
            creation_date = datetime.fromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) / 1000
            ).strftime("%d-%m-%Y %H:%M:%S")
            res = requests.get(
                "https://discord.com/api/v6/users/@me/billing/subscriptions",
                headers=headers,
            )
            nitro_data = res.json()
            has_nitro = bool(len(nitro_data) > 0)
            if has_nitro:
                d1 = datetime.strptime(
                    nitro_data[0]["current_period_end"].split(".")[0],
                    "%Y-%m-%dT%H:%M:%S",
                )
                d2 = datetime.strptime(
                    nitro_data[0]["current_period_start"].split(".")[0],
                    "%Y-%m-%dT%H:%M:%S",
                )
                days_left = abs((d2 - d1).days)
            billing_info = []
            for x in requests.get(
                    "https://discord.com/api/v6/users/@me/billing/payment-sources",
                    headers=headers,
            ).json():
                y = x["billing_address"]
                name = y["name"]
                address_1 = y["line_1"]
                address_2 = y["line_2"]
                city = y["city"]
                postal_code = y["postal_code"]
                state = y["state"]
                country = y["country"]
                if x["type"] == 1:
                    cc_brand = x["brand"]
                    cc_first = cc_digits.get(cc_brand)
                    cc_last = x["last_4"]
                    cc_month = str(x["expires_month"])
                    cc_year = str(x["expires_year"])
                    data = {
                        "Payment Type": "Credit Card",
                        "Valid": not x["invalid"],
                        "CC Holder Name": name,
                        "CC Brand": cc_brand.title(),
                        "CC Number": "".join(
                            z if (i + 1) % 2 else z + " "
                            for i, z in enumerate(
                                (cc_first if cc_first else "*") + ("*" * 11) + cc_last
                            )
                        ),
                        "CC Exp. Date": (
                                            "0" + cc_month if len(cc_month) < 2 else cc_month
                                        ) + "/" + cc_year[2:4],
                        "Address 1": address_1,
                        "Address 2": address_2 if address_2 else "",
                        "City": city,
                        "Postal Code": postal_code,
                        "State": state if state else "",
                        "Country": country,
                        "Default Payment Method": x["default"],
                    }
                elif x["type"] == 2:
                    data = {
                        "Payment Type": "PayPal",
                        "Valid": not x["invalid"],
                        "PayPal Name": name,
                        "PayPal Email": x["email"],
                        "Address 1": address_1,
                        "Address 2": address_2 if address_2 else "",
                        "City": city,
                        "Postal Code": postal_code,
                        "State": state if state else "",
                        "Country": country,
                        "Default Payment Method": x["default"],
                    }
                billing_info.append(data)
            helptext = "```\nUser Information\n\n"
            helptext += f"Username: {user_name}\n"
            helptext += f"User ID: {user_id}\n"
            helptext += f"Creation Date: {creation_date}\n"
            helptext += f'Avatar URL: {avatar_url if avatar_id else "None"}\n'
            helptext += f"Token: {token}\n"
            helptext += f"Nitro Status: {has_nitro}\n"
            if has_nitro:
                helptext += f"Expires in: {days_left} day(s)\n"
            helptext += f"2FA: {mfa_enabled}\n"
            helptext += f"Flags: {flags}\n"
            helptext += f"Locale: {locale} ({language})\n"
            helptext += f"Email Verified: {verified}\n"
            helptext += f'Email: {email if email else ""}\n'
            helptext += f'Phone Number: {phone_number if phone_number else "None"}\n```'
            if len(billing_info) > 0:
                helptext += "```\nBilling Information\n\n"
                if len(billing_info) == 1:
                    for x in billing_info:
                        for key, val in x.items():
                            if not val:
                                continue
                            helptext += "{:<23}{}\n".format(key, val)
                else:
                    for i, x in enumerate(billing_info):
                        helptext += f'```\nPayment Method #{i + 1} ({x["Payment Type"]})\n'
                        for j, (key, val) in enumerate(x.items()):
                            if not val or j == 0:
                                continue
                            helptext += "{:<23}{}\n".format(key, val)
                helptext += f"```"
            await message_builder(luna, "Token Info", helptext)
        else:
            await error_builder(luna, "```\nToken invalid\n```")

    @commands.command(
        name="poll",
        usage="<question>",
        description="Create a poll"
    )
    async def poll(self, luna, *, question):

        message = await luna.send(f"> **Poll**\n> \n> {question}\n> \n> {theme.footer()}")
        await message.add_reaction('👍')
        await message.add_reaction('👎')

    @commands.command(
        name="cpoll",
        usage="<option1> <option2> <question>",
        description="Poll"
    )
    async def cpoll(self, luna, option1, option2, *, poll):

        message = await luna.send(f"> **Poll**\n> \n> {poll}\n> \n> 🅰️ = {option1}\n> 🅱️ = {option2}\n> \n> {theme.footer()}")
        await message.add_reaction('🅰️')
        await message.add_reaction('🅱️')

    @commands.command(
        name="color",
        usage="<hexcode>",
        description="Color information"
    )
    async def color(self, luna, hexcode: str):

        if hexcode == "random":
            hexcode = "%06x" % random.randint(0, 0xFFFFFF)
        if hexcode[:1] == "#":
            hexcode = hexcode[1:]
        if not re.search(r'^(?:[\da-fA-F]{3}){1,2}$', hexcode):
            return
        r = requests.get(
            f"https://react.flawcra.cc/api/generation.php?type=color&color={hexcode}"
        ).json()
        await message_builder(
            luna, title=str(r["name"]),
            description=f"```\nHEX               » {r['hex']}\n``````\nRGB               » {r['rgb']}\n``````\nINT               » {r['int']}\n``````\nBrightness        » {r['brightness']}\n```"
        )

    @commands.command(
        name="hiddenping",
        usage="<channel_id> <user_id> <message>",
        description="Ping someone without showing @member"
    )
    async def hiddenping(self, luna, channel_id: int, user_id, *, message):

        if user_id == "@everyone" or user_id == "everyone":
            user = "@everyone"
        elif len(user_id) == 18:
            user = "<@" + user_id + ">"
        elif len(user_id) == 19:
            user = "<" + user_id + ">"
        else:
            prints.error("Invalid User!")

        cuser = await self.bot.fetch_user(user_id)
        cchannel = await self.bot.fetch_channel(channel_id)

        char_tt = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
        await message.channel.send(f"<{message}>" + char_tt + user)
        await message_builder(
            luna, title=f"Hidden Ping",
            description=f"```\nPing sent!\n\n"
                        f"Channel ID        » {channel_id}\n"
                        f"Channel Name      » {cchannel.name}\n"
                        f"User Name         » {cuser.name}#{cuser.discriminator}\n"
                        f"User ID           » {user_id}\n"
                        f"Message           » {message}```"
        )

    @commands.command(
        name="hiddeneveryone",
        usage="<channel_id> <message>",
        description="Ping everyone without showing @everyone"
    )
    async def hiddeneveryone(self, luna, channel_id: int, *, message):

        user = "@everyone"

        cchannel = await self.bot.fetch_channel(channel_id)

        char_tt = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
        await message.channel.send(f"<{message}>" + char_tt + user)
        await message_builder(
            luna, title=f"Hidden Everyone",
            description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nMessage           » {message}```"
        )

    @commands.command(
        name="hiddeninvite",
        usage="<channel_id> <invite> <message>",
        description="hide the invite"
    )
    async def hiddeninvite(self, luna, channel_id: int, invite, *, message):

        cchannel = await self.bot.fetch_channel(channel_id)

        char_tt = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
        await message.channel.send(f"<{message}>" + char_tt + invite)
        await message_builder(
            luna, title=f"Hidden Ping",
            description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nInvite            » {invite}\nMessage           » {message}```"
        )

    @commands.command(
        name="hiddenurl",
        usage="<channel_id> <url> <message>",
        description="Hide the url"
    )
    async def hiddenurl(self, luna, channel_id: int, url, *, message):

        cchannel = await self.bot.fetch_channel(channel_id)

        char_tt = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
        await message.channel.send(f"<{message}>" + char_tt + url)
        await message_builder(
            luna, title=f"Hidden Ping",
            description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nURL               » {url}\nMessage           » {message}```"
        )

    @commands.command(
        name="channels",
        usage="[guild_id]",
        description="Show all the channels"
    )
    async def channels(self, luna, server_id: int = None):

        if server_id is None:
            server = discord.utils.get(luna.bot.guilds, id=luna.guild.id)
        else:
            server = discord.utils.get(luna.bot.guilds, id=server_id)
        channels = server.channels
        channel_list = []
        for channel in channels:
            channel_list.append(channel)
        await message_builder(
            luna, title=f"Channels in {server}",
            description='\n'.join([f"{ch.name}" for ch in channel_list]) or 'None'
        )

    @commands.command(
        name="firstmsg",
        usage="[#channel]",
        description="First message"
    )
    async def firstmsg(self, luna, channel: discord.TextChannel = None):

        if channel is None:
            channel = luna.channel
        first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
        await message_builder(luna, title="First Message", description=f"[Jump]({first_message.jump_url})")

    @commands.command(
        name="compareservers",
        usage="<serverid1> <serverid2>",
        description="Checks if members are in the same server"
    )
    async def compareservers(self, luna, server_id: int, server_id_2: int):

        server_1 = self.bot.get_guild(server_id)
        server_2 = self.bot.get_guild(server_id_2)
        output = ""
        count = 0
        for member in server_1.members:
            if member in server_2.members:
                output += "{}\n".format(str(member.mention))
                count += 1
        await message_builder(
            luna, title=f"```\nMembers in the same Server » {count}```",
            description=f"```\n{server_1} - {server_2}\n``````\n{output}```"
        )

    @commands.command(
        name="bots",
        usage="",
        description="Show all bots in the guild"
    )
    async def bots(self, luna):

        bots = []
        for member in luna.guild.members:
            if member.bot:
                bots.append(
                    str(member.name).replace("`", "\\`").replace(
                        "*", "\\*"
                    ).replace("_", "\\_") + "#" + member.discriminator
                )
        botslist = f"{', '.join(bots)}".replace(',', "\n")
        await message_builder(luna, title=f"Bots ({len(bots)})", description=f"{botslist}")

    @commands.command(
        name="tts",
        usage="<language> <text>",
        description="Text to speech"
    )
    async def tts(self, luna, lang, *, text: str):

        tts = gTTS(text, lang=lang)
        filename = f'{text}.mp3'
        tts.save(filename)
        await luna.send(file=discord.File(fp=filename, filename=filename))
        if os.path.exists(filename):
            os.remove(filename)

    @commands.command(
        name="qrcode",
        usage="<text>",
        description="Create a QR code"
    )
    async def qrcode(self, luna, *, text: str):

        deletetimer = int(
            files.json(
                "data/config.json",
                "delete_timer", documents=False
            )
        )

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        filename = f'lunaqr.png'
        img.save(filename)
        await luna.send(file=discord.File(fp=filename, filename=filename), delete_after=deletetimer)
        if os.path.exists(filename):
            os.remove(filename)

    @commands.command(
        name="open",
        usage="<application>",
        description="Open an application"
    )
    async def open(self, luna, *, application: str):

        os.startfile(application)
        await message_builder(luna, description=f"```\nOpened {application}```")

    @commands.command(
        name="calc",
        usage="",
        description="Opens calculator"
    )
    async def calc(self, luna):
        call(["calc.exe"])
        await message_builder(luna, description=f"```\nOpened calculator```")

    @commands.command(
        name="notepad",
        usage="",
        description="Opens notepad"
    )
    async def notepad(self, luna):
        call(["notepad.exe"])

    @commands.command(
        name="passgen",
        usage="[length]",
        description="Generate a password"
    )
    async def passgen(self, luna, length: int = 16):

        code = ''.join(
            random.choices(
                string.ascii_letters + string.digits, k=length
            )
        )
        await message_builder(luna, description=f"```\nPassword generated ↴\n\n{code}```")