"""not working :)"""

import os, sys
param = sys.argv[1:]
source = str(param[0])
chaine = str(param[1])
sortie = str(param[2])
(dfr1,dfw1) = os.pipe()# création d’un tube père-fils
(dfr2,dfw2) = os.pipe()# création d’un tube fils-petit fils

pid1 = os.fork()
if pid1 != 0 :   #père
    #rècupère le fils et écrit le fichier
    os.close(dfw1)
    os.close(dfr2)
    os.close(dfw2)
    
    recu = os.read(dfr1,10)
    print("FINI",recu)
    
else : 
    pid2 = os.fork()
    if pid2 != 0 :   #fils
        #récupère le petit fils et lance le tail
        os.close(dfr1)
        os.close(dfw2)
        
        os.read(dfr2,10)
        os.dup2(dfw1,0)
        
        os.execlp("tail", "tail", "-n 5")

    else:   #petit fils
        #lance le grep 
        os.close(dfr1)
        os.close(dfw1)
        os.close(dfr2)

        #os.dup2(dfw2,0)
        os.close(dfw2)
        
        os.execlp("grep", "grep", "embre texte.txt")#"{} {}".format(chaine,source))


"""
if pid1 != 0 :   #père
    os.dup2(dfw , 1) # copie l’entrée du tube vers la sortie standard (écran)
    os.execlp("grep","grep" ,source + " " + chaine) # recouvre avec cat
    sys.wait()
    os.dup2(dfr , 0)
    print("allo")
    os.execlp("sort","sort")
else :  #fils
    os.dup2(dfr , 0)  # copie la sortie du tube vers l’entrée standard (clavier)
    os.dup2(dfw , 1)
    os.execlp("tail","tail", "-n 5") # recouvre avec wc –l

sys.exit(0)"""