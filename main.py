from scripts.MathChatBot import MathChatBot
from scripts.get_configs import get_configs
if __name__ == "__main__":
    # main(config_path="configs/valid/testing.yaml")
    configs = get_configs()
    for conf in configs:
        MathChatBot(config_path=conf)