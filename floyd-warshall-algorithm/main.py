import sys

# Simulate Infinity
INT_MAX = sys.maxsize

def floyd_warshall(graph):
    n = len(graph)
    
    dist = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    
		# For each vertex (K)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


if __name__ == "__main__":
    # Example matrix
    graph = [
        [0,     3,          INT_MAX,    7],
        [8,     0,          2,          INT_MAX],
        [5,     INT_MAX,    0,          1],
        [2,     INT_MAX,    INT_MAX,    0]
    ]

    result = floyd_warshall(graph)

    # Printing the shortest distances
    for row in result:
        print(row)