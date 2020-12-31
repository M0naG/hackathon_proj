import threading
from socket import *
import time
import struct
from threading import Thread 
from socketserver import ThreadingMixIn 
import struct

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] New server socket thread started for " + ip + ":" + str(port))
 
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print("Server received data:", data.decode())
            MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE.encode())  

TCP_PORT = 12004 
BUFFER_SIZE = 1024 

UDP_PORT = 13117

serverSocket = socket(AF_INET, SOCK_DGRAM) #open UDP broadcast connection
serverSocket.bind(('', UDP_PORT))
print("Server started, listening on IP address ???")
timeout = 10

def printit():
  if time.time() < timeout_start + timeout:
    threading.Timer(1.0, printit).start()
    serverSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    serverSocket.sendto(struct.pack('!IBH',0xfeedbeef,0x2,TCP_PORT), ('<broadcast>', 12345))

timeout_start = time.time()
printit() #send UDP broadcast 10 times, in different thread

tcpServer = socket(AF_INET, SOCK_STREAM) #open TCP connection with the port sent
tcpServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
tcpServer.bind(('', TCP_PORT)) 
threads = [] 
 
while time.time() < timeout_start + timeout: 
    tcpServer.listen(4) #how many non accepted connections are allowed
    print ("Multithreaded Python server : Waiting for connections from TCP clients..." )
    (conn, (ip,port)) = tcpServer.accept() #connect TCP with client
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 