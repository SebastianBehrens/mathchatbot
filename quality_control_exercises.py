# while loop
# generate tex
# generate pdf
# send message
import logging
from scripts.MathChatBot import MathChatBot
from scripts.instantiate_logger import instantiate_logger
from pathlib import Path
import time

if __name__ == "__main__":

    instantiate_logger(level=logging.ERROR)
    while True:
        for i in range(20):
            MathChatBot(config_path=Path('/home/behseb/mathchatbot/configs/valid/quality_control.yaml'))
            print(f"sampled {i}")
        print('\n\n')
        time.sleep(10)

