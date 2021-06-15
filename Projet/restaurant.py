# -*- coding: utf-8 -*-
"""
Created on Mon June 7 15:40:28 2021
@author: Axel François
github : https://github.com/AxFrancois/ProgrammationConcurrente

To do : affichage de la commande en cours de servie
"""

# %%----------------------Import----------------------------------------------#

import time,random,random
import multiprocessing as mp

# %%----------------------Sémaphores------------------------------------------#

semTampon = mp.Semaphore(1)
semServeur = mp.Semaphore(1)
mutex = mp.Lock()

# %%----------------------Fonctions-------------------------------------------#

def fServeur(pNumero, ptampon, petatServeur, pService):
    """Fonction simulant un serveur

    Args:
        pNumero (int): numéro du serveur
        ptampon (liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande dans la liste d'attente
        petatServeur ([liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande que les serveur sont en train de traiter. Chaque mp Array à la même taille que pNombreProcServeur
        pService (mp Array): indique si le serveur a fini sont plat
    """
    while True:
        semTampon.acquire()
        mutex.acquire()

        numeroClient = ptampon[1][0]
        lettreCommande = ptampon[0][0]

        if numeroClient != 0:   #s'il y a bien une commande, on la récupère et donc on la retire de la liste
            ptampon[1] = fDecaleurListe(ptampon[1])
            ptampon[0] = fDecaleurListe(ptampon[0])
            
        mutex.release()
        semTampon.release()
        
        if numeroClient == 0 :
            time.sleep(1)
        else:
            
            #print(f"le serveur {pNumero} s'occupe de la commande {(numeroClient,lettreCommande)}")
            semServeur.acquire()
            petatServeur[0][pNumero] = lettreCommande
            petatServeur[1][pNumero] = numeroClient
            semServeur.release()

            time.sleep(random.randint(3,6))

            semServeur.acquire()
            petatServeur[0][pNumero] = 0
            petatServeur[1][pNumero] = 0
            pService[pNumero] = 1 
            semServeur.release()


            #print(f"le serveur {pNumero} a fini avec la commande {(numeroClient,lettreCommande)}")

def clients(ptampon, pTamponSize):
    """Processus simulant les client, générant les commandes

    Args:
        ptampon (liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande dans la liste d'attente
        pTamponSize (int): taille du tampon
    """
    while True:
        semTampon.acquire()
        index = fFindLastNotNullIndex(ptampon[1])

        if index <= pTamponSize-1: #Si le carnet de commande n'est pas plein
            lettreCommande = random.randint(1,26)
            numeroClient = random.randint(1,10)

            ptampon[0][index] = lettreCommande
            ptampon[1][index] = numeroClient

        semTampon.release()

        time.sleep(1)

def major_dHomme(pNombreProcServeur, ptampon,pServeur, pService):
    """Fonction major d'homme qui sert à afficher toutes les informations du programme

    Args:
        pNombreProcServeur (int): nombre de serveur
        ptampon (liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande dans la liste d'attente
        pServeur (liste de 2 mp Array): contien 2 mp Array, respectivement le numéro du client et la lettre de la commande que les serveur sont en train de traiter. Chaque mp Array à la même taille que pNombreProcServeur
        pService (mp Array): indique si le serveur a fini sont plat
    """
    while True:
        semTampon.acquire()
        semServeur.acquire()
        mutex.acquire()

        ptamponLettre = fIntListToAlphabet(fArrayToList(ptampon[0]))
        ptamponNumero = fArrayToList(ptampon[1])
        pServeurLettre = fIntListToAlphabet(fArrayToList(pServeur[0]))
        pServeurNumero = fArrayToList(pServeur[1])
        pEnService = fArrayToList(pService)
        pService = fResetList(pService)

        mutex.release()
        semServeur.release()
        semTampon.release()

        print("\x1B[2J\x1B[;H",end='')

        for i in range(pNombreProcServeur):
            if pServeurNumero[i] == 0:
                print(f"Le serveur {i+1} traite la commande")
            else:
                print(f"Le serveur {i+1} traite la commande {(pServeurNumero[i],pServeurLettre[i])}")
        
        tailleListeCommande = fFindLastNotNullIndex(ptamponNumero)
        ListeCommande = []
        for i in range(tailleListeCommande):
            ListeCommande.append((ptamponNumero[i],ptamponLettre[i]))
        print(f"Les commandes clients en attentes : {ListeCommande}")
        print(f"Nombre de commandes en attente : {tailleListeCommande}")

        for i,element in enumerate(pEnService):
            if element == 1:
                print(f"Le serveur {i+1} à fini sa préparation et l'a servi au client")

        time.sleep(1)

def fFindLastNotNullIndex(pListe):
    """Retourne l'index du premier zéro trouvé dans pListe. Si pas de résultat, donne la TAILLE de la liste.

    Args:
        pListe (liste): liste de nombre avec un zéro (ou pas)

    Returns:
        int: index du premier zéro/longueur de la liste si pas trouvé
    """
    valren = len(pListe)
    for i,element in enumerate(pListe):
        if element == 0:
            valren = i
            break
    return valren

def fArrayToList(pArray):
    """Fonction permettant de transformer un Array de multiprocessing en liste 

    Args:
        pArray (mp Array): Array qui va être transformer en liste pour simplifier le traitement

    Returns:
        liste: exacte copie de l'array mais en liste :)
    """
    valren = []
    for i,element in enumerate(pArray):
        valren.append(element)
    return valren

def fIntListToAlphabet(pListe):
    """Converti les éléments d'une liste d'entier correspondant au numéro des lettres en liste de lettre

    Args:
        pListe (liste): liste d'élément dont les valeurs correspondent au numéro des lettres (0<=x<=26)

    Returns:
        liste: liste des lettres
    """
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valren = []
    for i,element in enumerate(pListe):
        valren.append(alphabet[element])
    return valren

def fIntToAlphabet(pEntier):
    """Retourne la lettre associé au numéro fourni

    Args:
        pEntier (int): numéro de la lettre à retourner

    Returns:
        str: lettre
    """
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet[pEntier]

def fDecaleurListe(pListe):
    """Décalle les éléments d'une liste d'un index vers la gauche et met un 0 à la fin

    Args:
        pListe (Liste): Liste à décallé

    Returns:
        Liste: Liste avec les éléments décallés de 1 vers la gauche
    """
    for i in range(len(pListe)-1):
        pListe[i] = pListe[i+1]
    pListe[len(pListe)-1] = 0
    return pListe

def fResetList(pListe):
    """Rempli pListe avec des 0

    Args:
        pListe (Liste): Liste à remplir de 0

    Returns:
        Liste: Liste de la même taille que pListe mais remplie de 0
    """
    for i in range(len(pListe)):
        pListe[i] = 0
    return pListe

# %%----------------------Constantes-----------------------------------------#

NombreProcServeur = 4
EquipeServeur =  [0 for i in range(NombreProcServeur)]
TamponSize = 20

# %%----------------------Initialisation des Arrays---------------------------------#

tamponLettre = mp.Array('i',TamponSize)
tamponNumero = mp.Array('i',TamponSize)
ServeurLettre =  mp.Array('i',NombreProcServeur)
ServeurNumero =  mp.Array('i',NombreProcServeur)
EnService = mp.Array('i',NombreProcServeur)

tampon = [tamponLettre, tamponNumero]
etatServeur = [ServeurLettre, ServeurNumero]

# %%----------------------Lancement multiprocessing---------------------------------#

PClient = mp.Process(target=clients, args= (tampon, TamponSize))
PMajorHomme = mp.Process(target=major_dHomme, args= (NombreProcServeur, tampon, etatServeur, EnService))
for i in range(NombreProcServeur):
    EquipeServeur[i] = mp.Process(target=fServeur, args= (i, tampon, etatServeur, EnService))
  
PClient.start()
PMajorHomme.start()
for i in range(NombreProcServeur):
    EquipeServeur[i].start()

PClient.join()
PMajorHomme.join()
for i in range(NombreProcServeur):
    EquipeServeur[i].join()