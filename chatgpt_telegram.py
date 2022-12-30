import logging as B,os,telegram
from telegram.ext import Updater as E,CommandHandler as F,MessageHandler as G,Filters as H
from dotenv import load_dotenv as C
from openai_functions import generate_response as D
C()
M=os.environ.get('DEBUG',False)
A=B.getLogger(__name__)
def I(update,context):update.message.reply_text('Hi, ich bin der Micro-ChatBot von DeepCore Developers integriert mit ChatGPT. Schreib mir eine Nachricht, und ich werde versuchen, dir zu antworten.')
def J(update,context):A=update;B=A.message.text;C=D(B);A.message.reply_text(C)
def K(update,context):A.warning('Update "%s" caused error "%s"',update,context.error)
def L():
	D=os.environ.get('TELEGRAM_TOKEN')
	if not D:A.error('TELEGRAM_TOKEN environment variable is not set');return
	B=E(D,use_context=True);C=B.dispatcher;L=F('start',I);C.add_handler(L);M=G(H.text,J);C.add_handler(M);C.add_error_handler(K)
	try:B.start_polling();B.idle()
	except Exception as N:A.exception('An error occurred: %s',N)
if __name__=='__main__':L()