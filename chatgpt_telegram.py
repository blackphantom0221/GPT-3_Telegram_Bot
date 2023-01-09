import os
import logging
import openai
import telegram
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()

# Gets the value of the "DEBUG" environment variable
debug = os.environ.get("DEBUG", False) 

logger = logging.getLogger(__name__)

# Connects to the OpenAI API and specifies the ChatGPT model
# Gets the value of the "OPENAI_API_KEY" environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

model_engine = "chatgpt"

def generate_response(text):
    prompt = (f"User : {text}")
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    message = completions.choices[0].text
    return message.strip()


# Functions for the Telegram chatbot
def start(update, context):
    update.message.reply_text("Hi, I'm Micro-ChatBot from DeepCore Developers integrated with ChatGPT. Send me a message, and I'll try to respond.")

def chat(update, context):
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Telegram-Bot starten und Nachrichten verarbeiten
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        logger.error("TELEGRAM_TOKEN environment variable is not set")
        return

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    chat_handler = MessageHandler(Filters.text, chat)
    dispatcher.add_handler(chat_handler)

    # Error-Handler hinzufügen
    dispatcher.add_error_handler(error)

    try:
        # Den Bot starten
        updater.start_polling()
        # Auf Cleanup-Interrupts reagieren (z.B. STRG+C oder SIGTERM)
        updater.idle()
    except Exception as e:
        logger.exception("An error occurred: %s", e)

if __name__ == "__main__":
    main()