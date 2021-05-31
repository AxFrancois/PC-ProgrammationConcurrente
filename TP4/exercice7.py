import time,os,sys,signal

def arreterProgramme(signal, frame) :
    sys.exit(0)

Time = 5
print(f"Entrez un entier en moins de {Time} secondes")
timeOut  = False
pid = os.fork()

if pid != 0 : #Processus Pere
    signal.signal(signal.SIGINT, arreterProgramme)
    for i in range(Time):
        time.sleep(1)
    os.kill(pid, signal.SIGKILL)
    print("Trop tard !!")
    sys.exit(0)
        
else:#Processus fils
    while timeOut == False:
        try:
            Entre = int(input("Svp un entier : "))
            print("Ok merci !!")
            os.kill(pid, signal.SIGKILL)
        except:
            pass