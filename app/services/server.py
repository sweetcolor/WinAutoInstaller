import _thread
import os
import pickle
import socket

from app.services.thread_decorator import thread


class Server:
    def __init__(self, network_manager):
        self.num_buff_size = 16
        self.bin_buff_size = 1024
        self.network_manager = network_manager
        host = ''
        port = 2000
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_obj.bind((host, port))
        self.socket_obj.listen(5)
        self.connections = dict()
        self.names = list()
        self.paths = dict()
        self.full_size_send_data = 0
        self.size_get_data = 0
        self.pickle_names = b''
        self.pickle_scripts = b''

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
                self.names = installers['names']
                self.pickle_names = pickle.dumps(self.names)
                self.paths = installers['paths']
                self.pickle_scripts = pickle.dumps(installers['scripts'])
                self.full_size_send_data = len(self.pickle_names)
                self.full_size_send_data += len(self.pickle_scripts)
                for file in self.paths.values():
                    self.full_size_send_data += os.path.getsize(file)
                self._send_installers(host)

    @thread
    def _send_installers(self, host):
        self.connections[host].send(b'START')
        self._send_data(host, self.pickle_names)
        for name in self.names:
            installer_file = open(self.paths[name], 'rb').read()
            self._send_data(host, installer_file)
        self._send_data(host, self.pickle_scripts)
        self._get_process_installation(host)

    def _send_data(self, host, data):
        self.connections[host].send('{:016x}'.format(len(data)).encode())
        self.connections[host].send(data)

    @thread
    def _get_process_installation(self, host):
        installed_program_count = 0
        while True:
            size = int(self.connections[host].recv(self.num_buff_size).decode(), self.num_buff_size)
            bin_message = self.connections[host].recv(size)
            while len(bin_message) < size:
                size -= len(bin_message)
                bin_message += self.connections[host].recv(size)
            message = bin_message.decode().strip()
            try:
                self.size_get_data += int(message)
                self.network_manager.updateProgressBar.emit(host,
                                                            int(self.size_get_data * 50 / self.full_size_send_data))
            except ValueError:
                self.network_manager.appendToLogFile.emit(host, message)
                if message.endswith('installed.'):
                    installed_program_count += 1
                    self.network_manager.updateProgressBar.emit(host, 50 + installed_program_count * 50 / len(
                        self.names))
                elif message == 'END':
                    return 0

    def close_connection(self):
        for connection in self.connections:
            connection.close()
