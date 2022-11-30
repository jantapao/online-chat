from client.client_class import Client

import signal
import readchar

RECEIVER = '<RECEIVER>'

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
    sender = Client(host, port, None)
    sender.define_type(RECEIVER)
    print('\nPressione Ctrl+C para encerrar a execução...\n')
    while (True):
        sender.receive()


if __name__ == '__main__':
    main()