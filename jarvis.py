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
    api_key = "API_KEY"
    chat = GeminiChat(api_key)

    while True:
        user_input = get_audio_input()
        if user_input:
            if "who are you" in user_input.lower():
                print("🤖 Response: I am Jarvis, your personal assistant.")
                speak_text("I am Jarvis, your personal assistant.")

            elif "start" in user_input.lower():
                print("🤖 Response: 🚀 Starting the program.")
                speak_text("Starting the program.")

            elif "hello" in user_input.lower():
                print("🤖 Response: 👋 Hello! Cheif How are you?")
                speak_text("Hello! Cheif How are you?")

            elif "how are you" in user_input.lower():
                print("🤖 Response: I'm doing great. Thanks for asking!")
                speak_text("I'm doing great. Thanks for asking")

            elif "what can you do" in user_input.lower():
                print("🤖 Response: I can help you with various tasks like sending emails, setting up reminders, and more.")
                speak_text("I can help you with various tasks like sending emails, setting up reminders, and more.")

            elif "Good Morning" in user_input:
                print("🤖 Response: Good Morning! How can I help you today?")
                speak_text("Good Morning! How can I help you today?")

            elif "Good Afternoon" in user_input:
                print("🤖 Response: Good Afternoon! How can I help you today?")
                speak_text("Good Afternoon! How can I help you today?")

            elif "Good Evening" in user_input:
                print("Good Evening! How can I help you today?")
                speak_text("Good Evening! How can I help you today?")

            elif "stop" in user_input.lower():
                print("🛑 Stopping the program.")
                break

            else:
                response_text = chat.send_message(user_input)
                print(f"🤖 Response: {response_text}")
                speak_text(response_text)
