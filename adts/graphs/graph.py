class GraphAdjMat(object):
    """
    Undirected, unweighted graph using an adjacency matrix
    """
    def __init__(self, node_count):
        self.node_count = node_count
        # Create empty adj matrix, but we only need half as undirected
        self.adj_mat = [[False for _ in range(i + 1)] for i in range(node_count)]
    
    def add_edge(self, v1, v2):
        self.adj_mat[max(v1, v2)][min(v1, v2)] = True
    
    def connected(self, v1, v2):
        return self.adj_mat[max(v1, v2)][min(v1, v2)]

    def print_matrix(self):
        for row in self.adj_mat:
            print(list(map(int, row)))


class GraphAdjList(object):
    """
    Undirected, unweighted graph using an adjacency list
    """
    def __init__(self, node_count):
        self.node_count = node_count
        self.adj_list = [[] for _ in range(node_count)]
    
    def add_edge(self, v1, v2):
        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].append(v2)
        if v1 not in self.adj_list[v2]:
            self.adj_list[v2].append(v1)
    
    def connected(self, v1, v2):
        return v2 in self.adj_list[v1]


g = GraphAdjMat(10)
g.add_edge(3, 6)
g.add_edge(5, 5)
print(g.connected(3, 5))
print(g.connected(3, 6))
g.print_matrix()