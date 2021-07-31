from shared.actions import Actions
class TimerService:
    def __init__(self):
        self.multiplier_keywords = ["segundos", "minutos", "horas"]

    def count(self, statement):
        words = statement.split()

        # Pega o numero do timer
        base_time = [int(w) for w in words if w.isdigit()]

        # Pega o multiplicador do numero
        multiplier = None
        if base_time != None:
            for i in range(len(words)):
                if words[i] in self.multiplier_keywords:
                    multiplier = self.multiplier_keywords.index(words[i])
                    break
        
        if multiplier != None:
            total_time = base_time[0] * (60 ** multiplier)
            response_text = "timer de {} {}".format(base_time, self.multiplier_keywords[multiplier])
            return {
                "text": "Iniciando " + response_text,
                "action": Actions.TIMER_COUNTDOWN,
                "values": [ total_time, response_text ]
            }
        else:
            return {
                "text": "Desculpe, não entendi",
                "action": None,
                "values": None
            }