import socket 
from threading import Thread 
from socketserver import ThreadingMixIn 
import struct

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] New server socket thread started for " + ip + ":" + str(port) )
 
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print( "Server received data:", data.decode())
            MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE.encode())  # echo 

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_PORT = 12004 
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

UDP_PORT = 13117

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(('', UDP_PORT))
while True:
    message, clientAddress = udpServer.recvfrom(2048)
    modifiedMessage = message.upper()
    udpServer.sendto(modifiedMessage, clientAddress)

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind(('', TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 
    print ("Multithreaded Python server : Waiting for connections from TCP clients..." )
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 