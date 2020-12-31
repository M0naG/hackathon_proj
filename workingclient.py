from socket import *
import struct
import msvcrt 
import time

BUFFER_SIZE = 1024 

s=socket(AF_INET, SOCK_DGRAM) #open UDP socket
s.bind(('',12345)) #listen to broadcasts on UDP on port
print("Client started, listening for offer requests...")
m = s.recvfrom(BUFFER_SIZE) #receive broadcast and store it in m=(message,(ip,port))
msg = struct.unpack('!IBH',m[0]) #get the broadcast message
print(msg+m[1])

s.close() #close udp
print("Received offer from ???, attempting to connect...") 
host = gethostname() 

MESSAGE = input("tcpClientA: Enter message/ Enter exit:") 
tcpClientA = socket(AF_INET, SOCK_STREAM) 
tcpClientA.connect((host, int(msg[2]))) #open TCP connection with the port that came in the udp message

tcpClientA.send(MESSAGE.encode()) 
data = tcpClientA.recv(BUFFER_SIZE)
print("Client received data:", data.decode())

timeout = 10 #seconds num

timeout_start = time.time() #time started

count = 0
while True:
    if time.time() < timeout_start + timeout: #do this in timeout seconds
        if msvcrt.kbhit():
            s = msvcrt.getch() #get the letter clicked on
            tcpClientA.send(bytes(s)) #send the letter to the server
    else:
        break

tcpClientA.send('!'.encode()) #announce no more letters, 10 seconds passed

tcpClientA.close() #close TCP connection