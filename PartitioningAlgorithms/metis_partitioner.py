# import metis
# import networkx as nx
#
#
# class metis_partitioner(object):
#     def __init__(self, graph, n_par):
#         self.graph = graph
#         self.n_par = n_par
#
#     def start(self):
#
#         G = nx.Graph()
#
#         for e in self.graph.get_edges():
#             G.add_edge(e.left_id, e.right_id, weight=e.weight)
#
#         G.graph['edge_weight_attr'] = 'weight'
#
#         (edgecuts, parts) = metis.part_graph(G, self.n_par)
#         print(edgecuts)
#         print(len(parts))
#         # print(parts)
#
#         # for i, p in enumerate(parts):
#         #     print(i, ": ", p)
#         # for node in G.nodes:
#         #     print(type(G[node]))
#         #     print(G[node].keys())
#
#         vertices = {}
#         # edges = {(e.left_id, e.right_id): e.left_id for e in self.graph.get_edges()}
#
#         for i, p in enumerate(parts):
#             # networkx starts from 0 but we want the nodes to start from 1
#             vertices[i+1] = p
#
#         return vertices, G.edges
