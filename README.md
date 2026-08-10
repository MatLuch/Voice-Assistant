# Voice Assistant

A Python-based voice assistant that uses speech recognition and AI models to understand voice input in real time.

This project currently focuses on converting live microphone audio into text using Faster Whisper with GPU acceleration. The goal is to continue expanding it into a full AI assistant that can interact with my computer, software, and hardware.

## Current Features

- Real-time microphone listening
- Speech-to-text conversion using Faster Whisper
- GPU acceleration using CUDA
- Processes audio directly from memory
- Fast voice command detection

## How It Works

The assistant continuously listens through the microphone and collects small chunks of audio. Every few seconds, the audio is processed by the Whisper model and converted into text.

Example:

User:
"plus"

Output:
+

## Technologies Used

- Python
- Faster Whisper
- NumPy
- SoundDevice
- NVIDIA CUDA

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