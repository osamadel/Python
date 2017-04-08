# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:24:13 2016

@author: Osama
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    isInc = False
    longestInc = []
    longestDec = []
    incStartIndex = 0
    incEndIndex = 0
    decStartIndex = 0
    decEndIndex = 0
    maxInc = 0
    maxDec = 0
    longestIncStartIndex = 0
    longestDecStartIndex = 0
#    print("List:", L)
    for i in range(len(L) - 1):
        print("L[i]:", L[i], ", L[i+1]:", L[i+1])
        if isInc:
            if L[i] <= L[i+1]:
                # still increasing ...
                incEndIndex = i+1
            else:
                # No longer increasing ...
                incEndIndex = i
                decStartIndex = i
                decEndIndex = i+1
                isInc = False
        else:
            if L[i] >= L[i+1]:
                # still decreasing ...
                decEndIndex = i+1
            else:
                # No longer decreasing ...
                decEndIndex = i
                incStartIndex = i
                incEndIndex = i+1
                isInc = True
#        print("Increasing?", isInc)
        # check if the current maxInc is the max length of continuous
        # increasing sequence
        if maxInc < (incEndIndex - incStartIndex + 1):
            maxInc = incEndIndex - incStartIndex + 1
            longestInc = L[incStartIndex : incEndIndex+1]
            longestIncStartIndex = incStartIndex
        
        if maxDec < (decEndIndex - decStartIndex + 1):
            maxDec = decEndIndex - decStartIndex + 1
            longestDec = L[decStartIndex : decEndIndex+1]
            longestDecStartIndex  = decStartIndex
            
        print("Increasing:", longestInc)
        print("Increasing Start Index:", incStartIndex)
        print("Increasing End Index:", incEndIndex)
        print("Max Increasing:", maxInc)
        
        print("Decreasing:", longestDec)
        print("Decreasing Start Index:", decStartIndex)
        print("Decreasing End Index:", decEndIndex)
        print("Max Decreasing:", maxDec)
        print()
    
    if len(longestInc) > len(longestDec):
        return sum(longestInc)
    elif len(longestInc) < len(longestDec):
        return sum(longestDec)
    else:
        if longestIncStartIndex < longestDecStartIndex:
            return sum(longestInc)
        else:
            return sum(longestDec)
        

def longest_run2(L):
    x1 = 0
    x2 = 0
    seq = []
    maxSeq = 0
    lastDirection = 1
    for i in range(1, len(L)):
        direction = L[i] - L[i-1]
        if lastDirection * direction <= 0:
            # changed direction
            x1 = x2
            x2 = i-1
#        else:
#            x1 = x2
        
        if L[i] - L[x2] == 0 or L[x2] - L[x1] == 0:
            if maxSeq < len(L[x1:i+1]):
                seq = L[x1:i+1]
                maxSeq = len(seq)
        else:
            if maxSeq < len(max(L[x1:x2+1], L[x2:i+1])):
                seq = max(L[x1:x2+1], L[x2:i+1])
                maxSeq = len(seq)
        if direction != 0:
            lastDirection = direction
        print("x1:i=", L[x1:i+1])
        print("Sequence:", seq)
    return sum(seq)

            
            
y = [100000, 10000, 1000, 100, 10, 8, 8, 5, 2, 1, 0]

#import pylab as plt
#x = [i for i in range(len(y)-4)]
#plt.figure("fig")
#plt.plot(x,y[:-4])
    
print(longest_run2(y))