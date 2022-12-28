import openai
import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Verbindung zur OpenAI-API herstellen und ChatGPT-Modell angeben
openai.api_key = "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"
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
updater = Updater("5831906865:AAEhPBs9SoYTbNjUri2vop8I1rsI12skgOI", use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

chat_handler = MessageHandler(Filters.text, chat)
dispatcher.add_handler(chat_handler)

updater.start_polling()

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Error-Handler hinzufügen
dispatcher.add_error_handler(error)

# Den Bot starten
updater.start_polling()

# Auf Cleanup-Interrupts reagieren (z.B. STRG+C oder SIGTERM)
updater.idle()
