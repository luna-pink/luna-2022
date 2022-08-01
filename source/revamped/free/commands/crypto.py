from discord.ext import commands
from .utilities import *


class CryptoCog(commands.Cog, name="Cryptocurrency commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="crypto",
        usage="<crypto>",
        description="Cryptocurrency prices"
    )
    async def crypto(self, luna, crypto: str):
        request = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=USD,EUR,GBP,CHF,CAD,AUD,RUB,JPY,CNY,INR,TRY,PLN'
        )
        data = request.json()
        usd = data['USD']
        eur = data['EUR']
        gbp = data['GBP']
        chf = data['CHF']
        cad = data['CAD']
        aud = data['AUD']
        rub = data['RUB']
        jpy = data['JPY']
        cny = data['CNY']
        inr = data['INR']
        pln = data['PLN']
        __try = data['TRY']
        desc = f"""```
USD: {usd}
EUR: {eur}
GBP: {gbp}
CHF: {chf}
CAD: {cad}
AUD: {aud}
RUB: {rub}
JPY: {jpy}
CNY: {cny}
INR: {inr}
TRY: {__try}
PLN: {pln}```"""
        await message_builder(luna, title=crypto, description=desc)