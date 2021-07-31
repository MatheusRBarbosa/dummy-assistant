import pyttsx3
import speech_recognition as sr

class Client:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', 'voices[0].id')

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Ouvindo...")
            audio=r.listen(source)

            try:
                statement = r.recognize_google(audio,language='pt-BR')
                print(f"user said:{statement}\n")
                return statement

            except Exception as e:
                return "None"