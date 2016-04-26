"""
This code uses Karger algorithm to find the minimum cut of a graph,
The algorithm is random and by probability should find the min-cut if he runs enough times.

The code use a graph the is undirected and represented in a dictionary of the following type:
[node 1: [adjacent node 1, adjacent node 2, ..., adjacent node n]]
[node 2: [adjacent node 1, adjacent node 2, ..., adjacent node k]]

[node m: [adjacent node 1, adjacent node 2, ..., adjacent node t]]
 
"""
import random
import copy


def min_cut (graph):
    """
    This function calculate the min cut of the graph with randomization, 
    each iteration we randomize the 2 starting node from which we calculate the min cut
    
    :param graph: the starting graph, it is duplicated so it won't change.
    :return min_cut: the minimum cut this iteration
    """
    node_list = [] 
    node_list = copy.deepcopy(graph)
    
    while (len(node_list) > 2):
        #print node_list
        i = random.choice(node_list.keys())
        j = random.choice(node_list[i])
        if (j < i): i, j = j, i
    
        #print 'marging nodes' ,i , ' and ', j
        for edge in node_list[j]:
            if (edge != i ): node_list[i].append(edge)
        while (j in node_list[i]):
            index = node_list[i].index(j)
            del node_list[i][index]
    
        for node in node_list:        
            while(j in node_list[node]):
                index = node_list[node].index(j)
                node_list[node][index] = i
            
        del node_list[j]
    
    this_min_cut =     len(node_list[random.choice(node_list.keys())])
    return this_min_cut

def findMinCut(graph, number):
    """
    This function calls the min cut function a fix amount of times and return the best result
    
    :param graph: the graph we wount to calculte his min cut
    :param number: number of iterations we want to run
    
    :return best_min_cat: the best min cut we got 
    """
    the_min_cut = None
    n = 0
    while (n < number):
        temp_min = min_cut (graph)
        if (the_min_cut == None): 
            the_min_cut = temp_min
        elif(temp_min < the_min_cut): 
            the_min_cut = temp_min
        #print ' The Minimmum Cut is ', the_min_cut
        n = n+1
    return the_min_cut
    


graph = { 1 : [3,6],
          2 : [4,5],
          3 : [1,4,5],
          4 : [5,2,3],
          5 : [2,3,4],
          6 : [1]
        }   
    
print ' The Minimmum Cut is ', findMinCut(graph, len(graph))

    

