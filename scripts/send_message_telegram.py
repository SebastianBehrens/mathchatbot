from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from pathlib import Path
from os import environ
import logging


def send_message_telegram(message, chat_id, config, image = None):
    token=environ["TELEGRAM_DEINMATHECHATBOT_API_KEY"]
    if image is None:
        request_url = (
            f"https://api.telegram.org/"
            f"bot{token}/"
            f"sendMessage?chat_id={chat_id}&"
            f'text={message}'
        )
        response = requests.post(request_url).json()
        logging.info(f"Message sent.")
        logging.info(f"└─ to: {config.contact.name}")
        logging.info(f"└─ id: {response['result']['message_id']}")
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
        logging.info(f"└─ to: {config.contact.name}")
        logging.info(f"└─ id: {response['result']['message_id']}")