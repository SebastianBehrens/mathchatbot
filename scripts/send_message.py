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
        body = 'Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',
        # body: str = f'Hi {config.contact.name}, löse doch bitte folgende Aufgabe. {media_url}',
    elif mode == "send_reminder":
        body: str = "Erinnerung."
    else:
        raise_txt = f"Unclear argument given to send_message: mode = {mode}"
        logging.error(raise_txt)
        raise Exception(raise_txt)

    logging.disable(logging.INFO)

    message = client.messages.create(
        from_='whatsapp:+19164722756',
        body=body,
        to=('whatsapp:'
            f'{re.sub( "^00", "+", str(config.contact.whatsapp_contact_string))}'
        ),
        media_url=[media_url]
    )
    # update interim.pickle

    logging.disable(logging.NOTSET)
    logging.info("Message sent to.")
    logging.info(f"└─run_id: {run_id}.")
    logging.info(f"└─name: {config.contact.name}.")

    print(message.sid)