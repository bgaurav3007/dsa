# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:12:54 2024

@author: Gaurav
"""

def binary_search(arr,low,high,item):
    
    print('low = ',low, 'high = ',high,end=' ')
    if low <= high: ##**
        mid = (low+high)//2 ##**
        print("mid value is ",arr[mid])
        if arr[mid] == item:
            return mid 
        elif arr[mid] > item: #Search RHS
            return binary_search(arr, low, mid-1, item) #Change new high to middle - 1
        else: #Search LHS
            return binary_search(arr, mid+1, high, item) # Change new low to middle
    else:
        return -1
    
arr = [1,2,3,4,5,78,99,100,5,41,187,979]
item = 100

binary_search(arr, 0, len(arr), item)
