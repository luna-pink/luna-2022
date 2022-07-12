import contextlib
import json
import os

import discord
import requests
from CEA256 import *
from discord import *
from discord.ext import commands

# ///////////////////////////////////////////////////////////////

r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
updater_url = r["updater"]
version_url = r["version"]

print()
print(f"Current version: {version_url}")
version = input("What should the new version be?: ")
print()


# ///////////////////////////////////////////////////////////////

class files:

    def documents():
        return os.path.expanduser("~/Documents")

    def json(file_name, value, documents=False):
        """
        Reads a json file
        
        Example:
            files.json("Luna/discord.luna", "token", documents=True)
        """
        if documents:
            return json.load(open(os.path.join(files.documents(), file_name), encoding="utf-8"))[value]
        else:
            return json.load(open(file_name, encoding="utf-8"))[value]

    def read_file(path, documents=False):
        """Reads a file"""
        if documents:
            with open(os.path.join(files.documents(), path), 'r', encoding="utf-8") as f:
                return f.read()
        else:
            with open(path, 'r', encoding="utf-8") as f:
                return f.read()

    def write_json(path, content, documents=False):
        """Writes a json file"""
        if documents:
            with open(os.path.join(files.documents(), path), "w", encoding="utf-8") as f:
                f.write(json.dumps(content, indent=4))
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(json.dumps(content, indent=4))


class config:

    def version(new_value):
        json_object = json.load(open("pastebin.json", encoding="utf-8"))
        json_object["version"] = new_value
        files.write_json("pastebin.json", json_object)

    def update(new_value):
        json_object = json.load(open("pastebin.json", encoding="utf-8"))
        json_object["update"] = new_value
        files.write_json("pastebin.json", json_object)


# ///////////////////////////////////////////////////////////////

bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    self_bot=True,
    help_command=None,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    key="Jgy67HUXLH!Luna"
)
guild_id = 893540274561765426
upload_channel_id = 893540849852489758
changelog_channel_id = 893639765855969345
announcement_channel_id = 896068189262331914
luna_role = 893541525575839785

public_guild_id = 793674589988323330
public_upload_channel_id = 951879313341448272
public_changelog_channel_id = 879050099563565106
public_announcement_channel_id = 810002706214420511
public_luna_role = 870056164107354142

# ///////////////////////////////////////////////////////////////

overwrite = False

# ///////////////////////////////////////////////////////////////

if overwrite:
    guild_id = 896620123463495690
    upload_channel_id = 896794849662103563
    changelog_channel_id = 896794849662103563
    announcement_channel_id = 896794849662103563
    luna_role = 896620280909291550


# ///////////////////////////////////////////////////////////////

@bot.event
async def on_ready():
    print(f"Logged in: {bot.user}")
    upload_guild = bot.get_guild(guild_id)
    upload_channel = upload_guild.get_channel(upload_channel_id)
    changelog_channel = upload_guild.get_channel(changelog_channel_id)
    announcement_channel = upload_guild.get_channel(announcement_channel_id)
    ping_role1 = upload_guild.get_role(luna_role)

    public_upload_guild = bot.get_guild(public_guild_id)
    public_upload_channel = public_upload_guild.get_channel(public_upload_channel_id)
    public_changelog_channel = public_upload_guild.get_channel(public_changelog_channel_id)
    public_announcement_channel = public_upload_guild.get_channel(public_announcement_channel_id)
    ping_role2 = public_upload_guild.get_role(public_luna_role)

    # ///////////////////////////////////////////////////////////////
    # With Mention

    announcement1 = f"""{ping_role1.mention}

> Luna {version} has been released.
> 
> Wait 5 minutes for Luna to automatically update it.
> Use (p)update or restart Luna to force the update.
> 
> Changelogs in #changelogs"""

    announcement2 = f"""{ping_role2.mention}

> Luna {version} has been released.
> 
> Wait 5 minutes for Luna to automatically update it.
> Use (p)update or restart Luna to force the update.
> 
> Changelogs in #changelogs"""

    # ///////////////////////////////////////////////////////////////
    # Without Mention

    #     announcement = f"""> Luna {version} has been released.
    # >
    # > Wait 5 minutes for Luna to automatically update it.
    # > Use (p)update or restart Luna to force the update.
    # >
    # > Changelogs in #changelogs"""

    # ///////////////////////////////////////////////////////////////

    if not overwrite:
        with contextlib.suppress(BaseException):
            await upload_channel.purge(limit=5)
    if not overwrite:
        with contextlib.suppress(BaseException):
            await public_upload_channel.purge(limit=5)
    await public_announcement_channel.send(announcement2)
    await announcement_channel.send(announcement1)
    await public_upload_channel.send(file=discord.File(r'Luna.exe'))
    exe_link = await upload_channel.send(file=discord.File(r'Luna.exe'))
    exe_link = exe_link.attachments[0].url
    with open("changelog.txt", "r") as file:
        file_data = file.read()
    await changelog_channel.send(f"```\nChangelogs: Luna {version}\n\n{file_data}\n```")
    await public_changelog_channel.send(f"```\nChangelogs: Luna {version}\n\n{file_data}\n```")
    config.version(version)
    config.update(exe_link)
    os._exit(0)


# ///////////////////////////////////////////////////////////////

token = files.json("Luna/discord.luna", "token", documents=True)
print("Logging into token...")
bot.run(Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token))
