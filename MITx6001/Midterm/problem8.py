# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:37:46 2016

@author: Osama
"""

def f(x):
    return x + 2

def g(x):
    return x > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    max = 0
    i = 0
    while i < len(L):
        if not g(f(L[i])):
            del L[i]
        else:
            if max < L[i]:
                max = L[i]
            i += 1
    if len(L) != 0:
        return max
    else:
        return -1
    
L = [0]
print(applyF_filterG(L, f, g))
print(L)