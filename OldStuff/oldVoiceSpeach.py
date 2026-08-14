import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("voice", engine.getProperty("voices")[1].id)  #

def speak(text):
    engine.say(text)
    engine.runAndWait()

    speak(text)
