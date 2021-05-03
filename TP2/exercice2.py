import os

for i in range(3):
    print("i : {} je suis le processus : {}, mon pere est : {}, retour : {} ".format(i, os.getpid(), os.getppid(), os.fork()))

os._exit(0)