import nmap


class NetworkManager(nmap.PortScanner):
    def __init__(self):
        super().__init__()

    def get_hosts_list(self):
        enable_hosts = self.scan(hosts='192.168.2.1-255', ports='22')
        ip = enable_hosts['scan'].keys()
        hostnames = [enable_hosts['scan'][i]['hostnames'] for i in ip]
        name = [hostname[0]['name'] if len(hostname) else '' for hostname in hostnames]
        status = [enable_hosts['scan'][i]['status']['state'] for i in ip]
        return list(zip(name, ip, status))
