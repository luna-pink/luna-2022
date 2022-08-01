from discord.ext import commands
from .utilities import *


class CustomCog(commands.Cog, name="Custom commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    try:
        # file = open(
        #     "data/scripts/example.py", "r"
        # )
        file_data = ""

        for filename in os.listdir("data/scripts"):
            if filename.endswith(".py"):
                file = open(
                    f"data/scripts/{filename}", "r"
                )
                file_data += file.read()
        file.close()

        if "sys.modules" in str(file_data):
            prints.error("Using sys.modules is not allowed.")
            time.sleep(5)
            os._exit(0)
        if "import inspect" in str(file_data):
            prints.error("Importing inspect is not allowed.")
            time.sleep(5)
            os._exit(0)
        if "import dill" in str(file_data):
            prints.error("Importing dill is not allowed.")
            time.sleep(5)
            os._exit(0)
        if "exec" in str(file_data):
            prints.error("Using exec is not allowed.")
            time.sleep(5)
            os._exit(0)
        if "auth_luna" in str(file_data):
            prints.error("\"auth_luna\" not allowed.")
            time.sleep(5)
            os._exit(0)
        if "atlas" in str(file_data):
            prints.error("\"atlas\" not allowed.")
            time.sleep(5)
            os._exit(0)
        exec(file_data)
    except Exception as e:
        prints.error(e)
        os.system('pause')