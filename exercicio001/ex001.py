# dict structure
# self.vertices = { vertex: {destination: weight} }

class Graph:
    def __init__(self):
        self.vertices = {}
        
        
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}
        else:
            print("Vertex already exists")


    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            if destination not in self.vertices[source]:
                self.vertices[source][destination] = weight
            else:
                print("Edge already exists")
        else:
            print("Invalid Vertices")
         
                
    def print_graph(self):
        for vertex, edges in self.vertices.items():
            if edges:
                for destination, weight in edges.items():
                    print(vertex, " -> ", destination, "| weight:", weight)
            
            print("")
              
                
graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 11)
graph.add_edge(1, 4, 12)

graph.add_edge(2, 3, 20)
graph.add_edge(2, 4, 21)

graph.add_edge(3, 1, 30)
graph.add_edge(3, 4, 31)

graph.add_edge(4, 1, 40)
graph.add_edge(4, 2, 41)

graph.print_graph()