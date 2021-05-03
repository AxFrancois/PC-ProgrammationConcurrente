#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:49:54 2021

@author: a.francois-charlot
"""

import sys 

val = sys.argv[1:]
valren = 0
AllInt = True

if len(val) < 1:
    print("Aucune moyenne à calculer")
    
for element in val:
    try:
        valren += int(element)
    except:
        AllInt = False

if AllInt == True:
    print("Moyenne est : {}".format(round(valren/len(val),2)))  
else:
    print("Note non valide" )   