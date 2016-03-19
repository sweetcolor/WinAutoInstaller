import socket
import _thread
import os


class Server:
    def __init__(self):
        host = ''
        port = 2000

        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_obj.bind((host, port))
        self.socket_obj.listen(5)
        self.connections = dict()

    def open_connection(self):
        _thread.start_new_thread(self._open_connection, ())

    def send_data(self, hosts, installers):
        for host in hosts:
            self.connections[host].send()

    def _open_connection(self):
        while True:
            connection, address = self.socket_obj.accept()
            self.connections[address] = connection
            print('Connecting ' + str(address))

    def close_connection(self):
        for connection in self.connections:
            connection.close()
