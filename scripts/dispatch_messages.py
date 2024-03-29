import logging
from scripts.send_message_telegram import send_message_telegram
from scripts.pdf_to_png import pdf_to_png

def dispatch_messages(messages_to_send, config):
    send_message_telegram(
        message=f"Hi {config.contact.name}, löse bitte kurz diese Aufgabe(n):",
        config=config,
        chat_id=config.contact.telegram_chat_id
    )
    for message in messages_to_send:
        send_message_telegram(
            message=message,
            chat_id=config.contact.telegram_chat_id,
            config=config,
            image=pdf_to_png(message['pdf_path'])
        )
