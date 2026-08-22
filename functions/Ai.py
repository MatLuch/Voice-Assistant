from google import genai
from API import *
client = genai.Client(api_key=key)
outputSett = " reply in 1.5 sentences"

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

def ask_ai(text):
    response = chat.send_message(text + outputSett)
    if text is not None: 
        return response.text




