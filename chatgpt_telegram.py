from openai_functions import generate_response
from telegram_functions import start, chat, error
import os
import logging
from dotenv import load_dotenv

# Lädt die Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Verwendet den Wert der Umgebungsvariablen "DEBUG"
debug = os.environ.get("DEBUG", False)

logger = logging.getLogger(__name__)

def main():
    # Code um Telegram-Bot zu starten und Nachrichten zu verarbeiten
    # ...
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

if __name__ == "__main__":
    main()

