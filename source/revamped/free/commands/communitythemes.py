from discord.ext import commands
from .utilities import *


class CommunitythemesCog(commands.Cog, name="Community themes"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="preview",
        usage="<theme>",
        description="Preview a theme"
    )
    async def preview(self, luna, theme: str):

        prefix = files.json("data/config.json", "prefix", documents=False)
        notfound = False
        theme = theme.lower()
        if theme == "luna":
            title = "Luna"
            footer = "www.team-luna.org"
            description = True
            madeby = "Nshout"
        elif theme == "lunaanimated":
            title = "Luna"
            footer = "www.team-luna.org"
            description = True
            madeby = "Nshout"
        elif theme == "chill":
            title = "F R E E D O M"
            footer = "No one knows what it is so it exists as an illusion"
            description = True
            madeby = "$Exodus"
        elif theme == "midnight":
            title = "Midnight."
            footer = "It's Midnight."
            description = True
            madeby = "Rainy"
        elif theme == "vaporwave":
            title = "Vapor Wave"
            footer = "Ride the vapor wave."
            description = True
            madeby = "Rainy"
        elif theme == "sweetrevenge":
            title = "Sweet Revenge."
            footer = "Sweet revenge is nice."
            description = True
            madeby = "Rainy"
        elif theme == "error":
            title = "Error™"
            footer = "Error displaying footer, please contact support"
            description = True
            madeby = "$Exodus"
        elif theme == "lunapearl":
            title = "Luna"
            footer = "Team Luna"
            description = True
            madeby = "Nshout"
        elif theme == "gamesense":
            title = "gamesense"
            footer = "Get Good Get Gamesense"
            description = True
            madeby = "Dragon"
        elif theme == "aimware":
            title = "Aimware"
            footer = "Aimware | One Step Ahead Of The Game"
            description = True
            madeby = "Dragon"
        elif theme == "guilded":
            title = "Guilded"
            footer = "Guilded (Discord v2)| 2021"
            description = True
            madeby = "Exodus"
        elif theme == "lucifer":
            title = "💙 Lucifer Selfbot 💙"
            footer = "Lucifer Selfbot"
            description = True
            madeby = "Exodus"
        elif theme == "nighty":
            title = "Nighty"
            footer = "nighty.one"
            description = True
            madeby = "Exodus"
        elif theme == "aries":
            title = "Aries"
            footer = "made withu2661 by bomt and destiny"
            description = True
            madeby = "Nshout"
        else:
            notfound = True
        if notfound:
            await error_builder(luna, description=f"```\nNo theme called {theme} found```")
            return
        if not description:
            description = ""
        else:
            description = "```\n<> is required | [] is optional\n\n```"
        command_count = len(self.bot.commands)
        cog = self.bot.get_cog('Custom commands')
        custom = cog.get_commands()
        custom_command_count = 0
        for _ in custom:
            custom_command_count += 1
        embed = discord.Embed(
            title=title,
            description=f"{description}```\n\
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
{prefix}raiding          » Raiding tools\n\
{prefix}text             » Text commands\n\
{prefix}trolling         » Troll commands\n\
{prefix}tools            » Tools\n\
{prefix}networking       » Networking\n\
{prefix}nuking           » Account nuking\n\
{prefix}utility          » Utilities\n\
{prefix}settings         » Settings\n\
{prefix}webhook          » Webhook settings\n\
{prefix}notifications    » Toast notifications\n\
{prefix}sharing          » Share with somebody\n\
{prefix}themes           » Themes\n\
{prefix}misc             » Miscellaneous\n\
{prefix}about            » Luna information\n\
{prefix}repeat           » Repeat last used command\n\
{prefix}search <command> » Search for a command\n``````\n\
Version\n\n{version}``````\nThis is a preview of the theme {theme}\nThis theme was made by {madeby}\n```"
        )
        embed.set_footer(text=footer)
        await send(luna, embed)

    @commands.command(
        name="install",
        usage="<theme>",
        description="Install a theme"
    )
    async def install(self, luna, theme: str):

        notfound = False
        theme = theme.lower()
        if theme == "luna":
            title = "Luna"
            footer = "www.team-luna.org"
            description = True
            madeby = "Nshout"
        elif theme == "lunaanimated":
            title = "Luna"
            footer = "www.team-luna.org"
            description = True
            madeby = "Nshout"
        elif theme == "chill":
            title = "F R E E D O M"
            footer = "No one knows what it is so it exists as an illusion"
            description = True
            madeby = "$Exodus"
        elif theme == "midnight":
            title = "Midnight."
            footer = "It's Midnight."
            description = True
            madeby = "Rainy"
        elif theme == "vaporwave":
            title = "Vapor Wave"
            footer = "Ride the vapor wave."
            description = True
            madeby = "Rainy"
        elif theme == "sweetrevenge":
            title = "Sweet Revenge."
            footer = "Sweet revenge is nice."
            description = True
            madeby = "Rainy"
        elif theme == "error":
            title = "Error™"
            footer = "Error displaying footer, please contact support"
            description = True
            madeby = "$Exodus"
        elif theme == "lunapearl":
            title = "Luna"
            footer = "Team Luna"
            description = True
            madeby = "Nshout"
        elif theme == "gamesense":
            title = "gamesense"
            footer = "Get Good Get Gamesense"
            description = True
            madeby = "Dragon"
        elif theme == "aimware":
            title = "Aimware"
            footer = "Aimware | One Step Ahead Of The Game"
            description = True
            madeby = "Dragon"
        elif theme == "guilded":
            title = "Guilded"
            footer = "Guilded (Discord v2)| 2021"
            description = True
            madeby = "Exodus"
        elif theme == "lucifer":
            title = "💙 Lucifer Selfbot 💙"
            footer = "Lucifer Selfbot"
            description = True
            madeby = "Exodus"
        elif theme == "nighty":
            title = "Nighty"
            footer = "nighty.one"
            description = True
            madeby = "Exodus"
        elif theme == "aries":
            title = "Aries"
            footer = "made withu2661 by bomt and destiny"
            description = True
            madeby = "Nshout"
        else:
            notfound = True
        if notfound:
            await error_builder(luna, description=f"```\nNo theme called {theme} found```")
            return
        data = {
            "title": f"{title}",
            "footer": f"{footer}",
            "description": description
        }
        files.write_json(f"data/themes/{theme}.json", data, documents=False)
        config.theme(f"{theme}")
        await message_builder(
            luna,
            description=f"```\nInstalled theme \"{theme}\" and applied it\nThis theme was made by {madeby}```"
        )