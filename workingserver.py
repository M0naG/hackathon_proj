import threading
from socket import *
import time
import struct
from threading import Thread 
from socketserver import ThreadingMixIn 
import struct

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,conn,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.sock = conn
        self.client_name = ""
        self.count = 0
        print ("[+] New server socket thread started for " + ip + ":" + str(port))
 
    def run(self): 
        #while True : 
        data = self.sock.recv(2048).decode()
        print("Server received client name:", data)
        #MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
        #if MESSAGE == 'exit':
        #    break
        #conn.send(MESSAGE.encode())  

        # receiving name - assuming data is the msg from the client *after* connecting
        self.client_name = data

    def send_msg(self, sock2, msg):
        self.sock.send(msg.encode())
        # maybe add here a while true for listening & store all packages
        # count the amount of packages and set to a field in the thread
        # in the game func we will have a count for each team and then announce the winner by it
    def play(self, sock2):
        count = 0
        while True:
            letter = self.sock.recv(1) #recieve from client
            if letter.decode()=='!': #check what we got
                break
            #print(letter.decode()) #print the letter (temporary)
            count = count+1
        self.count = count


TCP_PORT = 12004 
BUFFER_SIZE = 1024 

UDP_PORT = 13117

serverSocket = socket(AF_INET, SOCK_DGRAM) #open UDP broadcast connection
serverSocket.bind(('', UDP_PORT))
print("Server started, listening on IP address ???")
timeout = 10

def split(arr, size):
    if(size>=1):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
    else: 
        arrs = [arr]
    return arrs

def game():
    points1 = 0
    points2 = 0
    threads2 = threads
    if len(threads) > 0:
        names = []
        for t in threads:
            names.append(t.client_name)
        arr = split(threads2,(int)(len(threads2)/2))
        if(len(arr)>1):
            group1 = arr[0]
            group2 = arr[1]
        else:
            group1 = arr[0]
            group2 = []

        msg = "Welcome to Keyboard Spamming Battle Royale.\nGroup 1:\n==\n"
        for name in group1:
            msg += name.client_name + '\n' 
        
        msg += "Group 2:\n==\n" 
        for name in group2:
            msg += name.client_name + '\n' 
        
        msg += "Quick! Start pressing keys on your keyboard as fast as you can!!\n"

        for t in threads:
            t.send_msg(t.sock,msg)

        for t in threads:
            t.play(t.sock)

        for t in group1:
            points1 += t.count
        
        for t in group2:
            points2 += t.count

        print(points1)
        print(points2)

        # now listen for packages - maybe add it from in send func

        # count the amunt of msgs for each team and create a msg about the winner



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
tcpServer.settimeout(10)
 
while time.time() < timeout_start + timeout:  
    try:
        tcpServer.listen(5) #how many non accepted connections are allowed
        print ("Multithreaded Python server : Waiting for connections from TCP clients..." )
        (conn, (ip,port)) = tcpServer.accept() #connect TCP with client
        newthread = ClientThread(conn,ip,port) 
        newthread.start() 
        threads.append(newthread) 
    except Exception:
            break

print("time over")
game()

for t in threads: 
    t.join() 