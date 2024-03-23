from os import system
from pathlib import Path
import logging

def create_png(path: Path, run_id: str) -> None:
    file_pdf: Path = path / f"run_{run_id}.pdf"
    file_png: Path = path / f"run_{run_id}.png"
    system(
        f"convert -density 250 -size 150x100 -alpha remove {file_pdf} {file_png}")
    logging.info("└─ .png file created.")



