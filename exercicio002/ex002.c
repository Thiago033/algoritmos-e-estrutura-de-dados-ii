#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_NODES 20

typedef struct {
    int cost;
    int visited;
    int previous;
} Node;

int main() {
    int n, source, destination;
    int graph[MAX_NODES][MAX_NODES];

    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    printf("Enter the adjacency matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("[%d][%d]", i, j);
            scanf("%d", &graph[i][j]);
        }
    }

    printf("Enter the source node: ");
    scanf("%d", &source);

    printf("Enter the destination node: ");
    scanf("%d", &destination);

    //dijkstra(graph, n, source, destination);

    return 0;
}

int findMinNode(Node graph[], int n) {
    int minCost = INT_MAX;
    int minNode = -1;

    for (int i = 0; i < n; i++) {
        if (!graph[i].visited && graph[i].cost < minCost) {
            minCost = graph[i].cost;
            minNode = i;
        }
    }

    return minNode;
}

void dijkstra(int graph[MAX_NODES][MAX_NODES], int n, int source, int destination) {
    Node nodes[MAX_NODES];

    for (int i = 0; i < n; i++) {
        nodes[i].cost = INT_MAX;
        nodes[i].visited = 0;
        nodes[i].previous = -1;
    }

    nodes[source].cost = 0;

    for (int count = 0; count < n - 1; count++) {
        int u = findMinNode(nodes, n);
        if (u == -1)
            break;

        nodes[u].visited = 1;

        for (int v = 0; v < n; v++) {
            if (!nodes[v].visited && graph[u][v] && nodes[u].cost != INT_MAX && nodes[u].cost + graph[u][v] < nodes[v].cost) {
                nodes[v].cost = nodes[u].cost + graph[u][v];
                nodes[v].previous = u;
            }
        }
    }

    printf("Shortest Path from %d to %d: ", source, destination);

    printPath(nodes, destination);

    printf("\nShortest Distance: %d\n", nodes[destination].cost);
}

void printPath(Node graph[], int dest) {
    if (graph[dest].previous != -1) {
        printPath(graph, graph[dest].previous);
    }
    printf("%d ", dest);
}
