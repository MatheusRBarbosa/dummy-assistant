from client.client import Client
from shared.configs import Configs
from client import actions
from server.parser import Parser

class Boot:
    def __init__(self):
        self.configs = Configs()
        self.client = Client()
        self.parser = Parser(self.configs)

    def start(self):
        while True:
            statement = self.client.listen()
            if self.configs.name in statement:
                answer = self.parser.process(statement)

                self.__has_action(answer)
                self.__has_text(answer)

    def __has_action(self, answer):
        action = answer.get("action")
        values = answer.get("values")
        if action != None:
            action_method = getattr(actions, action.value)
            action_method(values) if values != None else action_method()
        
    def __has_text(self, answer):
        text = answer.get("text")
        if text != None:
            self.client.speak(text)
