"""
Endpoints for reminders and daily messages
"""
import datetime
import os
import random
from fastapi import FastAPI
from messages import reminders
app = FastAPI()

CURR_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES_PATH = os.path.join(CURR_FILE_PATH, 'messages')

@app.get("/")
def index():
    "The home page"
    return {"msg":"This is the endpoint for the home page. /message \
        and /reminder are more useful starting points."}

@app.get("/message")
def get_message():
    "Return a random message"
    culture_file = os.path.join(MESSAGES_PATH, 'culture.txt')
    with open(culture_file, 'r') as fp:
        lines = fp.readlines()
    message = random.choice(lines)

    return {'msg':message.strip()}

@app.get("/reminder")
def get_reminder():
    "Return a reminder based on day of the week"
    weekday = datetime.datetime.today().weekday()
    #Note: Monday is 0 and Sunday is 6
    lines = reminders.messages.get(weekday, [''])
    message = "<b>Reminder:</b> " + random.choice(lines)

    return {'msg':message.strip()}
