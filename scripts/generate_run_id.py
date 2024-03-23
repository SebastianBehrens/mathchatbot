from time import time

def generate_run_id() -> str:
    out = time()*100000
    return (f"{out:.0f}")