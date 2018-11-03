# import community
# import networkx as nx
#
#
# class louvain_partitioner(object):
#     def __init__(self, graph, n_par):
#         self.graph = graph
#         self.nPar = n_par
#
#     def start(self):
#         edges = [(e.left_id, e.right_id) for e in self.graph.get_edges()]
#
#         G = nx.Graph()
#
#         G.add_edges_from(edges)
#
#         parts = community.best_partition(G)
#         values = [parts.get(node) for node in G.nodes()]
#         print(parts)
#         print(values)
#
#         vertices = {}
#         edges = {(e.left_id, e.right_id): e.left_id for e in self.graph.get_edges()}
#
#         for i, p in parts.items:
#             vertices[i+1] = p
#
#         print("louvain vertices: ", vertices)
#         return vertices, edges, self.nPar
