import nmap


class NetworkManager(nmap.PortScanner):
    def __init__(self):
        super().__init__()

    def get_hosts_list(self, known_list_ip=None):
        list_ip = known_list_ip if known_list_ip else '192.168.0.1-255'
        enable_hosts = self.scan(hosts=list_ip, ports='22')
        ip = enable_hosts['scan'].keys()
        hostnames = [enable_hosts['scan'][i]['hostnames'] for i in ip]
        name = [hostname[0]['name'] if len(hostname) else '' for hostname in hostnames]
        status = [enable_hosts['scan'][i]['status']['state'] for i in ip]
        return list(zip(name, ip, status))
