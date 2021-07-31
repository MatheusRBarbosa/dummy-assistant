from server.services.greetener_service import GreetenerService

class Parser:
    def __init__(self, configs):
        self.greetener = GreetenerService()
        self.configs = configs

    def process(self, statement):
        statement = statement.lower()
        
        if self.configs.name == statement:
            return { "text": None, "action": None }
        
        elif "oi" in statement:
            return self.greetener.hello()
        
        elif "tchau" in statement or "parar" in statement:
            return self.greetener.bye()
