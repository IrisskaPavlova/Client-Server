import socket as Socket

from server import port, address,encoding

socket = Socket.socket()
socket.connect((address, port))

while 1:
	message = input("Client>")
	if message == "q":
		break
	socket.sendall(message.encode(encoding))

socket.close()