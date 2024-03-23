from os import system
import logging

def create_pdf(path, run_id):
    file = path / f"run_{run_id}.tex"
    system(f"pdflatex -interaction=batchmode -output-directory {path} {file}")
    logging.info("└─ .pdf file created.")
