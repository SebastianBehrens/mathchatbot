from munch import DefaultMunch
from pathlib import Path
import argparse
import logging
import yaml

def load_config(config_path) -> dict:

    # # with command line arguments to config
    # if config_path is None:
    #     # parse
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument('conf_file',
    #                         type=str,
    #                         nargs='?',
    #                         default='configs/valid/testing.yaml')

    #     conf_file: Path = Path().cwd() / parser.parse_args().conf_file

    #     if conf_file is None:
    #         raise "Config missing. It should be the first argument given to main.py."
    # else:
        # conf_file: Path = Path().cwd() / config_path

    conf_file: Path = Path().cwd() / config_path

    with open(conf_file,'r',encoding='utf8') as file:
        config: dict = DefaultMunch.fromDict(yaml.safe_load(file))

    # add path of config to config, to then later on update that config
    config["self"] = conf_file

    # log only name_of_config
    logging.info(f"Config loaded: {str(conf_file).split("/")[-1]}.")

    return(config)
