import asyncio

from discord.ext import commands

from .utilities import *


class HelpCog(commands.Cog, name="Help commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name='help',
        usage="[command]",
        description="Display the help message",
        aliases=['h', '?']
    )
    async def help(self, luna, commandName: str = None):
        prefix = files.json("data/config.json", "prefix", documents=False)

        command_name2 = None
        stop = False

        if commandName is None:
            command_count = len(self.bot.commands)
            cog = self.bot.get_cog('Custom commands')
            custom = cog.get_commands()
            custom_command_count = sum(1 for _ in custom)
            await message_builder(
                luna,
                description=f"{theme.description()}```\n\
Luna\n\nCommands          » {command_count - custom_command_count}\n\
Custom Commands   » {custom_command_count}\n``````\n\
Categories\n\n\
{prefix}help [command]   » Display all commands\n\
{prefix}chelp            » Display custom commands\n\
{prefix}admin            » Administrative commands\n\
{prefix}abusive          » Abusive commands\n\
{prefix}animated         » Animated commands\n\
{prefix}dump             » Dumping\n\
{prefix}fun              » Funny commands\n\
{prefix}game             » Game commands\n\
{prefix}image            » Image commands\n\
{prefix}hentai           » Hentai explorer\n\
{prefix}profile          » Profile settings\n\
{prefix}protection       » Protections\n\
{prefix}text             » Text commands\n\
{prefix}trolling         » Troll commands\n\
{prefix}tools            » Tools\n\
{prefix}networking       » Networking\n\
{prefix}utility          » Utilities\n\
{prefix}settings         » Settings\n\
{prefix}sharing          » Share with somebody\n\
{prefix}themes           » Themes\n\
{prefix}misc             » Miscellaneous\n\
{prefix}repeat           » Repeat last used command\n\
{prefix}search <command> » Search for a command\n``````\n\
Version\n\n{version}```"
            )
        else:
            for i in self.bot.commands:
                if i.name == commandName.lower():
                    command_name2 = i
                    break
                else:
                    for j in i.aliases:
                        if j == commandName.lower():
                            command_name2 = i
                            stop = True
                            break
                        if stop is True:
                            break

            if command_name2 is None:
                if configs.error_log() == "console":
                    prints.error(
                        f"No command found with name or alias {color.print_gradient(commandName)}"
                    )
                else:
                    await error_builder(luna, f"```\nNo command found with name or alias {commandName}```")
            else:
                alias_list = ""
                if configs.mode() == 2:
                    aliases = command_name2.aliases
                    if len(aliases) > 0:
                        for alias in aliases:
                            alias_list += f"{alias}, "
                        alias_list = alias_list[:-2]
                        sent = await luna.send(
                            f"```ini\n[ {command_name2.name.title()} Command ]\n\n" f"{theme.description()}" f"Name\n{command_name2.name}\n\n" f"Aliases\n{alias_list}\n\n" f"Usage\nNone\n\n" f"Description\n{command_name2.description}\n\n" f"[ {theme.footer()} ]```"
                            ) if command_name2.usage is None else await luna.send(
                            f"```ini\n[ {command_name2.name.title()} Command ]\n\n" f"{theme.description()}" f"Name\n{command_name2.name}\n\n" f"Aliases\n{alias_list}\n\n" f"Usage\n{prefix}{command_name2.name} {command_name2.usage}\n\n" f"Description\n{command_name2.description}\n\n" f"[ {theme.footer()} ]```"
                            )

                    elif command_name2.usage is None:
                        sent = await luna.send(
                            f"```ini\n[ {command_name2.name.title()} Command ]\n\n"
                            f"{theme.description()}"
                            f"Name\n{command_name2.name}\n\n"
                            f"Aliases\nNone\n\n"
                            f"Usage\nNone\n\n"
                            f"Description\n{command_name2.description}\n\n"
                            f"[ {theme.footer()} ]```"
                        )
                    else:
                        sent = await luna.send(
                            f"```ini\n[ {command_name2.name.title()} Command ]\n\n"
                            f"{theme.description()}"
                            f"Name\n{command_name2.name}\n\n"
                            f"Aliases\nNone\n\n"
                            f"Usage\n{prefix}{command_name2.name} {command_name2.usage}\n\n"
                            f"Description\n{command_name2.description}\n\n"
                            f"[ {theme.footer()} ]```"
                        )
                else:
                    aliases = command_name2.aliases
                    if len(aliases) > 0:
                        for alias in aliases:
                            alias_list += f"{alias}, "
                        alias_list = alias_list[:-2]
                        sent = await luna.send(
                            f"> **{command_name2.name.title()} Command**\n>n> " f"```\n> Name\n> {command_name2.name}```" f"```\n> Aliases\n> {alias_list}```" f"```\n> Usage\n> None```" f"```\n> Description\n> {command_name2.description}```\n" f"> {theme.footer()}"
                            ) if command_name2.usage is None else await luna.send(
                            f"> **{command_name2.name.title()} Command**\n>n> " f"```\n> Name\n> {command_name2.name}```" f"```\n> Aliases\n> {alias_list}```" f"```\n> Usage\n> {prefix}{command_name2.name} {command_name2.usage}```" f"```\n> Description\n> {command_name2.description}```\n" f"> {theme.footer()}"
                            )

                    elif command_name2.usage is None:
                        sent = await luna.send(
                            f"> **{command_name2.name.title()} Command**\n>n> "
                            f"```\n> Name\n> {command_name2.name}```"
                            f"```\n> Aliases\n> None```"
                            f"```\n> Usage\n> None```"
                            f"```\n> Description\n> {command_name2.description}```\n"
                            f"> {theme.footer()}"
                        )
                    else:
                        sent = await luna.send(
                            f"> **{command_name2.name.title()} Command**\n>n> "
                            f"```\n> Name\n> {command_name2.name}```"
                            f"```\n> Aliases\n> None```"
                            f"```\n> Usage\n> {prefix}{command_name2.name} {command_name2.usage}```"
                            f"```\n> Description\n> {command_name2.description}```\n"
                            f"> {theme.footer()}"
                        )

                await asyncio.sleep(configs.delete_timer())
                await sent.delete()

    @commands.command(
        name="admin",
        usage="[2, 3]",
        description="Administrative commands"
    )
    async def admin(self, luna, page: str = "1"):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Administrative commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Channel commands')
        commands = cog.get_commands()
        channeltext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Member commands')
        commands = cog.get_commands()
        membertext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Nickname commands')
        commands = cog.get_commands()
        nicktext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Role commands')
        commands = cog.get_commands()
        roletext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Invite commands')
        commands = cog.get_commands()
        invitetext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Ignore commands')
        commands = cog.get_commands()
        ignoretext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        if page == "2":
            await message_builder(luna, title="Administrative", footer_extra="Page 2", description=f"{theme.description()}" f"```\nMember Control\n\n{membertext}```" f"```\nNickname Control\n\n{nicktext}```" f"```\nGuild Control\n\n{helptext}```" f"```\nNote\n\n{prefix}admin 3 » Page 3```")

        elif page == "3":
            await message_builder(luna, title="Administrative", footer_extra="Page 3", description=f"{theme.description()}" f"```\nInvite Control\n\n{invitetext}```" f"```\nIgnore Control\n\n{ignoretext}```")

        else:
            await message_builder(luna, title="Administrative", footer_extra="Page 1", description=f"{theme.description()}" f"```\nChannel Control\n\n{channeltext}```" f"```\nRole Control\n\n{roletext}```" f"```\nNote\n\n{prefix}admin 2 » Page 2```")

    @commands.command(
        name="profile",
        usage="",
        description="Profile settings"
    )
    async def profile(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Profile commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Animated statuses')
        commands = cog.get_commands()
        status_helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(
            luna, title="Profile",
            description=f"{theme.description()}"
                        f"```\nCurrent profile\n\n"
                        f"User              » {self.bot.user}\n"
                        f"Username          » {self.bot.user.name}\n"
                        f"Discriminator     » {self.bot.user.discriminator}\n```"
                        f"```\nNickname Control\n\n"
                        f"{prefix}nick <name>      » Change your nickname\n"
                        f"{prefix}invisiblenick    » Make your nickname invisible\n"
                        f"{prefix}junknick         » Pure junk nickname\n```"
                        f"```\nUser Control\n\n{helptext}```"
                        f"```\nStatus Control\n\n{status_helptext}```"
        )

    @commands.command(
        name="animated",
        usage="",
        description="Animated commands"
    )
    async def animated(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Animated commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Animated commands", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="dump",
        usage="",
        description="Dumping"
    )
    async def dump(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Dump commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Dumping", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="text",
        usage="",
        description="Text commands"
    )
    async def text(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Text commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Codeblock commands')
        commands = cog.get_commands()
        helptext1 = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Text commands", description=f"{theme.description()}```\nText\n\n{helptext}``````\nCodeblock\n\n{helptext1}```")

    @commands.command(
        name="game",
        usage="",
        description="Game commands"
    )
    async def game(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Game commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Game commands", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="image",
        usage="",
        description="Image commands"
    )
    async def image(self, luna, page: str = "1"):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Image commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Image commands 2')
        commands = cog.get_commands()
        helptext2 = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        if page == "2":
            await message_builder(luna, title="Image commands", footer_extra="Page 2", description=f"{theme.description()}```\n{helptext2}```")

        else:
            await message_builder(luna, title="Image commands", footer_extra="Page 1", description=f"{theme.description()}```\n{helptext}``````\nNote\n\n{prefix}image 2 » Page 2```")

    @commands.command(
        name="hentai",
        usage="",
        description="Hentai explorer"
    )
    async def hentai(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)

        cog = self.bot.get_cog('Hentai commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('HScroller commands')
        commands = cog.get_commands()
        helptext1 = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(
            luna, title="Hentai Explorer", description=f"{theme.description()}```\nHScroller\n\nHigh quality anime provided by ThatOneCodeDev\n\n{helptext1}``````\n{helptext}```"
        )

    @commands.command(
        name="trolling",
        usage="",
        description="Trolling"
    )
    async def trolling(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Troll commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Trolling", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="fun",
        usage="",
        description="Fun commands"
    )
    async def fun(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Fun commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Fun commands", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="tools",
        usage="",
        description="Tools"
    )
    async def tools(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Tools commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Tools", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="networking",
        usage="",
        description="Networking"
    )
    async def networking(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Nettool commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Networking", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="utility",
        usage="",
        aliases=['utils', 'utilities'],
        description="Utilities"
    )
    async def utility(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Util commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Utilities", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="abusive",
        usage="[2]",
        description="Abusive commands"
    )
    async def abusive(self, luna, page: str = "1"):

        if configs.risk_mode() == "on":
            prefix = files.json("data/config.json", "prefix", documents=False)
            cog = self.bot.get_cog('Abusive commands')
            commands = cog.get_commands()
            helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

            cog = self.bot.get_cog('Guild commands')
            commands = cog.get_commands()
            guildtext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

            cog = self.bot.get_cog('Mass commands')
            commands = cog.get_commands()
            masstext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

            cog = self.bot.get_cog('All commands')
            commands = cog.get_commands()
            alltext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

            cog = self.bot.get_cog('Spam commands')
            commands = cog.get_commands()
            spamtext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

            cog = self.bot.get_cog('Exploit commands')
            commands = cog.get_commands()
            if page == "2":
                await message_builder(luna, title="Abusive commands", footer_extra="Page 2", description=f"{theme.description()}" f"```\nGuild\n\n{guildtext}\n```" f"```\nGeneral\n\n{helptext}\n```")

            else:
                exploittext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

                await message_builder(luna, title="Abusive commands", footer_extra="Page 1", description=f"{theme.description()}" f"```\nExploits\n\n{exploittext}\n```" f"```\nSpam\n\n{spamtext}\n```" f"```\nMass\n\n{masstext}\n```" f"```\nAll\n\n{alltext}\n```" f"```\nNote\n\n{prefix}abusive 2 » Page 2```")

        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="protection",
        usage="",
        aliases=['protections', 'protect'],
        description="Protections"
    )
    async def protection(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Protection commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Privacy commands')
        commands = cog.get_commands()
        privacytext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Backup commands')
        commands = cog.get_commands()
        backuptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        cog = self.bot.get_cog('Whitelist commands')
        commands = cog.get_commands()
        whitelisttext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        activetext = f"\n\nActive protections:" if active_list != [] else ""
        for active in active_list:
            activetext += f"\n{active.title()}"
        cog = self.bot.get_cog('Protection Guild commands')
        commands = cog.get_commands()
        guildtext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        guilds = files.json(
            "data/protections/config.json",
            "guilds", documents=False
        )
        activeguildtext = ""
        if guilds:
            activeguildtext = f"\nProtected guilds:"
            for guild_id in guilds:
                with contextlib.suppress(BaseException):
                    guild = self.bot.get_guild(guild_id)
                    activeguildtext += f"\n{guild.name:17} » {guild}"
        await message_builder(
            luna, title="Protections",
            description=f"{theme.description()}"
                        f"```\nEnabled Protections\n\n"
                        f"{'Enabled':17} » {active_protections}{activetext}\n```"
                        f"```\nGuild Configuration\n\n{guildtext}{activeguildtext}```"
                        f"```\nProtections\n\n{helptext}```"
                        f"```\nWhitelist\n\n{whitelisttext}\n```"
                        f"```\nPrivacy | Streamer Mode\n\n{privacytext}\n```"
                        f"```\nBackups\n\n{backuptext}\n```"
        )

    @commands.command(
        name="misc",
        usage="",
        description="Miscellaneous commands"
    )
    async def misc(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Miscellaneous commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(luna, title="Miscellaneous", description=f"{theme.description()}```\n{helptext}```")

    @commands.command(
        name="settings",
        usage="",
        description="Settings"
    )
    async def settings(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        deletetimer = int(
            files.json(
                "data/config.json",
                "delete_timer", documents=False
            )
        )
        errorlog = files.json("data/config.json", "error_log", documents=False)
        riskmode = files.json("data/config.json", "risk_mode", documents=False)
        themesvar = files.json("data/config.json", "theme", documents=False)
        console_mode = files.json(
            "data/console/console.json", "mode", documents=False
        )
        console_mode = "information" if console_mode == "2" else "standard"
        if themesvar != "default":
            themesvar = (themesvar[:-5])
        if themesvar == "default":
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
        startup_status = files.json(
            "data/config.json", "startup_status", documents=False
        )
        title = theme.title()
        footer = theme.footer()
        selfbotdetection = files.json(
            "data/snipers/selfbot.json", "sniper", documents=False
        )
        pings = files.json(
            "data/notifications/console.json",
            "pings", documents=False
        )
        if title == "":
            title = "None"
        if footer == "":
            footer = "None"
        cog = self.bot.get_cog('Settings commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        share = configs.share()
        user_id = configs.share_id()
        sharinguser = "None" if user_id == "" else await self.bot.fetch_user(user_id)
        await message_builder(
            luna, title="Settings",
            description=f"{theme.description()}"
                        f"```\nYour current settings\n\n"
                        f"Error logging     » {errorlog}\n"
                        f"Auto delete timer » {deletetimer}\n"
                        f"Startup status    » {startup_status}\n"
                        f"Theme             » {themesvar}\n"
                        f"Console Mode      » {console_mode}\n"
                        f"Riskmode          » {riskmode}\n"
                        f"Description       » {theme_description}\n"
                        f"selfbot detection » {selfbotdetection}\n"
                        f"Mention notify    » {pings}\n```"
                        f"```\nYour current theme settings\n\n"
                        f"Theme             » {themesvar}\n"
                        f"Title             » {title}\n"
                        f"Footer            » {footer}\n"
                        f"Description       » {theme_description}\n```"
                        f"```\nShare Settings\n\n"
                        f"Share             » {share}\n"
                        f"User              » {sharinguser}```"
                        f"```\nSettings\n\n{helptext}```"
        )

    @commands.command(
        name="sharing",
        usage="",
        description="Share commands"
    )
    async def sharing(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        share = configs.share()
        user_id = configs.share_id()
        sharinguser = "None" if user_id == "" else await self.bot.fetch_user(user_id)
        cog = self.bot.get_cog('Share commands')
        commands = cog.get_commands()
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n" for command in commands)

        await message_builder(
            luna, title="Sharing",
            description=f"{theme.description()}```\nYour current settings\n\nShare             » {share}\nUser              » {sharinguser}\n``````\n{helptext}```"
        )

    @commands.command(
        name="chelp",
        aliases=['customhelp'],
        usage="",
        description="Show custom commands"
    )
    async def chelp(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        cog = self.bot.get_cog('Custom commands')
        commands = cog.get_commands()
        helptext = ""
        if not commands:
            helptext = "No custom commands found!"
        else:
            for command in commands:
                helptext += f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
        await message_builder(
            luna, title="Your custom commands",
            description=f"{theme.description()}```\n{helptext}``````\nCommand Control\n\n{prefix}restart          » Restart to load your commands\n{prefix}newcmd <name>    » Create new command```"
        )

    @commands.command(
        name="repeat",
        usage="",
        description="Repeat last used command"
    )
    async def repeat(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        await luna.send(f"{prefix}{last_used}")

    @commands.command(
        name="search",
        usage="<command>",
        description="Search for a command"
    )
    async def search(self, luna, commandName: str):

        prefix = files.json("data/config.json", "prefix", documents=False)
        helptext = "".join(f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}," for command in self.bot.commands)

        commandlist = helptext.split(",")
        commandlistfind = [
            string for string in commandlist if commandName in string]
        if commandlistfind := '\n'.join(str(e) for e in commandlistfind):
            await message_builder(
                luna, title=f"Searched for » {commandName.title()}",
                description=f"{theme.description()}```\n{commandlistfind}``````\nNote\n\n{prefix}help <command>   » To get more information```"
            )
        else:
            await message_builder(
                luna, title=f"Searched for » {commandName.title()}",
                description=f"```\nNo command has been found\n``````\nNote\n\n{prefix}help <command>   » To get more information```"
            )
