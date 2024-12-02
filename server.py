import socket as Socket

address = "localhost" # localhost ensures that clients are running only on the local computer
port = 1801
dataPackageSize = 1024 # max size of buffer in bytes 
encoding = "utf-8"

# if the user disconnected not using 'q'
def getDataPackage(connection):
    try:
        data = connection.recv(dataPackageSize) #receiving data from client (here will be message)
        return data
    except ConnectionError:
        return 0

def startServer():
    socket = Socket.socket() # creating a server socket object
    socket.settimeout(180)
    try:
        socket.bind((address, port)) #assign the socket instance an IP address and a port number
    except OSError:
        print("Port number", port, "is occupied")
        exit()
    socket.listen() # switching the server to connection acceptance mode(waiting for the message)
    while 1:
        try:
            connection, clientAddress = socket.accept() # receiving incoming connections
                                                        # using  conn server communicating with client
                                                        # address - address of connected client
        # if function accept() if waiting for client more than 1 minute -  throw TimeoutException
        except TimeoutError:
            print("There have been no clients for 3 minutes")
            exit()

        print(f"{clientAddress}, has connected")
        while data := getDataPackage(connection):
            data=data.decode(encoding) # decoding a set of bytes
            print("Servser>",data[::-1])
            connection.sendall(data.encode(encoding)) # send an answer to client
        print(f"{clientAddress} has disconnected")

if __name__ == '__main__':
    startServer()
