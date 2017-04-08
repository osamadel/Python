# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:14:56 2016

@author: Osama
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def f(x):
        y = 0
        k = len(L) - 1
        for i in L:
            y += i * x**k
            k -= 1
        return y
    return f

print(general_poly([1, 2, 3, 4])(10))