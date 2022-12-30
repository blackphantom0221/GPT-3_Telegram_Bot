from openai_functions import generate_response
from telegram_functions import start, chat, error

def main():
    # Code um Telegram-Bot zu starten und Nachrichten zu verarbeiten
    # ...
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

if __name__ == "__main__":
    main()
