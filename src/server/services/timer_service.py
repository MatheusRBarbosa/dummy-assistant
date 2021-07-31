from shared.actions import Actions
class TimerService:
    def __init__(self):
        self.multiplier_keywords = ["segundos", "minutos", "dias"]

    def count(self, statement):
        words = statement.split()
        
        # Pega o numero do timer
        time = [int(w) for w in words if w.isdigit()]

        # Pega o multiplicador do numero
        multiplier = None
        for w in words:
            if w in self.multiplier_keywords:
                multiplier = w
        
        if multiplier != None and time != None:
            return {
                "text": "Timer de {} {}".format(time, multiplier),
                "action": Actions.TIMER_COUNTDOWN,
                "values": [ time, multiplier ]
            }
        else:
            return {
                "text": "Desculpe, não entendi",
                "action": None,
                "values": None
            }