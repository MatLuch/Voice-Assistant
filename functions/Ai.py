from google import genai
client = genai.Client(api_key="API")
outputSett = " reply in 2.5 sentences"

chat = client.chats.create(
    model="gemini-3.1-flash-lite"
)

def ask_ai(text):
    response = chat.send_message(text + outputSett)
    if text is not None: 
        return response.text



