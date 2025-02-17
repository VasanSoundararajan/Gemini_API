import requests
import speech_recognition as sr
import pyttsx3

class GeminiChat:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={self.api_key}"

    def send_message(self, message):
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "contents": [{"parts": [{"text": message}]}]
        }
        response = requests.post(self.endpoint, headers=headers, json=data)

        if response.status_code == 200:
            try:
                return response.json()["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError):
                return "Sorry, I couldn't process the response."
        else:
            return f"Error {response.status_code}: {response.text}"

def get_audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"✅ You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")
        except sr.RequestError:
            print("❌ Error with the speech recognition service.")

    return None

def speak_text(text):
    engine = pyttsx3.init()  # Initialize the speech engine
    engine.setProperty('rate', 150)  # Set speech rate
    engine.setProperty('volume', 1)  # Set volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    chat = GeminiChat(api_key)

    while True:
        user_input = get_audio_input()
        if user_input:
            if "stop" in user_input.lower():
                print("🛑 Stopping the program.")
                break

            response_text = chat.send_message(user_input)
            print(f"🤖 Gemini Response: {response_text}")
            speak_text(response_text)
