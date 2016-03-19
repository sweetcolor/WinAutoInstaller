import nmap
import socket
import os


class NetworkManager(nmap.PortScanner):
    def __init__(self):
        super().__init__()

    def get_hosts_list(self, known_list_ip=None):
        list_ip = known_list_ip if known_list_ip else '192.168.0.1-255'
        enable_hosts = self.scan(hosts=list_ip, ports='22')
        ip = enable_hosts['scan'].keys()
        host_names = [enable_hosts['scan'][i]['hostnames'] for i in ip]
        name = [hostname[0]['name'] if len(hostname) else '' for hostname in host_names]
        status = [enable_hosts['scan'][i]['status']['state'] for i in ip]
        return list(zip(name, ip, status))

    def run_installers_on_hosts(self, hosts, installers):
        pass

    def run_server(self):
        host = ''
        port = 2000

        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.bind((host, port))
        socket_obj.listen(5)

        while True:
            connection, address = socket_obj.accept()
            print('Connecting ' + str(address))
