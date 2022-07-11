from discord.ext import commands
from .utilities import *


class SettingsCog(commands.Cog, name="Settings commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="prefix",
        usage="<prefix>",
        description="Change the prefix"
    )
    async def prefix(self, ctx, newprefix):

        config.prefix(newprefix)
        self.bot.command_prefix = newprefix
        luna.console(False, clear=True)
        command_count = len(self.bot.commands)
        if privacy:
            cog = self.bot.get_cog('Custom commands')
            try:
                custom = cog.get_commands()
                custom_command_count = sum(1 for _ in custom)
            except BaseException:
                custom_command_count = 0
            print(motd.center(os.get_terminal_size().columns))
            if beta:
                print("Beta Build".center(os.get_terminal_size().columns))
            console_mode = files.json(
                "data/console/console.json", "mode", documents=False
            )
            if console_mode == "2":
                riskmode = files.json(
                    "data/config.json",
                    "risk_mode", documents=False
                )
                themesvar = files.json(
                    "data/config.json", "theme", documents=False
                )
                deletetimer = int(
                    files.json(
                        "data/config.json", "delete_timer", documents=False
                    )
                )
                startup_status = files.json(
                    "data/config.json", "startup_status", documents=False
                )
                nitro_sniper = files.json(
                    "data/snipers/nitro.json", "sniper", documents=False
                )
                giveawayjoiner = files.json(
                    "data/snipers/giveaway.json", "joiner", documents=False
                )
                if themesvar != "default":
                    themesvar = themesvar[:-5]
                ui_user = f" {color.print_gradient('User:')} {'Luna#0000':<26}"
                ui_guilds = f" {color.print_gradient('Guilds:')} {'0':<24}"
                ui_friends = f" {color.print_gradient('Friends:')} {'0':<23}"
                ui_prefix = f" {color.print_gradient('Prefix:')} {newprefix:<24}"
                ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                print()
                print(
                    f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                )
                print(f"               {ui_user}     {ui_prefix}")
                print(f"               {ui_guilds}     {ui_theme}")
                print(f"               {ui_friends}     {ui_nitro_sniper}")
                print(
                    f"               ════════════════════════════════      {ui_giveaway_sniper}"
                )
                print(
                    f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                )
                print(f"               {ui_commands}     {ui_deletetimer}")
                print(f"               {ui_commands_custom}     {ui_startup}")
                print(
                    f"               ════════════════════════════════      ════════════════════════════════\n"
                )
            else:
                print()
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                )
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} Luna#0000 | {color.print_gradient('0')} Guilds | {color.print_gradient('0')} Friends"
                )
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {newprefix}\n"
                )
        else:
            cog = self.bot.get_cog('Custom commands')
            try:
                custom = cog.get_commands()
                custom_command_count = sum(1 for _ in custom)
            except BaseException:
                custom_command_count = 0
            print(motd.center(os.get_terminal_size().columns))
            if beta:
                print("Beta Build".center(os.get_terminal_size().columns))
            console_mode = files.json(
                "data/console/console.json", "mode", documents=False
            )
            if console_mode == "2":
                riskmode = files.json(
                    "data/config.json",
                    "risk_mode", documents=False
                )
                themesvar = files.json(
                    "data/config.json", "theme", documents=False
                )
                deletetimer = int(
                    files.json(
                        "data/config.json", "delete_timer", documents=False
                    )
                )
                startup_status = files.json(
                    "data/config.json", "startup_status", documents=False
                )
                nitro_sniper = files.json(
                    "data/snipers/nitro.json", "sniper", documents=False
                )
                giveawayjoiner = files.json(
                    "data/snipers/giveaway.json", "joiner", documents=False
                )
                if themesvar != "default":
                    themesvar = themesvar[:-5]
                bot_user = f"{self.bot.user}"
                ui_user = f" {color.print_gradient('User:')} {bot_user:<26}"
                ui_guilds = f" {color.print_gradient('Guilds:')} {len(self.bot.guilds):<24}"
                ui_friends = f" {color.print_gradient('Friends:')} {len(self.bot.user.friends):<23}"
                ui_prefix = f" {color.print_gradient('Prefix:')} {newprefix:<24}"
                ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                print()
                print(
                    f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                )
                print(f"               {ui_user}     {ui_prefix}")
                print(f"               {ui_guilds}     {ui_theme}")
                print(f"               {ui_friends}     {ui_nitro_sniper}")
                print(
                    f"               ════════════════════════════════      {ui_giveaway_sniper}"
                )
                print(
                    f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                )
                print(f"               {ui_commands}     {ui_deletetimer}")
                print(f"               {ui_commands_custom}     {ui_startup}")
                print(
                    f"               ════════════════════════════════      ════════════════════════════════\n"
                )
            else:
                print()
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                )
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} "
                    f"{self.bot.user} | "
                    f"{color.print_gradient(f'{len(self.bot.guilds)}')} Guilds | "
                    f"{color.print_gradient(f'{len(self.bot.user.friends)}')} Friends"
                )
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {newprefix}\n"
                )
        print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
        prints.message(
            f"{color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
        )
        prints.message(f"Prefix changed to {color.print_gradient(f'{newprefix}')}")
        await message_builder(ctx, description=f"```\nPrefix changed to {newprefix}```")

    @commands.command(
        name="themes",
        usage="",
        description="Themes"
    )
    async def themes(self, luna):

        path_to_json = 'data/themes/'
        json_files = [pos_json for pos_json in os.listdir(
            path_to_json
        ) if pos_json.endswith('.json')]
        prefix = files.json("data/config.json", "prefix", documents=False)
        themesvar = files.json("data/config.json", "theme", documents=False)
        if themesvar != "default":
            themesvar = (themesvar[:-5])

        string = f"{json_files}"
        stringedit = string.replace(
            ',',
            f"\n{prefix}theme"
        ).replace(
            "'",
            ""
        ).replace(
            '[',
            f"{prefix}theme "
        ).replace(
            ']',
            ""
        ).replace(
            '.json',
            ""
        )

        cog = self.bot.get_cog('Theme commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(
            luna, title="Themes",
            description=f"{theme.description()}"
                        f"```\nCurrent theme     » {themesvar}\n```"
                        f"```\nTheme customization\n\n"
                        f"{prefix}customize        » Theme customization\n```"
                        f"```\nTheme control\n\n"
                        f"{helptext}\n```"
                        f"```\nAvailable themes\n\n"
                        f"{prefix}theme default\n{stringedit}```"
        )

    @commands.command(
        name="customize",
        usage="",
        aliases=['customise', 'customization', 'customisation'],
        description="Theme customization"
    )
    async def customize(self, luna):

        themevar = files.json("data/config.json", "theme", documents=False)
        prefix = files.json("data/config.json", "prefix", documents=False)
        title = theme.title()
        footer = theme.footer()

        if themevar != "default":
            themevar = (themevar[:-5])
        if themevar == "default":
            theme_description = descriptionvar_request
            theme_description = "off" if theme_description != "true" else "on"
        else:
            theme_json = files.json(
                "data/config.json", "theme", documents=False
            )
            theme_description = files.json(
                f"data/themes/{theme_json}", "description", documents=False
            )
            if theme_description is None:
                theme_description = True
            theme_description = "on" if theme_description else "off"
        if title == "":
            title = "None"
        if footer == "":
            footer = "None"

        cog = self.bot.get_cog('Customization commands')
        commands = cog.get_commands()
        helptext1 = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Webhook customisation')
        commands = cog.get_commands()
        helptext2 = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Toast customization')
        commands = cog.get_commands()
        helptext3 = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(
            luna, title="Customization",
            description=f"{theme.description()}"
                        f"```\nYour current theme settings\n\n"
                        f"Theme             » {themevar}\n"
                        f"Title             » {title}\n"
                        f"Footer            » {footer}\n"
                        f"Description       » {theme_description}\n```"
                        f"```\nSelfbot theme settings\n\n"
                        f"{helptext1}\n```"
                        f"```\nWebhook theme settings\n\n"
                        f"{helptext2}\n```"
                        f"```\nToast theme settings\n\n{helptext3}\n```"
                        f"```\nNote\n\nIf you want to remove a customization,\n"
                        f"You can use \"None\" to remove it.\n```"
        )

    @commands.command(
        name="webhook",
        usage="[2]",
        description="Webhook settings"
    )
    async def webhook(self, luna, page: str = "1"):

        prefix = files.json("data/config.json", "prefix", documents=False)
        webhooks = files.json(
            "data/webhooks/webhooks.json",
            "webhooks", documents=False
        )
        login = files.json(
            "data/webhooks/webhooks.json",
            "login", documents=False
        )
        nitro = files.json(
            "data/webhooks/webhooks.json",
            "nitro", documents=False
        )
        giveaway = files.json(
            "data/webhooks/webhooks.json",
            "giveaway", documents=False
        )
        privnote = files.json(
            "data/webhooks/webhooks.json",
            "privnote", documents=False
        )
        selfbot = files.json(
            "data/webhooks/webhooks.json",
            "selfbot", documents=False
        )
        pings = files.json(
            "data/webhooks/webhooks.json",
            "pings", documents=False
        )
        ghostpings = files.json(
            "data/webhooks/webhooks.json", "ghostpings", documents=False
        )
        friendevents = files.json(
            "data/webhooks/webhooks.json", "friendevents", documents=False
        )
        guildevents = files.json(
            "data/webhooks/webhooks.json", "guildevents", documents=False
        )
        roleupdates = files.json(
            "data/webhooks/webhooks.json", "roleupdates", documents=False
        )
        nickupdates = files.json(
            "data/webhooks/webhooks.json", "nickupdates", documents=False
        )
        protection = files.json(
            "data/webhooks/webhooks.json", "protection", documents=False
        )
        cog = self.bot.get_cog('Webhook setup')
        commands = cog.get_commands()
        setuptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Webhook commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Webhook urls')
        commands = cog.get_commands()
        urltext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        if page == "2":
            await message_builder(
                luna, title="Webhooks",
                description=f"{theme.description()}```\nWebhook url's\n\n{urltext}```"
            )
        else:
            await message_builder(
                luna, title="Webhooks",
                description=f"{theme.description()}"
                            f"```\nWebhook configuration\n\n"
                            f"Webhooks          » {webhooks}\n"
                            f"Login webhooks    » {login}\n"
                            f"Nitro webhooks    » {nitro}\n"
                            f"Giveaway webhooks » {giveaway}\n"
                            f"Privnote webhooks » {privnote}\n"
                            f"Selfbot webhooks  » {selfbot}\n"
                            f"Ping webhooks     » {pings}\n"
                            f"Ghostping webhooks » {ghostpings}\n"
                            f"Friendevent webhooks » {friendevents}\n"
                            f"Guildevent webhooks » {guildevents}\n"
                            f"Roleupdate webhooks » {roleupdates}\n"
                            f"Nickname webhooks » {nickupdates}\n"
                            f"Protection webhooks » {protection}\n```"
                            f"```\nWebhook setup\n\n{setuptext}\n```"
                            f"```\nWebhook control\n\n{helptext}\n```"
                            f"```\nNote\n\n{prefix}webhook 2 » Page 2```"
            )

    @commands.command(
        name="notifications",
        usage="",
        description="Toast notifications"
    )
    async def notifications(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        toasts = files.json(
            "data/notifications/toasts.json",
            "toasts", documents=False
        )
        login = files.json(
            "data/notifications/toasts.json",
            "login", documents=False
        )
        nitro = files.json(
            "data/notifications/toasts.json",
            "nitro", documents=False
        )
        giveaway = files.json(
            "data/notifications/toasts.json", "giveaway", documents=False
        )
        privnote = files.json(
            "data/notifications/toasts.json", "privnote", documents=False
        )
        selfbot = files.json(
            "data/notifications/toasts.json", "selfbot", documents=False
        )
        pings = files.json(
            "data/notifications/toasts.json",
            "pings", documents=False
        )
        ghostpings = files.json(
            "data/notifications/toasts.json", "ghostpings", documents=False
        )
        friendevents = files.json(
            "data/notifications/toasts.json", "friendevents", documents=False
        )
        guildevents = files.json(
            "data/notifications/toasts.json", "guildevents", documents=False
        )
        roleupdates = files.json(
            "data/notifications/toasts.json", "roleupdates", documents=False
        )
        nickupdates = files.json(
            "data/notifications/toasts.json", "nickupdates", documents=False
        )
        protection = files.json(
            "data/notifications/toasts.json", "protection", documents=False
        )
        cog = self.bot.get_cog('Toast commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(
            luna, title="Toast notifications",
            description=f"{theme.description()}"
                        f"```\nToast configuration\n\n"
                        f"Toasts            » {toasts}\n"
                        f"Login toasts      » {login}\n"
                        f"Nitro toasts      » {nitro}\n"
                        f"Giveaway toasts   » {giveaway}\n"
                        f"Privnote toasts   » {privnote}\n"
                        f"Selfbot toasts    » {selfbot}\n"
                        f"Ping toasts       » {pings}\n"
                        f"Ghostping toasts  » {ghostpings}\n"
                        f"Friendevent toast » {friendevents}\n"
                        f"Guildevent toasts » {guildevents}\n"
                        f"Roleupdate toasts » {roleupdates}\n"
                        f"Nickname toasts   » {nickupdates}\n"
                        f"Protection toasts » {protection}\n```"
                        f"```\nToast control\n\n{helptext}```"
        )

    # @commands.command(name = "embedmode",
    # 				usage="",
    # 				description = "Switch to embed mode")
    # async def embedmode(self, luna):
    #
    # 	config.mode("1")
    # 	prints.message(f"Switched to {color.print_gradient('embed')} mode")
    # await message_builder(luna, title="Embed mode",
    # description=f"```\nSwitched to embed mode.```")

    @commands.command(
        name="indentmode",
        usage="",
        description="Switch to indent mode"
    )
    async def indentmode(self, luna):

        config.mode("1")
        prints.message(f"Switched to {color.print_gradient('indent')} mode")
        await message_builder(luna, title="Indent mode", description=f"```\nSwitched to indent mode.```")

    @commands.command(
        name="textmode",
        usage="",
        description="Switch to text mode"
    )
    async def textmode(self, luna):

        config.mode("2")
        prints.message(f"Switched to {color.print_gradient('text')} mode")
        await message_builder(luna, title="Text mode", description="```Switched to text mode.```")

    @commands.command(
        name="sniper",
        usage="",
        description="Sniper settings"
    )
    async def sniper(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        nitro_sniper = files.json(
            "data/snipers/nitro.json", "sniper", documents=False
        )
        privnote_sniper = files.json(
            "data/snipers/privnote.json", "sniper", documents=False
        )
        cog = self.bot.get_cog('Sniper settings')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(
            luna, title="Sniper settings",
            description=f"{theme.description()}```\nYour current settings\n\nNitro Sniper      » {nitro_sniper}\nPrivnote Sniper   » {privnote_sniper}\n``````\nSettings\n\n{helptext}```"
        )

    @commands.command(
        name="giveaway",
        usage="",
        description="Giveaway settings"
    )
    async def giveaway(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        giveaway_joiner = files.json(
            "data/snipers/giveaway.json", "joiner", documents=False
        )
        delay_in_minutes = files.json(
            "data/snipers/giveaway.json", "delay_in_minutes", documents=False
        )
        guild_joiner = files.json(
            "data/snipers/giveaway.json", "guild_joiner", documents=False
        )

        cog = self.bot.get_cog('Giveaway settings')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(
            luna, title="Giveaway settings",
            description=f"{theme.description()}"
                        f"```\nYour current settings\n\n"
                        f"Giveaway Joiner   » {giveaway_joiner}\n"
                        f"Delay             » {delay_in_minutes} minute/s\n"
                        f"Server Joiner     » {guild_joiner}\n```"
                        f"```\nSettings\n\n{helptext}```"
        )

    @commands.command(
        name="errorlog",
        usage="<console/message>",
        description="Switch errorlog"
    )
    async def errorlog(self, luna, mode: str):

        if mode in {"message", "console"}:
            prints.message(f"Error logging » {color.print_gradient(f'{mode}')}")
            config.error_log(mode)
            await message_builder(luna, description=f"```\nError logging » {mode}```")
        else:
            await mode_error(luna, "message or console")

    @commands.command(
        name="deletetimer",
        usage="<seconds>",
        description="Auto delete timer"
    )
    async def deletetimer(self, luna, seconds: int):

        await message_builder(luna, description=f"```\nAuto delete timer » {seconds} seconds```")
        prints.message(
            f"Auto delete timer » {color.print_gradient(f'{seconds} seconds')}"
        )
        config.delete_timer(f"{seconds}")

    @commands.command(
        name="afkmessage",
        usage="<text>",
        description="Change the afk message"
    )
    async def afkmessage(self, luna, *, afkmessage):

        await message_builder(luna, description=f"```\nAFK message » {afkmessage}```")
        prints.message(f"AFK message » {color.print_gradient(f'{afkmessage}')}")
        config.afk_message(f"{afkmessage}")

    @commands.command(
        name="riskmode",
        usage="<on/off>",
        description="Enable abusive commands"
    )
    async def riskmode(self, luna, mode: str):

        if mode in {"on", "off"}:
            prints.message(f"Riskmode » {color.print_gradient(f'{mode}')}")
            config.risk_mode(mode)
            await message_builder(luna, description=f"```\nRiskmode » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="selfbotdetection",
        usage="<on/off>",
        description="Sb detection"
    )
    async def selfbotdetection(self, luna, mode: str):

        if mode in {"on", "off"}:
            prints.message(f"Selfbot detection » {color.print_gradient(f'{mode}')}")
            config.selfbot.sniper(mode)
            await message_builder(luna, description=f"```\nSelfbot detection » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="mention",
        usage="<on/off>",
        description="Mention notification"
    )
    async def mention(self, luna, mode: str):

        if mode in {"on", "off"}:
            prints.message(f"Mention notification » {color.print_gradient(f'{mode}')}")
            config.toast.pings(mode)
            await message_builder(luna, description=f"```\nMention notification » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="password",
        usage="<new_password>",
        description="Change password"
    )
    async def password(self, luna, password: str):

        config.password(f"{password}")
        await message_builder(luna, description=f"```\nChanged password to » {password}```")
        prints.message(f"Changed password to » {color.print_gradient(f'{password}')}")

    @commands.command(
        name="console",
        usage="<1/2>",
        description="Change console mode"
    )
    async def console(self, ctx, mode: str):

        if mode in {"1", "2"}:
            config._global("data/console/console.json", "mode", mode)
            prints.message(f"Console mode » {color.print_gradient(f'{mode}')}")
            await message_builder(ctx, description=f"```\nConsole mode » {mode}```")
            luna.console(False, clear=True)
            command_count = len(self.bot.commands)
            if privacy:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    ui_user = f" {color.print_gradient('User:')} {'Luna#0000':<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {'0':<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {'0':<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} Luna#0000 | {color.print_gradient('0')} Guilds | {color.print_gradient('0')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            else:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    bot_user = f"{self.bot.user}"
                    ui_user = f" {color.print_gradient('User:')} {bot_user:<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {len(self.bot.guilds):<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {len(self.bot.user.friends):<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} "
                        f"{self.bot.user} | "
                        f"{color.print_gradient(f'{len(self.bot.guilds)}')} Guilds | "
                        f"{color.print_gradient(f'{len(self.bot.user.friends)}')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            print(
                f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n"
            )
            prints.message(
                f"{color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
            )
        else:
            await mode_error(ctx, "1 or 2")

    @commands.command(
        name="lgradient",
        usage="<1-7>",
        description="Change logo gradient",
    )
    async def lgradient(self, ctx, mode: str):

        if mode in {"1", "2", "3", "4", "5", "6", "7"}:
            config._global("data/console/console.json", "logo_gradient", mode)
            prints.message(f"Logo gradient » {color.print_gradient(f'{mode}')}")
            await message_builder(ctx, description=f"```\nLogo gradient » {mode}```")
            luna.console(False, clear=True)
            command_count = len(self.bot.commands)
            if privacy:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    ui_user = f" {color.print_gradient('User:')} {'Luna#0000':<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {'0':<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {'0':<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} Luna#0000 | {color.print_gradient('0')} Guilds | {color.print_gradient('0')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            else:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    bot_user = f"{self.bot.user}"
                    ui_user = f" {color.print_gradient('User:')} {bot_user:<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {len(self.bot.guilds):<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {len(self.bot.user.friends):<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} "
                        f"{self.bot.user} | "
                        f"{color.print_gradient(f'{len(self.bot.guilds)}')} Guilds | "
                        f"{color.print_gradient(f'{len(self.bot.user.friends)}')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            print(
                f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n"
            )
            prints.message(
                f"{color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
            )
        else:
            await mode_error(ctx, "1-7")

    @commands.command(
        name="pgradient",
        usage="<1-7>",
        description="Change print gradient",
    )
    async def pgradient(self, ctx, mode: str):

        if mode in {"1", "2", "3", "4", "5", "6", "7"}:
            config._global("data/console/console.json", "print_gradient", mode)
            prints.message(f"Print gradient » {color.print_gradient(f'{mode}')}")
            await message_builder(ctx, description=f"```\nPrint gradient » {mode}```")
            luna.console(False, clear=True)
            command_count = len(self.bot.commands)
            if privacy:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    ui_user = f" {color.print_gradient('User:')} {'Luna#0000':<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {'0':<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {'0':<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} Luna#0000 | {color.print_gradient('0')} Guilds | {color.print_gradient('0')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            else:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    bot_user = f"{self.bot.user}"
                    ui_user = f" {color.print_gradient('User:')} {bot_user:<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {len(self.bot.guilds):<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {len(self.bot.user.friends):<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} "
                        f"{self.bot.user} | "
                        f"{color.print_gradient(f'{len(self.bot.guilds)}')} Guilds | "
                        f"{color.print_gradient(f'{len(self.bot.user.friends)}')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            print(
                f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n"
            )
            prints.message(
                f"{color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
            )
        else:
            await mode_error(ctx, "1-7")

    @commands.command(
        name="spacer",
        usage="<spacer>",
        description="Change print spacer",
    )
    async def spacer(self, ctx, mode: str):

        config._global("data/console/console.json", "spacer", mode)
        prints.message(f"Print spacer » {color.print_gradient(f'{mode}')}")
        await message_builder(ctx, description=f"```\nPrint spacer » {mode}```")
        luna.console(False, clear=True)
        command_count = len(self.bot.commands)
        if privacy:
            cog = self.bot.get_cog('Custom commands')
            try:
                custom = cog.get_commands()
                custom_command_count = sum(1 for _ in custom)
            except BaseException:
                custom_command_count = 0
            print(motd.center(os.get_terminal_size().columns))
            if beta:
                print("Beta Build".center(os.get_terminal_size().columns))
            prefix = files.json(
                "data/config.json",
                "prefix", documents=False
            )
            console_mode = files.json(
                "data/console/console.json", "mode", documents=False
            )
            if console_mode == "2":
                riskmode = files.json(
                    "data/config.json", "risk_mode", documents=False
                )
                themesvar = files.json(
                    "data/config.json", "theme", documents=False
                )
                deletetimer = int(
                    files.json(
                        "data/config.json", "delete_timer", documents=False
                    )
                )
                startup_status = files.json(
                    "data/config.json", "startup_status", documents=False
                )
                nitro_sniper = files.json(
                    "data/snipers/nitro.json", "sniper", documents=False
                )
                giveawayjoiner = files.json(
                    "data/snipers/giveaway.json", "joiner", documents=False
                )
                if themesvar != "default":
                    themesvar = themesvar[:-5]
                ui_user = f" {color.print_gradient('User:')} {'Luna#0000':<26}"
                ui_guilds = f" {color.print_gradient('Guilds:')} {'0':<24}"
                ui_friends = f" {color.print_gradient('Friends:')} {'0':<23}"
                ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                print()
                print(
                    f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                )
                print(f"               {ui_user}     {ui_prefix}")
                print(f"               {ui_guilds}     {ui_theme}")
                print(f"               {ui_friends}     {ui_nitro_sniper}")
                print(
                    f"               ════════════════════════════════      {ui_giveaway_sniper}"
                )
                print(
                    f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                )
                print(f"               {ui_commands}     {ui_deletetimer}")
                print(
                    f"               {ui_commands_custom}     {ui_startup}"
                )
                print(
                    f"               ════════════════════════════════      ════════════════════════════════\n"
                )
            else:
                print()
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                )
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} Luna#0000 | {color.print_gradient('0')} Guilds | {color.print_gradient('0')} Friends"
                )
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                )
        else:
            cog = self.bot.get_cog('Custom commands')
            try:
                custom = cog.get_commands()
                custom_command_count = sum(1 for _ in custom)
            except BaseException:
                custom_command_count = 0
            print(motd.center(os.get_terminal_size().columns))
            if beta:
                print("Beta Build".center(os.get_terminal_size().columns))
            prefix = files.json(
                "data/config.json",
                "prefix", documents=False
            )
            console_mode = files.json(
                "data/console/console.json", "mode", documents=False
            )
            if console_mode == "2":
                riskmode = files.json(
                    "data/config.json", "risk_mode", documents=False
                )
                themesvar = files.json(
                    "data/config.json", "theme", documents=False
                )
                deletetimer = int(
                    files.json(
                        "data/config.json", "delete_timer", documents=False
                    )
                )
                startup_status = files.json(
                    "data/config.json", "startup_status", documents=False
                )
                nitro_sniper = files.json(
                    "data/snipers/nitro.json", "sniper", documents=False
                )
                giveawayjoiner = files.json(
                    "data/snipers/giveaway.json", "joiner", documents=False
                )
                if themesvar != "default":
                    themesvar = themesvar[:-5]
                bot_user = f"{self.bot.user}"
                ui_user = f" {color.print_gradient('User:')} {bot_user:<26}"
                ui_guilds = f" {color.print_gradient('Guilds:')} {len(self.bot.guilds):<24}"
                ui_friends = f" {color.print_gradient('Friends:')} {len(self.bot.user.friends):<23}"
                ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                print()
                print(
                    f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                )
                print(f"               {ui_user}     {ui_prefix}")
                print(f"               {ui_guilds}     {ui_theme}")
                print(f"               {ui_friends}     {ui_nitro_sniper}")
                print(
                    f"               ════════════════════════════════      {ui_giveaway_sniper}"
                )
                print(
                    f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                )
                print(f"               {ui_commands}     {ui_deletetimer}")
                print(
                    f"               {ui_commands_custom}     {ui_startup}"
                )
                print(
                    f"               ════════════════════════════════      ════════════════════════════════\n"
                )
            else:
                print()
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                )
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} "
                    f"{self.bot.user} | "
                    f"{color.print_gradient(f'{len(self.bot.guilds)}')} Guilds | "
                    f"{color.print_gradient(f'{len(self.bot.user.friends)}')} Friends"
                )
                print(
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                )
        print(
            f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n"
        )
        prints.message(
            f"{color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
        )

    @commands.command(
        name="spacers",
        usage="<on/off>",
        description="Print spacers on/off",
    )
    async def spacers(self, ctx, mode: str):

        if mode in {"on", "off"}:
            if mode == "off":
                config._global("data/console/console.json", "spacers", False)
            else:
                config._global("data/console/console.json", "spacers", True)
            prints.message(f"Print spacers » {color.print_gradient(f'{mode}')}")
            await message_builder(ctx, description=f"```\nPrint spacers » {mode}```")
            luna.console(False, clear=True)
            command_count = len(self.bot.commands)
            if privacy:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    ui_user = f" {color.print_gradient('User:')} {'Luna#0000':<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {'0':<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {'0':<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} Luna#0000 | {color.print_gradient('0')} Guilds | {color.print_gradient('0')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            else:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    bot_user = f"{self.bot.user}"
                    ui_user = f" {color.print_gradient('User:')} {bot_user:<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {len(self.bot.guilds):<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {len(self.bot.user.friends):<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} "
                        f"{self.bot.user} | "
                        f"{color.print_gradient(f'{len(self.bot.guilds)}')} Guilds | "
                        f"{color.print_gradient(f'{len(self.bot.user.friends)}')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            print(
                f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n"
            )
            prints.message(
                f"{color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
            )
        else:
            await mode_error(ctx, "on or off")

    @commands.command(
        name="timestamp",
        usage="<on/off>",
        description="Print timestamp on/off",
    )
    async def timestamp(self, ctx, mode: str):

        if mode in {"on", "off"}:
            if mode == "off":
                config._global("data/console/console.json", "timestamp", False)
            else:
                config._global("data/console/console.json", "timestamp", True)
            prints.message(f"Print timestamp » {color.print_gradient(f'{mode}')}")
            await message_builder(ctx, description=f"```\nPrint timestamp » {mode}```")
            luna.console(False, clear=True)
            command_count = len(self.bot.commands)
            if privacy:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    ui_user = f" {color.print_gradient('User:')} {'Luna#0000':<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {'0':<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {'0':<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} Luna#0000 | {color.print_gradient('0')} Guilds | {color.print_gradient('0')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            else:
                cog = self.bot.get_cog('Custom commands')
                try:
                    custom = cog.get_commands()
                    custom_command_count = sum(1 for _ in custom)
                except BaseException:
                    custom_command_count = 0
                print(motd.center(os.get_terminal_size().columns))
                if beta:
                    print("Beta Build".center(os.get_terminal_size().columns))
                prefix = files.json(
                    "data/config.json",
                    "prefix", documents=False
                )
                console_mode = files.json(
                    "data/console/console.json", "mode", documents=False
                )
                if console_mode == "2":
                    riskmode = files.json(
                        "data/config.json", "risk_mode", documents=False
                    )
                    themesvar = files.json(
                        "data/config.json", "theme", documents=False
                    )
                    deletetimer = int(
                        files.json(
                            "data/config.json", "delete_timer", documents=False
                        )
                    )
                    startup_status = files.json(
                        "data/config.json", "startup_status", documents=False
                    )
                    nitro_sniper = files.json(
                        "data/snipers/nitro.json", "sniper", documents=False
                    )
                    giveawayjoiner = files.json(
                        "data/snipers/giveaway.json", "joiner", documents=False
                    )
                    if themesvar != "default":
                        themesvar = themesvar[:-5]
                    bot_user = f"{self.bot.user}"
                    ui_user = f" {color.print_gradient('User:')} {bot_user:<26}"
                    ui_guilds = f" {color.print_gradient('Guilds:')} {len(self.bot.guilds):<24}"
                    ui_friends = f" {color.print_gradient('Friends:')} {len(self.bot.user.friends):<23}"
                    ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
                    ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
                    ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
                    ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
                    ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
                    ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
                    ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
                    ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
                    ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
                    print()
                    print(
                        f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
                    )
                    print(f"               {ui_user}     {ui_prefix}")
                    print(f"               {ui_guilds}     {ui_theme}")
                    print(f"               {ui_friends}     {ui_nitro_sniper}")
                    print(
                        f"               ════════════════════════════════      {ui_giveaway_sniper}"
                    )
                    print(
                        f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
                    )
                    print(f"               {ui_commands}     {ui_deletetimer}")
                    print(
                        f"               {ui_commands_custom}     {ui_startup}"
                    )
                    print(
                        f"               ════════════════════════════════      ════════════════════════════════\n"
                    )
                else:
                    print()
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} "
                        f"{self.bot.user} | "
                        f"{color.print_gradient(f'{len(self.bot.guilds)}')} Guilds | "
                        f"{color.print_gradient(f'{len(self.bot.user.friends)}')} Friends"
                    )
                    print(
                        f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                    )
            print(
                f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n"
            )
            prints.message(
                f"{color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
            )
        else:
            await mode_error(ctx, "on or off")

    # @commands.command(
    #     name="reload",
    #     usage="",
    #     description="Reload custom commands"
    # )
    # async def reload(self, ctx):
    #
    #     path = getattr(sys, '_MEIPASS', os.getcwd())
    #     cogs_path = path + "\\cogs"
    #     luna.loader_check()
    #     for filename in os.listdir(cogs_path):
    #         if filename.endswith(".py"):
    #             try:
    #                 self.bot.reload_extension(f"cogs.{filename[:-3]}")
    #             except BaseException:
    #                 self.bot.load_extension(f"cogs.{filename[:-3]}")
    #     prints.message(f"Reloaded custom commands")
    #     await message_builder(ctx, description=f"```\nReloaded custom commands```")
    #     # prefix = files.json("data/config.json", "prefix", documents=False)
    #     # await message_builder(ctx, description=f"```\nReload has been disabled until further notice, use {prefix}restart instead```")

    @commands.command(
        name="newcmd",
        usage="<name>",
        description="Create new command"
    )
    async def newcmd(self, ctx, name: str):

        content = f"""
@commands.command(
    name = "{name}",
    usage="",
    description = "New command"
    )
async def {name}(self, luna):

    await luna.send("Documentation for custom commands can be found here: https://www.team-luna.org/documentation")
"""
        files.write_file(f"data/scripts/{name}.py", content, documents=False, append=True)
        await message_builder(ctx, description=f"```\nCreated new custom command in \"Documents/data/scripts/{name}.py\"```")

    @commands.command(
        name="darkmode",
        usage="",
        description="Discord darkmode"
    )
    async def darkmode(self, luna):

        requests.patch(
            f'https://discord.com/api/{api_version}/users/@me/settings',
            json={
                'theme': "dark"
            },
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description=f"```\nChanged to darkmode```")

    @commands.command(
        name="lightmode",
        usage="",
        description="Discord lightmode"
    )
    async def lightmode(self, luna):

        requests.patch(
            f'https://discord.com/api/{api_version}/users/@me/settings',
            json={
                'theme': "light"
            },
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description=f"```\nChanged to lightmode```")