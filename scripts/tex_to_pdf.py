import urllib.parse
import requests
import logging
from pathlib import Path

def tex_to_pdf(tex, path, run_id):
    file = path / f"run_{run_id}.pdf"
    logging.info("Fetching pdf.")
    tex_str_enc: urllib = urllib.parse.quote(tex, safe='')
    url: str = f"https://latexonline.cc/compile?text={tex_str_enc}"
    response: requests = requests.get(url = url, timeout = 5)
    if response.status_code == 400:
        logging.error("Error occurred in tex_to_pdf. No pdf was created.")
        logging.info(f"└─ run_id: {run_id}")
        logging.info(f"└─ url: {url}")
        logging.error(f"└─ Response: {response.text}")
        logging.error("Program exited because of Exception.")
        raise Exception("Error occurred in tex_to_pdf. No pdf was created.")
    with open(file, 'wb') as f:
        f.write(response.content)
    logging.info("Saved pdf.")
    return(file)
