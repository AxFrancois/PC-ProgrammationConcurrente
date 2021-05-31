import os,sys


pipeEntree = "nombresPairs"
pipeSortie = "sommePairs"

fdq = os.open(pipeEntree, os.O_RDONLY)
fdr = os.open(pipeSortie, os.O_WRONLY)

entree = str(os.read(fdq,100).decode())

entreeList = list(entree[:-2])
liste = [int(item) for item in entreeList]
somme = sum(liste)

os.write(fdr,str(somme).encode())

os.close(fdr)
os.close(fdq)
sys.exit(0)