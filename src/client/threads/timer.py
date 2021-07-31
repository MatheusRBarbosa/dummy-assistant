from threading import Thread
from time import sleep

class TimerThread(Thread):
    def __init__(self, args):
        self.client = args[0]
        self.timer = args[1]
        self.finish_text = args[2]
        Thread.__init__(self)
    
    def run(self):
        for i in range(self.timer):
            sleep(1)
        self.client.speak(self.finish_text)