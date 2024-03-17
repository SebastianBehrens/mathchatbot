from bs4 import BeautifulSoup
import requests
from http import cookiejar  # Python 2: import cookielib as cookiejar
from markdownify import markdownify as md

def create_material(link, thema):
    class BlockAll(cookiejar.CookiePolicy):
        return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
        netscape = True
        rfc2965 = hide_cookie2 = False

    s = requests.Session()
    s.cookies.set_policy(BlockAll())
    html = s.get(link)

    soup = BeautifulSoup(html.content, "html.parser")

    with open(f"material/{thema}.yaml", "w") as file:
        file.write(md(str(soup)))

create_material("https://studyflix.de/mathematik/potenzregeln-4323", "potregel")
