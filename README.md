# Voice Assistant

A Python-based voice assistant that uses speech recognition and AI models to understand voice input in real time.

This project currently focuses on converting live microphone audio into text using external speech recognition. The goal is to continue expanding it into a full AI assistant that can interact with my computer, software, and hardware.

## Current Features

- Real-time microphone listening
- Speech-to-text conversion using Speach recogntion by Google
- uses it to spend the audio to google servers to process
- Fast voice command detection
- can outsource questions to Gemini AI

## How It Works

The assistant continuously listens through the microphone and collects small chunks of audio. Every few seconds, the audio is processed by the speach model and converted into text.

Example:

User:
"whats 10 - 20"

Output:
-10

Example: 

User: 
"whats the weather in Toronto"

Output:


## Technologies Used

- Python
- Speach recogntion 
- NumPy
- SoundDevice
- edge-tts
- asyncio 
- math functions
- requests(for API's)
## Future Plans

This project is still in development and will continue to gain more AI features.

Some planned improvements include:

- Opening applications using voice commands
- Creating custom shortcuts and automations
- Controlling programs like VS Code, Chrome, Spotify, and other software
- Adding a more advanced AI system for understanding natural language
- Adding memory so the assistant can remember information
- Connecting it with hardware projects and smart devices
- Adding computer vision features using cameras
- Creating a physical AI assistant/robot called Carrot that can interact with the real world

The long-term goal is to build a personal AI assistant that can understand voice commands, perform tasks on a computer, control hardware, and use AI to make decisions.

## Installation

Clone the repository:

```bash
git clone https://github.com/MatLuch/Voice-Assistant.git