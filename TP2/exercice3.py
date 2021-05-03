import os,sys

print("simultanément")

if os.fork() == 0:
    os.system('ps')
    os.system('ls -l')
    sys.exit(0)

os.system('who')

pid,status=os.wait()

print("successivement")
os.system('who')
os.system('ps')
os.system('ls -l')