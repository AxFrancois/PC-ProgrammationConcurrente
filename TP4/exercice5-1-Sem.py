import sys,time
import multiprocessing as mp


semP1 = mp.Semaphore(0)
semP2 = mp.Semaphore(0)

def fP1():
    print("Je suis P1")
    time.sleep(1)
    print("p1 fini")
    semP1.release()
    semP2.acquire()
    rdv1()
    sys.exit(0)

def fP2():
    print("Je suis P2")
    time.sleep(3)
    print("P2 fini")
    semP2.release()
    semP1.acquire()
    rdv2()
    sys.exit(0)

def rdv1():
    print("je suis le rdv1")
    
def rdv2():
    print("je suis le rdv2")

P1 = mp.Process(target = fP1, args = ())
P2 = mp.Process(target = fP2, args = ())


P1.start()
P2.start()

P1.join()
P2.join()

sys.exit(0)