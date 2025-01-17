import threading
import random
from socket import *
import time
import struct
from threading import Thread 
from socketserver import ThreadingMixIn 
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
       # print (f"{text_colors.WARNING}[+] New server socket thread started for {text_colors.ENDC}" + ip + f"{text_colors.WARNING}:{text_colors.ENDC}" + str(port)) #to remove
 
    def run(self): 
            double_buffer = 2048
        #while True : 
            data = conn.recv(double_buffer).decode()
            #print(f"{text_colors.OKGREEN}Server received client name:", data) #to remove
            #MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            #if MESSAGE == 'exit':
            #    break
            #conn.send(MESSAGE.encode())  

            # receiving name - assuming data is the msg from the client *after* connecting
            self.client_name = data

    def send_msg(self, sock2, msg):
        try:
            sock2.send(msg.encode())
        except:
            return
        # maybe add here a while true for listening & store all packages
        # count the amount of packages and set to a field in the thread
        # in the  gamme func we will have a count for each team and then announce the winner by it
    def play(self, sock2):
        count = 0
        while True:
            letter = sock2.recv(1) #recieve from client
            if(letter.decode()==""):
                break
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
        random.shuffle(threads2)
        arr = split(threads2,(int)(len(threads2)/2))
        if(len(arr)>1):
            group1 = arr[0]
            group2 = arr[1]
        else:
            group1 = arr[0]
            group2 = []

        msg = f"{text_colors.OKCYAN}Welcome to Keyboard Spamming Battle Royale.\nGroup 1:\n==\n"
        group1_names = ""
        for name in group1:
            group1_names += name.client_name + '\n' 
        msg+=group1_names
        
        msg += f"{text_colors.OKCYAN}Group 2:\n==\n"
        group2_names = ""
        for name in group2:
            group2_names += name.client_name + '\n' 
        msg+=group2_names
        
        msg += f"{text_colors.OKCYAN}Quick! Start pressing keys on your keyboard as fast as you can!!\n"

        for t in threads:
            t.send_msg(t.sock,msg)

        for t in threads:
            t.play(t.sock)

        for t in group1:
            points1 += t.count
        
        for t in group2:
            points2 += t.count

        winner = (group1,1,group1_names) if points1>points2 else (group2,2,group2_names)

        for t in threads:
            t.send_msg(t.sock,("""Game over!
Group 1 typed in %i characters. Group 2 typed in %i characters.
Group %i wins!

Congratulations to the winners:
==
%s"""%(points1, points2, winner[1], winner[2])))

def printit():
    if time.time() < timeout_start + timeout:
        threading.Timer(1.0, printit).start()
        serverSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        serverSocket.sendto(struct.pack('!IBH',cookie,mtype,TCP_PORT), (brod_ip, UDP_PORT))
        #big endian, unsigned int, unsigned char, unsigned short

TCP_PORT = 12004 
BUFFER_SIZE = 1024 

UDP_PORT = 13107

cookie = 0xfeedbeef

mtype = 0x2

brod_ip = "172.1.255.255"

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
            tcpServer.listen(5) #how many non accepted connections are allowed
            #print (f"{text_colors.HEADER}Multithreaded Python server : Waiting for connections from TCP clients..." ) #to remove            (conn, (ip,port)) = tcpServer.accept() #connect TCP with client
            (conn, (ip,port)) = tcpServer.accept() #connect TCP with client            
            newthread = ClientThread(conn,ip,port) 
            newthread.start() 
            threads.append(newthread) 
        except Exception:
            break

    #print(f"{text_colors.WARNING}time over") #to remove
    game()

    again = input(f"{text_colors.OKGREEN}Game over, sending out offer requests...\nDo you want another round? y for yes, anything else for no: ")

    for t in threads: 
        t.join() 
    tcpServer.close()
    if again!='y':
        break