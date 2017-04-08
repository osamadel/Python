# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:24:37 2016

@author: Osama
"""

def f(a,b):
    return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersection = {}
    difference = {}
    for item in d1:
        if item in d2:
            intersection[item] = f(d1[item],d2[item])
        else:
            difference[item] = d1[item]
    for item in d2:
        if item not in d1:
            difference[item] = d2[item]
    return (intersection, difference)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
print(dict_interdiff(d1, d2))