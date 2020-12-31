from socket import *
serverName = 'localhost'
serverPort = 12008
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:').encode('ascii')
clientSocket.send(sentence)
while True:
    modifiedSentence = clientSocket.recv(1024).decode('ascii')
    if modifiedSentence!='':
        print('From Server: ' + modifiedSentence)
clientSocket.close()