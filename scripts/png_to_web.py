from os import path
from imgurpython import ImgurClient
import logging
from os import environ

def png_to_web(path, run_id):
    file_png = path / f"run_{run_id}.png"
    client_id = environ["IMGUR_CLIENT_ID"]
    client_secret = environ["IMGUR_CLIENT_SECRET"]

    
    client = ImgurClient(client_id, client_secret)

    try:
        image = client.upload_from_path(file_png, config=None, anon=True)
        link_image = image["link"]
        logging.info("└─ .png file  uploaded to Imgur.")
        return(link_image)

    except FileNotFoundError:
        print('File not found')
