import sys,os
from anytree import Node, RenderTree



param = sys.argv[1]

if param == "creation":
    os.remove("ExoBonus.csv")
    f=open("ExoBonus.csv", 'x')
    f.close()
    for i in range(3):
        pid_fork = os.fork()
        pid = os.getpid()
        ppid = os.getppid()
        print("i : {} je suis le processus : {}, mon pere est : {}, retour : {} ".format(i, pid, ppid, pid_fork))
        f = open("ExoBonus.csv", 'a')
        f.write("{},{},{},{} \n".format(i, pid, ppid, pid_fork))
        f.close()

elif param == "display":
    f = open("ExoBonus.csv", 'r')
    pid_pere_list = []
    pid_fils_list = []
    data = []
    for ligne in f:
        donnees = ligne.rstrip('\n\r').split(",")
        pid_pere_list.append(donnees[2])
        if int(donnees[1]) not in pid_fils_list:
            pid_fils_list.append(int(donnees[1]))
            data.append(donnees)

    Process2315 = Node("Process " + str(min(pid_pere_list)))
    for i,val in enumerate(pid_fils_list):
        exec(f'Process{val} = Node("Process "+ str(pid_fils_list[i]), parent=Process{pid_pere_list[i]})')


    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)

    for pre, fill, node in RenderTree(Process2315):
        print("%s%s" % (pre, node.name))