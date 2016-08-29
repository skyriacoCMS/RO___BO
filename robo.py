import time
import sys

for i in range(1,4):
 ll = i%2
 fname="/home/savvas/RO___BO/robo"+str(ll)+".txt"
 f1 = open(fname,"rb")
 for line in f1: 
    k = line.rstrip()
    str(k)
    print (k)    #, end='\r')


 for j in range(0,15):
    if(i != 3):
        sys.stdout.write("\033[F")

 time.sleep(1) 

