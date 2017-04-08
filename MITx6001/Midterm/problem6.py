# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:59:04 2016

@author: Osama
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in range(len(L)//2):
        temp = L[i]
        L[i] = L[-1-i]
        L[-1-i] = temp
    
    for i in L:
        for j in range(len(i)//2):
            temp = i[j]
            i[j] = i[-1-j]
            i[-1-j] = temp
    

L = [[1, 2], [3, 4], [5, 6, 7]]
print(L)
deep_reverse(L)
print(L)