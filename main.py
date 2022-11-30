from server.server import start_server
from client.sender import start_sender
from client.receiver import start_receiver
from util.handler import handler

import os
import sys
import signal

def main():
    print('\nPressione Ctrl+C para encerrar a execução...\n')
    signal.signal(signal.SIGINT, handler)
    match sys.argv[1]:
        case '1':
            start_server(sys.argv[2], int(sys.argv[3]))
        case '2':
            start_sender(sys.argv[2], int(sys.argv[3]))
        case '3':
            start_receiver(sys.argv[2], int(sys.argv[3]))

if __name__ == '__main__':
    command = 'python' if os.name == 'nt' else 'python3'
    if (len(sys.argv) != 4):
        print(f'Chamada Correta: {command} main.py [tipo] [host] [porta]')
    else:
        main()