from server.services.greetener_service import GreetenerService
from server.services.timer_service import TimerService

class Parser:
    def __init__(self, configs):
        self.configs = configs
        self.greetener = GreetenerService()
        self.timer = TimerService()

    def process(self, statement):
        statement = statement.lower()
        
        if self.configs.name == statement:
            return { "text": None, "action": None, "values": None }
        
        elif "oi" in statement:
            return self.greetener.hello()
        
        elif "desligar" in statement:
            return self.greetener.bye()
        
        elif "timer"in statement:
            return self.timer.count(statement)
        
        else:
            return self.greetener.not_found()
