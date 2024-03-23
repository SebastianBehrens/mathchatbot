import logging
from pathlib import Path

def create_tex(string: str, path: Path, run_id: str) -> None:
    with open(path / f"run_{run_id}.tex", "w") as file:
        file.write(string)
    logging.info("└─ .tex file created.")