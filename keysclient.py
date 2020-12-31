import msvcrt 
import time
from socket import *
host = gethostname() 
serverPort = 12004
BUFFER_SIZE = 2000 
tcpClientA = socket(AF_INET, SOCK_STREAM) 
tcpClientA.connect((host, serverPort))

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

tcpClientA.send('done!'.encode()) #announce no more letters, 10 seconds passed
tcpClientA.close()