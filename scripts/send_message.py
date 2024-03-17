import logging
import re
import logging_tree

def send_message(run_id, config, mode ,client ,media_url = ""):
    # TODO: store as os variables
    logging.disable(logging.INFO)
    if mode == "send_exercise":
        body = 'Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',
    elif mode == "send_reminder":
        body = "Erinnerung."
    else:
        raise_txt = f"Unclear argument given to send_message: mode = {mode}"
        logging.error(raise_txt)
        raise Exception(raise_txt)


    message = client.messages.create(
        from_='whatsapp:+14155238886',
        # body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',
        body=body,
        to=('whatsapp:'
            f'{re.sub( "^00", "+", str(config.contact.whatsapp_contact_string))}'
        )
        # media_url=[media_url]
    )
    # update interim.pickle

    logging.disable(logging.NOTSET)
    logging.info("Message sent to.")
    logging.info(f"└─run_id: {run_id}.")
    logging.info(f"└─name: {config.contact.name}.")

    print(message.sid)