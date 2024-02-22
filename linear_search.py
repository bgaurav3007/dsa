# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:22:14 2024

@author: Gaurav
"""


def linear_search(arr,item):
    
    for i in range(0,len(arr)):
        if arr[i] == item:
            return i
    
    return -1

arr= [59,78,46,13,2,4,899,78,564,100]
item = 564

linear_search(arr, item)
    