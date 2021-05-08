#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket


# sock = socket.socket()
# sock.connect(('localhost', 8686))
# sock.send(b"client send")
#
# data = sock.recv(1024)
# sock.close()
#
# print(data)


print("Begin simple client")

# params
MAX_CONNECTIONS = 20
address_to_server = ('localhost', 8686)

# generate clients
clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]

# client params
for client in clients:
	client.connect(address_to_server)

# all client sending
for i in range(MAX_CONNECTIONS):
	clients[i].send(bytes("Hello from client number " + str(i), encoding='UTF-8'))

# get all client responses
for client in clients:
	data = client.recv(1024)
	print(str(data))

print("End simple client")

