from client.client import Client

if __name__=='__main__':
    client = Client()
    while True:
        client.listen()