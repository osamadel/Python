# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:41:50 2016

@author: Osama
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    num = int(num)
    difference = 0
    best_exponent = 0
    min_difference = num
    for exponent in range(0, num//2):
        difference = abs(num - base**exponent)
        if min_difference > difference:
            min_difference = difference
            best_exponent = exponent
    return best_exponent
    
print(closest_power(4,32))
print(closest_power(4,12))
print(closest_power(4,1))