import socket as Socket

address = "localhost"
port = 801
dataPackageSize = 1024
encoding = "utf-8"

def getDataPackage(connection):
	try:
		data = connection.recv(dataPackageSize)
		return data
	except ConnectionError:
		return 0
	
def startServer():
    print()
    socket = Socket.socket()
    socket.bind((address, port))
    socket.listen()
    connection, clientAddress = socket.accept()
    print(f"{clientAddress} has connected")
    while data := getDataPackage(connection):
        data=data.decode(encoding)
        print("Servser>",data[::-1])
        connection.sendall(data.encode(encoding))
    print(f"{clientAddress} has disconnected")
	
if __name__ == '__main__':
	startServer()