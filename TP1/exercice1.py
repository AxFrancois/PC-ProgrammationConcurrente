#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:34:09 2021

@author: a.francois-charlot
"""

import sys 
print("Nom du programme : ", sys.argv[0]) 
print("Nombre d’arguments : ", len(sys.argv)-1) 
print("Les arguments sont : ") 
for arg in sys.argv[1:] : 
    print(arg)
    