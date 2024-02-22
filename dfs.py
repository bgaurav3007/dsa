# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:58:35 2024

@author: Gaurav
"""

graph = {
    'A' : ['B','C','D'], 'B':['E'],'C':['D','E'],'D':[],'E':[]
    }

visited = set()
def dfs(visited,graph,root):
    if root not in visited:
        #print(root)
        visited.add(root)
        
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
    
a = dfs(graph,visited,'A')

