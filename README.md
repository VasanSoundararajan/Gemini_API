# Jarvis Voice Assistant 🤖

A voice-activated AI assistant powered by Google's Gemini API, capable of natural conversation and task execution through voice commands.

## Features ✨

- **Voice Interaction**  
  🎤 Speech-to-text input using microphone
- **AI-Powered Responses**  
  🧠 Gemini Pro integration for intelligent responses
- **Text-to-Speech**  
  🔊 Natural voice output responses
- **Predefined Commands**  
  ⚡ Quick responses for common queries:
  - Greetings (Good Morning/Afternoon/Evening)
  - Self-introduction ("Who are you?")
  - Capabilities overview ("What can you do?")
  - Program control ("Start"/"Stop")

## Requirements 📋

- Python 3.7+
- Google Gemini API Key
- Microphone (hardware requirement)
- Internet connection

## Installation 🛠️

1. Install required packages:
```bash
pip install requests speechrecognition pyttsx3 pyaudio
```

2. Get Gemini API key from [Google AI Studio](https://aistudio.google.com/)

3. Replace placeholder in code:
```python
api_key = "YOUR_ACTUAL_API_KEY_HERE"  # Line 46
```

## Usage 🚀

```bash
python jarvis_assistant.py
```

**Voice Commands Examples**:
- "Hello Jarvis"
- "What can you do?"
- "Good morning"
- "Start the main program"
- "Stop"

## Configuration ⚙️

Customize voice settings in `speak_text()` function:
```python
engine.setProperty('rate', 150)  # Speech speed (words/min)
engine.setProperty('volume', 1)  # Volume level (0.0-1.0)
```

Add new commands by extending the `if/elif` chain in main loop:
```python
elif "your command" in user_input.lower():
    # Custom response logic
```

## Notes 📝

1. **API Key Security**  
   Never commit actual API keys to version control

2. **Dependencies**  
   - PyAudio might require additional setup on Linux:
   ```bash
   pip install portaudio19-dev python3-pyaudio
   ```

3. **Troubleshooting**:
   - Microphone access issues: Check OS permissions
   - API errors: Verify internet connection and API key validity
   - Speech recognition failures: Ensure clear audio input

## License 📄

MIT License - [See full license text](LICENSE)
