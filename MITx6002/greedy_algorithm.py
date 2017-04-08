# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:57:59 2016

@author: Osama
"""

class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCost()
    
    def __str__(self):
        return self.name + ": <" + str(self.value) \
                + ", " + str(self.calories) + ">"

def build_menu(names, values, calories):
    """ names, values, calories : lists storing corresponding names, values
        and calories of foods. requires all of them of the same length.
        return: a list of objects Food each one contains the corresponding
        name, value and calories."""
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    total_cost = 0
    total_value = 0
    result = []
    for i in range(len(itemsCopy)):
        if total_cost + itemsCopy[i].getCost() <= maxCost:
            result.append(itemsCopy[i])
            total_cost += itemsCopy[i].getCost()
            total_value += itemsCopy[i].getValue()
    return (result, total_value)


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print ("Total value of items taken =", val)
    for i in taken:
        print(' ', i)

def testGreedys(foods, maxUnits):
    print("\nUse greedy by value to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)
    
    print("\nUse greedy by cost to allocate" , maxUnits, "calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    
    print("\nUse greedy by density to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.density)

def maxVal(toConsider, available):
    """
    @param toConsider: (list) items not considered by previous calls.
    @param available: (number) amount of space still available.
    @returns a tuble (total value of a solution to the 0/1 knapsack
             problem, the items of that solution).
    """
    result = ()
    if toConsider == [] or available == 0:
        result = (0, ())
    elif toConsider[0].getCost() > available:
        # Get the maxVal for the rest of itmes in toConsider
        result = maxVal(toConsider[1:], available)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:],
                                    available - nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], available)
        if withVal > withoutVal :
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(items, constraint):
    val, taken = maxVal(items, constraint)
    print()
    print("Use Search Tree to allocate", constraint, "calories")
    print ("Total value of items taken =", val)
    for i in taken:
        print(' ', i)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola',
             'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = build_menu(names, values, calories)
for i in [500, 550, 600, 700, 750, 800, 900, 950, 1000]:
    print ("Test for", i, "calories")
    testGreedys(foods, i)
    testMaxVal(foods, i)
    print("=========")










