from pathlib import Path


def get_base_dir(flg_relative=0):
    if flg_relative:
        base_path = Path().cwd()
    else:
        base_path = Path('/home/behseb/mathchatbot/')

    return base_path

