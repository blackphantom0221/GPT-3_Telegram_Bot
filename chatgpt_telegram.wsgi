import os
import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def create_app():
    # Load environment variables
    TOKEN = os.environ["TELEGRAM_TOKEN"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    model_engine = "chatgpt"

    # Connect to the OpenAI API and specify the ChatGPT model
    openai.api_key = OPENAI_API_KEY

    # Create an instance of Updater
    updater = Updater(TOKEN, use_context=True)

    # Add handlers for your bot
    start_handler = CommandHandler("start", start)
    updater.dispatcher.add_handler(start_handler)

    chat_handler = MessageHandler(Filters.text, chat)
    updater.dispatcher.add_handler(chat_handler)

    # Add error handler
    updater.dispatcher.add_error_handler(error)

    return updater

def start(update, context):
    update.message.reply_text("Hi, I am the Micro-ChatBot from DeepCore Developers integrated with ChatGPT. Send me a message, and I will try to respond.")

def chat(update, context):
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

def error(update, context):
    """Log errors caused by updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

