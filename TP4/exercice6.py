import time,os,sys,signal

def arreterProgramme(signal, frame) :
    global Affichage
    if signal == 10:
        Affichage = True
    elif signal == 12:
        print("This is the end")
        print("Hold your breath and count to ten")
        sys.exit(0)

Affichage = False
pid = os.fork()

if pid != 0 : #Processus Pere 
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    for i in range(1,10):
        print(f"{i} secondes sont passées")
        if i == 3 or i == 5:
            os.kill(pid, signal.SIGUSR1)
        time.sleep(1)
    print("bakala, il est temps pour toi de disparaitre, za warldo !!")
    os.kill(pid, signal.SIGUSR2)

else:#Processus 
    signal.signal(signal.SIGUSR1, arreterProgramme)
    signal.signal(signal.SIGUSR2, arreterProgramme)
    while True:
        time.sleep(0.1)
        if Affichage:
            print("Je boucle, tu ne peux pas m'arreter !")
            Affichage = False