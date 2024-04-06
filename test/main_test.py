import unittest
from scripts.MathChatBot import MathChatBot
from scripts.get_configs import get_configs

class Main(unittest.TestCase):

    def test_everything(self):
        # main(config_path="configs/valid/testing.yaml")
        configs = get_configs("configs/testing/*.yaml")
        for conf in configs:
            MathChatBot(config_path=conf)

if __name__ == '__main__':
    unittest.main()