import socket as Socket

address = "localhost" # localhost гарантирует, что клиенты запущены только на локальном компьютере
port = 801
dataPackageSize = 1024 # максимальный размер буфера в байтах
encoding = "utf-8"

# если пользователь отключился не через q
def getDataPackage(connection):
    try:
        data = connection.recv(dataPackageSize) # получение данных от client (здесь будет message)
        return data
    except ConnectionError:
        return 0

def startServer():
    socket = Socket.socket() # создаем объект сокета сервера
    socket.settimeout(60)
    try:
        socket.bind((address, port)) # присваиваем экземпляру socket IP-адрес и номер порта
    except OSError:
        print("Port number", port, "is occupied")
        exit()
    socket.listen() # переводим сервер в режим приёма соединений
    while 1:
        try:
            connection, clientAddress = socket.accept() # получение входящих подключений:
                                                        # через conn сервер взаимодействует с клиентом
                                                        # address - адрес подключившегося клиента
        # Если функция accept() ожидает клиента дольше минуты - выбрасывается TimeoutException
        except TimeoutError:
            print("There have been no clients for 1 minute")
            exit()

        print(f"{clientAddress}, has connected")
        while data := getDataPackage(connection):
            data=data.decode(encoding) # декодируем набор байт
            print("Servser>",data[::-1])
            connection.sendall(data.encode(encoding)) # отправляем ответ client
        print(f"{clientAddress} has disconnected")

if __name__ == '__main__':
    startServer()