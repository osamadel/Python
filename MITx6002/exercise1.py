# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:14:11 2016

@author: Osama
"""

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    def shiftTrinary(number, bits):
        for i in range(bits):
            number = number // 3
        return number
        
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (shiftTrinary(i,j)) % 3 == 2:
                bag1.append(items[j])
            elif (shiftTrinary(i,j)) % 2 == 1:
                bag2.append(items[j])
        yield (bag1, bag2)

y = yieldAllCombos(["horse","car","bike"])
res = []
for i in y:
    res.append(i)
    print(i)
