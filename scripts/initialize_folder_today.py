import datetime
from pathlib import Path
from os import system
import logging

def initialize_folder_today() -> Path:
    folder_today: str = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    path: Path = Path().cwd() / "runs" / folder_today
    path.mkdir(parents=True, exist_ok=True)
    # TODO: remove this again
    system(f"rm -f {path / '*'}")
    logging.info("Run folder created")
    return (path)

