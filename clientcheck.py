import socket 
import keypressdetect

host = socket.gethostname() 
port = 12004
BUFFER_SIZE = 2000 
MESSAGE = input("tcpClientA: Enter message/ Enter exit:").encode()
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE)     
    data = tcpClientA.recv(BUFFER_SIZE)
    print (" Client received data:", data)
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")

tcpClientA.close() 