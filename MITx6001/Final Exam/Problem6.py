# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:00:58 2016

@author: Osama
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff): 
        return 'It is obvious that I believe that ' + Person.say(self, stuff)

ae = ArrogantProfessor('eric')
pe = Professor('eric') 
print(pe.say('the sky is blue'))
print(ae.say('the sky is blue'))