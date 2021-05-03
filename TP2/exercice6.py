import os, time, random, sys 
for i in range(4) :
    if os.fork() != 0 : 
        break 
random.seed() 
delai = random.randint(0,4) 
time.sleep(delai)
if i < 3:
    os.wait()
print("Mon  nom  est  "  +  chr(ord('A')+i)  +  "  j  ai  dormi  "  + str(delai) +  "  ") 
sys.exit(0)

#Mon  nom  est  B  j  ai  dormi  2  secondes
#Mon  nom  est  A  j  ai  dormi  1  secondes
#Mon  nom  est  C  j  ai  dormi  1  secondes
#Mon  nom  est  D  j  ai  dormi  3  secondes
#Mon  nom  est  D  j  ai  dormi  4  secondes