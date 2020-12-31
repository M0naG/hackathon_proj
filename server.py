# hachanot
import socket, time 
import threading 
from socketserver import ThreadingMixIn 
from pygame import event


#def send_broadcast(udp_socket):
    #send broadcast and sleeps for 1 sec
    
class ClientThread(Thread): 

    def __init__(self ,ip, port,client_socket): 
        threading.Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.client_socket = client_socket
        print ("[+] New server socket thread started for " + ip + ":" + str(port)) 

    def run(self): 
        while True : 
            data = client_socket.recv(2048) 
            print ("Server received data:", data)
            MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            client_socket.send(MESSAGE)  # echo    


def setup():
    #UDP socket
    udp_socket = socket.socket()
    tcp_socket = socket.socket()

    udp_socket.bind((socket.gethostname(), 1234)) # the udp socket will now use port 1234
    tcp_socket.bind((socket.gethostname(), 1235))

   #udp_thread = threading.Thread(target = send_broadcast, args=(udp_socket, event)) # a special thread for sending broadcasts
   # udp_thread.start()
   # udp_thread.join()

    cnlt_socks = []
    names = []

    initial_time = time.time()
    timeout = 10
    while True:
        while time.time() < initial_time + timeout:
            # listen
            (client_socket, (ip,port)) = tcp_socket.accept() 
            newthread = ClientThread(ip, port, client_socket) 
            newthread.start() 
            cnlt_socks.append(newthread) 
            # ack = "Welcome to the sever! what is your name?"
            # client_socket.send(bytes(ack, "utf-8"))


if __name__ == "__main__":
    
    print("thread finished...exiting")