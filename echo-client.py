import socket
import sys
import pickle

host = 'localhost'
port = 2000


massage = open('7z920.exe', mode='rb').read()
# massage = pickle.dumps(text)
if len(sys.argv) > 1:
    host = sys.argv[1]

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect((host, port))

socket_obj.send(massage)
# curr_get_data = socket_obj.recv(1024)
# res_data = b''
# while curr_get_data:
#     res_data += curr_get_data
#     curr_get_data = socket_obj.recv(1024)
# print('++', len(res_data), '++')
# print('Get from server: ', pickle.loads(res_data))

socket_obj.close()
