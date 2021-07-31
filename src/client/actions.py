import sys
from client.threads.timer import TimerThread
from client.client import Client

def exit_program():
    sys.exit()

def timer_countdown(args):
    client = Client()
    timer = args[0]
    text = "O seu " + args[1] + " acabou"

    thread = TimerThread([client, timer, text])
    thread.start()