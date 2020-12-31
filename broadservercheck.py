import threading
from socket import *
import time
import struct

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

def printit():
    serverSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    serverSocket.sendto(struct.pack('!IBH',0xfeedbeef,0x2,serverPort), ('<broadcast>', 12345))

printit()