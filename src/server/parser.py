from server.services.greetener_service import GreetenerService

class Parser:
    def __init__(self):
        self.greetener = GreetenerService()

    def process(self, statement):
        statement = statement.lower()
        
        if "oi" in statement:
            return self.greetener.hello()
        
        elif "tchau" in statement or "parar" in statement:
            return self.greetener.bye()
