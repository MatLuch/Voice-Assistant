from google import genai
from API import *
client = genai.Client(api_key=key)
outputSett = " reply in 2 sentences"

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

def ask_ai(text):
    response = chat.send_message(text)
    return response.text


print("ask ai Anything to test: ")
user = input("")
user += outputSett
out = ask_ai(user)
print(out)