from socket import *
HOST = 'localhost'
PORT = 5000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()
while True:
    data = conn.recv(1024)   
    #split the data into two numbers and sum
    numbers = str(data, 'utf-8').split(',')
    sum = int(numbers[0]) + int(numbers[1])
    conn.send(bytes(str(sum), 'utf-8'))
    if not data:
        break
    conn.close()
