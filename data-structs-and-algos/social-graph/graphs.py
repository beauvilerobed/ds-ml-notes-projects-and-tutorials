class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbors = {}

    def add_to_neighbors(self, neighbor, w):
        self.neighbors[neighbor] = w

    def get_neighbors(self):
        return self.neighbors.keys()
    

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, val):
        new_vertex = Vertex(val)
        self.vertices[val] = new_vertex
        return new_vertex
    
    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.add_vertex(Vertex(u))
        if v not in self.vertices:
            self.add_vertex(Vertex(v))
        self.vertices[u].add_to_neighbors(self.vertices[v], weight)

    def get_vertex(self, val):
        return self.vertices[val]
    
    def get_vertices(self):
        return self.vertices.keys()
    
    def _iter__(self):
        return iter(self.vertices)