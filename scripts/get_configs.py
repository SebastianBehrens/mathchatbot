from pathlib import Path

def get_configs() -> None:
    pathlist = Path().cwd().glob('configs/valid/*.yaml')
    pathlist_rel = [
        path.relative_to(Path().cwd()) for path in pathlist]

    list_of_configs = [str(path) for path in pathlist_rel]
    return(list_of_configs)

    