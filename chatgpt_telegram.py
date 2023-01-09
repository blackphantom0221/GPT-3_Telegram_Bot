import os
import logging
import openai
import telegram
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
load_dotenv()
debug = os.environ.get("DEBUG", False)
logger = logging.getLogger(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def generate_response(text):
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: tell me a joke\nAI: What did the fish say when it hit the wall? \"Dam!\"",
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

def start(update, context):
    update.message.reply_text("Hi, ich bin der Micro-ChatBot von DeepCore Developers integriert mit ChatGPT. Schreib mir eine Nachricht, und ich werde versuchen, dir zu antworten.")

def chat(update, context):
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
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
    dispatcher.add_error_handler(error)
    try:
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.exception("An error occurred: %s", e)
if __name__ == "__main__":
    main()