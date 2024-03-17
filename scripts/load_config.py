from munch import DefaultMunch 
from pathlib import Path
import argparse
import logging
import yaml

def load_config():
    # with command line arguments to config

    parser = argparse.ArgumentParser()
    parser.add_argument('conf_file',
                        type=str,
                        nargs='?',
                        default='configs/valid/testing.yaml')

    conf_file = Path().cwd() / parser.parse_args().conf_file

    if conf_file is None:
        raise "Config missing. It should be the first argument given to main.py."
    with open(conf_file,'r',encoding='utf8') as file:
        config: dict = DefaultMunch.fromDict(yaml.safe_load(file))
    
    config["self"] = conf_file


    file = str(conf_file).split("/")[-1]
    logging.info(f"Config loaded: {file}.")

    return(config)