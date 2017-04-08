# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:46:33 2016

@author: Osama
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flattened_list = []
    def depth_first(alist, blist):
        if type(alist) != list:
            blist.append(alist)
            return
        else:   # aList is list
            for i in alist:
                depth_first(i, blist)
    
    depth_first(aList, flattened_list)
    return flattened_list


x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(x))
y = [1, 2, 3]
print(flatten(y))
