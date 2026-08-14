import asyncio
import edge_tts
import soundfile as sf
import sounddevice as sd

VOICE = "en-US-JennyNeural"

async def create_audio(text):
    communicate = edge_tts.Communicate(
        text,
        VOICE
    )

    await communicate.save("temp.wav")


def speak(text):
    asyncio.run(create_audio(text))

    data, samplerate = sf.read("temp.wav")

    sd.play(data, samplerate)
    sd.wait()