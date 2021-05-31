import sys,time
import multiprocessing as mp

sem = mp.Semaphore(0)


Somme = mp.Value('i', 0)

def fP1():
    print("Debut P1")
    time.sleep(5)
    print("T1 fini, fin P1")
    sem.release()
    sys.exit(0)

def fP2():
    sem.acquire()
    print("Debut P2")
    time.sleep(2)
    print("T2 fini, fin P1")
    sys.exit(0)



P1 = mp.Process(target = fP1, args = ())
P2 = mp.Process(target = fP2, args = ())

P1.start()
P2.start()

P1.join()
P2.join()

sys.exit(0)