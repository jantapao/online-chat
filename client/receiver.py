from client.client_class import Client
from util.type import Types

def start_receiver(host: str, port: str):
    sender = Client(host, port, None)
    sender.define_type(Types.RECEIVER.value)
    while (True):
        sender.receive()