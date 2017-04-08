# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:48:49 2016

@author: Osama
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # us_num can be numbers from 0 to 10
    # us_num can be numbers from 11 to 19
    # us_num can be numbers from 20 to 99
    num = int(us_num)
    if num < 11:
        return trans[us_num]
    elif num < 20:
        return trans['10'] + ' ' + trans[us_num[1]]
    else:
        if us_num[1] != '0':
            return trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[1]]
        else:
            return trans[us_num[0]] + ' ' + trans['10']

#for i in range(99):
#    print(i, ':', convert_to_mandarin(str(i)))
