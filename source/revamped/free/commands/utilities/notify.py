import dhooks
from notifypy import Notify
from .prints import *
from .webhook import *


class notify:

    def toast(self, audio_path=None, title=None):
        """Create a toast notification"""
        notification = Notify(default_notification_application_name="Luna")
        if title is None:
            notification.title = files.json(
                "data/notifications/toast.json", "title", documents=False
            )
        else:
            notification.title = title
        if self is not None:
            notification.message = self
        notification.icon = f'data/resources/{files.json("data/notifications/toast.json", "icon", documents=False)}'
        if audio_path is not None:
            notification.audio = audio_path
        with contextlib.suppress(BaseException):
            notification.send(block=False)

    def webhook(url="", description="", name="", error=False):
        """Create a webhook notification"""
        try:
            if url == "":
                prints.error(
                    f"The webhook url can't be empty » {name} » Has been cleared"
                )
                json_object = json.load(open("data/webhooks/url.json", encoding="utf-8"))

                json_object[f"{name}"] = "webhook-url-here"
                files.write_json("data/webhooks/url.json", json_object)

                return
            elif "https://discord.com/api/webhooks/" not in url:
                prints.error(
                    f"Invalid webhook url » {name} » Has been cleared"
                )
                json_object = json.load(open("data/webhooks/url.json", encoding="utf-8"))

                json_object[f"{name}"] = "webhook-url-here"
                files.write_json("data/webhooks/url.json", json_object)

                return
            hook = dhooks.Webhook(url=url, avatar_url=webhook.image_url())
            color = 0x000000
            if error:
                color = 0xE10959
            elif color is not None:
                color = webhook.hex_color()
            embed = dhooks.Embed(
                title=webhook.title(
                ), description=f"```{description}```", color=color
            )
            embed.set_thumbnail(url=webhook.image_url())
            embed.set_footer(text=webhook.footer())
            hook.send(embed=embed)
        except BaseException:
            json_object = json.load(open("data/webhooks/url.json", encoding="utf-8"))

            json_object[f"{name}"] = "webhook-url-here"
            files.write_json("data/webhooks/url.json", json_object)

            return