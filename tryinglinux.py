import sys, termios, atexit
from select import select
import time

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

timeout = 10 #seconds num

timeout_start = time.time() #time started

count = 0
while time.time() < timeout_start + timeout: 
    if kbhit():
        ch = getch()
        count = count + 1

print (count)