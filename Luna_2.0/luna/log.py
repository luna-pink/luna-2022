from time import strftime, localtime


def log(log_type: str, message: str):
    for line in message.split('\n'):
        print(f"{strftime('%H:%M', localtime())} |{f' {log_type.upper()}':<9}| {line}")
    return
