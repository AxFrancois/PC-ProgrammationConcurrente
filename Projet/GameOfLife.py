# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:30:28 2021
@author: Axel François
github : https://github.com/AxFrancois/ProgrammationConcurrente

To do : placement manuel des points avant le lancement
"""

# %%----------------------Import----------------------------------------------#

import tkinter as tk
import time,random,sys
import multiprocessing as mp

# %%----------------------Sémaphores------------------------------------------#

sempActual1 = mp.Semaphore(1)
sempActual2 = mp.Semaphore(1)
sempActual3 = mp.Semaphore(1)
sempActual4 = mp.Semaphore(1)
semPHG = mp.Semaphore(0)
semPHD = mp.Semaphore(0)
semPBG = mp.Semaphore(0)
semPBD = mp.Semaphore(0)

# %%----------------------Fonctions-------------------------------------------#

def ProcessusCalcul(pNombreDeCase,pPosition,pListeModif,pAffichageActuel):
    """Processus de calcul principal : pour chaque processus, attribue les limites de calculs et de test, vérifie pour chaque case ses voisines, retourne les cases nécéssitant un changement dans pListeModif
        Les commentaires correspondent à mes périgrinations pour les tests avec la grille de 10x10
    Args:
        pNombreDeCase (int): nombre de case par coté
        pPosition (str): HG, HD, BG ou BD : permet de découper la case pour chaque process
        pListeModif (mp Array): permet de faire passer la liste des cases à changer
        pAffichageActuel (mp Array): permet de connaitre l'état actuel de toutes les cases
    """
    moitie = int(pNombreDeCase / 2)
    if pPosition == "HG":
        limiteActualGauche,limiteActualHaut,limiteActualDroite,limiteActualBas = 0, 0, moitie, moitie #0,0,5,5 #0,0,4,4 mais faut prendre en compte que ça s'arrete un avant les range
        limiteTestGauche,limiteTestHaut,limiteTestDroite, limiteTestBas = 0, 0, moitie, moitie #0,0,5,5
    elif pPosition == "HD":
        limiteActualGauche,limiteActualHaut,limiteActualDroite,limiteActualBas = moitie, 0, pNombreDeCase, moitie #5,0,10,5 #5,0,9,4
        limiteTestGauche,limiteTestHaut,limiteTestDroite, limiteTestBas =  moitie - 1, 0, pNombreDeCase - 1, moitie #4,0,9,5
    elif pPosition == "BG":
        limiteActualGauche,limiteActualHaut,limiteActualDroite,limiteActualBas = 0, moitie, moitie, pNombreDeCase #0,5,5,10 #0,5,4,9
        limiteTestGauche,limiteTestHaut,limiteTestDroite, limiteTestBas = 0, moitie - 1, moitie, pNombreDeCase - 1 #0,4,5,9
    elif pPosition == "BD":
        limiteActualGauche,limiteActualHaut,limiteActualDroite,limiteActualBas = moitie, moitie, pNombreDeCase, pNombreDeCase #5,5,10,10 #5,5,9,9
        limiteTestGauche,limiteTestHaut,limiteTestDroite, limiteTestBas = moitie - 1, moitie - 1, pNombreDeCase - 1, pNombreDeCase - 1 #4,4,9,9
    else:
        print("Valeur de pPosition inatendue")
    for row in range(limiteActualHaut,limiteActualBas):
        for col in range(limiteActualGauche,limiteActualDroite):#Pour toutes les cases de la zones attribuée
            numeroRectangleEtudie = row * pNombreDeCase + col + 1
            Etat = pAffichageActuel[numeroRectangleEtudie-1]
            VoisinsVivants = 0
            listeVoisins = [(row-1,col-1),(row,col-1),(row+1,col-1),(row-1,col),(row+1,col),(row-1,col+1),(row,col+1),(row+1,col+1)]    #Liste des voisins
            for CoordVoisins in listeVoisins:   #Test de l'état de vie/mort de chaque voisins
                if (limiteTestHaut <= CoordVoisins[0] <= limiteTestBas) and (limiteTestGauche <= CoordVoisins[1] <= limiteTestDroite):
                    numeroRectangleVerif = CoordVoisins[0]*pNombreDeCase + CoordVoisins[1]
                    if pAffichageActuel[numeroRectangleVerif] == 1 :
                        VoisinsVivants += 1
            if Etat == 1: #Si la cellule est vivante
                if VoisinsVivants < 2 or VoisinsVivants > 3:
                    pListeModif[numeroRectangleEtudie-1] = numeroRectangleEtudie
            elif Etat == 0: #Si la cellule est morte
                if VoisinsVivants == 3:
                    pListeModif[numeroRectangleEtudie-1] = numeroRectangleEtudie
            else:
                print("couleur inatendue")       

def ProcessusHG(pNombreDeCase,pPosition,pListeModif,pAffichageActuel):
    """Fonction du processus de calcul de la section en haut à gauche

    Args:
        pNombreDeCase (int): nombre de case par coté
        pPosition (str): HG, HD, BG ou BD : permet de découper la case pour chaque process
        pListeModif (mp Array): permet de faire passer la liste des cases à changer
        pAffichageActuel (mp Array): permet de connaitre l'état actuel de toutes les cases
    """
    global Run
    while bool(Run.value) == True:
        sempActual1.acquire()

        ProcessusCalcul(pNombreDeCase,pPosition,pListeModif,pAffichageActuel)
        #print("HG Fini")
        semPHG.release()
    sys.exit(0)

def ProcessusHD(pNombreDeCase,pPosition,pListeModif,pAffichageActuel):
    """Fonction du processus de calcul de la section en haut à droite

    Args:
        pNombreDeCase (int): nombre de case par coté
        pPosition (str): HG, HD, BG ou BD : permet de découper la case pour chaque process
        pListeModif (mp Array): permet de faire passer la liste des cases à changer
        pAffichageActuel (mp Array): permet de connaitre l'état actuel de toutes les cases
    """
    global Run
    while bool(Run.value) == True:
        sempActual2.acquire()
        
        ProcessusCalcul(pNombreDeCase,pPosition,pListeModif,pAffichageActuel)
        #print("HD fini")
        semPHD.release()

    sys.exit(0)

def ProcessusBG(pNombreDeCase,pPosition,pListeModif,pAffichageActuel):
    """Fonction du processus de calcul de la section en bas à gauche

    Args:
        pNombreDeCase (int): nombre de case par coté
        pPosition (str): HG, HD, BG ou BD : permet de découper la case pour chaque process
        pListeModif (mp Array): permet de faire passer la liste des cases à changer
        pAffichageActuel (mp Array): permet de connaitre l'état actuel de toutes les cases
    """
    global Run
    while bool(Run.value) == True:
        sempActual3.acquire()
        
        ProcessusCalcul(pNombreDeCase,pPosition,pListeModif,pAffichageActuel)
        #print("BG fini")
        semPBG.release()

    sys.exit(0)

def ProcessusBD(pNombreDeCase,pPosition,pListeModif,pAffichageActuel):
    """Fonction du processus de calcul de la section en bas à droite

    Args:
        pNombreDeCase (int): nombre de case par coté
        pPosition (str): HG, HD, BG ou BD : permet de découper la case pour chaque process
        pListeModif (mp Array): permet de faire passer la liste des cases à changer
        pAffichageActuel (mp Array): permet de connaitre l'état actuel de toutes les cases
    """
    global Run
    while bool(Run.value) == True:
        sempActual4.acquire()

        ProcessusCalcul(pNombreDeCase,pPosition,pListeModif,pAffichageActuel)
        #print("BD fini")
        semPBD.release()
    sys.exit(0)

def Actualisation(ArrayModif,ArrayEtat,Canevas, window):
    """Fonction du processus de synchronisation et d'actualisation. Modifie la couleur sur le Canvas en fonction de ArrayModif

    Args:
        ArrayModif (mp Array): permet de faire passer la liste des cases à changer
        ArrayEtat (mp Array): permet de connaitre l'état actuel de toutes les cases
        Canevas (tk Canvas): permet de modifier le Canvas en fonction de ArrayModif
        window (Tk window): fenêtre tkinter contenant de Canevas
    """
    global Run, Pause
    while bool(Run.value) == True:
        try:
            #print("J'attend")
            semPHG.acquire()
            semPHD.acquire()
            semPBG.acquire()
            semPBD.acquire()
            #print("J'ai tout")
            for i in range(len(ArrayModif)):
                if ArrayModif[i] != 0:
                    if Canevas.itemcget(ArrayModif[i],"fill") == "black":
                        Canevas.itemconfig(ArrayModif[i],fill='white')
                        ArrayEtat[i] = 0
                    elif Canevas.itemcget(ArrayModif[i],"fill") == "white":
                        Canevas.itemconfig(ArrayModif[i],fill='black')
                        ArrayEtat[i] = 1
                ArrayModif[i] = 0

            while bool(Pause.value) == True:
                window.update()
                time.sleep(0.5)

            sempActual1.release()
            sempActual2.release()
            sempActual3.release()
            sempActual4.release()
            
            window.update()
            time.sleep(0.1)
        
        except:
            Run.value = 0
            sempActual1.release()
            sempActual2.release()
            sempActual3.release()
            sempActual4.release()
            sys.exit(0)

def fPause():
    """Fonction pour gérer la pause
    """
    global Pause
    if Pause.value == 0:
        Pause.value = 1
    else:
        Pause.value = 0

# %%----------------------Constantes-----------------------------------------#

width = 500     #<------------- Changer cette valeur pour augmenter/diminuer le nombre de case
height = width + 30
cellSize = 5    #<------------- Changer cette valeur pour augmenter/diminuer la taille et donc le nombre de case
NombreDeCase = int(width/cellSize)
Run = mp.Value('i',1)
Pause = mp.Value('i', 0)
Grille = [[] for i in range(NombreDeCase)]

# %%----------------------Interface graphique---------------------------------#

window = tk.Tk()
window.title("Game Of Life")
widthScreen = window.winfo_screenwidth()
heightScreen = window.winfo_screenheight()
x = (widthScreen // 2) - (width // 2)
y = (heightScreen // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width,height,x,y))

MainFrame = tk.Frame(window)
MainFrame.grid(row=1,column=0)

SecondaryFrame = tk.Frame(window)
SecondaryFrame.grid(row=0,column=0)

Canevas = tk.Canvas(MainFrame,width=width,height=height, bg = '#FFFFFF', highlightthickness=0)
Canevas.pack(side=tk.RIGHT)

for row in range(NombreDeCase):
    for col in range(NombreDeCase):
        BordHaut = row * cellSize
        BordGauche = col * cellSize
        BordBas = (row+1) * cellSize
        BordDroite = (col+1) * cellSize
        Rectangle = Canevas.create_rectangle(BordGauche,BordHaut,BordDroite,BordBas,outline='gray',fill='white')
        Grille[row].append(Rectangle)

replayButton = tk.Button(SecondaryFrame, text = 'Play/Pause', height = 1, width = 10, command=fPause)
replayButton.grid(row = 0, column = 0)

# %%----------------------Test Batch pour 10 carré de chaque coté---------------------------------#

"""
Canevas.itemconfig(55,fill='black')
Canevas.itemconfig(56,fill='black')
Canevas.itemconfig(57,fill='black')
Canevas.itemconfig(65,fill='black')

Canevas.itemconfig(1,fill='black')
Canevas.itemconfig(2,fill='black')
Canevas.itemconfig(11,fill='black')
Canevas.itemconfig(3,fill='black')
Canevas.itemconfig(80,fill='black')
Canevas.itemconfig(81,fill='black')

Canevas.itemconfig(55,fill='black')
Canevas.itemconfig(56,fill='black')
Canevas.itemconfig(57,fill='black')
Canevas.itemconfig(46,fill='black')
"""

# %%----------------------Remplissage aléatoire de la grille---------------------------------#

for i in range(2000):
    Canevas.itemconfig(random.randint(1,NombreDeCase**2),fill='black')

# %%----------------------Initialisation des Arrays---------------------------------#

ArrayModif = mp.Array('i',range(NombreDeCase**2))
for i in range(len(ArrayModif)):
    ArrayModif[i] = 0

ArrayEtat = mp.Array('i',range(NombreDeCase**2))
for i in range(len(ArrayEtat)):
    if Canevas.itemcget(i+1,"fill") == "black":
        ArrayEtat[i] = 1
    else:
        ArrayEtat[i] = 0

# %%----------------------Affichage état initial---------------------------------#

window.update()
time.sleep(1)

# %%----------------------Lancement multiprocessing---------------------------------#

P1 = mp.Process(target = ProcessusHG, args = (NombreDeCase,"HG",ArrayModif,ArrayEtat))
P2 = mp.Process(target = ProcessusHD, args = (NombreDeCase,"HD",ArrayModif,ArrayEtat))
P3 = mp.Process(target = ProcessusBG, args = (NombreDeCase,"BG",ArrayModif,ArrayEtat))
P4 = mp.Process(target = ProcessusBD, args = (NombreDeCase,"BD",ArrayModif,ArrayEtat))
P5 = mp.Process(target = Actualisation, args = (ArrayModif, ArrayEtat, Canevas, window))

P1.start()
P2.start()
P3.start()
P4.start()
P5.start()

P1.join()
P2.join()
P3.join()
P4.join()
P5.join()

sys.exit(0)
