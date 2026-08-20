import speech_recognition as sr
import sounddevice as sd
import numpy as np
import openwakeword
from openwakeword.model import Model
from pointer import pointer
from Speach import speak 

recognizer = sr.Recognizer()

sample_rate = 16000
seconds = 4

stat = True 

openwakeword.utils.download_models()

model = Model(wakeword_models=["hey_jarvis"], vad_threshold=0.6)

RATE = 16000
CHUNK = 1280

while True:
    model.reset()
    print("listening for 'Hey jarvis")

    with sd.InputStream(samplerate=RATE, channels=1, dtype='int16', blocksize=CHUNK) as stream:
        while True:
            pcm_data, overflowed = stream.read(CHUNK)

            pcm_data = pcm_data.flatten()
            prediction = model.predict(pcm_data)

            if prediction.get("hey_jarvis", 0) > 0.80:
                if stat == False:
                    print("\n Wake word detected! Triggering assistant")
                model.reset()
                break
    if stat:
        speak("welcome Mateo how can i assist you")
        stat = False 
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