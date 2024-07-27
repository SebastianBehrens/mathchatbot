from scripts import MathChatBot
from scripts import get_configs
from scripts import instantiate_logger

# TODO: whether to make specific imports across package

if __name__ == "__main__":

    instantiate_logger.instantiate_logger()
    configs = get_configs.get_configs()
    for conf in configs:
        MathChatBot.MathChatBot(config_path=conf)
