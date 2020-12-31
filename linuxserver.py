import threading
from socket import *
import time
from threading import Thread 
from socketserver import ThreadingMixIn 
import struct
from coloring import text_colors
from scapy.arch import get_if_addr

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,conn,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.sock = conn
        self.client_name = ""
        self.count = 0
        print (f"{text_colors.WARNING}[+] New server socket thread started for {text_colors.ENDC}" + ip + f"{text_colors.WARNING}:{text_colors.ENDC}" + str(port)) #to remove
 
    def run(self): 
        #while True : 
            data = conn.recv(2048).decode()
            print(f"{text_colors.OKGREEN}Server received client name:", data) #to remove
            #MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            #if MESSAGE == 'exit':
            #    break
            #conn.send(MESSAGE.encode())  

            # receiving name - assuming data is the msg from the client *after* connecting
            self.client_name = data

    def send_msg(self, sock2, msg):
        sock2.send(msg.encode())
        # maybe add here a while true for listening & store all packages
        # count the amount of packages and set to a field in the thread
        # in the  gamme func we will have a count for each team and then announce the winner by it
    def play(self, sock2):
        count = 0
        while True:
            letter = sock2.recv(1) #recieve from client
            if letter.decode()=='!': #check what we got
                break
            #print(letter) #print the letter (temporary)
            count = count+1
        self.count = count

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

        msg = f"{text_colors.OKCYAN}Welcome to Keyboard Spamming Battle Royale.\nGroup 1:\n==\n"
        for name in group1:
            msg += name.client_name + '\n' 
        
        msg += f"{text_colors.OKCYAN}Group 2:\n==\n" 
        for name in group2:
            msg += name.client_name + '\n' 
        
        msg += f"{text_colors.OKCYAN}Quick! Start pressing keys on your keyboard as fast as you can!!\n"

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
        serverSocket.sendto(struct.pack('!IBH',0xfeedbeef,0x2,TCP_PORT), ("172.1.255.255", UDP_PORT))


TCP_PORT = 12004 
BUFFER_SIZE = 1024 

UDP_PORT = 13117

udp_ip = get_if_addr('eth1')

while True:
    serverSocket = socket(AF_INET, SOCK_DGRAM) #open UDP broadcast connection
    serverSocket.bind((udp_ip, 0))

    print(f"{text_colors.OKBLUE}Server started, listening on IP address "+udp_ip) #to change
    timeout = 10

    timeout_start = time.time()
    printit() #send UDP broadcast 10 times, in different thread

    tcpServer = socket(AF_INET, SOCK_STREAM) #open TCP connection with the port sent
    tcpServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
    tcpServer.bind((udp_ip, TCP_PORT)) 
    threads = [] 
    tcpServer.settimeout(10)
    
    while time.time() < timeout_start + timeout:  
        try:
            tcpServer.listen(4) #how many non accepted connections are allowed
            print (f"{text_colors.HEADER}Multithreaded Python server : Waiting for connections from TCP clients..." ) #to remove
            (conn, (ip,port)) = tcpServer.accept() #connect TCP with client
            newthread = ClientThread(conn,ip,port) 
            newthread.start() 
            threads.append(newthread) 
        except Exception:
            break

    print(f"{text_colors.WARNING}time over") #to remove
    game()

    again = input(f"{text_colors.OKGREEN}The game is over!\nDo you want another round? y for yes, anything else for no: ") 

    for t in threads: 
        t.join() 
    if again!='y':
        tcpServer.close()
        break
