from scripts.send_message_telegram import send_message_telegram
def dispatch_messages(messages_to_send, config):
    send_message_telegram(
        message = f"Hi {config.contact.name}, löse bitte kurz diese Aufgabe(n):",
        chat_id = config.contact.telegram_contact_string
    )
    for message in messages_to_send:
        send_message_telegram(
            message = message,
            chat_id = config.contact.telegram_contact_string,
            image_path = message['image_path']
        )