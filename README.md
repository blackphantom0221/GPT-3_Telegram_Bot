```javascript
def start(update, context): = "Python_ChatGPT_Bot-Telegramm"; 
updater.start_polling();
``` 
![alt text][logo] 
 
[logo]:https://github.com/DeepCoreB4/Phyton_ChatGPT_Bot-Telegramm/blob/master/microBot.jpg "MicroBot DeepCore"
# ChatGPT on Telegram
ChatGPT is a chatbot that uses the OpenAI GPT-3 language model to generate human-like responses to user messages. It has been integrated with the Telegram messaging platform, allowing users to chat with ChatGPT through their Telegram app or on the web.

## How to use ChatGPT
To use ChatGPT, you will need a Telegram account and the Telegram app (available for both mobile and desktop). Once you have an account, you can find ChatGPT by searching for its username on Telegram, which is @chatgpt_bot.

To start chatting with ChatGPT, simply send it a message and it will respond with a generated response. You can ask ChatGPT questions, have a conversation with it, or just have fun chatting. ChatGPT is capable of understanding and responding to a wide variety of topics, so feel free to engage with it on any subject that interests you.

First you need to go to / open your Telegram App/ and tip in the search bar "BotFather"
1.  /newbot - reate a new bot
    - then lets name your bot and and hit enter
    - now we gotta choose a username for your bot. It must end with _bot like this "yourBotsName_bot"
    - you created your first bot like a pro!
2.  Now you can see your Access HTTP API TOKEN it looks like; "6241906262:OBGSO8Rpam1e8nx6_41ltzWsWj6mRWMRl92I"

Now your ready: IMPORTEND! DO NOT SHARE YOUR TOKEN.

The token should not be displayed anywhere publicly. Because Telegram and Openai rotate the token automatically for security reasons, so that the token is no longer accessible.

## Setup in VSCODE
1.  Clone Repositori from given link
    https://github.com/DeepCoreB4/Phyton_ChatGPT_Bot-Telegramm
2.  Rename the example.env file to .env and open it. Edit the 1.Line/ OPENAI_API_KEY with =<YOUR-OPENAI_API_KEY>
    Also add in line 2. your TELEGRAM_TOKEN ="YOUR-TELEGRAM-API-TOKEN"
3.  If you don't now your openAI API-KEY go to https://beta.openai.com/overview if necessary log in. Visit this link
    https://beta.openai.com/account/api-keys and click [+ Create new secret key] 
    this generates your unique OPENAI-API-KEY
4.  Open an PowerShell Terminal in your workspace folder and install NPM with "npm install"

Now we need to install the following packages to us our bot!

(+) openai

(+) python-telegram-bot

(+) python-dotenv

6.  Open Terminal again and install [python-dotenv] with this command <pip install python-dotenv> 
    if you get errors you may try to upgrade your [python-dotenv] 

    with "pip install --upgrade python-dotenv" and this command "pip install --upgrade pip"

    If it still doesn't work! Could it be that Python is not installed on your system or is not up to date? In that case, you need to install the latest version of Python. You can do this from here https://www.python.org/downloads/"

7.  After that you need to install with this command "pip install openai"  
8.  Then you can install with the following command "pip install python-telegram-bot"

## now run command " npm run start-local" to start the bot

# Hosting your ChatGPT-Telegram BOT to Heroku

1. "I use Heroku to host the Telegram bot. 
    I recommend this tutorial video if you don't know how to use Heroku

    "Create a Telegram Bot and Deploy it to Heroku"

    https://www.youtube.com/watch?v=-yWuLRJhoNI

    To use automatic workers you have to pay 7Euro a month!"

2.  Followe this steps: Download my Repositori and upload to your GitHup make it <"Privat not Public">

3.  open .gitignore and DELETE the first line ".env" if your not using Next.js / you 

4.  Deploy to Heroku! 🎉🎉🎉

Now your Bot is online and can be use in your Telegram Chat/Groups etc.

✌️😁

### Disclaimer
Please note that ChatGPT is a chatbot and is not a human. Its responses are generated using advanced artificial intelligence algorithms, but it may not always produce responses that are accurate, appropriate, or sensitive to your individual circumstances. Use ChatGPT at your own risk, and always use common sense and good judgment when interacting with it or any other chatbot.
## License

This repository is licensed under the [MIT License](LICENSE).
