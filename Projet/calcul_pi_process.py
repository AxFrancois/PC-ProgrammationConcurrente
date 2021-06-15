
import multiprocessing as mp
import time

start_time = time.time()

Nb_process = 5

def arc_tangente(n):
    """Processus de calcul principal : Chaque process va calculer une somme de même taille et ajouter celle-ci dans la variable partagée pi
Args:
    n (int): nombre d'itération du process
"""
    sommePart = 0
    for i in range(n):
        sommePart += 4/(1+ ((i+0.5)/n)**2)

    pi.value += (1/nb_total_iteration)*sommePart
    


if __name__ == "__main__" :

    # Nombre d’essai pour l’estimation
    nb_total_iteration = 1000000
    """
    On divise notre nombre total d'itération pour l'approximation de pi par le nombre de processus
    """
    nb_iteration_par_process = nb_total_iteration/Nb_process

    listeProcess = []
    mutex = mp.Lock()
    pi = mp.Value('f',0)


    print("Temps d'execution : ", time.time() - start_time)

    """
    On génère autant de processus que voulu et ceux-ci vont executer la fonction arc_tangente
    """
    for _ in range(Nb_process) :
        process = mp.Process(target = arc_tangente, args = (int(nb_iteration_par_process),))
        
        listeProcess.append(process)
        process.start()
    
    for p in listeProcess :
        p.join()

    print("Valeur estimée Pi par la méthode Tangente : ", pi.value)