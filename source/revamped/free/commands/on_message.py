from discord.ext import commands
from .utilities import *
import asyncio
import re
import httpx
import pyPrivnote


class OnMessage(commands.Cog, name="on message"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        sniped_start_time = time.time()
        if message.author == self.bot.user:
            return
        try:
            global nitro_cooldown
            if files.json(
                    "data/snipers/nitro.json",
                    "sniper",
                    documents=False
            ) == "on" and 'discord.gift/' in message.content.lower():
                elapsed_snipe = '%.4fs' % (time.time() - sniped_start_time)
                code = re.search("discord.gift/(.*)", message.content).group(1)
                if len(code) >= 16:
                    code = code[:16]
                    async with httpx.AsyncClient() as client:
                        start_time = time.time()
                        result = await client.post(
                            f'https://discord.com/api/{api_version}/entitlements/gift-codes/{code}/redeem',
                            json={'channel_id': message.channel.id},
                            headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'}
                        )
                        elapsed = '%.3fs' % (time.time() - start_time)
                    if 'nitro' in str(result.content):
                        status = 'Nitro successfully redeemed'
                    elif 'This gift has been redeemed already' in str(result.content):
                        status = 'Has been redeemed already'
                    else:
                        status = 'Unknown gift code'

                    if nitro_cooldown.count(code) == 0:
                        nitro_cooldown.append(code)

                        print()
                        prints.sniper(status)
                        prints.sniper(
                            f"Server  | {message.guild}"
                        )
                        prints.sniper(
                            f"Channel | {message.channel}"
                        )
                        prints.sniper(
                            f"Author  | {message.author}"
                        )
                        prints.sniper(f"Code    | {code}")
                        prints.sniper('Elapsed Times')
                        prints.sniper(
                            f"Sniped  | {elapsed_snipe}"
                        )
                        prints.sniper(
                            f"Request | {elapsed}"
                        )
                        print()

                        if files.json(
                                "data/notifications/toasts.json",
                                "nitro",
                                documents=False
                        ) == "on" and files.json(
                            "data/notifications/toasts.json",
                            "toasts",
                            documents=False
                        ) == "on":
                            notify.toast(
                                f"{status}\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}"
                            )
                        if files.json(
                                "data/webhooks/webhooks.json",
                                "nitro",
                                documents=False
                        ) == "on" and files.json(
                            "data/webhooks/webhooks.json",
                            "webhooks",
                            documents=False
                        ) == "on" and not webhook.nitro_url() == "webhook-url-here":
                            notify.webhook(
                                url=webhook.nitro_url(),
                                name="nitro",
                                description=f"{status}\n"
                                            f"Server » {message.guild}\n"
                                            f"Channel » {message.channel}\n"
                                            f"Author » {message.author}\n"
                                            f"Code » {code}\n"
                                            f"Elapsed Times\n"
                                            f"Sniped » {elapsed_snipe}\n"
                                            f"Request » {elapsed}"
                            )

                        nitro_ratelimit = files.json(
                            "data/snipers/nitro.json", "charge", documents=False
                        )
                        if nitro_ratelimit == "on":
                            startup_status = files.json(
                                "data/config.json", "startup_status", documents=False
                            )
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                                'Content-Type': 'application/json',
                                'Authorization': user_token,
                            }
                            request = requests.Session()
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [⠀⠀⠀⠀⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [#⠀⠀⠀⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [##⠀⠀⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [###⠀⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [####⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [#####]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)

            elif files.json(
                    "data/snipers/nitro.json", "sniper",
                    documents=False
            ) == "on" and 'discord.com/gifts' in message.content.lower():
                elapsed_snipe = '%.4fs' % (time.time() - sniped_start_time)
                code = re.search(
                    "discord.com/gifts/(.*)",
                    message.content
                ).group(1)
                if len(code) >= 16:
                    async with httpx.AsyncClient() as client:
                        start_time = time.time()
                        result = await client.post(
                            f'https://discord.com/api/{api_version}/entitlements/gift-codes/{code}/redeem',
                            json={'channel_id': message.channel.id},
                            headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'}
                        )
                        elapsed = '%.3fs' % (time.time() - start_time)
                    if 'nitro' in str(result.content):
                        status = 'Nitro successfully redeemed'
                    elif 'This gift has been redeemed already' in str(result.content):
                        status = 'Has been redeemed already'
                    else:
                        status = 'Unknown gift code'

                    if nitro_cooldown.count(code) == 0:
                        nitro_cooldown.append(code)

                        print()
                        prints.sniper(status)
                        prints.sniper(
                            f"Server  | {message.guild}"
                        )
                        prints.sniper(
                            f"Channel | {message.channel}"
                        )
                        prints.sniper(
                            f"Author  | {message.author}"
                        )
                        prints.sniper(f"Code    | {code}")
                        prints.sniper('Elapsed Times')
                        prints.sniper(
                            f"Sniped  | {elapsed_snipe}"
                        )
                        prints.sniper(
                            f"Request | {elapsed}"
                        )
                        print()

                        if files.json(
                                "data/notifications/toasts.json",
                                "nitro",
                                documents=False
                        ) == "on" and files.json(
                            "data/notifications/toasts.json",
                            "toasts",
                            documents=False
                        ) == "on":
                            notify.toast(
                                f"{status}\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}"
                            )
                        if files.json(
                                "data/webhooks/webhooks.json",
                                "nitro",
                                documents=False
                        ) == "on" and files.json(
                            "data/webhooks/webhooks.json",
                            "webhooks",
                            documents=False
                        ) == "on" and not webhook.nitro_url() == "webhook-url-here":
                            notify.webhook(
                                url=webhook.nitro_url(),
                                name="nitro",
                                description=f"{status}\n"
                                            f"Server » {message.guild}\n"
                                            f"Channel » {message.channel}\n"
                                            f"Author » {message.author}\n"
                                            f"Code » {code}\n"
                                            f"Elapsed Times\n"
                                            f"Sniped » {elapsed_snipe}\n"
                                            f"Request » {elapsed}"
                            )

                        nitro_ratelimit = files.json(
                            "data/snipers/nitro.json", "charge", documents=False
                        )
                        if nitro_ratelimit == "on":
                            startup_status = files.json(
                                "data/config.json", "startup_status", documents=False
                            )
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                                'Content-Type': 'application/json',
                                'Authorization': user_token,
                            }
                            request = requests.Session()
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [⠀⠀⠀⠀⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [#⠀⠀⠀⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [##⠀⠀⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [###⠀⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [####⠀]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
                            await asyncio.sleep(1)
                            setting = {
                                'status': startup_status,
                                "custom_status": {"text": f"Ratelimit: [#####]"}
                            }
                            request.patch(f"https://discord.com/api/{api_version}/users/@me/settings", headers=headers, json=setting, timeout=10)
        except Exception as e:
            prints.error(e)

        giveaway_joiner = files.json(
            "data/snipers/giveaway.json", "joiner", documents=False
        )
        delay_in_minutes = int(
            files.json(
                "data/snipers/giveaway.json", "delay_in_minutes", documents=False
            )
        )
        giveaway_blocked_words = files.json(
            "data/snipers/giveaway.json", "blocked_words", documents=False
        )
        guild_joiner = files.json(
            "data/snipers/giveaway.json", "guild_joiner", documents=False
        )
        if giveaway_joiner == "on" and message.author.bot and message.guild is not None and not isinstance(
                message.channel, discord.GroupChannel
        ):
            custom_giveaway_bot_ids = []
            custom_giveaway_bot_reactions = []
            try:
                if os.path.exists(f"data/snipers/giveaway_bots.json"):
                    with open(
                            f"data/snipers/giveaway_bots.json", "r",
                            encoding="utf-8"
                    ) as jsonFile:
                        data = json.load(jsonFile)

                    for key, value in data.items():
                        try:
                            custom_giveaway_bot_ids.append(int(key))
                            custom_giveaway_bot_reactions.append(str(value))
                        except BaseException:
                            pass
            except BaseException:
                pass
            embeds = message.embeds
            for embed in embeds:
                if ((("giveaway" in str(message.content).lower()) and (
                        int(message.author.id) in custom_giveaway_bot_ids) and (
                             "cancelled" not in str(message.content).lower()) and (
                             "mention" not in str(message.content).lower()) and (
                             "specify" not in str(message.content).lower()) and (
                             "congratulations" not in str(message.content).lower())) and embed is not None):
                    found_something_blacklisted = 0
                    for blocked_word in giveaway_blocked_words:
                        if str(blocked_word).lower() in str(
                                message.content
                        ).lower():
                            print()
                            prints.sniper(
                                f"Skipped giveaway"
                            )
                            prints.sniper(
                                f"Reason  | Backlisted word » {blocked_word}"
                            )
                            prints.sniper(
                                f"Server  | {message.guild}"
                            )
                            prints.sniper(
                                f"Channel | {message.channel}"
                            )
                            print()
                            if files.json(
                                    "data/notifications/toasts.json",
                                    "giveaway",
                                    documents=False
                            ) == "on" and files.json(
                                "data/notifications/toasts.json",
                                "toasts",
                                documents=False
                            ) == "on":
                                notify.toast(
                                    f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}"
                                )
                            if files.json(
                                    "data/webhooks/webhooks.json",
                                    "giveaway",
                                    documents=False
                            ) == "on" and files.json(
                                "data/webhooks/webhooks.json",
                                "webhooks",
                                documents=False
                            ) == "on" and not webhook.giveaway_url() == "webhook-url-here":
                                notify.webhook(
                                    url=webhook.giveaway_url(),
                                    name="giveaway",
                                    description=f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}"
                                )
                            found_something_blacklisted = 1
                    try:
                        for _embed in message.embeds:
                            embed_dict = _embed.to_dict()
                            for blocked_word in giveaway_blocked_words:
                                try:
                                    found = re.findall(
                                        blocked_word, str(embed_dict).lower()
                                    )[0]
                                    if found:
                                        print()
                                        prints.sniper(
                                            f"Skipped giveaway"
                                        )
                                        prints.sniper(
                                            f"Reason  | Backlisted word » {blocked_word}"
                                        )
                                        prints.sniper(
                                            f"Server  | {message.guild}"
                                        )
                                        prints.sniper(
                                            f"Channel | {message.channel}"
                                        )
                                        print()
                                        if files.json(
                                                "data/notifications/toasts.json",
                                                "giveaway",
                                                documents=False
                                        ) == "on" and files.json(
                                            "data/notifications/toasts.json",
                                            "toasts",
                                            documents=False
                                        ) == "on":
                                            notify.toast(
                                                f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}"
                                            )
                                        if files.json(
                                                "data/webhooks/webhooks.json",
                                                "giveaway",
                                                documents=False
                                        ) == "on" and files.json(
                                            "data/webhooks/webhooks.json",
                                            "webhooks",
                                            documents=False
                                        ) == "on" and not webhook.giveaway_url() == "webhook-url-here":
                                            notify.webhook(
                                                url=webhook.giveaway_url(),
                                                name="giveaway",
                                                description=f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}"
                                            )
                                        found_something_blacklisted = 1
                                        break
                                except BaseException:
                                    pass

                                if found_something_blacklisted > 0:
                                    break
                    except BaseException:
                        pass

                    if found_something_blacklisted == 0:
                        try:
                            embeds = message.embeds
                            joined_server = 'None'
                            giveaway_prize = None
                            try:
                                for embed_1 in embeds:
                                    giveaway_prize = embed_1.to_dict()[
                                        'author']['name']
                            except Exception:
                                for embed_2 in embeds:
                                    giveaway_prize = embed_2.to_dict()['title']
                            if guild_joiner == "on":
                                try:
                                    for embed_3 in embeds:
                                        embed_dict = embed_3.to_dict()
                                        code = re.findall(
                                            r"\w[a-z]*\W*\w[a-z]+\.\wg*\W\S*", str(
                                                embed_dict['description']
                                            )
                                        )[0].replace(
                                            ")", ""
                                        ).replace(
                                            "https://discord.gg/", ""
                                        )
                                        async with httpx.AsyncClient() as client:
                                            await client.post(f'https://discord.com/api/{api_version}/invites/{code}', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
                                            joined_server = f'discord.gg/{code}'
                                            await asyncio.sleep(5)
                                except BaseException:
                                    pass
                            else:
                                pass
                            print()
                            prints.sniper("Giveaway found")
                            prints.sniper(
                                f"Prize   | {giveaway_prize}"
                            )
                            prints.sniper(
                                f"Server  | {message.guild}"
                            )
                            prints.sniper(
                                f"Channel | {message.channel}"
                            )
                            prints.sniper(
                                f"Joining | In {delay_in_minutes} minute/s"
                            )
                            prints.sniper(
                                f"Invite  | Joined guild » {joined_server}"
                            )
                            print()
                            if files.json(
                                    "data/notifications/toasts.json",
                                    "giveaway",
                                    documents=False
                            ) == "on" and files.json(
                                "data/notifications/toasts.json",
                                "toasts",
                                documents=False
                            ) == "on":
                                notify.toast(
                                    f"Giveaway found\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}"
                                )
                            if files.json(
                                    "data/webhooks/webhooks.json",
                                    "giveaway",
                                    documents=False
                            ) == "on" and files.json(
                                "data/webhooks/webhooks.json",
                                "webhooks",
                                documents=False
                            ) == "on" and not webhook.giveaway_url() == "webhook-url-here":
                                notify.webhook(
                                    url=webhook.giveaway_url(),
                                    name="giveaway",
                                    description=f"Giveaway found\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}"
                                )
                        except Exception as e:
                            prints.error(e)
                            return

                        await asyncio.sleep(delay_in_minutes * 60)

                        try:
                            if int(
                                    message.author.id
                            ) in custom_giveaway_bot_ids:
                                index = custom_giveaway_bot_ids.index(
                                    int(message.author.id)
                                )
                                try:
                                    await message.add_reaction(custom_giveaway_bot_reactions[index])
                                except Exception as e:
                                    prints.error(e)
                                    return
                                print()
                                prints.sniper(
                                    f"Joined giveaway"
                                )
                                prints.sniper(
                                    f"Prize   | {giveaway_prize}"
                                )
                                prints.sniper(
                                    f"Server  | {message.guild}"
                                )
                                prints.sniper(
                                    f"Channel | {message.channel}"
                                )
                                print()
                                if files.json(
                                        "data/notifications/toasts.json",
                                        "giveaway",
                                        documents=False
                                ) == "on" and files.json(
                                    "data/notifications/toasts.json",
                                    "toasts",
                                    documents=False
                                ) == "on":
                                    notify.toast(
                                        f"Joined giveaway\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}"
                                    )
                                if files.json(
                                        "data/webhooks/webhooks.json",
                                        "giveaway",
                                        documents=False
                                ) == "on" and files.json(
                                    "data/webhooks/webhooks.json",
                                    "webhooks",
                                    documents=False
                                ) == "on" and not webhook.giveaway_url() == "webhook-url-here":
                                    notify.webhook(
                                        url=webhook.giveaway_url(),
                                        name="giveaway",
                                        description=f"Joined giveaway\n"
                                                    f"Prize » {giveaway_prize}\n"
                                                    f"Server »  {message.guild}\n"
                                                    f"Channel » {message.channel}"
                                    )
                        except BaseException:
                            pass

                if '<@' + str(self.bot.user.id) + '>' in message.content and (
                        'giveaway' in str(message.content).lower() or ' won ' in message.content or ' winner ' in str(
                    message.content
                ).lower()) and message.author.bot and message.author.id in custom_giveaway_bot_ids:
                    print()
                    prints.sniper("Won giveaway")
                    prints.sniper(
                        f"Server  | {message.guild}"
                    )
                    prints.sniper(
                        f"Channel | {message.channel}"
                    )
                    print()
                    if files.json(
                            "data/notifications/toasts.json",
                            "giveaway",
                            documents=False
                    ) == "on" and files.json(
                        "data/notifications/toasts.json",
                        "toasts",
                        documents=False
                    ) == "on":
                        notify.toast(
                            f"Won giveaway\nServer »  {message.guild}\nChannel » {message.channel}"
                        )
                    if files.json(
                            "data/webhooks/webhooks.json",
                            "giveaway",
                            documents=False
                    ) == "on" and files.json(
                        "data/webhooks/webhooks.json",
                        "webhooks",
                        documents=False
                    ) == "on" and not webhook.giveaway_url() == "webhook-url-here":
                        notify.webhook(
                            url=webhook.giveaway_url(),
                            name="giveaway",
                            description=f"Won giveaway\nServer »  {message.guild}\nChannel » {message.channel}"
                        )
            if giveaway_joiner == "on" and message.author.bot:
                if "joining" in str(
                        message.content
                ).lower() and guild_joiner == "on":
                    try:
                        for _ in embeds:
                            code = re.findall(
                                r"\w[a-z]*\W*\w[a-z]+\.\w[g]*\W\S*", str(
                                    message.content
                                ).replace(
                                    ")", ""
                                ).replace(
                                    "https://discord.gg/", ""
                                )
                            )
                            async with httpx.AsyncClient() as client:
                                await client.post(
                                    f'https://canary.discord.com/api/{api_version}/invites/{code}',
                                    headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'}
                                )
                                joined_server = f'discord.gg/{code}'
                                if files.json(
                                        "data/notifications/toasts.json",
                                        "giveaway",
                                        documents=False
                                ) == "on" and files.json(
                                    "data/notifications/toasts.json",
                                    "toasts",
                                    documents=False
                                ) == "on":
                                    notify.toast(
                                        f"Joined guild\nInvite » {joined_server}"
                                    )
                                if files.json(
                                        "data/webhooks/webhooks.json",
                                        "giveaway",
                                        documents=False
                                ) == "on" and files.json(
                                    "data/webhooks/webhooks.json",
                                    "webhooks",
                                    documents=False
                                ) == "on" and not webhook.giveaway_url() == "webhook-url-here":
                                    notify.webhook(
                                        url=webhook.giveaway_url(),
                                        name="giveaway",
                                        description=f"Joined guild\nInvite » {joined_server}"
                                    )
                                await asyncio.sleep(5)
                    except BaseException:
                        pass
                else:
                    pass
        # ///////////////////////////////////////////////////////////////
        # Copy Member

        if copycat is not None and copycat.id == message.author.id:
            await message.channel.send(chr(173) + message.content)

        # ///////////////////////////////////////////////////////////////
        # Share command
        prefix = files.json("data/config.json", "prefix", documents=False)
        share = files.json(f"data/sharing.json", "share", documents=False)
        user_id = files.json(f"data/sharing.json", "user_id", documents=False)

        if share == "on":
            if message.author.id == user_id:
                if message.content.startswith(prefix + "prefix"):
                    try:
                        await message.delete()
                    except BaseException:
                        pass
                    try:
                        await message.channel.send("You are prohibited from using that command")
                    except BaseException:
                        pass
                elif message.content.startswith(prefix + "darkmode"):
                    try:
                        await message.delete()
                    except BaseException:
                        pass
                    try:
                        await message.channel.send("You are prohibited from using that command")
                    except BaseException:
                        pass
                elif message.content.startswith(prefix + "lightmode"):
                    try:
                        await message.delete()
                    except BaseException:
                        pass
                    try:
                        await message.channel.send("You are prohibited from using that command")
                    except BaseException:
                        pass
                elif message.content.startswith(prefix + "ip"):
                    try:
                        await message.delete()
                    except BaseException:
                        pass
                    try:
                        await message.channel.send("You are prohibited from using that command")
                    except BaseException:
                        pass
                elif message.content.startswith(prefix):
                    try:
                        await message.delete()
                    except BaseException:
                        pass
                    try:
                        await message.channel.send(message.content)
                    except BaseException:
                        pass
            else:
                pass

        # ///////////////////////////////////////////////////////////////
        # AFK System

        global afk_status
        global afk_user_id
        global afk_reset

        if afk_status == 1 and afk_user_id == 0:
            afkmessage = files.json(
                "data/config.json", "afk_message", documents=False
            )
            if afkmessage == "":
                afkmessage = "This is an autoresponse message! User is now AFK.."
            if message.guild is None and not isinstance(
                    message.channel, discord.GroupChannel
            ):
                if message.author == self.bot.user:
                    return

                if configs.mode() == 2:
                    sent = await message.channel.send(f"```ini\n[ AFK ]\n\n{afkmessage}\n\n[ {theme.footer()} ]```")
                else:
                    sent = await message.channel.send(f"**AFK**\n\n```\n{afkmessage}\n```\n\n{theme.footer()}")

                afk_user_id = message.author.id
                await asyncio.sleep(60)
                afk_user_id = 0
                await sent.delete()

        # ///////////////////////////////////////////////////////////////
        # Mention

        if f'<@{self.bot.user.id}>' in message.content or f'<@!{self.bot.user.id}>' in message.content.lower():
            if files.json(
                    "data/notifications/toasts.json",
                    "pings",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(
                    f"You have been mentioned\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}"
                )
            if files.json(
                    "data/webhooks/webhooks.json",
                    "pings",
                    documents=False
            ) == "on" and files.json(
                "data/webhooks/webhooks.json",
                "webhooks",
                documents=False
            ) == "on" and not webhook.pings_url() == "webhook-url-here":
                notify.webhook(
                    url=webhook.pings_url(),
                    name="pings",
                    description=f"You have been mentioned\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}"
                )
            if files.json(
                    "data/notifications/console.json",
                    "pings",
                    documents=False
            ) == "on":
                print()
                prints.sniper("You have been mentioned")
                prints.sniper(f"Server  | {message.guild}")
                prints.sniper(
                    f"Channel | {message.channel}"
                )
                prints.sniper(f"Author  | {message.author}")
                print()

        # ///////////////////////////////////////////////////////////////
        # Privnote Sniper

        if 'privnote.com' in message.content.lower():
            elapsed_snipe = '%.3fs' % (time.time() - sniped_start_time)
            privnote_sniper = files.json(
                f"data/snipers/privnote.json", "sniper", documents=False
            )
            if privnote_sniper == "on":
                code = re.search('privnote.com/(.*)', message.content).group(1)
                link = 'https://privnote.com/' + code
                try:
                    start_time = time.time()
                    note_text = pyPrivnote.read_note(link)
                    elapsed = '%.3fs' % (time.time() - start_time)
                    print()
                    prints.sniper('Privnote sniped')
                    prints.sniper(
                        f"Server  | {message.guild}"
                    )
                    prints.sniper(
                        f"Channel | {message.channel}"
                    )
                    prints.sniper(
                        f"Author  | {message.author}"
                    )
                    prints.sniper(f"Link    | {link}")
                    prints.sniper(f"Code    | {code}")
                    prints.sniper('Elapsed Times')
                    prints.sniper(
                        f"Sniped  | {elapsed_snipe}"
                    )
                    prints.sniper(
                        f"Read    | {elapsed}"
                    )
                    print()
                    file = open(

                        f"data/privnote/{code}.txt", 'wb'
                    )
                    file.write(str(note_text))
                    file.close()
                except Exception:
                    print()
                    prints.sniper('Privnote already sniped')
                    prints.sniper(
                        f"Server  | {message.guild}"
                    )
                    prints.sniper(
                        f"Channel | {message.channel}"
                    )
                    prints.sniper(
                        f"Author  | {message.author}"
                    )
                    prints.sniper(f"Link    | {link}")
                    prints.sniper(f"Code    | {code}")
                    prints.sniper('Elapsed Times')
                    prints.sniper(
                        f"Sniped  | {elapsed_snipe}"
                    )
                    print()
            else:
                return

        # ///////////////////////////////////////////////////////////////
        # Anti-Invite
        if 'discord.gg/' in message.content.lower() and anti_invite:
            guilds = files.json(
                "data/protections/config.json", "guilds", documents=False
            )
            if message.guild.id in guilds:
                try:
                    await message.delete()
                except BaseException:
                    pass
                try:
                    sent = await message.channel.send(
                        f"```ini\n[ Anti Invite ]\n\n\"Anti Invite\" is enabled, sending Discord invites is not allowed.\n\n[ {theme.footer()} ]```"
                    )
                    await asyncio.sleep(30)
                    await sent.delete()
                except BaseException:
                    pass

        # ///////////////////////////////////////////////////////////////
        # Anti-Upper
        if message.content.isupper() and anti_upper:
            guilds = files.json(
                "data/protections/config.json", "guilds", documents=False
            )
            if message.guild.id in guilds:
                try:
                    await message.delete()
                except BaseException:
                    pass
                try:
                    sent = await message.channel.send(
                        f"```ini\n[ Anti Upper ]\n\n\"Anti Upper\" is enabled, sending all uppercase is not allowed.\n\n[ {theme.footer()} ]```"
                    )
                    await asyncio.sleep(30)
                    await sent.delete()
                except BaseException:
                    pass

        # ///////////////////////////////////////////////////////////////
        # Anti-Phishing
        if message.content in phishing_list and anti_phishing:
            guilds = files.json(
                "data/protections/config.json", "guilds", documents=False
            )
            if message.guild.id in guilds:
                try:
                    await message.delete()
                except BaseException:
                    pass
                try:
                    sent = await message.channel.send(
                        f"```ini\n[ Anti Phishing Links ]\n\n\"Anti Phishing Links\" is enabled, the url you sent, is banned.\n\n[ {theme.footer()} ]```"
                    )
                    await asyncio.sleep(30)
                    await sent.delete()
                except BaseException:
                    pass
