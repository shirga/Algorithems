"""
This code implement Dijkstra algorithm - finding the shortest path in a directed graph. 
The code use a directed graph with the following represented in a dictionary of the following type:

node 1: [(edge head, edge len), (edge head, edge len), ... (edge head, edge len)]
node 2: [(edge head, edge len), (edge head, edge len), ... ,(edge head, edge len)]

node m: [(edge head, edge len),  (edge head, edge len)]

"""

def DijkstrasShortestPath(graph, nodes_num, start_node):
    """
    This function in the main function which initialize all the lists ans dic
    
    :param graph: the directed graph
    :param nudes_num: the number of nodes in the graph
    :param start_node: the node from which we will calculate the shortest path
    
    :return shortest_path: a list of the shoetest path len fron the start node to each node in the graph
    """
    #initializing the algorithm
    # hold status for each node if it has been procces or not
    processed = {}
    # hold a set of all the proccessed nodes
    processed_list = set()
    # a dic that hold the shortest path to each node
    shortest_path = {}
    for i in range(1,nodes_num+1):
        processed[i] = False
        shortest_path[i] = 1000000
        
    shortest_path[start_node] = 0
    node = start_node

    while (len(processed_list)< len(graph)):
        print node, processed_list
        processed[node] = True
        processed_list.add(node)
        shortest_edge = 100000
        next_node = None
        for node in processed_list:
            if node in graph:
                for pair in graph[node]:
                    head = pair[0]
                    edge_len = pair[1]
                    if (shortest_path[node]+ edge_len <shortest_path[head]):
                        shortest_path[head] = shortest_path[node]+edge_len
                    if (processed[head] == False):
                        if(edge_len < shortest_edge):
                            shortest_edge = edge_len
                            next_node = head
        node = next_node

    return shortest_path


graph = {1: [(2,2),(4,1)],
         2: [(4,3), (5,10)],
         3: [(1,4),(6,5)],
         4: [(3,2),(5,2),(6,8),(7,4)],
         5: [(7,6)],
         7: [(6,1)]}
         
nodes_num = 7
          
shortest_path = DijkstrasShortestPath(graph, nodes_num, 1)
print "shortest path from node 1 to node 7 = ", shortest_path[7]

