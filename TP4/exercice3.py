import time,os,sys,signal

def arreterProgramme(signal, frame) :
    global fin
    if fin:
        fin = False
    else:
        fin = True

fin = False
signal.signal(signal.SIGINT, arreterProgramme)


while True:
    time.sleep(2)
    if fin:
        print("Je boucle") 