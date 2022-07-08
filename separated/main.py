import requests
from discord import *
from discord.ext import commands

# ///////////////////////////////////////////////////////////////
# Special Imports

from Functions import *
from Encryption import *

from demo_category import democategory

bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    strip_after_prefix=True,
    self_bot=True,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    max_messages=1000,
    key="Jgy67HUXLH!Luna",
    afk=True
)


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")

print("1")

bot.add_cog(democategory(bot))

print("2")
for command in bot.commands:
    print(f"{command.name}")


def login():
    token = files.json("data/discord.luna", "token", documents=False)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'authorization': Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)
    }
    r = requests.get("https://discord.com/api/v10/users/@me", headers=headers).json()
    print(
        f"Logging into {color.print_gradient(r['username'])}#{color.print_gradient(r['discriminator'])}..."
    )
    global user_token
    user_token = Decryption(
        '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
    ).CEA256(token)
    bot.run(
        Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(
            token
        ),
        reconnect=True
    )


if __name__ == "__main__":
    login()
