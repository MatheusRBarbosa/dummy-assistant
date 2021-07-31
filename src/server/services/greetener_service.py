from typing import Text
from shared.actions import Actions

class GreetenerService:

    def hello(self):
        return {
            "text": "Olá, tudo bem?",
            "action": None,
            "values": None
        }

    def bye(self):
        return {
            "text": "Tudo bem, tchau",
            "action": Actions.EXIT_PROGRAM,
            "values": None
        }

    def not_found(self):
        return {
            "text": "Desculpe, não entedi, pode repetir?",
            "action": None,
            "values": None
        }
