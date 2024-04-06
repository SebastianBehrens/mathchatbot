from pathlib import Path
import logging

def get_configs(folder='configs/valid/') -> None:
    file_regex = f"{folder}/*.yaml".replace("//", "/")
    pathlist = Path().cwd().glob(file_regex)
    pathlist_rel = [path.relative_to(Path().cwd()) for path in pathlist]

    list_of_configs = [str(path) for path in pathlist_rel]

    if len(list_of_configs) == 0:
        logging.info(f"No configs in directory {folder}. Program exited.")
        raise Exception(f"No configs in directory {folder}. Program exited.")

    return(list_of_configs)

    