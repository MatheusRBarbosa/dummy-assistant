from typing import Text
from shared.actions import Actions

class GreetenerService:

    def hello(self):
        return {
            "text": "Olá, tudo bem?",
            "action": None
        }

    def bye(self):
        return {
            "text": "Tudo bem, tchau",
            "action": Actions.EXIT_PROGRAM
        }
