import urllib.parse
import requests
from pathlib import Path

def tex_to_pdf(tex, path, run_id):
    file = path / f"run_{run_id}.pdf"
    tex_str_enc: urllib = urllib.parse.quote(tex, safe='')
    url: str = f"https://latexonline.cc/compile?text={tex_str_enc}"
    response: requests = requests.get(url = url)
    with open(file, 'wb') as f:
        f.write(response.content)
    return(file)