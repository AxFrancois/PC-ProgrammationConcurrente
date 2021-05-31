import sys,time
import multiprocessing as mp


semA = mp.Semaphore(0)
semB = mp.Semaphore(0)
semC = mp.Semaphore(0)
semD = mp.Semaphore(0)
semE = mp.Semaphore(0)

def A():
    print("Je suis A")
    time.sleep(1)
    print("A fini")
    semA.release()
    semA.release()
    semA.release()
    sys.exit(0)

def B():
    semA.acquire()
    print("Je suis B")
    time.sleep(3)
    print("B fini")
    semB.release()
    sys.exit(0)

def C():
    semA.acquire()
    print("Je suis C")
    time.sleep(1)
    print("C fini")
    semC.release()
    sys.exit(0)

def D():
    semA.acquire()
    print("Je suis D")
    time.sleep(2)
    print("D fini")
    semD.release()
    sys.exit(0)

def E():
    semB.acquire()
    semC.acquire()
    print("Je suis E")
    time.sleep(3)
    print("E fini")
    semE.release()
    sys.exit(0)

def F():
    semE.acquire()
    semD.acquire()
    print("Je suis F")
    time.sleep(2)
    print("F fini")
    sys.exit(0)


P1 = mp.Process(target = A, args = ())
P2 = mp.Process(target = B, args = ())
P3 = mp.Process(target = C, args = ())
P4 = mp.Process(target = D, args = ())
P5 = mp.Process(target = E, args = ())
P6 = mp.Process(target = F, args = ())

P1.start()
P2.start()
P3.start()
P4.start()
P5.start()
P6.start()

P1.join()
P2.join()
P3.join()
P4.join()
P5.join()
P6.join()

sys.exit(0)