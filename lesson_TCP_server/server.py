import select
import socket


SERVER_ADDRESS = ('localhost', 8686)
MAX_CONNECTIONS = 10
INPUTS = list()
OUTPUT = list()


def get_non_blocking_server_socket():
	# create server, don't blocked from main thread
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(socket.AF_INET, socket.SOCK_STREAM)

	server.setblocking(0)

	# bind server to address and port
	server.bind(SERVER_ADDRESS)

	# set max connection count
	server.listen(MAX_CONNECTIONS)

	return server


def handle_readables(readables, server):
	"""
	event on input
	:param readables:
	:param server:
	:return:
	"""

	for resource in readables:
		# if event on server socket, create new connection
		if resource is server:
			connection, client_address = resource.accept()
			connection.setblocking(0)
			INPUTS.append(connection)
			print(f"new connection from {client_address}")
		else:
			data = ""
			try:
				data = resource.recv(1024)
			except ConnectionResetError:
				pass

			if data:
				# print all response to console
				print(f"getting data: {data}")
				if resource not in OUTPUT:
					OUTPUT.append(resource)

			# if data not found, but event,
			else:
				clear_resource(resource)


def clear_resource(resource):
	"""
	clear resource on socket
	:param resource:
	:return:
	"""
	if resource in OUTPUT:
		OUTPUT.remove(resource)
	if resource in INPUTS:
		INPUTS.remove(resource)
	resource.close()

	print("closing connection", resource)


def handle_writables(writables):
	# buffer cleaned
	for resource in writables:
		try:
			resource.send(b"Hello from server!")
		except OSError:
			clear_resource(resource)


if __name__ == "__main__":
	print("Start programm")

	# create server socket without blocking
	server_socket = get_non_blocking_server_socket()
	INPUTS.append(server_socket)

	print("server is running, please, press ctrl+c to stop")

	try:
		while INPUTS:
			readables, writables, exceptional = select.select(INPUTS, OUTPUT, INPUTS)
			handle_readables(readables, server_socket)
			handle_writables(writables)
	except KeyboardInterrupt:
		clear_resource(server_socket)
		print("Server stopped! Thank you for using!")

