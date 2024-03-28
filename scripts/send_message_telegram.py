from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from pathlib import Path
from os import environ
import logging


def send_message_telegram(message, chat_id, image_path = None):
    token=environ["TELEGRAM_DEINMATHECHATBOT_API_KEY"]
    if image_path is None:
        request_url = (
            f"https://api.telegram.org/"
            f"bot{token}/"
            f"sendMessage?chat_id={chat_id}&"
            f'text={message}'
        )
        response = requests.post(request_url).json()
        logging.info(response)
    else:
        request_url = (
            f"https://api.telegram.org/"
            f"bot{token}/"
            f"sendPhoto?chat_id={chat_id}"
        )

        files = {
            'photo': open(image_path, 'rb')
        }

        # response = requests.post(request_url, files = files).json()
        # print(response)