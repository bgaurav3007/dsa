# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:18:19 2024

@author: Gaurav
"""
    
import ctypes #Using C dynamic array to create our list class

class MyList():
    def __init__(self):
        self.size = 1 # How many items can we store in our array
        self.n = 0 # Current items in our array
        # Create a C type array with size = self.size
        
        self.A = self.__make_array(self.size)  ##
    
    def __len__(self):
        return self.n # How much is the size of the array
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0 <= index < self.n: ##
            return self.A[index]
        else:
            return 'Index Error - Index out of range'
        
    def __delitem__(self,pos):
        # delete
        if 0 <= pos < self.n:
            for i in range(pos,self.n - 1):
                self.A[i] = self.A[i+1]
            
        self.n = self.n - 1
    
    def append(self,item):
        # Check if there is space to append in the list?
        if self.n == self.size:
            #resize 
            self.__resize(self.size*2) ##
            
        #Append new item
        self.A[self.n] = item
        self.n = self.n + 1        
    
    def pop(self):
        if self.n == 0:
            return 'Empty List'
        
        print(self.A[self.n-1])    
        self.n = self.n - 1
        
    def clear(self):
        self.n = 0
        self.size = 1
        
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'Value Error - Not in list'
    
    def remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
        
    def __resize(self,new_capacity):
        # Create a new array with new capacity
        B = self.__make_array(new_capacity) # size is double of A
        self.size = new_capacity
        #Copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i] # copying elements to index
        # reassign A
        self.A = B
    
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        
        self.A[pos] = item
        self.n = self.n + 1
        
    
    def __make_array(self,capacity):
        # Creates a C type array(static,referential) with size capacity
        return (capacity*ctypes.py_object)() 

    
    
