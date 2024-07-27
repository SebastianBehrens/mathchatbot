import logging
from scripts.yield_exercise_tex import yield_exercise_tex
from scripts.tex_to_pdf import tex_to_pdf
from datetime import datetime

def prepare_messages(exercises: list, path: str, config: dict):
    """Prepare the messages by converting .tex into pdf.

    Args:
        exercises: List of exercises as returned by fetch_exercises().
        path: String containing the daily runtime path as returned by initialize_folder_today().
        config: Configuration dictionary.
    """

    messages_to_be_sent: list = []
    for exercise in exercises:
        uid = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        tex = yield_exercise_tex(
                type=exercise.type,
                topic=exercise.topic,
                instruction=exercise.instruction,
                math=exercise.math)
        pdf_file = tex_to_pdf(tex, path, uid)

        messages_to_be_sent.append(
            {
            "run_id": uid,
            "config": config,
            "mode": "send_message",
            "pdf_path": pdf_file
            })
    return messages_to_be_sent
