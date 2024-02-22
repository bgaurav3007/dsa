# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:36:44 2024

@author: Gaurav
"""

def is_sorted(arr):
    sorted = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            sorted = False
        
    return sorted

arr = [1,5,6,7,8]
is_sorted(arr)

        