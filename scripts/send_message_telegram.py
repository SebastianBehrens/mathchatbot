from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from pathlib import Path
from os import environ
from pprint import pformat
import logging


def send_message_telegram(message, chat_id, config, image = None):
    """Send a message to a telegram chat.

    Args:
        message: Textual message to be sent.
        chat_id: ID of the Chat.
        config: Configuration file.
        image: Image bytes to send as returned by pdf_to_png(). Defaults to None.

    Raises:
        Exception: _description_
    """

    token: str =environ["TELEGRAM_DEINMATHECHATBOT_API_KEY"]

    if image is None:
        request_url = (
            f"https://api.telegram.org/"
            f"bot{token}/"
            f"sendMessage?chat_id={chat_id}&"
            f'text={message}'
        )

        response = requests.post(request_url).json()
        logging.info(f"Message sent.")
    else:
        request_url = (
            f"https://api.telegram.org/"
            f"bot{token}/"
            f"sendPhoto?chat_id={chat_id}"
        )

        files = {
            'photo': image
        }

        response = requests.post(request_url, files = files).json()
        logging.info(f"Image sent.")
    
    if not response['ok']:
        logging.error("Attempt to send message to telegram failed.")
        logging.error(f"Telegram \n{pformat(response)}")
        raise Exception("Attempt to send message to telegram failed.")

    logging.info(f"└─ to: {config.contact.name}")
    logging.info(f"└─ id: {response['result']['message_id']}")