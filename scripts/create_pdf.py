from os import system
from pathlib import Path
import logging

def create_pdf(path: Path, run_id: str) -> None:
    file = path / f"run_{run_id}.tex"
    system(f"pdflatex -interaction=batchmode -output-directory {path} {file}")
    logging.info("└─ .pdf file created.")
