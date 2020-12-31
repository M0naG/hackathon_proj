from socket import *
serverName = 'localhost'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode('ascii'))
clientSocket.close()