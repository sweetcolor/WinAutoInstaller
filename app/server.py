import os
import socket
import pickle
from lib.thread_decorator import thread


class Server:
    def __init__(self):
        host = ''
        port = 2000

        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_obj.bind((host, port))
        self.socket_obj.listen(5)
        self.connections = dict()

    @thread
    def open_connection(self):
        while True:
            connection, address = self.socket_obj.accept()
            self.connections[address[0]] = connection
            print('Connecting ' + str(address))

    def send_data(self, hosts, installers):
        for host in hosts:
            if host in self.connections:
                self._send_installers(host, installers)

    @thread
    def _send_installers(self, host, installers):
        installers_count = str(len(installers)).encode()
        self.connections[host].send('{:016x}'.format(len(installers_count)).encode())
        self.connections[host].send(installers_count)
        for installer_desc in installers:
            desc_bin = pickle.dumps(installer_desc[::2])
            print(desc_bin)
            print(len(desc_bin))
            self.connections[host].send('{:016x}'.format(len(desc_bin)).encode())
            self.connections[host].send(desc_bin)
            installer_file = open(installer_desc[1], 'rb')
            installer_size = os.path.getsize(installer_desc[1])
            self.connections[host].send('{:016x}'.format(installer_size).encode())
            self.connections[host].send(installer_file.read())

    def close_connection(self):
        for connection in self.connections:
            connection.close()
