import time
import sys

fowl     = open("/home/savvas/RO___BO/owl.txt","rb")
fowl2    = open("/home/savvas/RO___BO/owl.txt","rb")
fowlpck0 = open("/home/savvas/RO___BO/owlpck0.txt","rb")
fowlpck02= open("/home/savvas/RO___BO/owlpck0.txt","rb")

fowlpck1 = open("/home/savvas/RO___BO/owlpck1.txt","rb")
fowlpck  = open("/home/savvas/RO___BO/owlpck.txt","rb")
fowlfly  = open("/home/savvas/RO___BO/owlfl.txt","rb")



for line in fowl: 
    k = line.rstrip()
    str(k)
    print (k)    #, end='\r')
time.sleep(1) 


for j in range(0,10):
 sys.stdout.write("\033[F")



for line in fowlpck0: 
    k = line.rstrip()
    str(k)
    print (k)    #, end='\r'
time.sleep(1) 



for j in range(0,10):
 sys.stdout.write("\033[F")


for line in fowlpck1: 
    k = line.rstrip()
    str(k)
    print (k)    #, end='\r')
time.sleep(1) 


for j in range(0,10):
 sys.stdout.write("\033[F")



for line in fowlpck: 
    k = line.rstrip()
    str(k)
    print (k)    #, end='\r')
time.sleep(1) 


for j in range(0,10):
 sys.stdout.write("\033[F")

for line in fowlpck02: 
    k = line.rstrip()
    str(k)
    print (k)    #, end='\r')
time.sleep(1) 


for j in range(0,10):
 sys.stdout.write("\033[F")



for line in fowl2: 
    k = line.rstrip()
    str(k)
    print (k)    #, end='\r')
time.sleep(1) 

for j in range(0,10):
 sys.stdout.write("\033[F")

for line in fowlfly: 
    k = line.rstrip()
    str(k)
    print (k)    #, end='\r')






