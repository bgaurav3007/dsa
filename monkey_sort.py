# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:48:12 2024

@author: Gaurav
"""

import random
import time
#a = [1,2,3,4]
#random.shuffle(a)
#print(a)

def is_sorted(arr):
    sorted = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            sorted = False
        
    return sorted


def monkey_sort(arr):
    while not is_sorted(arr):
        time.sleep(1)
        random.shuffle(arr)
        print(arr)
    print(arr)
    
monkey_sort([23,14,15,11,47,61])