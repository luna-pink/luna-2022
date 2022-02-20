from notifypy import Notify
import dhooks
from Functions.prints import *
from FileHandling.jsonhandler import *

class notify:

    def toast(title=None, message=None, audio_path=None):
        """Create a toast notification"""
        notification = Notify(default_notification_application_name="Luna")
        if title == None:
            notification.title = JsonHandler("toast.json", "data/notifications").read_value("title")
        else:
            notification.title = title
        if not message == None:
            notification.message = message
        icon_name = JsonHandler("toast.json", "data/resources").read_value("icon")
        notification.icon = "data/resources/" + icon_name
        if not audio_path == None:
            notification.audio = audio_path
        try:
            notification.send(block=False)
        except:
            pass

    def webhook(url="", description="", name="", error=False):
        """Create a webhook notification"""
        try:
            if url == "":
                prints.error(f"The webhook url was empty » {name} » Has been cleared")
                JsonHandler("url.json", "data/webhooks").write_value(name, "webhook-url-here")
                return
            elif not "https://discord.com/api/webhooks/" in url:
                prints.error(f"The webhook url was invalid » {name} » Has been cleared")
                JsonHandler("url.json", "data/webhooks").write_value(name, "webhook-url-here")
                return
            hook = dhooks.Webhook(url=url, avatar_url=webhook.image_url())
            color = 0x000000
            if error == True:
                color = 0xE10959
            elif color == None:
                pass
            else:
                color = webhook.hex_color()
            embed = dhooks.Embed(title=webhook.title(), description=f"```{description}```", color=color)
            embed.set_thumbnail(url=webhook.image_url())
            embed.set_footer(text=webhook.footer())
            hook.send(embed=embed)
        except Exception as e:
            prints.error(e)