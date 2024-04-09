from scripts.MathChatBot        import MathChatBot
from scripts.get_configs        import get_configs
from scripts.instantiate_logger import instantiate_logger

if __name__ == "__main__":

    instantiate_logger()
    configs = get_configs()
    for conf in configs:
        MathChatBot(config_path=conf)