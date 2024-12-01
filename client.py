import socket as Socket

from server import port, address,encoding

socket = Socket.socket()

# connecting to a socket on the server
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
	except KeyboardInterrupt: #programm is waiting forinput, however the user is disconnecting using not 'q'
		print("\n\nThe connection is broken!")
		break

	try:
		socket.sendall(message.encode(encoding))
	except OSError: # server is not connected anymore
		print("\nThe server is not running!")
		break

socket.close()
