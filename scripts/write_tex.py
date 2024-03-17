import logging

def create_tex(string, path, run_id):
    with open(path / f"run_{run_id}.tex", "w") as file:
        file.write(string)
    logging.info("└─ .tex file created.")