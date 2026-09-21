# Voice Assistant info 

A Python-based voice assistant that detects a wake word, processes speech in real time, handles calculator and weather commands, uses Gemini for general questions, responds with text-to-speech, and communicates with a C++ programmed ESP32 TFT display through serial communication.

## Current Features

- Real-time microphone listening
- Speech-to-text conversion using Speach recogntion by Google
- sending audio to google servers to process into text rapidly
- can outsource questions to Gemini AI
- can answer weather questions using OpenMeteo
- can do basic math 
- has a screen that displayes what is currently happening with animations 

## How It Works

The assistant is actived when it detects the wake word, it then listens through the microphone and records a short segment of audio. The audio is then converted into text using speech recognition. The text us then analayzed by the assistant's intent routing system. Caucaltor and weather requests are handeled by python functions, while general questions are send to Gemini. The response is the spoken aloud using text-to-speech, and serial commands are send to the ESP32 to update the TFT display. 

Example:

User:
"whats 10 * 20"

Output:
"the answer is 200"

Example: 

User: 
"whats the weather in Toronto"

Output:
"The temperature is: 16.3, The chance of rain today is: 2% and expected rain is: 0.0 mm, The cloud cover is: 100%"

Example: 

User:
"will it rain in Toronto:

Output:
"The chance of rain today is: 2% and expected rain is: 0.0 mm"

Example: 

User: 
"whats a GPU"

Output:
Gemini is called and its output is spoken

## Technologies Used

- Python
- Speach recogntion 
- NumPy
- SoundDevice
- edge-tts
- asyncio 
- math functions
- requests(for API's)
- Gemini API
- OpenMeteo
- openwakeword
- ESP32
- 2.4 Inch TFT LCD display

## Future Plans

This project is still in development and will continue to gain more AI features.

The long-term goal is to build a personal AI assistant that can understand voice commands, answer questions of all types, control hardware, and use AI to make decisions.

## Wiring 

```bash
ESP32: 3.3V -> TFT: BL 
ESP32: 3.3V -> TFT: VCC
ESP32: GND -> TFT: GND
ESP32: GPIO 2 -> TFT: DC
ESP32: GPIO 4 -> TFT: RST 
ESP32: GPIO 5 -> TFT: CS 
ESP32: GPIO 18 -> TFT: CLK
ESP32: GPIO 23 -> TFT: DIN
```

## Installation

### Software

Clone the repository:

```bash
git clone https://github.com/MatLuch/Voice-Assistant.git

```

Install all necessary libraries or make sure there installed with this:

```bash
& "C:\Users\mateo\AppData\Local\Programs\Python\Python311\python.exe" -m pip install SpeechRecognition sounddevice numpy openwakeword edge-tts soundfile requests pyserial google-genai pyttsx3
```

Create a file called info.py and follow this format:

```bash
key = "YourAPIKey"
name = "YourName"
com = "the COM your esp32 uses"
```
---

### Hardware 

Make sure these libraries are installed:

```bash
<SPI.h> 
<Adafruit_GFX.h> 
<Adafruit_ILI9341.h> 
```

Copy and paste code from Main.cpp to arduino ide and upload it

## Demo Video

[Watch my 1.5minute demo][https://github.com/MatLuch/Voice-Assistant/issues/1#issue-5532324452]
