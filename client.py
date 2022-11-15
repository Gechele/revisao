from socket import *

HOST = 'localhost'
PORT = 5000


s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'5,10')
data = s.recv(1024)
print(data)
s.close()
