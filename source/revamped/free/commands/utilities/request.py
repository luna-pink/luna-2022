import requests

title_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["title"]

title_url_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["title_url"]

footer_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["footer"]

footer_icon_url_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["footer_icon_url"]

image_url_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["image_url"]

large_image_url_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["large_image_url"]

hexcolorvar_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["hex_color"]

author_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["author"]

author_icon_url_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["author_icon_url"]

author_url_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["author_url"]

descriptionvar_request = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/default.json"
).json()["description"]
