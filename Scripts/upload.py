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
            files.json("Luna/discord.json", "token", documents=True)
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

bot = commands.Bot(".", self_bot=True, guild_subscription_options=GuildSubscriptionOptions.off())
guild_id = 893540274561765426
upload_channel_id = 893540849852489758
changelog_channel_id = 893639765855969345
announcement_channel_id = 896068189262331914
guild_id_sbstore = 923317142701617193
changelog_channel_id_sbstore = 923355464249528360
luna_role = 893541525575839785

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
    ping_role = upload_guild.get_role(luna_role)
    upload_guild_sbstore = bot.get_guild(guild_id_sbstore)
    changelog_channel_sbstore = upload_guild_sbstore.get_channel(changelog_channel_id_sbstore)

# ///////////////////////////////////////////////////////////////
# With Mention

    announcement = f"""{ping_role.mention}

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
        try:
            await upload_channel.purge(limit=5)
        except:
            pass

    exe_link = await upload_channel.send(file=discord.File(r'Luna.exe'))
    exe_link = exe_link.attachments[0].url
    file = open("changelog.txt", "r")
    file_data = file.read()
    file.close()
    await announcement_channel.send(announcement)
    await changelog_channel.send(f"```\nChangelogs: Luna {version}\n\n{file_data}\n```")
    config.version(version)
    config.update(exe_link)
    await changelog_channel_sbstore.send(f"```\nChangelogs: Luna {version}\n\n{file_data}\n```")
    os._exit(0)

# ///////////////////////////////////////////////////////////////

token = files.json("Luna/discord.json", "token", documents=True)
print("Logging into token...")
bot.run(Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token))
