import socket

BUFFER_SIZE = 4096 # Send 4096 bytes each time step
RECEIVER = '<RECEIVER>'
SENDER = '<SENDER>'

class Client:
    def __init__(self, host: str, port: str, client_username: str) -> None:
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connection.connect((host, port))
        self._username = client_username

    def __del__(self) -> None:
        self._connection.close()

    def send_message(self, message: str):
        self._connection.sendall(f'{self._username}: {message}'.encode())

    def define_type(self, type: str):
        self._connection.sendall(f'{type}'.encode())

    def receive(self):
        message = self._connection.recv(BUFFER_SIZE).decode()
        print(message)