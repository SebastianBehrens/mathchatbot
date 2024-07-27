from munch import DefaultMunch
from pathlib import Path
import argparse
import logging
import yaml
from scripts.get_base_dir import get_base_dir

def load_config(config_path: str) -> dict:
    """Load the configuration file of a student from the supplied path.

    Args:
        config_path: string containing the path to the config relative to the bots base directory.

    Returns:
        Configuration file as a dictionary.
    """


    with open(config_path,'r',encoding='utf8') as file:
        config: dict = DefaultMunch.fromDict(yaml.safe_load(file))

    # add path of config to config, to then later on update that config
    # config["self"] = conf_file # removed to be replaced with proper handling of past exercises

    # log name_of_config (xyz.yaml) instead of full path
    logging.info(f"Config loaded: {config_path.name}.")

    return config
