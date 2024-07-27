import urllib.parse
import requests
import logging
from scripts.run_command import run_command


def tex_to_pdf(tex, path, run_id, flg_online=0):
    if flg_online:
        logging.info("Fetching pdf.")
        tex_str_enc: urllib = urllib.parse.quote(tex, safe='')
        url: str = f"https://latexonline.cc/compile?text={tex_str_enc}"
        response: requests = requests.get(url = url, timeout = 60)
        if response.status_code != 200:
            logging.error("Error occured in tex_to_pdf. No pdf was created.")
            logging.info(f"└─ run_id: {run_id}")
            logging.info(f"└─ url: {url}")
            logging.error(f"└─ Response: {response.text}")
            logging.error("Program exited because of Exception.")
            raise Exception("Error occurred in tex_to_pdf. No pdf was created.")
        logging.info("Received pdf.")
        with open(file, 'wb') as f:
            f.write(response.content)

    else:
        tex_path = path / f'run_{run_id}.tex'
        with open(str(tex_path), 'w') as f:
            f.write(tex)

        run_command([
            'pdflatex',
            '-output-directory',
            str(path),
            str(tex_path)])
    logging.info("Pdf created.")

    pdf_file = path / f"run_{run_id}.pdf"
    return pdf_file

