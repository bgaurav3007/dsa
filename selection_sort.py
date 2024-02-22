# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:18:41 2024

@author: Gaurav
"""

def selection_sort(arr):
    
    for i in range(0,len(arr) - 1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    print(arr)
    
arr = [7,8,1,4,9]
selection_sort(arr)    