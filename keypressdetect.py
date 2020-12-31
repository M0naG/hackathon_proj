import msvcrt 
import time

timeout = 10 #seconds num

timeout_start = time.time() #time started

count = 0
while time.time() < timeout_start + timeout: #do this in timeout seconds
    s = msvcrt.getch() #get the letter clicked on
    count = count + 1 

print(count) #print letters number