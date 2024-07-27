from pathlib import Path
import logging
from scripts.get_base_dir import get_base_dir


def get_configs(folder: str = 'configs/valid/') -> list[str]:
    """Fetch all configuration files in a directory.

    The entry point of this program (main.py) is set up to go through every configuration file (.yaml). The configuration file then serves as the decision point for selective processing.
    Args:
        folder: The directory to scan for configuration files of type yaml. Defaults to 'configs/valid/'.

    Raises:
        NameError: If directory specified does not contain any .yaml files.
    """
    path_to_configs = get_base_dir() / folder

    file_regex = f"*.yaml".replace("//", "/")

    # for file name only without path to it
    # configs = [file.name for file in path_to_configs.glob('*.yaml')]

    configs = list(path_to_configs.glob('*.yaml'))

    if len(configs) == 0:
        logging.info(f"No configs in directory {folder}. Program exited.")
        raise FileNotFoundError(f"No configs in directory '{folder}'.")

    return (configs)

