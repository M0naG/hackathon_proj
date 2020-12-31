from socket import *
import struct
import time
import sys, termios, atexit
from select import select
from coloring import text_colors

# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def getch():
    return sys.stdin.read(1)

def kbhit():
    dr,dw,de = select([sys.stdin], [], [], 0)
    return dr != []

if __name__ == '__main__':
    atexit.register(set_normal_term)
    set_curses_term()

UDP_PORT = 13117

BUFFER_SIZE = 1024

while True:
    s=socket(AF_INET, SOCK_DGRAM) #open UDP socket
    s.bind(('',UDP_PORT)) #listen to broadcasts on UDP on port
    print(f"{text_colors.OKBLUE}Client started, listening for offer requests...") #to remove
    (m,(ip,port)) = s.recvfrom(BUFFER_SIZE) #receive broadcast and store it in m=(message,(ip,port))
    msg = struct.unpack('!IBH',m) #get the broadcast message
    print(msg+m[1])

    s.close() #close udp
    print(f"{text_colors.OKGREEN}Received offer from {ip}, attempting to connect...") #to change
    host = gethostname() 

    MESSAGE = input(f"{text_colors.WARNING}tcpClientA: Enter message/ Enter exit:") #to remove
    tcpClientA = socket(AF_INET, SOCK_STREAM) 
    tcpClientA.connect((ip, int(msg[2]))) #open TCP connection with the port that came in the udp message

    tcpClientA.send(MESSAGE.encode()) 
    data = tcpClientA.recv(BUFFER_SIZE)
    print(f"{text_colors.OKBLUE}Client received data:", data.decode()) #to change

    timeout = 10 #seconds num

    timeout_start = time.time() #time started

    count = 0
    while time.time() < timeout_start + timeout: #do this in timeout seconds
            if kbhit():
                s = getch() #get the letter clicked on
                tcpClientA.send(s.encode()) #send the letter to the server
                
    tcpClientA.send('!'.encode()) #announce no more letters, 10 seconds passed

    again = input(f"{text_colors.OKGREEN}The game is over!\nDo you want another round? y for yes, anything else for no: ") 


    if again!='y':
        tcpClientA.close() #close TCP connection
        break
