import os
import sys

n=0 
for i in range(1,5):
    fils_pid = os.fork()    #1     
    if (fils_pid > 0) :     #2  
        #os.wait()           #3 Ici on est dans père 
        n = i*2 
        break
        
print("n = ", n)            #4 
sys.exit(0)

#Programme déterministe (car execution toujours dans le même ordre)
#Si on enlève 3 bah c'est plus déterministe
#Exécution : 
#n =  0
#n =  8
#n =  6
#n =  4
#n =  2
