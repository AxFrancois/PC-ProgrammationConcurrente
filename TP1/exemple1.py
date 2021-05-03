import os

Nb_PROC= 5

for process in range(Nb_PROC):
    pid= os.fork()
    if pid> 0:
        print("Je suis le processus PERE : ", os.getpid())
    else:
        print("Je suis le processus FILS : ", os.getpid())
        os._exit(0)
print("Sortie du processus PERE")