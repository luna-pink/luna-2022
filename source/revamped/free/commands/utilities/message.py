import discord
from theme import *
from prints import *
from configs import *
from dependencies.variables import *


def convert_to_text(embed: discord.Embed):
    """[summary]

    Args:
            embed (discord.Embed): [description]

    Returns:
            [type]: [description]
    """
    if embed.image.url != "" and str(embed.image.url) != "Embed.Empty":
        return embed.image.url if embed.description == "" or str(embed.description) == "Embed.Empty" else f"{embed.description}\n{embed.image.url}"

    embed.description = embed.description.replace(
        '[', '[34m['
    ).replace(
        ']', '][0m'
    ).replace(
        '<', '[35m<'
    ).replace(
        '>', '>[0m'
    ).replace(
        '```ansi\n', '```\n'
    )
    if not embed.description.startswith("\n"):
        extra_start = "\n"
    if embed.description.startswith("```\n"):
        extra_start = ""
    if embed.description.endswith("\n```"):
        embed.description = embed.description[:-5]
    text_mode_builder = f"```ansi\n[ [34m{embed.title.replace('**', '')}[0m ]\n{extra_start}{embed.description.replace('```', '')}\n\n[ [34m{embed.footer.text}[0m ]\n```"
    if len(text_mode_builder) >= 2000:
        prints.error("INVALID, OVER 2000 CHARS. PLEASE REPORT THIS TO A DEVELOPER.")
    return text_mode_builder


def convert_to_indent(embed: discord.Embed):
    """[summary]

    Args:
            embed (discord.Embed): [description]

    Returns:
            [type]: [description]
    """
    if embed.image.url == "" or str(embed.image.url) == "Embed.Empty":
        embed.description = embed.description.replace(
            '[', '[34m['
        ).replace(
            ']', '][0m'
        ).replace(
            '<', '[35m<'
        ).replace(
            '>', '>[0m'
        ).replace(
            '```\n', '```ansi\n'
        )
        text = ""

        for line in embed.description.split("\n"):
            indent = f"> {line}"
            text += indent + "\n"

        indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
        if len(indent_builder) >= 2000:
            prints.error("INVALID, OVER 2000 CHARS. PLEASE REPORT THIS TO A DEVELOPER.")
    elif embed.description == "" or str(embed.description) == "Embed.Empty":
        return embed.image.url
    else:
        indent_builder = f"{embed.description}\n{embed.image.url}"
    return indent_builder


async def send(luna, embed, delete_after=None):
    """[summary]

    Args:
            luna ([type]): [description]
            embed ([type]): [description]
            delete_after ([type], optional): [description]. Defaults to None.
    """
    deletetimer = configs.delete_timer()
    if delete_after is not None:
        deletetimer = delete_after
    mode = configs.mode()
    return await luna.send(convert_to_text(embed), delete_after=deletetimer) if int(mode) == 2 else await luna.send(convert_to_indent(embed), delete_after=deletetimer)


async def message_builder(luna, title: str = theme.title(), description="", large_image: str = "", delete_after: int = None, footer_extra: str = None, footer: str = None):
    """
    It's a function that builds an embed message

    :param luna: The bot instance
    :param title: str = theme.title()
    :type title: str
    :param description: The description of the embed
    :param large_image: str = ""
    :type large_image: str
    :param delete_after: int = None
    :type delete_after: int
    :param footer_extra: This is the footer text that will be displayed at the bottom of the embed
    :type footer_extra: str
    :param footer: str = None
    :type footer: str
    :return: The embed is being returned.
    """

    if footer == "None":
        footer_extra = ""
    elif footer_extra is None:
        footer_extra = f"Enabled Protections » {active_protections} | {theme.footer()}" if files.json("data/protections/config.json", "footer", documents=False) else theme.footer()

    elif files.json(
            "data/protections/config.json",
            "footer",
            documents=False
    ):
        footer_extra = f"{footer_extra} | Enabled Protections » {active_protections} | {theme.footer()}"
    else:
        footer_extra = f"{footer_extra} | {theme.footer()}"
    embed = discord.Embed(
        title=title,
        description=description
    )
    embed.set_footer(text=footer_extra)
    embed.set_image(url=large_image)
    return await send(luna, embed, delete_after)


async def error_builder(luna, description=""):
    """[summary]

    Args:
            luna ([type]): [description]
            description (str, optional): [description]. Defaults to "".
    """
    if configs.error_log() == "console":
        prints.error(description.replace('\n', ' ').replace('`', ''))
    else:
        embed = discord.Embed(
            title="Error", description=description
        )
        embed.set_footer(text=theme.footer())
        await send(luna, embed)


async def mode_error(luna, modes: str):
    """
    Sends an error message to the user if the mode is not set to 2.
    param `luna` The user that sent the command.
    param `modes` The mode that the user is using.

    returns `None`
    """
    if configs.error_log() == "console":
        prints.error(f"That mode does not exist! Only {modes}")
        return None
    else:
        embed = discord.Embed(
            title="Error",
            description=f"```\nThat mode does not exist!\nOnly {modes}```"
        )
        embed.set_footer(text=theme.footer())
        return await send(luna, embed)
