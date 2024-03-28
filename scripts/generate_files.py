import logging
from scripts.write_tex import create_tex
from scripts.create_pdf import create_pdf
from scripts.create_png import create_png
from scripts.yield_exercise_tex import yield_exercise_tex
from datetime import datetime

def generate_files(exercises, path, config):
    messages_to_be_sent: list = []
    for exercise in exercises:
        # uid = generate_run_id()
        uid = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        tex = yield_exercise_tex(
                type=exercise.type,
                topic=exercise.topic,
                instruction=exercise.instruction,
                math=exercise.math)
        logging.info("Starting to create files.")
        create_tex(tex, path, uid)
        create_pdf(path, uid)
        create_png(path, uid)

        messages_to_be_sent.append(
            {
            "run_id": uid,
            "config": config,
            "mode": "send_message",
            "image_path": path / f"run_{uid}.png"

            })
    return(messages_to_be_sent)