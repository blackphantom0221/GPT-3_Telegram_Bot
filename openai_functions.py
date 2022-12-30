import os,openai as A
A.api_key=os.environ.get('OPENAI_API_KEY')
B='chatgpt'
def C(text):B=f"User: {text}\nMicroBot: ";C=A.Completion.create(model='text-davinci-003',prompt=B,max_tokens=1024,n=1,stop=None,temperature=0.5,top_p=0.3,frequency_penalty=0.5,presence_penalty=0);D=C.choices[0].text;return D.strip()