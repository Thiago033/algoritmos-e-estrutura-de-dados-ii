class Graph:
    def __init__(self, vertices):
        self.verticies = vertices
        self.graph = {}
        
    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}

        self.graph[u][v] = w
        self.graph[v][u] = w

    
    
def read_graph_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        num_vertices = len(lines)
        graph = Graph(num_vertices)

        for i in range(num_vertices):
            line_values = lines[i].strip().split()
            for j in range(num_vertices):
                weight = int(line_values[j])
                if weight != 0:
                    graph.add_edge(i, j, weight)

        return graph
    
    
def main():
    filename = "grafo.txt"
    g = read_graph_from_file(filename)
    
    for i in range(5):
        for j in range(5):
            print(g[i])
    
    
    
    

    # agm_result = g.kruskal()
    # print("Árvore Geradora Mínima:")
    # for u, v, weight in agm_result:
    #     print(f"{u} -- {v} | Peso: {weight}")
        
        
if __name__ == "__main__":
    main()