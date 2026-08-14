import queue
import sys
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
from pointer import pointer
from OldStuff.oldVoiceSpeach import speak 
# Load Whisper model
model = WhisperModel(
    "base",
    device="cuda",
    compute_type="float16"
)

sampleR = 16000
chunkDur = 4
q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)

    q.put(indata.copy())


audio_buffer = np.array([], dtype=np.float32)

try:
    with sd.InputStream(
        samplerate=sampleR,
        channels=1,
        dtype="float32",
        callback=callback
    ):

        while True:
            x = input("Enter Y to speak: ").lower()

            if x != "y":
                print("Please enter Y ")
                continue

            print("Listening...\n")

            # Clear old audio
            while not q.empty():
                q.get()

            audio_buffer = np.array([], dtype=np.float32)

            # Record fresh audio for 2 seconds
            while len(audio_buffer) < sampleR * chunkDur:
                data = q.get()
                audio_buffer = np.append(
                    audio_buffer,
                    data.flatten()
                )

            print("Processing...")

            segments, _ = model.transcribe(
                audio_buffer,
                beam_size=1,
                language="en"
            )

            text = "".join(
                segment.text for segment in segments
            ).strip().lower()

            if text:
                print(f"You said: {text}")
                try:
                    result = pointer(text)
                except Exception:
                    result = None
                if result:
                    print(result)
                    speak(result)
            print()

except KeyboardInterrupt:
    print("\nStopped.")