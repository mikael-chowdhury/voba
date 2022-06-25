import socket
import pickle
import _thread

from crystal_engine.server.config import *

class Server:
    def __init__(self):
        self.host = None

        self.connections = []
        self.variables = {}
        
        self.connection_number = 0

    def threaded_client(self, conn, currentPlayer, first_join):
        if first_join:
            self.host = currentPlayer

        self.connections.append(None)

        while True:
            try:
                data = conn.recv(2048)
                
                try:
                    data = pickle.loads(data)

                    if hasattr(data, "player"):
                        self.connections[currentPlayer] = data.player

                    kvs = {key:value for key, value in data.__dict__.items() if not key.startswith('__') and not callable(key)}

                    for key, value in zip(kvs.keys(), kvs.values()):
                        if key != "player":
                            self.variables[key] = value

                    conn.sendall(pickle.dumps({ "connections": self.connections, "variables": self.variables }))

                except EOFError as e:
                    str(e)
                    self.connections[currentPlayer] = None
                    break

            except ConnectionResetError as e:
                str(e)
                self.connections[currentPlayer] = None
                break

    def start(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.s.bind((ip, port))
        except socket.error as e:
            str(e)

        print("listening for connections")

        self.s.listen()

        while True:
            conn, addr = self.s.accept()

            self.connection_number += 1

            first_join = False

            if len(self.connections) == 0:
                first_join = True

            _thread.start_new_thread(self.threaded_client, (conn, self.connection_number - 1, first_join))