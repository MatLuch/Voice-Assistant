import speech_recognition as sr
import sounddevice as sd
import numpy as np
from pointer import pointer
from speach import speak 

recognizer = sr.Recognizer()

sample_rate = 16000
seconds = 4

while True:
    input("Press Enter to speak: ")

    print("Listening...")

    audio = sd.rec(
        int(seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    print("Processing...")

    audio_data = sr.AudioData(
        audio.tobytes(),
        sample_rate,
        2
    )

    try:
        text = recognizer.recognize_google(audio_data)
        if text:
            print("You said:", text)
            try:
                result = pointer(text)
            except Exception:
                result = None
            if result: 
                print(result)
                speak(result)

    except sr.UnknownValueError:
        print("Could not understand")

    except sr.RequestError as e:
        print("API error:", e)