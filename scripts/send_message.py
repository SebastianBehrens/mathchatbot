import logging
import re

def send_message(
        run_id: str,
        config: dict,
        mode: str,
        client,
        media_url: str = "") -> None:
# TODO: set up that this function returns message sid, that is stored in pickle to be checked up on.

    if mode == "send_exercise":
        message: str = f'Hi {config.contact.name}, löse doch bitte folgende Aufgabe.',
    elif mode == "send_reminder":
        message: str = "Erinnerung."
    else:
        raise_txt = f"Unclear argument given to send_message: mode = {mode}"
        logging.error(raise_txt)
        raise Exception(raise_txt)

    logging.disable(logging.INFO)

    # update interim.pickle

    logging.disable(logging.NOTSET)
    logging.info("Message sent to.")
    logging.info(f"└─run_id: {run_id}.")
    logging.info(f"└─name: {config.contact.name}.")

    print(message.sid)