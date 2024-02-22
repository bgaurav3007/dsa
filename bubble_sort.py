# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:13:12 2024

@author: Gaurav
"""


def bubble_sort(arr):
    for i in range(0,len(arr) - 1):
        for j in range(0,len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
    
arr = [5,3,91,7,6]
bubble_sort(arr)
            