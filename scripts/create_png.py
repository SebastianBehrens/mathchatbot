from os import system
import logging

def create_png(path, run_id):
    file_pdf = path / f"run_{run_id}.pdf"
    file_png = path / f"run_{run_id}.png"
    system(
        f"convert -density 300 -size 150x100 -alpha remove {file_pdf} {file_png}")
    logging.info("└─ .png file created.")



