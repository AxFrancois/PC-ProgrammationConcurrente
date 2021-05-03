#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:47:31 2021

@author: a.francois-charlot
"""

import sys

word = sys.argv[1:]
valren=""
for element in word:
    valren += element[::-1] + " "
print(valren)