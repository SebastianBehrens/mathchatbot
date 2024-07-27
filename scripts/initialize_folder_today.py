import datetime
from pathlib import Path
from os import system
import logging
from scripts.get_base_dir import get_base_dir
from scripts.run_command import run_command

def initialize_folder_today() -> Path:
    """Initialize the runtime folder of the day.

    Every run needs to write pdf files to disk.
    The daily runtime folder is the location for that.

    Returns:
        Path of the daily runtime folder.
    """

    folder_today: str = str(datetime.datetime.now().strftime('%Y-%m-%d'))

    path: Path = get_base_dir() / "runs" / folder_today

    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        logging.info("Run folder created.")

    else:
        # clean up daily folder
        run_command(['rm', '-f', f'{path / "*"}'])

    return (path)

