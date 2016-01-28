import nmap


class NetworkManager(nmap.PortScanner):
    def __init__(self):
        super().__init__()

    def get_hosts_list(self):
        enable_hosts = self.scan(hosts='192.168.2.1-255', ports='22')
        return enable_hosts['scan'].keys()
