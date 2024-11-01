#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:15:38 2024

@author: gurkan
"""
#--- Definition of the class structure ------
class Person:
    name = ''
    age = 99
    
    def showContent(self):
        if self.age < 18:
            print(f'Sorry {self.name} you can not view this restricted content!')
        
        else:
            print(f'{self.name}! Here is the political corruption throughout the world.')

#--- Creating an object from the class -------
person = Person()

# getting and setting the object variables
person.name = input('Enter your name:')
person.age = int(input('Enter your age:'))

# calling the method of the object -----------
person.showContent()
