import socket
import threading

def read_sock():
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
server = '127.0.0.1', 5055
name = input()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5055))
sock.sendto((name + ' connect to server').encode('utf-8'), server)
thread = threading.Thread(target=read_sock)
thread.start()
while True:
    message = input()
    sock.sendto(('['+name+']'+message).encode('utf-8'), server)