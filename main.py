from scripts.check_up_on_past_exercises import check_up_on_past_exercises
from scripts.instantiate_logger import instantiate_logger
from scripts.initialize_folder_today import initialize_folder_today
from scripts.generate_run_id import generate_run_id
from scripts.load_config import load_config
from scripts.yield_exercise_tex import yield_exercise_tex
# from scripts.fetch_exercises import fetch_exercises
from scripts.fetch_exercises import fetch_exercises
# from scripts.select_exercise import fetch_exercise
from scripts.write_tex import create_tex
from scripts.create_pdf import create_pdf
from scripts.create_png import create_png
from scripts.png_to_web import png_to_web
from scripts.send_message import send_message
# from scripts.prepare_messages import prepare_messages

import logging
from twilio.rest import Client


if __name__ == "__main__":
    
    instantiate_logger()
    config = load_config()
    path = initialize_folder_today()
    uid = generate_run_id()
    # print(uid)
    # check_up_on_past_exercises(uid, config)
    exercises = fetch_exercises(config)
    messages_to_be_sent = []
    for exercise in exercises:
        tex = yield_exercise_tex(
                type=exercise.type,
                topic=exercise.topic,
                instruction=exercise.instruction,
                math=exercise.math)
        logging.info("Starting to create files.")
        create_tex(tex, path, uid)
        create_pdf(path, uid)
        create_png(path, uid)
        link = png_to_web(path, uid)
        print(link)
        messages_to_be_sent.append(
            {
            "run_id": uid,
            "config": config,
            "mode": "send_message",
            "link": "link"
            })
        
        # for msg in messages_to_be_sent:
        # account_sid = environ["TWILIO_ACCOUNT_SID"]
        # auth_token = environ["TWILIO_AUTH_TOKEN"]

        #     client = Client(account_sid, auth_token)
        #     send_message(
        #         run_id=uid,
        #         config=config,
        #         media_url=link,
        #         mode="send_exercise",
        #         client=client)