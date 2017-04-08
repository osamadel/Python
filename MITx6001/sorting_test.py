# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:02:26 2016

@author: Osama
"""

def bubble_sort(x):
    """return a sorted copy of the input list x"""
    L = x[:]
    swap = False
    while not swap:
        swap = True
        print(L)
        for i in range(1,len(L)):
            if L[i] < L[i-1]:
                swap = False
                L[i-1], L[i] = L[i], L[i-1]
    return L

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

x = [5, 2, 9, 4, 1, 3, 7, 0, 2]
modSwapSort(x)                
                