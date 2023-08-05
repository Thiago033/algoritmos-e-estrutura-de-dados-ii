import sys
import os

NODES_NUM = 9

def minKey(key, set):
    min = sys.maxsize
    min_index = 0
    
    for vertex in range(NODES_NUM):
        if (key[vertex] < min) and (set[vertex] == False):
            min = key[vertex]
            min_index = vertex
            
    return min_index

def prim(graph):
    # pick minimum weight edge in cut
    key = [sys.maxsize] * NODES_NUM
    
    # constructed MST
    result = [0] * NODES_NUM
    
    set = [False] * NODES_NUM
    
    # first vertex
    key[0] = 0
    
    # first node is always the root
    result[0] = 0
    
    
    for _ in range(NODES_NUM):
        u = minKey(key, set)

        set[u] = True
        
        for v in range(NODES_NUM):
            if (graph[u][v] > 0) and (set[v] == False) and (key[v] > graph[u][v]):
                key[v] = graph[u][v]
                result[v] = u
    
    return result
        
    
def main():
    graph = [[0] * NODES_NUM for _ in range(NODES_NUM)]
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'adjacency-matrix.txt')
    
    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            values = line.split()
            numbers = [int(value) for value in values]
            
            graph[i] = numbers
            i += 1

    #print(graph)

    result = prim(graph)
    
    total_distance = 0
    
    for i in range(1, NODES_NUM):
        print(result[i], "->", i, " Weight:", graph[i][result[i]])
        total_distance += graph[i][result[i]]
        
    print("Total distance: ", total_distance)
        
if __name__ == "__main__":
    main()