# Voice Assistant

A Python-based voice assistant that uses speech recognition and AI models to understand voice input in real time mixed with a ESP32, C++ based hardware device

This project currently focuses on converting live microphone audio into text using external speech recognition. It can also interact with Hardware to display answers and more visually 

## Current Features

- Real-time microphone listening
- Speech-to-text conversion using Speach recogntion by Google
- uses it to spend the audio to google servers to process
- Fast voice command detection
- can outsource questions to Gemini AI
- can answer weather questions using OpenMeteo
- can do basic math 
- has a screen that displayes what is currently happening 

## How It Works

The assistant is activate by a keyword then it will listen through the microphone and collects a small chunk of audio. the audio is then processed by the speach model and converted into text which is then processed once again which then decides what functions to use, using this the answer is given and showcased on the screen.

Example:

User:
"whats 10 - 20"

Output:
-10

Example: 

User: 
"whats the weather in Toronto"

Output:
"The temperature is: 25"

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

## Installation

Clone the repository:

```bash
git clone https://github.com/MatLuch/Voice-Assistant.git