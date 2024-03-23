from imgurpython import ImgurClient
from pathlib import Path
import logging
from os import environ
from re import sub
import boto3

# abandoned because the .png links redirect to the non .png website
def png_to_imgur(path: Path, run_id: str) -> str:

    file_png: Path = path / f"run_{run_id}.png"

    client_id: str = environ["IMGUR_CLIENT_ID"]
    client_secret: str = environ["IMGUR_CLIENT_SECRET"]

    client = ImgurClient(client_id, client_secret)

    try:
        image: dict = client.upload_from_path(file_png, config=None, anon=True)
        link_image: str = image["link"]
        logging.info("└─ .png file  uploaded to Imgur.")
        return(link_image)
    except FileNotFoundError:
        print('File not found')
