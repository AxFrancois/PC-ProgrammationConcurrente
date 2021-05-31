import sys
import multiprocessing as mp

liste = [1,68,5,5,26,5,98,4,5,1,47,2,3,14,8,99,2]
N = len(liste)
sem = mp.Semaphore(1)
mutex = mp.Lock()

Somme = mp.Value('i', 0)

def fP1(pliste):
    j = 1
    SommeImpairs = 0
    while j <= N-1:
        SommeImpairs += pliste[j]
        j += 2
    sem.acquire()
    mutex.acquire()
    Somme.value += SommeImpairs
    mutex.release()
    sem.release()
    sys.exit(0)
    
def fP2(pliste):
    i = 0
    SommePairs = 0
    while i <= N:
        SommePairs += pliste[i]
        i += 2
    sem.acquire()
    mutex.acquire()
    Somme.value += SommePairs
    mutex.release()
    sem.release()
    sys.exit(0)


P1 = mp.Process(target = fP1, args = (liste,))
P2 = mp.Process(target = fP2, args = (liste,))

P1.start()
P2.start()

P1.join()
P2.join()

print(Somme.value)
print("Verif :", sum(liste))

sys.exit(0)