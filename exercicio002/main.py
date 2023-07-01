import sys
import os

MAX_NODES = 20
INT_MAX = sys.maxsize

class Node:
    def __init__(self):
        self.cost = INT_MAX
        self.visited = 0
        self.previous = -1


def findMinNode(nodes, n):
    minCost = INT_MAX
    minNode = -1

    for i in range(n):
        if not nodes[i].visited and nodes[i].cost < minCost:
            minCost = nodes[i].cost
            minNode = i

    return minNode

def dijkstra(graph, n, source, destination):
    nodes = [Node() for _ in range(n)]
    
    for i in range(n):
        nodes[i].cost = INT_MAX
        nodes[i].visited = 0
        nodes[i].previous = -1
        
    nodes[source].cost = 0
    
    for count in range(n - 1):
        minNodeIndex = findMinNode(nodes, n)
        if minNodeIndex == -1:
            break
    
        nodes[minNodeIndex].visited = 1
    
        for nodeIndex in range(n):
            if  (not nodes[nodeIndex].visited and #Checks if the node has not been visited yet
                graph[minNodeIndex][nodeIndex] and #Checks if there is an edge between the two nodes
                nodes[minNodeIndex].cost + graph[minNodeIndex][nodeIndex] < nodes[nodeIndex].cost and #Checks if the cost of reaching node "nodeIndex" through node "minNodeIndex" is less than the current cost of reaching node "nodeIndex"
                nodes[minNodeIndex].cost != INT_MAX #Checks if the cost of node "minNodeIndex" is not INT_MAX 
            ): 
            
                nodes[nodeIndex].cost = nodes[minNodeIndex].cost + graph[minNodeIndex][nodeIndex] #update the cost of node "nodeIndex" to the cost of reaching node "minNodeIndex" plus the weight of the edge between "minNodeIndex" and "nodeIndex"
                nodes[nodeIndex].previous = minNodeIndex #Update the previous node of node "nodeIndex" to be node "minNodeIndex"
    
    print("Shortest Path from", source, "to", destination,":")
    printPath(nodes, destination)
    print("\nShortest Distance:", nodes[destination].cost)
    
    
def printPath(nodes, dest):
    if nodes[dest].previous != -1:
        printPath(nodes, nodes[dest].previous)
    print(dest, end=" ")
    

def main():
    n = int(input("Enter the number of nodes (MAX = 20): "))
    
    graph = [[0] * MAX_NODES for _ in range(MAX_NODES)]
    
    #############################################
    # Reading a file with the adjacency matrix: #
    #############################################
    
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the file path
    file_path = os.path.join(current_directory, 'adjacency-matrix.txt')
    
    # Open the file
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        i = 0
        for line in file:
            values = line.split()
            numbers = [int(value) for value in values]
            
            graph[i] = numbers
            i = i + 1
            
    # print("Enter the adjacency matrix:")
    # for i in range(n):
    #     for j in range(n):
    #         print(f"[{i}][{j}]", end=" ")
    #         graph[i][j] = int(input())
                
    source = int(input("Enter the source node: "))
    destination = int(input("Enter the destination node: "))

    dijkstra(graph, n, source, destination)

if __name__ == "__main__":
    main()