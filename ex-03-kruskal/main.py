import sys
import os

MAX_NODES = 9

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
        
    elif rank[x] > rank[y]:
        parent[y] = x
        
    else:
        parent[y] = x
        rank[x] += 1


def find_parent(parent, index):
    if parent[index] == index:
        return index
    
    return find_parent(parent, parent[index])


def kruskal(graph):
    edges = []
    
    for row in graph:
        for col in graph[row]:
            edges.append((row, col, graph[row][col]))
    
    # sort edges by weight value
    edges = sorted(edges, key=lambda item: item[2])
    
    parent = []
    rank = []
    
    for node in range(MAX_NODES):
        parent.append(node)
        rank.append(0)
    
    result = []
    edges_count = 0
    index = 0

    while edges_count < (MAX_NODES - 1):
        vertice_1, vertice_2, weight = edges[index]
        index += 1
        
        x = find_parent(parent, vertice_1)
        y = find_parent(parent, vertice_2)
        
        if x != y:
            edges_count += 1
            result.append((vertice_1, vertice_2, weight))
            union(parent, rank, x, y)

    return result
    
def main():
    graph = {}
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'adjacency-matrix.txt')
    
    with open(file_path, "r") as file:
        lines = file.readlines()
        
        for row in range(MAX_NODES):
            line_values = lines[row].strip().split()
            
            for column in range(MAX_NODES):
                weight = int(line_values[column])
                
                if weight != 0:
                    if row not in graph:
                        graph[row] = {}
                    
                    graph[row][column] = weight

    # print(graph)

    result = kruskal(graph)
    
    # print(result)
    
    for row, col, weight in result:
        print(f"{row} -> {col} | Weight: {weight}")
        
        
if __name__ == "__main__":
    main()