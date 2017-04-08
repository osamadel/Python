# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:12:28 2017

@author: Osama
"""

import pylab as plt

x = []
y = []
y_to2 = []
y_to3 = []
y_exp = []

for i in range(30):
    x.append(i)
    y.append(i)
    y_to2.append(i**2)
    y_to3.append(i**3)
    y_exp.append(1.5**i)

plt.figure('lin')
plt.plot(x,y)
plt.figure('quad')
plt.plot(x,y_to2)
plt.plot(x,y_to3)
plt.plot(x,y_exp)