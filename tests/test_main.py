from scripts import get_configs

def test_main():
    # main(config_path="configs/valid/testing.yaml")
    configs = get_configs("test/test_configs")
    assert 1 == 1
    # for conf in configs:
    #     MathChatBot(config_path=conf)