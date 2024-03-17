import logging
import datetime
from pathlib import Path

def instantiate_logger():

    suffix = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    file_path = Path().cwd() / "logs" / f"{suffix}.log"

    logging.basicConfig(
        filename=file_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("MathChatBot")

    logger.info("\n")