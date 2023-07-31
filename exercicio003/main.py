import sys
import os

MAX_NODES = 9

def union(parent, rank, x, y):
    root_x = find_parent(parent, x)
    root_y = find_parent(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


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
    count = 0
    index = 0

    while count < (MAX_NODES - 1):
        vertice_1, vertice_2, weight = edges[index]
        index += 1
        
        x = find_parent(parent, vertice_1)
        y = find_parent(parent, vertice_2)
        
        if x != y:
            count += 1
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