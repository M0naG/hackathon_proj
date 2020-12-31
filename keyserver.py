from socket import *
serverPort = 12004
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()
while True:
    letter = connectionSocket.recv(1024) #recieve from client
    if letter.decode()=='done!': #check what we got
        break
    print(letter) #print the letter (temporary)

connectionSocket.close()