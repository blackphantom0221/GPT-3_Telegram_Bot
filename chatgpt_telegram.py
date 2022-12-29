import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from dotenv import load_dotenv
import os

# Lädt die Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Verwendet den Wert der Umgebungsvariablen "DEBUG"
debug = os.getenv("DEBUG")

logger = logging.getLogger(__name__)

# Verbindung zur OpenAI-API herstellen und ChatGPT-Modell angeben
# Verwendet den Wert der Umgebungsvariablen "OPENAI_API_KEY"
openai.api_key = os.getenv("OPENAI_API_KEY")

model_engine = "chatgpt"

# Funktion, die ChatGPT verwendet, um auf eine Nachricht zu antworten
def generate_response(text):
    prompt = (f"User: {text}\n"
             f"MicroBot: ")
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

# Funktionen für den Telegram-Chatbot
def start(update, context):
    update.message.reply_text("Hi, ich bin der Micro-ChatBot von DeepCore Developers integriert mit ChatGPT. Schreib mir eine Nachricht, und ich werde versuchen, dir zu antworten.")

def chat(update, context):
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

# Telegram-Bot starten und Nachrichten verarbeiten
updater = Updater(os.getenv("TELEGRAM_TOKEN"), use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

chat_handler = MessageHandler(Filters.text, chat)
dispatcher.add_handler(chat_handler)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Error-Handler hinzufügen
dispatcher.add_error_handler(error)

try:
    # Den Bot starten
    updater.start_polling()

    # Auf Cleanup-Interrupts reagieren (z.B. STRG+C oder SIGTERM)
    updater.idle()
except Exception as e:
    print("An error occurred:", e)
