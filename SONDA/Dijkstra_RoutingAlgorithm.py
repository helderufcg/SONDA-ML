import networkx as nx

"""
The Dijkstra class represents the dijkstra routing algorithm.
"""

class Dijkstra:

    def __init__(self):  
        pass
    
    def Dijkstra(self, A, src_node, dst_node):
        G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
        route = nx.dijkstra_path(G, src_node, dst_node)
        return route

    def KSP(self, A, src_node, dst_node, k):
        G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
        return list(nx.shortest_simple_paths(G, src_node, dst_node, weight='weight'))[:k]
    
    def KMH(self, A, src_node, dst_node, k):
        G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
        return list(nx.shortest_simple_paths(G, src_node, dst_node))[:k]


