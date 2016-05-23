import _thread
import os
import pickle
import socket

from app.lib.thread_decorator import thread


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

    def _open_connection(self):
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
        self.get_log_file(host)

    @thread
    def get_log_file(self, host):
        bin_buff_size = 1024
        num_buff_size = 16
        log_file_size = int(self.connections[host].recv(num_buff_size).decode(), num_buff_size)
        log_file = open('win_auto_installer.log', 'w')
        for i in range(log_file_size // bin_buff_size):
            self.connections[host].revc(bin_buff_size)
            log_file_part = self.connections[host].recv(bin_buff_size)
            log_file.write(log_file_part.decode())
            diff = bin_buff_size - len(log_file_part)
            while diff:
                log_file_part = self.connections[host].recv(diff)
                log_file.write(log_file_part.decode())
                diff -= len(log_file_part)
        log_file_part = self.connections[host].recv(log_file_size % bin_buff_size)
        log_file.write(log_file_part.decode())
        log_file.close()

    def close_connection(self):
        for connection in self.connections:
            connection.close()
