from google import genai
import speech_recognition as sr
import time
recognizer = sr.Recognizer()
client = genai.Client(api_key="AIzaSyCmNV85KlEdqiS-w-23H9RQSikfJfMFZDo")

def send(input):
    
        response = client.models.generate_content(model="gemini-2.0-flash",contents= input)   

        print("User:",input)
        print("AI_BOT:",response.text)
def listen(timeout_seconds=5):
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Adjusting for ambient noise... Please wait.")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Please say something")
                print(f"(Waiting up to {timeout_seconds} s for speech to start )")
                audio = recognizer.listen(source, timeout=timeout_seconds)
                print("Got It Thank You")
                text=recognizer.recognize_google(audio)
                return text;



text=listen()
send(text)