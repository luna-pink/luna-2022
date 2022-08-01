import sys

from .notify import *


def restart_program():
    """
    It restarts the program
    """
    if files.json(
            "data/notifications/toasts.json",
            "login",
            documents=False
    ) == "on" and files.json(
        "data/notifications/toasts.json",
        "toasts", documents=False
    ) == "on":
        notify.toast("Restarting Luna...")
    if (
            files.json("data/webhooks/webhooks.json", "login", documents=False)
            == "on"
            and files.json(
        "data/webhooks/webhooks.json", "webhooks", documents=False
    )
            == "on"
            and webhook.login_url() != "webhook-url-here"
    ):
        notify.webhook(
            url=webhook.login_url(),
            name="login",
            description="Restarting Luna...",
        )

    python = sys.executable
    os.execl(python, python, *sys.argv)
