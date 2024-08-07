import logging
import datetime
from pathlib import Path
import sys
from scripts.get_base_dir import get_base_dir

def instantiate_logger(level) -> None:

    suffix: str = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    file_path: Path = get_base_dir() / "logs" / f"{suffix}.log"

    # validate

    logs_folder = get_base_dir() / "logs"
    if not logs_folder.exists():
        logs_folder.mkdir()

    file_handler = logging.FileHandler(filename=file_path)
    console_handler = logging.StreamHandler(stream=sys.stdout)
    handlers = [file_handler, console_handler]

    logging.basicConfig(
        level=level,
        handlers=handlers,
        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("MathChatBot")
    logger.setLevel(level)
