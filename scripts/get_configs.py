from pathlib import Path

def get_configs(folder='configs/valid/') -> None:
    file_regex = f"{folder}/*.yaml".replace("//", "/")
    pathlist = Path().cwd().glob(folder)
    pathlist_rel = [path.relative_to(Path().cwd()) for path in pathlist]

    list_of_configs = [str(path) for path in pathlist_rel]
    return(list_of_configs)

    