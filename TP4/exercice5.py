import time,os,sys,signal


def arreterProgramme(signal, frame) :
    print("This is the end")
    print("Hold your breath and count to ten")
    sys.exit(0)

pid = os.fork()

if pid != 0 : #Processus Pere 
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    for i in range(1,4):
        time.sleep(1)
        print(f"{i} secondes sont passées")
    print("bakala, il est temps pour toi de disparaitre, za warldo !!")
    os.wait()   #si on met pas cette ligne le père se ferme et le fils n'arrive plus à recevoir le signal d'interruption :(

else:#Processus fils
    signal.signal(signal.SIGINT, arreterProgramme)
    while True:
        print("Je boucle, tu ne peux pas m'arreter !")
        time.sleep(1)