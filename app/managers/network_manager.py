import nmap
from PyQt5.QtCore import QObject, pyqtSignal
from app.services.server import Server


class NetworkManager(QObject, nmap.PortScanner):
    appendToLogFile = pyqtSignal(str, str, name='appendToLogFile')
    updateProgressBar = pyqtSignal(str, int, name='updateProgressBar')

    def __init__(self):
        QObject.__init__(self)
        nmap.PortScanner.__init__(self)
        self.server = Server(self)
        self.server.open_connection()

    def get_hosts_list(self, known_list_ip=None):
        list_ip = known_list_ip if known_list_ip else '192.168.0.1-255'
        enable_hosts = self.scan(hosts=list_ip, ports='22')
        ip = enable_hosts['scan'].keys()
        host_names = [enable_hosts['scan'][i]['hostnames'] for i in ip]
        name = [hostname[0]['name'] if len(hostname) else '' for hostname in host_names]
        status = ['up' if i in self.server.connections else 'down' for i in ip]
        return list(zip(name, ip, status))

    def run_installers_on_hosts(self, hosts, installers):
        self.server.send_data(hosts, installers)
