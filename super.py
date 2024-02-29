# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 17:00:44 2024

@author: Gaurav
"""

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang 
        

gaurav = Programmer("Gaurav", 4420, "Python")

print(gaurav.name)
print(gaurav.id)
print(gaurav.lang)