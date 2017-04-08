# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:05:25 2016

@author: Osama
"""
import pylab as plt


my_samples = []
linear = []
quadratic = []
cubic = []
exponential = []

for i in range(30):
    my_samples.append(i)
    linear.append(i)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.5**i)

plt.figure("lin_quad")
plt.clf()
plt.subplot(211)
plt.ylim(0,1000)
plt.plot(my_samples, linear, 'ro', label = "Linear")
plt.subplot(212)
plt.ylim(0, 1000)
plt.plot(my_samples, quadratic, 'b^', label = "Quadratic")
plt.legend(loc = 'upper left')
plt.title("Linear vs Quadratic")

#plt.figure("quadratic")
#plt.xlabel('samples')
#plt.ylabel('quadratic function')


#plt.figure('cub_exp')
#plt.clf()
#plt.title("Cubic vs Exponential")
#plt.ylim(0,20000)
#plt.plot(my_samples, cubic, label = "Cubic", linewidth = 2)
#plt.plot(my_samples, exponential, label = "Exponential")
#plt.legend()

#plt.figure("exponential")
#plt.xlabel('samples')
#plt.ylabel('exponential function')


