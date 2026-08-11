import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("voice", engine.getProperty("voices")[1].id)  # Zira

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am your assistant.")