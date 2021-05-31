import time,os,sys,signal

pid = os.fork()

if pid != 0 : #Processus Pere 
    for i in range(1,4):
        time.sleep(1)
        print(f"{i} secondes sont passées")
    print("bakala, il est temps pour toi de disparaitre, za warldo !!")
    os.kill(pid, signal.SIGKILL)
else:#Processus fils
    while True:
        print("Je boucle, tu ne peux pas m'arreter !")
        time.sleep(1)