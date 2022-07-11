import urllib

from discord.ext import commands
from .utilities import *


class PrivacyCog(commands.Cog, name="Privacy commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="privacy",
        aliases=['streamermode'],
        usage="<on/off>",
        description="Privacy mode"
    )
    async def privacy(self, ctx, mode: str):
        motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ')

        global privacy

        if mode == "on" or mode == "off":
            luna.console(False, clear=True)
            if mode == "on":
                privacy = True
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
                privacy = False
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
            prints.message(f"Privacy mode » {color.print_gradient(f'{mode}')}")
            await message_builder(ctx, description=f"```\nPrivacy mode » {mode}```")
        else:
            await mode_error(ctx, "on or off")