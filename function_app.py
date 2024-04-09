import azure.functions as func
import logging
from scripts.MathChatBot import MathChatBot
from scripts.get_configs import get_configs

app = func.FunctionApp()

@app.schedule(schedule="*/5 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger_mathchatbot(myTimer: func.TimerRequest) -> None:
    configs = get_configs()
    for conf in configs:
        MathChatBot(config_path=conf)