#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket


# server address
SERVER_ADDRESS = ('localhost', 8686)

# socket settings
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print("server is running, please, press ctrl+c to stop")

# listen requests
while True:
	# print("listen begin")
	connection, address = server_socket.accept()
	print(f"new connection from {address}")
	# print(connection)

	data = connection.recv(1024)
	print(str(data))

	# send responses
	connection.send(b"Hello from server!")

	connection.close()

