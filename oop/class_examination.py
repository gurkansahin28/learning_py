#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:15:38 2024

@author: gurkan
"""
def dividerLine():
    print('-' * 60)

#--- CONDITIONAL METHOD OF THE CLASS
# --- Definition of the class structure ------
class Person:
    name = ''
    age = 99

    def showContent(self):
        if self.age < 18:
            print(f'Sorry {self.name} you can not view this restricted content!')

        else:
            print(f'{self.name}! Here is the political corruption throughout the world.')


# --- Creating an object from the class -------
person = Person()

# getting and setting the object variables
person.name = input('Enter your name:')
person.age = int(input('Enter your age:'))

# calling the method of the object -----------
person.showContent()

dividerLine()

#---
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = [] # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

myDog = Dog('Reno')
myDog.add_trick('licking rusty cars')
myDog.add_trick('laying on a bad of nails')
print(myDog.tricks)

yourDog = Dog('Rezzo')
yourDog.add_trick('waving its tail like a chopper')
yourDog.add_trick('rolling over its head')
print(yourDog.tricks)

dividerLine()

#----------------------------------------------

class Junkyard:
    owner = 'Gurkan'
    location = 'Back garden'

myJunkyard = Junkyard()
print(myJunkyard.owner)
print(myJunkyard.location)

yourJunkyard = Junkyard()
yourJunkyard.owner = 'you'
yourJunkyard.location = 'Your working room! Huh...'
print(yourJunkyard.owner)
print(yourJunkyard.location)

dividerLine() #---------------------------------

