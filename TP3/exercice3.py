import os,sys,random

pipeEntree1 = "sommeImpairs"
pipeEntree2 = "sommePairs"
pipeSortie1 = "nombresImpairs"
pipeSortie2 = "nombresPairs"

os.unlink(pipeEntree1)
os.unlink(pipeEntree2)
os.unlink(pipeSortie1)
os.unlink(pipeSortie2)

os.mkfifo(pipeEntree1,644)
os.mkfifo(pipeEntree2,644)
os.mkfifo(pipeSortie1,644)
os.mkfifo(pipeSortie2,644)

fdr1 = os.open(pipeSortie1, os.O_WRONLY)
fdr2 = os.open(pipeSortie2, os.O_WRONLY)

N = int(sys.argv[1])

for i in range(N):
    nombre = random.randint(0,9)
    if nombre%2 == 0:
        os.write(fdr2,str(nombre).encode())
    else:
        os.write(fdr1,str(nombre).encode())

#pose -1 dans chaque tube
os.write(fdr2,str(-1).encode())
os.write(fdr1,str(-1).encode())

#Recupère les sommes et les ajoutes, puis print
fdq2 = os.open(pipeEntree2, os.O_RDONLY)
fdq1 = os.open(pipeEntree1, os.O_RDONLY)

val1 = str(os.read(fdq1,100))
val2 = str(os.read(fdq2,100))

os.unlink(pipeEntree1)
os.unlink(pipeEntree2)
os.unlink(pipeSortie1)
os.unlink(pipeSortie2)

nombre1 = int(val1[2:-1])
nombre2 = int(val2[2:-1])

resultat = nombre1 + nombre2
print(resultat)