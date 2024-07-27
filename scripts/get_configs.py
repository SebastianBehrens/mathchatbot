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

    file_regex = f"{folder}/*.yaml".replace("//", "/")
    pathlist = get_base_dir().glob(file_regex)
    pathlist_rel = [path.relative_to(get_base_dir()) for path in pathlist]

    list_of_configs = [str(path) for path in pathlist_rel]

    if len(list_of_configs) == 0:
        logging.info(f"No configs in directory {folder}. Program exited.")
        raise FileNotFoundError(f"No configs in directory '{folder}'.")

    # TODO: return list of config file names not the path with valid
    print(list_of_configs)
    return (list_of_configs)
