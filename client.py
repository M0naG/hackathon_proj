from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:').encode('ascii')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024).decode('ascii')
print('From Server: ' + modifiedSentence)
clientSocket.close()