"""
Endpoints for reminders and daily messages
"""
import datetime
import random
from fastapi import FastAPI
from messages import culture

app = FastAPI()

def get_weekday():
    "Return the current day of the week"
    #Src: https://stackoverflow.com/a/9847269
    #Note: Monday is 0 and Sunday is 6
    return datetime.datetime.today().weekday()

def is_weekday():
    "Is today a weekday?"
    weekday = get_weekday()
    result_flag = False
    if 0 <= weekday <= 4:
        result_flag = True

    return result_flag

@app.get("/")
def index():
    "The home page"
    return {"msg":"This is the endpoint for the home page. /message \
        and /reminder are more useful starting points."}

@app.get("/message")
def get_message():
    "Return a random message"
    message = None
    if not is_weekday():
        message = random.choice(culture.MESSAGES)
        message = ' '.join(message.split())

    return message
