import logging
import datetime
from pathlib import Path
import sys

def instantiate_logger() -> None:

    suffix: str = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    file_path: Path = get_base_dir() / "logs" / f"{suffix}.log"

    file_handler = logging.FileHandler(filename=file_path)
    console_handler = logging.StreamHandler(stream=sys.stdout)
    handlers = [file_handler, console_handler]

    logging.basicConfig(
        level=logging.INFO,
        handlers=handlers,
        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("MathChatBot")
