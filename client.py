import socket as Socket

from server import port, address,encoding

socket = Socket.socket()

# выполняем подключение к сокету на сервере
try:
	socket.connect((address, port))
except OSError:
	print("The server is not running!")
	exit()

print("\nThe connection to the server is established!")
print("To complete the connection, send a 'q' request \n")

while 1:

	try:
		message = input("Client>")
		if message == "q":
			print("\nThe connection is broken!")
			break
	except KeyboardInterrupt: # программа ждет input, а пользователь отключается не через q
		print("\n\nThe connection is broken!")
		break

	try:
		socket.sendall(message.encode(encoding))
	except OSError: # сервер больше не подключен
		print("\nThe server is not running!")
		break

socket.close()