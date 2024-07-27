from pathlib import Path
import pickle
import logging
from scripts.send_message import send_message

def pickle_handler(mode, string = ""):
    path = Path().cwd() / "interim.pickle"
    if mode == "fetch":
        try:
            with open(path ,'rb') as file:
                content = pickle.load(file)
        except FileNotFoundError:
            content = set()
            pass
        return content
    if mode == "append":
        sids = pickle_handler(mode = "fetch")
        sids.add(string)
        with open(path, "wb") as file:   #Pickling
            pickle.dump(sids, file)
        logging.info("Cached sid.")
    else:
        raise_txt = f"Unclear argument given to pickle_handler: mode = {mode}"
        logging.error(raise_txt)
        raise Exception(raise_txt)
