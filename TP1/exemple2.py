import os
Nb_PROC= 5
listeFils= [ ]
for process in range(Nb_PROC):
    pid= os.fork()
    if pid> 0:
        print("Je suis le processus PERE : ", os.getpid())
        listeFils.append(pid)
    else:
        print("Je suis le processus FILS : ", os.getpid())
        os._exit(0)

for p in listeFils:
    os.waitpid(p , 0)
    print("Sortie du processus FILS : ", p)
print("Sortie du processus PERE")