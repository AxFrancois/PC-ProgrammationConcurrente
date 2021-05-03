import sys,os,time

import os , sys 
# Communication par tube anonyme 

N = int(sys.argv[1])
for i in range(N):
        pid=os.fork()  
        if pid == 0 :
             # je suis le fils
            my_pid=os.getpid()
            my_ppid=os.getppid()
            print(f"mon pid = {my_pid}, et mon ppid = {my_ppid}")
            time.sleep(2*i)
            sys.exit(i)

for i in range(N):
    pid_fils,etat = os.wait()
    print(f"le fil de pid {pid_fils}, et sont etat est {os.WEXITSTATUS(etat)}")

sys.exit(0)