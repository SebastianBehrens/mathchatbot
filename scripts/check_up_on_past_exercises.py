from twilio.rest import Client
from pathlib import Path
import pickle
import json
from scripts.pickle_handler import pickle_handler
from munch import DefaultMunch 
import datetime
import pytz
from scripts.send_message import send_message
from os import environ

def check_up_on_past_exercises(run_id, config):
    past_sids = pickle_handler(mode="fetch")

    
    account_sid = environ["TWILIO_ACCOUNT_SID"]
    auth_token = environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    for sid in past_sids:
        message = DefaultMunch.fromDict(client.messages(sid).fetch())
        status = message.status
        read_time = message.date_sent
        now_time = datetime.datetime.now(pytz.timezone("UTC"))
        diff_h = (now_time-read_time).total_seconds()/3600
        if diff_h > 3.5:
            send_message(
                run_id=run_id,
                config=config,
                client = client,
                mode = "send_reminder")
    #     if status == "read" and


