# import networkx as nx
#
#
# class KernighanLin(object):
#     def __init__(self, graph, nPar):
#         self.graph = graph
#         self.nPar = nPar
#
#     def start(self):
#
#         G = nx.Graph()
#
#         for e in self.graph.get_edges():
#             G.add_edge(e.left_id, e.right_id, weight=e.weight)
#
#         # print(G.edges(data=True))
#         # G.graph['edge_weight_attr'] = 'weight'
#         parts = nx.algorithms.community.kernighan_lin_bisection(G)
#         print(parts)
#         vertices = {}
#         p = 0
#         for nodes in parts:
#             # networkx starts from 0 but we want the nodes to start from 1
#             for node in nodes:
#                 vertices[node] = p
#             p += 1
#
#         print(vertices)
#
#         # self.group_a_unchosen, self.group_b_unchosen = \
#         #     self.graph.get_random_groups()
#         # cut_size = self.graph.get_cut_size()
#         # nominal_cut_size = float("Inf")
#         #
#         # min_id = -1
#         # self.swaps = []
#         # while self.get_nominal_cut_size() < nominal_cut_size:
#         #     nominal_cut_size = self.get_nominal_cut_size()
#         #     min_cost = float("Inf")
#         #     for i in range(cut_size):
#         #         self.single_swaps()
#         #         cost = self.get_nominal_cut_size()
#         #         if cost < min_cost:
#         #             min_cost = cost
#         #             min_id = i
#         #
#         #     # Undo swaps done after the minimum was reached
#         #     for i in range(min_id + 1, cut_size):
#         #         vertice_b, vertice_a = self.swaps[i]
#         #         self.do_swap((vertice_a, vertice_b))
#         #
#         #     self.group_a_unchosen, self.group_b_unchosen = \
#         #         self.graph.get_groups()
#         #
#         # vertices = {v.id: v.get_group() for v in self.graph.get_vertices()}
#
#         edges = {(e.left_id, e.right_id): e.left_id for e in self.graph.get_edges()}
#
#         return vertices, edges, self.nPar
#
#     def single_swaps(self):
#         best_pair = False
#         best_heuristic = -1 * float("Inf")
#
#         for vertice_a in self.group_a_unchosen:
#             for vertice_b in self.group_b_unchosen:
#                 cost_edge = len(set(vertice_a.get_edges()).intersection(vertice_b.get_edges()))
#                 heuristic = vertice_a.get_cost() + vertice_b.get_cost() - 2 * cost_edge
#                 if heuristic > best_heuristic:
#                     best_heuristic = heuristic
#                     best_pair = vertice_a, vertice_b
#         if best_pair:
#             vertice_a, vertice_b = best_pair
#             self.group_a_unchosen.remove(vertice_a)
#             self.group_b_unchosen.remove(vertice_b)
#             self.do_swap((vertice_a, vertice_b))
#             self.swaps.append(best_pair)
#
#             return best_heuristic
#         else:
#             raise Exception('empty maximum')
#
#     def get_nominal_cut_size(self):
#         cost = 0
#         for edge in self.graph.get_edges():
#             if edge.left_vertex.get_group() != edge.right_vertex.get_group():
#                 cost += 1
#
#         return cost
#
#     def do_swap(self, vertices):
#         vertice_a, vertice_b = vertices
#
#         vertice_a.set_group('2')
#         vertice_b.set_group('1')
