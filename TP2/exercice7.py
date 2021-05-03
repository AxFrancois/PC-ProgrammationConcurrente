import os, sys
N = 3
for i in range(N):
    if os.fork() != 0:
        if os.fork() != 0:
            os.fork()


print("Bonjour")
sys.exit(0)