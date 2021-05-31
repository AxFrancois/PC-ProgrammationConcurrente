import time,os,sys,signal

def arreterProgramme(signal, frame) :
    print("This is the end")
    print("Hold your breath and count to ten")
    sys.exit(0)
    
signal.signal(signal.SIGINT, arreterProgramme)

while True:
    time.sleep(2)
    print("Je boucle") 

