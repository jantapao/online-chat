from server.server_class import Server
from client.client_class import Client

import signal
import readchar

RECEIVER = '<RECEIVER>'
SENDER = '<SENDER>'

def handler(signum, frame):
    msg = "Digita S para encerrar ou N para continuar: "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'S':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)

def main():
    signal.signal(signal.SIGINT, handler)
    host = input('Host: ')
    port = int(input('Port: '))
    option = input('Digite [1] para Servidor e [2] para Cliente: ')
    match option:
        case '1':
            server = Server(host, port)
            print('\nPressione Ctrl+C para encerrar a execução...\n')
            while (True):
                print('Chamou a conexão')
                server.receive_connection()
                print('Finaliza a chamada')
        case '2':
            username = input('Username: ')
            print('\nPressione Ctrl+C para encerrar a execução...\n')
            sender = Client(host, port, username)
            sender.define_type(SENDER)
            while (True):
                message = input('Mensagem: ')
                sender.send_message(message)
        case _:
            print('Opção não definida...')

if __name__ == '__main__':
    main()