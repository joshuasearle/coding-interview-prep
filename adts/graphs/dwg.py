class DirectedWeightedGraphAdjMat(object):
    def __init__(self, node_count):
        self.node_count = node_count
        # Create empty adj matrix
        self.adj_mat = [[float('inf') for _ in range(node_count)] for _ in range(node_count)]
    
    def add_edge(self, v1, v2, weight):
        self.adj_mat[v1][v2] = weight
    
    def weight(self, v1, v2):
        return self.adj_mat[v1][v2]

class Edge(object):
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

class DirectedWeightedGraphAdjList(object):
    def __init__(self, node_count):
        self.node_count = node_count
        self.adj_list = [[] for _ in range(node_count)]
    
    def add_edge(self, v1, v2, weight):
        for edge in self.adj_list[v1]:
            if edge.v2 == v2:
                edge.weight = weight
                return
        self.adj_list[v1].append(Edge(v1, v2, weight))
        
    def weight(self, v1, v2):
        for edge in self.adj_list[v1]:
            if edge.v2 == v2:
                return edge.weight
        return float('inf')