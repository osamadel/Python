# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:56:08 2016

@author: Osama
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    result = 0
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    return result


a = [1,2,3]
b = [4,5,6]
print(dotProduct(a,b))