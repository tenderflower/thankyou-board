from fastapi import FastAPI
from pydantic import BaseModel
import json


app = FastAPI()


class Message(BaseModel):
    name: str
    message: str


@app.post("/messages")
async def create_message(message: Message):
    """
    Create a new thank you message.

    Parameters:
        message (Message): The message object containing name and message text

    Returns:
        dict: Status response indicating success
    """
    try:
        with open("messages.json", "r") as f:
            messages = json.load(f)
    except FileNotFoundError:
        messages = []

    messages.append({"name": message.name, "message": message.message})

    with open("messages.json", "w") as f:
        json.dump(messages, f)

    return {"status": "success"}


@app.get("/messages")
async def get_messages():
    """
    Retrieve all thank you messages.

    Returns:
        list: List of all messages with name and message content
    """
    try:
        with open("messages.json", "r") as f:
            messages = json.load(f)
    except FileNotFoundError:
        messages = []

    return messages
