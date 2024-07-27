# from scripts.check_up_on_past_exercises import check_up_on_past_exercises
import logging

from scripts.dispatch_messages import dispatch_messages
from scripts.fetch_exercises import fetch_exercises
from scripts.prepare_messages import prepare_messages
from scripts.initialize_folder_today import initialize_folder_today
from scripts.load_config import load_config
from scripts.validate_config import validate_config


def MathChatBot(config_path):
    """Main function of the MathChatBot which samples from exercises, creates compiled images, and sends them via telegram.

    Args:
        config_path: Relative path to config from cwd.
    """

    config = load_config(config_path=config_path)

    validate_config(config=config)

    run_path = initialize_folder_today()

    # check_up_on_past_exercises(uid, config)

    # one could create a list of dictionaries each containing all content to a client.
    # one would then enrich those dictionaries when processing a configs content.

    exercises: list[dict] = fetch_exercises(config=config)

    messages_to_be_sent: list[dict] = prepare_messages(
            exercises=exercises,
            run_path=run_path,
            config=config
            )

    dispatch_messages(messages_to_send=messages_to_be_sent, config=config)

    logging.info("Run finished.")
