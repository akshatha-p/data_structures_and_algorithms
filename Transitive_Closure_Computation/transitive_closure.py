# -*- coding: utf-8 -*-
"""
DSA CS610 Programming Assignment 3
"""

import numpy as np

if __name__ == "__main__": 

    #getting total number of nodes of the graph from user 
    total_nodes = int(input("total graph nodes: "))
    # creating a nXn zero square matrix of n =  total nodes
    adj_matrix = []
    for i in range(total_nodes): 
        row = [] 
        for j in range(total_nodes): 
            row.append(0) 
        adj_matrix.append(row) 
    
    #User input, number of node pair values of the graph 
    n = int(input("total node pair values: "))
    #empty lists to create adjacency matrix
    values = [] 
    temp = []
    print("\nPlease enter node pair values with a blank space between them")    
    
    """creating adjacency matrix"""
    for i in range(n):
        node_pair = input("value1 value2\t") #User input, get node pair values
        values = [] #empty this list after each iteration
        for j in node_pair.split(): #splitting the pair to add each value 
            values.append(j)
         
        # adding only disticnt values to the temp list               
        if(values[0] not in temp):
            temp.append(values[0])
        if(values[1] not in temp):
            temp.append(values[1])  
        #setting matrix values to 1 as per the node pairs
        v1 = values[0]
        v2 = values[1]
        adj_matrix[temp.index(v1)][temp.index(v2)] = 1 #final adjacency matrix
          
    """Printing adjacency matrix """
    print("\nThe Adjacency Matrix is:")
    print(np.array(adj_matrix))
    
     
    """creating transitive closure matrix"""
    #creating a nXn zero square matrix of n =  total nodes
    TC_matrix=[] 
    for i in range(total_nodes): 
        TC_row = [] 
        for j in range(total_nodes): 
            TC_row.append(0) 
        TC_matrix.append(TC_row)
   
    """ computing transitive closure """   
    TC_matrix = adj_matrix #setting the transitive closure matrix to adjacency matrix
    
    for k in range(total_nodes):  
        for m in range(total_nodes):
            for n in range(total_nodes):
                TC_matrix[m][n]= TC_matrix[m][n] or (TC_matrix[m][k] and TC_matrix[k][n])
    
    """Printing transitive closure"""
    print("\n Transitive Closure ")
    print(np.array(TC_matrix))    


    