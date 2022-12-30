import os

from telegram.ext import Updater
from chatgpt import ChatGPT

def create_app():
    # Load environment variables
    TOKEN = os.environ["TELEGRAM_TOKEN"]
    CHATGPT_MODEL_PATH = os.environ["OPENAI_API_KEY"]

    # Create instances of ChatGPT and Updater
    chatgpt = ChatGPT(CHATGPT_MODEL_PATH)
    updater = Updater(TOKEN, use_context=True)

    # Add handlers for your bot
    # ...

    return updater

app = create_app()
