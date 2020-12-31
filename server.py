from socket import *
import keyboard
serverPort = 12008
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    while 1:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            connectionSocket.send(capitalizedSentence)
            break
    connectionSocket.close()