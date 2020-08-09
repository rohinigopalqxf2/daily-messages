"""
Endpoints for reminders and daily messages
"""
import random
from fastapi import FastAPI
from messages import culture

app = FastAPI()

@app.get("/")
def index():
    "The home page"
    return {"msg":"This is the endpoint for the home page. /message \
        and /reminder are more useful starting points."}

@app.get("/message")
def get_message():
    "Return a random message"
    message = random.choice(culture.MESSAGES)
    message = ' '.join(message.split())

    return message
