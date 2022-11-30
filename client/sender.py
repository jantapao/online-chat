from client.client_class import Client
from util.type import Types

def start_sender(host: str, port: str):
    sender = Client(host, port, input('Digite o seu usuário: '))
    sender.define_type(Types.SENDER.value)
    while (True):
        message = input('Mensagem: ')
        sender.send_message(message)