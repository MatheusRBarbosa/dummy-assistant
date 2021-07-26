import pyttsx3
import speech_recognition as sr
from server.parser import Parser
from client import actions

class Client:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', 'voices[0].id')
        self.parser = Parser()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Ouvindo...")
            audio=r.listen(source)

            try:
                statement=r.recognize_google(audio,language='pt-BR')
                print(f"user said:{statement}\n")

            except Exception as e:
                self.speak("Por favor, pode repetir?")
                return "None"
                
        answer = self.parser.process(statement)
        self.__has_action(answer)
        self.speak(answer.get('text'))

    def __has_action(self, answer):
        action = answer.get("action")
        if action != None:
            action_method = getattr(actions, action.value)
            action_method()