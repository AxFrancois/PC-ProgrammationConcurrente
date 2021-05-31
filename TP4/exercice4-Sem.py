import sys,time,random
import multiprocessing as mp


N = 5

semQ1Vide = mp.Semaphore(1)
semQ2Vide = mp.Semaphore(1)
semConso1 = mp.Semaphore(0)
semConso2 = mp.Semaphore(0)

Q1 = mp.Queue()
Q2 = mp.Queue()

def P1(N):
    for i in range(N):
        semQ1Vide.acquire()
        val = random.randint(0,9)
        Q1.put(val)
    sys.exit(0)

def P2(N):
    for i in range(N):
        semQ2Vide.acquire()
        val = random.randint(0,9)
        Q2.put(val)
    sys.exit(0)
    
def C1(N):
    for i in range(N):
        semConso2.release()
        val = Q1.get()
        semQ1Vide.release()
        print("C1",val)
        semConso1.acquire()

def C2(N):
    for i in range(N):
        semConso2.acquire()
        val = Q2.get()
        semQ2Vide.release()
        print("C2",val)
        semConso1.release()



P1 = mp.Process(target = P1, args = (N,))
P2 = mp.Process(target = P2, args = (N,))
P3 = mp.Process(target = C1, args = (N,))
P4 = mp.Process(target = C2, args = (N,))


P1.start()
P2.start()
P3.start()
P4.start()

P1.join()
P2.join()
P3.join()
P4.join()

sys.exit(0)