import nmap

sc = nmap.PortScanner()

r = sc.scan('192.168.2.1-255', '80')
print(sc.command_line())
open('res.txt', 'w').write(str(r))
