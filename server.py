import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5055))
clients = []
while True:
    data, addres = sock.recvfrom(1024)
    print(addres[0], addres[1])
    if addres not in clients:
        clients.append(addres)
    for client in clients:
        if client == addres:
            continue
        sock.sendto(data, client)