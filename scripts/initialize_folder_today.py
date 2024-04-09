import datetime
from pathlib import Path
from os import system
import logging

def initialize_folder_today() -> Path:
    """Initialize the runtime folder of the day.

    Every run needs to write pdf files to disk. The daily runtime folder is the location for that.

    Returns:
        Path of the daily runtime folder
    """

    folder_today: str = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    path: Path = Path().cwd() / "runs" / folder_today
    path.mkdir(parents=True, exist_ok=True)
    system(f"rm -f {path / '*'}")
    logging.info("Run folder created.")
    return (path)

