from server.server_class import Server

def start_server(host: str, port: str):
    server = Server(host, port)
    while (True):
        server.receive_connection()