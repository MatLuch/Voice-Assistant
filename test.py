import queue
import sys
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

# 1. Load Whisper model
model = WhisperModel("base", device="cuda", compute_type="float16")

# 2. Set recording parameters
sampleR = 16000
chunkDur = 2  # process audio every 2 seconds
q = queue.Queue()


def callback(indata, frames, time, status):
  if status:
    print(status, file=sys.stderr)
  q.put(indata.copy())


# 3. Stream and transcribe live
print("Listening: \n")

audio_buffer = np.array([], dtype=np.float32)

try:
  with sd.InputStream(
      samplerate=sampleR, channels=1, dtype="float32", callback=callback
  ):
    while True:
      data = q.get()
      audio_buffer = np.append(audio_buffer, data.flatten())

      # Process whenever 2 seconds of audio accumulate
      if len(audio_buffer) >= sampleR * chunkDur:
        # Transcribe directly from memory (no WAV file writing)
        segments, _ = model.transcribe(
            audio_buffer, beam_size=1, language="en"
        )

        text = "".join(segment.text for segment in segments).strip().lower()

        if text:
          if "plus" in text:
            print("+")
          print(f"You said: {text}")

        # Clear buffer for the next chunk
        audio_buffer = np.array([], dtype=np.float32)

except KeyboardInterrupt:
  print("\nStopped.")