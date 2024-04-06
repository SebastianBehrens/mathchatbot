# from scripts.check_up_on_past_exercises import check_up_on_past_exercises
import logging

from scripts.dispatch_messages          import dispatch_messages
from scripts.fetch_exercises            import fetch_exercises
from scripts.prepare_messages           import prepare_messages
from scripts.initialize_folder_today    import initialize_folder_today
from scripts.instantiate_logger         import instantiate_logger
from scripts.load_config                import load_config
from scripts.validate_config            import validate_config

def MathChatBot(config_path=None):
    """Main function of the MathChatBot which samples from exercises, creates compiled images, and sends them via telegram.

    Args:
        config_path: Relative path to config from cwd. Defaults to None.
    """

    instantiate_logger()

    config = load_config(config_path)

    validate_config(config)

    path = initialize_folder_today()
    
    # check_up_on_past_exercises(uid, config)

    exercises = fetch_exercises(config)

    messages_to_be_sent = prepare_messages(exercises, path, config)

    dispatch_messages(messages_to_be_sent, config)

    logging.info("Run finished")