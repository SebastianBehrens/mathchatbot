import logging
from scripts.send_message_telegram import send_message_telegram
from scripts.pdf_to_png import pdf_to_png

def dispatch_messages(messages_to_send: list, config: dict):
    """Dispatch the messages to their destination.

    Every recipient of exercises is sent his batch of exercises.

    Args:
        messages_to_send: List of messages to send as returned by prepare_messages().
        config: Configuration dictionary.
    """
    plural_of_tasks = '' if len(messages_to_send)==1 else 'n'
    send_message_telegram(
        message=f"Hi {config.contact.name}, löse bitte kurz diese Aufgabe{plural_of_tasks}:",
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
