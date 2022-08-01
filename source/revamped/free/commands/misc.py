from discord.ext import commands
from .utilities import *


class MiscCog(commands.Cog, name="Miscellaneous commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="uptime",
        usage="",
        description="Uptime"
    )
    async def uptime(self, luna):
        global hour
        global minute
        global second
        global day

        if day == 0:
            await message_builder(
                luna, title="Uptime",
                description=f"```\n{hour:02d} Hours, {minute:02d} Minutes and {second:02d} Seconds```"
            )
        else:
            await message_builder(
                luna, title="Uptime",
                description=f"```\n{day:02d} Days, {hour:02d} Hours, {minute:02d} Minutes and {second:02d} Seconds```"
            )

    @commands.command(
        name="about",
        usage="",
        description="Luna information"
    )
    async def about(self, luna):

        motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ')
        for line in motd:
            motd = line.decode().strip()
        command_count = len(self.bot.commands)
        cog = self.bot.get_cog('Custom commands')
        custom = cog.get_commands()
        custom_command_count = 0
        for _ in custom:
            custom_command_count += 1
        if beta:
            beta_info = f" Beta Build"
        else:
            beta_info = ""
        await message_builder(
            luna,
            description=f"```\nMOTD\n\n{motd}\n```"
                        f"```\nVersion\n\n{version}{beta_info}\n```"
                        f"```\nUptime\n\n{hour:02d} Hours, {minute:02d} Minutes and {second:02d} Seconds\n```"
                        f"```\nCommands\n\n{command_count - custom_command_count}\n```"
                        f"```\nCustom commands\n\n{custom_command_count}\n```"
                        f"```\nEnviroment\n\nDiscord.py » {discord.__version__}\n```"
                        f"```\nPublic server invite\n\nhttps://discord.gg/rnq876Kcd7\n```"
                        f"```\nCustomer only server invite\n\nhttps://discord.gg/3FGEaCnZST\n```"
                        f"```\nWebsite\n\nhttps://www.team-luna.org\n```"
        )

    @commands.command(
        name="logout",
        usage="",
        description="Logout of the bot"
    )
    async def logout(self, luna):

        prints.message(f"Logging out of the bot")
        await message_builder(luna, description=f"```\nLogging out of the bot```")
        files.remove('data/discord.luna', documents=False)
        restart_program()

    @commands.command(
        name="thelp",
        usage="",
        description="All commands in a text file"
    )
    async def thelp(self, luna):

        # ///////////////////////////////////////////////////////////////////
        try:
            helptext = ""

            cog = self.bot.get_cog('Help commands')
            helptext += "Help commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Profile commands')
            helptext += "\nProfile commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Animated statuses')
            helptext += "\nStatus commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Channel commands')
            helptext += "\nChannel commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Member commands')
            helptext += "\nMember commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Role commands')
            helptext += "\nRole commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Nickname commands')
            helptext += "\nNickname commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Invite commands')
            helptext += "\nInvite commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Administrative commands')
            helptext += "\nAdministrative commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Ignore commands')
            helptext += "\nIgnore commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Animated commands')
            helptext += "\nAnimated commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Dump commands')
            helptext += "\nDump commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Text commands')
            helptext += "\nText commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Codeblock commands')
            helptext += "\nCodeblock commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Image commands')
            helptext += "\nImage commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Troll commands')
            helptext += "\nTroll commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Fun commands')
            helptext += "\nFun commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Tools commands')
            helptext += "\nTools commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Nettool commands')
            helptext += "\nNettool commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Util commands')
            helptext += "\nUtil commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Spam commands')
            helptext += "\nSpam commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('All commands')
            helptext += "\nAll commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Mass commands')
            helptext += "\nMass commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Guild commands')
            helptext += "\nGuild commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Exploit commands')
            helptext += "\nExploit commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Abusive commands')
            helptext += "\nAbusive commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Raid commands')
            helptext += "\nRaid commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Nuking commands')
            helptext += "\nNuking commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Privacy commands')
            helptext += "\nPrivacy commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Protection Guild commands')
            helptext += "\nProtection Guild commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Protection commands')
            helptext += "\nProtection commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Backup commands')
            helptext += "\nBackup commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Whitelist commands')
            helptext += "\nWhitelist commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Settings commands')
            helptext += "\nSettings commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"
            cog = self.bot.get_cog('Share commands')
            helptext += "\nShare commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Encode commands')
            helptext += "\nEncode commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Decode commands')
            helptext += "\nDecode commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Giveaway settings')
            helptext += "\nGiveaway settings:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Cryptocurrency commands')
            helptext += "\nCryptocurrency commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Customization commands')
            helptext += "\nCustomization commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Hentai commands')
            helptext += "\nHentai commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Sniper settings')
            helptext += "\nSniper settings:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Theme commands')
            helptext += "\nTheme commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Toast customization')
            helptext += "\nToast customization:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Toast commands')
            helptext += "\nToast commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Webhook setup')
            helptext += "\nWebhook setup:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Webhook commands')
            helptext += "\nWebhook commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Webhook urls')
            helptext += "\nWebhook urls:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Webhook customisation')
            helptext += "\nWebhook customisation:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Miscellaneous commands')
            helptext += "\nMiscellaneous commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            cog = self.bot.get_cog('Game commands')
            helptext += "\nGame commands:\n"
            commands = cog.get_commands()
            for command in commands:
                helptext += f"{command.name + ' ' + command.usage:<17} » {command.description}\n"

            # ///////////////////////////////////////////////////////////////////

            commandcount = len(self.bot.commands)
            try:
                custom = cog.get_commands()
                custom_command_count = 0
                for _ in custom:
                    custom_command_count += 1
            except BaseException:
                custom_command_count = 0

            file = open("data/commands.txt", "w")
            file.write(f"{commandcount - custom_command_count} Commands\n\n<> is required | [] is optional\n\n{helptext}")
            file.close()
            await message_builder(luna, title="Text Help", description=f"```\nSaved all commands in Documents/data/commands.txt```")
        except Exception as e:
            await error_builder(luna, e)

    @commands.command(
        name="update",
        usage="",
        description="Updates Luna"
    )
    async def update(self, luna):

        r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
        version_url = r["version"]
        if developer_mode:
            await message_builder(
                luna, title="Update",
                description=f"```\nDeveloper mode active! No updates will be downloaded.```"
            )
        elif version == version_url:
            await message_builder(
                luna, title="Update",
                description=f"```\nYou are on the latest version! ({version_url})```"
            )
        else:
            if files.json(
                    "data/notifications/toasts.json",
                    "login",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(f"Starting update {version_url}")
            if files.json(
                    "data/webhooks/webhooks.json",
                    "login",
                    documents=False
            ) == "on" and files.json(
                "data/webhooks/webhooks.json",
                "webhooks",
                documents=False
            ) == "on" and not webhook.login_url() == "webhook-url-here":
                notify.webhook(
                    url=webhook.login_url(), name="login",
                    description=f"Starting update {version_url}"
                )
            await message_builder(luna, title="Update", description=f"```\nStarted update » {version_url}```")
            luna.update()

    @commands.command(
        name="restart",
        usage="",
        aliases=['reboot'],
        description="Restart Luna"
    )
    async def restart(self, luna):

        # if configs.mode() == 2:
        # 	sent = await luna.send(f"```ini\n[ Restarting ]\n\nAllow up to 5 seconds\n\n[ {theme.footer()} ]```")
        # 	await asyncio.sleep(3)
        # 	await sent.delete()
        # if configs.mode() == 3:
        # 	sent = await luna.send(f"> **Restarting**\n>n> Allow up to 5 seconds\n>n> {theme.footer()}")
        # 	await asyncio.sleep(3)
        # 	await sent.delete()
        # else:
        # 	embed = discord.Embed(title="Restarting", description=f"```\nAllow up to 5 seconds```")
        #
        # 	embed.set_footer(text=theme.footer())
        # 	embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
        #
        # 	sent = await send(luna, embed)
        # 	await asyncio.sleep(3)
        # 	await sent.delete()
        restart_program()

    @commands.command(
        name="shutdown",
        usage="",
        description="Shutdown Luna"
    )
    async def shutdown(self, luna):

        os._exit(0)

    @commands.command(
        name="panic",
        usage="",
        description="Quickly close Luna"
    )
    async def panic(self, luna):

        os._exit(0)

    @commands.command(
        name="clear",
        aliases=['cls'],
        usage="",
        description="Clear the console"
    )
    async def clear(self, ctx):

        luna.console(False, clear=True)
        if privacy:
            command_count = len(self.bot.commands)
            cog = self.bot.get_cog('Custom commands')
            try:
                custom = cog.get_commands()
                custom_command_count = 0
                for _ in custom:
                    custom_command_count += 1
            except BaseException:
                custom_command_count = 0
            print(motd.center(os.get_terminal_size().columns))
            if beta:
                print("Beta Build".center(os.get_terminal_size().columns))
            prefix = files.json("data/config.json", "prefix", documents=False)
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
                if themesvar == "default":
                    pass
                else:
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
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                )
        else:
            command_count = len(self.bot.commands)
            cog = self.bot.get_cog('Custom commands')
            try:
                custom = cog.get_commands()
                custom_command_count = 0
                for _ in custom:
                    custom_command_count += 1
            except BaseException:
                custom_command_count = 0
            print(motd.center(os.get_terminal_size().columns))
            if beta:
                print("Beta Build".center(os.get_terminal_size().columns))
            prefix = files.json("data/config.json", "prefix", documents=False)
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
                if themesvar == "default":
                    pass
                else:
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
                    f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
                )
        print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
        prints.message(
            f"{color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
        )

    @commands.command(
        name="covid",
        aliases=['corona'],
        usage="",
        description="Corona statistics"
    )
    async def covid(self, luna):

        request = requests.get(f'https://api.covid19api.com/summary')
        data = request.json()
        info = data['Global']
        totalconfirmed = info['TotalConfirmed']
        totalrecovered = info['TotalRecovered']
        totaldeaths = info['TotalDeaths']
        newconfirmed = info['NewConfirmed']
        newrecovered = info['NewRecovered']
        newdeaths = info['NewDeaths']
        date = info['Date']
        await message_builder(
            luna, title="Covid-19 Statistics",
            description=f"```Total Confirmed Cases\n{totalconfirmed}```"
                        f"```Total Deaths\n{totaldeaths}```"
                        f"```Total Recovered\n{totalrecovered}```"
                        f"```New Confirmed Cases\n{newconfirmed}```"
                        f"```New Deaths\n{newdeaths}```"
                        f"```New Recovered\n{newrecovered}```"
                        f"```Date\n{date}```"
        )

    typing = False

    @commands.command(
        name="typing",
        usage="<on/off>",
        description="Enable or disable typing"
    )
    async def typing(self, luna, mode: str):

        if mode == "on":
            await message_builder(luna, title="Typing", description=f"```\nTyping enabled```")
            typing = True
            while typing:
                async with luna.typing():
                    await asyncio.sleep(1)
                    if not typing:
                        break
        elif mode == "off":
            await message_builder(luna, title="Typing", description=f"```\nTyping disabled```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="hwid",
        usage="",
        description="Prints your hwid"
    )
    async def hwid(self, luna):

        hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
            '\\r\\n'
        )[1].strip('\\r').strip()
        prints.message(f"Your HWID » {hwid}")

    @commands.command(
        name="edited",
        usage="<message>",
        description="Add the \"edited\" tag to the message"
    )
    async def edited(self, luna, message: str):

        magic_char = '\u202b'
        headers = {'Authorization': user_token}
        message_ = f'{magic_char} {message} {magic_char}'
        res = requests.post(
            f'https://discord.com/api/{api_version}/channels/{luna.channel.id}/messages', headers=headers,
            json={'content': message_}
        )
        if res.status_code == 200:
            message_id = res.json()['id']
            requests.patch(
                f'https://discord.com/api/{api_version}/channels/{luna.channel.id}/messages/{message_id}',
                headers=headers, json={'content': ' ' + message_}
            )