import socket
import subprocess

from discord.ext import commands
from .utilities import *


class NettoolCog(commands.Cog, name="Nettool commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="latency",
        usage="",
        description="Display Luna's latency"
    )
    async def latency(self, luna):

        await message_builder(luna, description=f"```\nPinging...```", delete_after=3)
        ip = socket.gethostbyname("discord.com")
        output = subprocess.run(
            f"ping {ip}",
            text=True,
            stdout=subprocess.PIPE
        ).stdout.splitlines()
        values = "".join(output[-1:])[4:].split(", ")
        minimum = values[0][len("Minimum = "):]
        maximum = values[1][len("Maximum = "):]
        average = values[2][len("Average = "):]
        ip = socket.gethostbyname("www.team-luna.org")
        output1 = subprocess.run(
            f"ping {ip}",
            text=True,
            stdout=subprocess.PIPE
        ).stdout.splitlines()
        values1 = "".join(output1[-1:])[4:].split(", ")
        minimum1 = values1[0][len("Minimum = "):]
        maximum1 = values1[1][len("Maximum = "):]
        average1 = values1[2][len("Average = "):]
        await message_builder(luna, title="Latency", description=f"```\nDiscord API\n\n" f"Minimum » {minimum}\n" f"Maximum » {maximum}\n" f"Average » {average}```" f"```\nLuna API\n\n" f"Minimum » {minimum1}\n" f"Maximum » {maximum1}\n" f"Average » {average1}```")

    @commands.command(
        name="ping",
        usage="<url/ip>",
        description="Ping an IP or URL"
    )
    async def ping(self, luna, *, url: str):

        await message_builder(luna, description=f"```\nPinging...```", delete_after=3)
        if url.startswith("https://") or url.startswith("http://"):
            url = url.replace("https://", "").replace("http://", "")
            try:
                url = socket.gethostbyname(url)
            except BaseException:
                await message_builder(luna, title="Resolve", description=f"```\nURL is invalid```")
                return
        output = subprocess.run(
            f"ping {url}",
            text=True,
            stdout=subprocess.PIPE
        ).stdout.splitlines()
        values = "".join(output[-1:])[4:].split(", ")
        minimum = values[0][len("Minimum = "):]
        maximum = values[1][len("Maximum = "):]
        average = values[2][len("Average = "):]
        await message_builder(
            luna, title=f"{url}",
            description=f"```\nMinimum » {minimum}\nMaximum » {maximum}\nAverage » {average}```"
        )

    @commands.command(
        name="iplookup",
        usage="",
        description="Display IP information"
    )
    async def iplookup(self, luna, ip: str):

        if ip is None:
            await luna.send("Please specify a IP address")
            return
        else:
            try:
                with requests.session() as ses:
                    resp = ses.get(f'https://ipinfo.io/{ip}/json')
                    if "Wrong ip" in resp.text:
                        await message_builder(luna, description="Invalid IP address")
                        return
                    else:
                        j = resp.json()
                        await message_builder(
                            luna, title=f"IP » {ip}",
                            description=f'```\nCity\n{j["city"]}\n```'
                                        f'```\nRegion\n{j["region"]}\n```'
                                        f'```\nCountry\n{j["country"]}\n```'
                                        f'```\nCoordinates\n{j["loc"]}\n```'
                                        f'```\nPostal\n{j["postal"]}\n```'
                                        f'```\nTimezone\n{j["timezone"]}\n```'
                                        f'```\nOrganization\n{j["org"]}```'
                        )
            except Exception as e:
                await luna.send(f"Error: {e}")

    @commands.command(
        name="tcpping", usage="<ip> <port>",
        description="Checks if host is online"
    )
    async def tcpping(self, luna, ip, port):

        if ip is None:
            await luna.send("Please specify a IP address")
            return
        if port is None:
            await luna.send("Please specify a port")
            return
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        try:
            sock.connect((ip, int(port)))
        except BaseException:
            await message_builder(
                luna, title="TCP-Ping",
                description=f"```Status » Offline\n``````\nIP » {ip}\n``````\nPort » {port}\n```"
            )
        else:
            await message_builder(
                luna, title="TCP-Ping",
                description=f"```Status » Online\n``````\nIP » {ip}\n``````\nPort » {port}\n```"
            )

    @commands.command(
        name="portscan", usage="<ip>",
        description="Checks for common open ports"
    )
    async def portscan(self, luna, ip):

        if ip is None:
            await luna.send("Please specify an IP address")
            return
        ports = [
            "10",
            "12",
            "13",
            "14",
            "16",
            "17",
            "18",
            "20",
            "21",
            "22",
            "23",
            "25",
            "40",
            "42",
            "45",
            "47",
            "48",
            "50",
            "53",
            "80",
            "81",
            "110",
            "139",
            "389",
            "443",
            "445",
            "996",
            "1433",
            "1521",
            "1723",
            "3066",
            "3072",
            "3306",
            "3389",
            "5900",
            "8080",
            "8181",
            "65530",
            "65535"]
        open_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.2)
            try:
                sock.connect((ip, int(port)))
            except BaseException:
                pass
            else:
                sock.close()
                open_ports.append(port)
        await message_builder(
            luna, title="Port Scanner",
            description=f'```\nIP » {ip}\n``````\nPorts Checked » {",".join(ports)}\n``````\nOpen Ports » {",".join(open_ports)}\n```'
        )

    @commands.command(
        name="resolve", usage="<url>",
        description="Get the url host IP"
    )
    async def resolve(self, luna, url):

        new_url = ""
        if url is None:
            await luna.send("Please specify a URL")
            return
        if url.startswith("https://"):
            new_url = url.replace("https://", "")
        elif url.contains("http://"):
            new_url = url.replace("http://", "")

        try:
            ip = socket.gethostbyname(new_url)
        except BaseException:
            await message_builder(luna, title="Resolve", description=f"```\nURL is invalid```")
            return
        await message_builder(luna, title="Host Resolver", description=f"```\nURL » {url}\n``````\nIP » {ip}\n```")

    @commands.command(
        name="webhookinfo", usage="<id>",
        description="Webhook information"
    )
    async def webhookinfo(self, luna, _id):

        try:
            webhook = await self.bot.fetch_webhook(_id)
            await message_builder(
                luna, title=f"Webhook » {webhook.name}",
                description=f"```\nID » {webhook.id}\n```"
                            f"```\nName » {webhook.name}\n```"
                            f"```\nChannel » {webhook.channel.name}\n```"
                            f"```\nGuild » {webhook.guild.name}\n```"
                            f"```\nToken » {webhook.token}\n```"
            )
        except BaseException:
            await error_builder(luna, "```\nInvalid webhook ID```")

    @commands.command(
        name="maclookup", usage="<mac>",
        description="MAC address Information"
    )
    async def maclookup(self, luna, mac: str):

        if mac is None:
            await luna.send("Please specify a MAC address")
            return
        if len(mac) != 17:
            await luna.send("Invalid MAC address")
            return
        try:
            resp = requests.get(f'https://api.macvendors.com/{mac}')
            if "Not Found" in resp.text:
                await message_builder(luna, description="```\nInvalid MAC address```")
            else:
                j = resp.json()
                await message_builder(luna, title=f"MAC » {mac}", description=f"```\nVendor » {j}\n```")
        except BaseException:
            await error_builder(luna, "```\nError » Invalid MAC address```")

    @commands.command(
        name="reverseip", usage="<ip>",
        description="Reverse DNS"
    )
    async def reverseip(self, luna, ip):

        if ip is None:
            await message_builder(luna, description="```\nPlease specify an IP address```")
            return
        try:
            resp = requests.get(
                f'https://api.hackertarget.com/reverseiplookup/?q={ip}'
            )
            if "error" in resp.text:
                await message_builder(luna, description="```\nInvalid IP address```")
            else:
                j = resp.json()
                await message_builder(luna, title=f"Reverse DNS » {ip}", description=f"```\n{j}\n```")
        except BaseException:
            await error_builder(luna, "```\nError » Invalid IP address```")

    @commands.command(name="mtr", usage="<ip>", description="MTR Traceroute")
    async def mtr(self, luna, ip):

        if ip is None:
            await message_builder(luna, description="```\nPlease specify an IP address```")
            return
        try:
            resp = requests.get(f'https://api.hackertarget.com/mtr/?q={ip}')
            if "error" in resp.text:
                await message_builder(luna, description="```\nInvalid IP address```")
            else:
                j = resp.json()
                await message_builder(luna, title=f"MTR Traceroute » {ip}", description=f"```\n{j}\n```")
        except BaseException:
            await error_builder(luna, "```\nError » Invalid IP address```")

    @commands.command(name="asn", usage="<ip>", description="ASN Information")
    async def asn(self, luna, ip):

        if ip is None:
            await message_builder(luna, description="```\nPlease specify an IP address```")
            return
        try:
            resp = requests.get(
                f'https://api.hackertarget.com/asnlookup/?q={ip}'
            )
            if "error" in resp.text:
                await message_builder(luna, description="```\nInvalid IP address```")
            else:
                j = resp.json()
                await message_builder(luna, title=f"ASN » {ip}", description=f"```\n{j}\n```")
        except BaseException:
            await error_builder(luna, "```\nError » Invalid IP address```")

    @commands.command(
        name="zonetransfer", usage="<domain>",
        description="Zone Transfer"
    )
    async def zonetransfer(self, luna, domain):

        if domain is None:
            await message_builder(luna, description="```\nPlease specify a domain```")
            return
        try:
            resp = requests.get(
                f'https://api.hackertarget.com/zonetransfer/?q={domain}'
            )
            if "error" in resp.text:
                await message_builder(luna, description="```\nInvalid domain```")
            else:
                j = resp.json()
                await message_builder(luna, title=f"Zone Transfer » {domain}", description=f"```\n{j}\n```")
        except BaseException:
            await error_builder(luna, "```\nError » Invalid domain```")

    @commands.command(
        name="httpheaders", usage="<url>",
        description="HTTP Headers"
    )
    async def httpheaders(self, luna, url):

        if url is None:
            await message_builder(luna, description="```\nPlease specify a URL```")
            return
        try:
            resp = requests.get(
                f'https://api.hackertarget.com/httpheaders/?q={url}'
            )
            if "error" in resp.text:
                await message_builder(luna, description="```\nInvalid URL```")
            else:
                j = resp.json()
                await message_builder(luna, title=f"HTTP Headers » {url}", description=f"```\n{j}\n```")
        except BaseException:
            await error_builder(luna, "```\nError » Invalid URL```")

    @commands.command(
        name="subnetcalc", usage="<ip>",
        description="Subnet Calculator"
    )
    async def subnetcalc(self, luna, ip):

        if ip is None:
            await message_builder(luna, description="```\nPlease specify an IP address```")
            return
        try:
            resp = requests.get(
                f'https://api.hackertarget.com/subnetcalc/?q={ip}'
            )
            if "error" in resp.text:
                await message_builder(luna, description="```\nInvalid IP address```")
            else:
                j = resp.json()
                await message_builder(luna, title=f"Subnet Calculator » {ip}", description=f"```\n{j}\n```")
        except BaseException:
            await error_builder(luna, "```\nError » Invalid IP address```")

    @commands.command(
        name="crawl", usage="<url>",
        description="Crawl a website"
    )
    async def crawl(self, luna, url):

        if url is None:
            await message_builder(luna, description="```\nPlease specify a URL```")
            return
        try:
            resp = requests.get(
                f'https://api.hackertarget.com/pagelinks/?q={url}'
            )
            if "error" in resp.text:
                await message_builder(luna, description="```\nInvalid URL```")
            else:
                j = resp.json()
                await message_builder(luna, title=f"Crawl » {url}", description=f"```\n{j}\n```")
        except BaseException:
            await error_builder(luna, "```\nError » Invalid URL```")

    @commands.command(
        name="scrapeproxies",
        usage="",
        aliases=['proxyscrape',
                 'scrapeproxy'],
        description="Scrape for proxies"
    )
    async def scrapeproxies(self, luna):

        file = open("data/raiding/proxies/http.txt", "a+")
        res = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500")
        proxies = []
        for proxy in res.text.split('\n'):
            if proxy := proxy.strip():
                proxies.append(proxy)
        for p in proxies:
            file.write(p + "\n")
        file = open(
            "data/raiding/proxies/https.txt", "a+"
        )
        res = requests.get(
            'https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500'
        )
        proxies = []
        for proxy in res.text.split('\n'):
            if proxy := proxy.strip():
                proxies.append(proxy)
        for p in proxies:
            file.write(p + "\n")
        file = open(
            "data/raiding/proxies/socks4.txt", "a+"
        )
        res = requests.get(
            'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500'
        )
        proxies = []
        for proxy in res.text.split('\n'):
            if proxy := proxy.strip():
                proxies.append(proxy)
        for p in proxies:
            file.write(p + "\n")
        file = open(
            "data/raiding/proxies/socks5.txt", "a+"
        )
        res = requests.get(
            'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500'
        )
        proxies = []
        for proxy in res.text.split('\n'):
            if proxy := proxy.strip():
                proxies.append(proxy)
        for p in proxies:
            file.write(p + "\n")
        await message_builder(
            luna, title="Proxy Scraper",
            description=f"```\nSaved all scraped proxies in data/raiding/proxies```"
        )  #

    @commands.command(name="ip", usage="", description="Show your ip")
    async def ip(self, luna):

        ip = requests.get('https://api.ipify.org').text
        prints.message(f"Your IP » {ip}")
