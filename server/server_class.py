from threading import Thread
from util.type import Types

import socket

BUFFER_SIZE = 4096 # Send 4096 bytes each time step
MAX_CLIENTS = 10

class Server:
    def __init__(self, host: str, port: str) -> None:
        self._keep_alive = True
        self._broadcast_list = []
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connection.bind((host, port))
        self._connection.listen(MAX_CLIENTS)

    def __del__(self) -> None:
        self._connection.close()

    def close(self) -> None:
        self._keep_alive = False

    def _threaded(self, connection: socket, address: str) -> None:
        while (True):
            client_recv = connection.recv(BUFFER_SIZE)
            if (not client_recv):
                print(f'Encerrando a conexão com {address}')
                break
            message = client_recv.decode()
            for conn in self._broadcast_list:
                conn.sendall(f'{message}'.encode())

    def receive_connection(self) -> None:
        client, address = self._connection.accept()
        print(f'Conectado com {address}')
        client_recv = client.recv(BUFFER_SIZE)
        if (client_recv.decode() == Types.RECEIVER.value):
            self._broadcast_list.append(client)
            Thread(target=self._threaded, args=(client, address, )).start()
        else:
            Thread(target=self._threaded, args=(client, address, )).start()
