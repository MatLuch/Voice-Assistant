from google import genai
from speach import speak
client = genai.Client(api_key="API")
outputSett = " reply in 2.5 sentences"

chat = client.chats.create(
    model="gemini-3.1-flash-lite"
)

def ask_ai(text):
    response = chat.send_message(text)
    return response.text



user = "whats a gpu"
user += outputSett
out = ask_ai(user)
speak(out)