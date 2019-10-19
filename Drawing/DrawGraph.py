# # networkx
# import networkx as nx
#
# # plotly
# import plotly
# import plotly.graph_objs as go
#
# # matplotlib
# # import matplotlib.pyplot as plt
#
# from Drawing.community_layout import community_layout
#
# # plt.figure(figsize=(8, 8))
#
# # from networkx.algorithms.isomorphism.isomorph import graph_could_be_isomorphic as isomorphic
# # import random
# # import os
# # import wx
#
# # plotly.tools.set_credentials_file(username='zhua1987', api_key='7tupnmzgj5')
#
# # edges = [(1, 10, {"block": 2}), (1, 4, {"block": 2}), (1, 7, {"block": 2}), (8, 7, {"block": 2}),
# #          (10, 2, {"block": 3}), (2, 3, {"block": 3}), (2, 5, {"block": 3}), (2, 6, {"block": 3})]
# #
# # nodes = [(1, "s"), (2, "s"), (3, ""), (4, ""), (5, ""), (6, ""), (7, ""), (8, ""), (10, "")]
# #
# colors = ["green", "blue", "red", "aliceblue", "antiquewhite", "aquamarine", "chartreuse", "brown", "coral", "gold",
#           "darkgreen"]
#
#
# # Scatter colorscale options
# # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
# # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
# # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
#
# class DrawGraph:
#
#     def draw(vertices, edges, npar, name, edge_par=True):
#         G = nx.Graph()
#
#         for e in edges.keys():
#             # print(e, edges[e])
#             G.add_edge(*e, name=str(e), type='edge', tag=edges[e])
#
#         for v in vertices.keys():
#             # print(v, vertices[v])
#             G.add_node(v, name=str(v), type='node', tag=vertices[v])
#
#     # # a dictionary to store these edges by their partition id
#     # partitionsDic = {}
#     #
#     # for n in G.nodes():
#     #     print(n, G.node[n]['tag'])
#     #     k = int(G.node[n]['tag'])
#     #     if k in partitionsDic:
#     #         partitionsDic[k].append(n)
#     #     else:
#     #         partitionsDic[k] = [n]
#
#         pos = community_layout(G, vertices)
#
#         for n, p in enumerate(pos):
#             # print(n+1, ": ", p, " ,", pos[p])
#             G.node[n+1]['pos'] = pos[n+1]
#
#     # print(G.nodes(data=True))
#
#     # pos = nx.spring_layout(G)
#     #
#     # nx.draw_networkx_nodes(G, pos,
#     #                        nodelist=A_Vertices,
#     #                        node_color='b',
#     #                        node_size=50)
#     # nx.draw_networkx_nodes(G, pos,
#     #                        nodelist=B_Vertices,
#     #                        node_color='r',
#     #                        node_size=50)
#     #
#     # nx.draw_networkx_edges(G, pos,
#     #                        edgelist=edges,
#     #                        width=2, alpha=0.5, edge_color='g')
#     #
#     # # nx.draw_circular(G, with_labels=True)
#     # nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
#     #
#     # plt.axis('off')
#     # plt.savefig("draw.png")
#     # plt.show()
#
#     # set node positions
#     # pos = nx.spring_layout(G)
#     #
#     # for node in G.nodes():
#     #     G.node[node]['pos'] = pos[int(G.node[node]['tag'])+1]
#
#         node_trace = go.Scatter(
#             x=[],
#             y=[],
#             text=[],
#             mode='markers+text',
#             hoverinfo='text',
#             textposition='top center',
#             marker=dict(
#                 showscale=True,
#                 colorscale='YlGnBu',
#                 reversescale=True,
#                 color=[],
#                 # size=10,
#                 line=dict(width=2)))
#
#     # for node, adjacencies in enumerate(G.adjacency()):
#     #     node_info = '# of connections: ' + str(len(adjacencies[1]))
#     #     # node_trace['text'] += tuple([node_info])
#     #     node_trace['name'] = str(node)
#     #     # node_trace['marker']['size'] += len(adjacencies[1])
#
#         for node in G.nodes():
#             x, y = G.node[node]['pos']
#             node_trace['x'] += tuple([x])
#             node_trace['y'] += tuple([y])
#
#             # Color Node Points in plotly
#             # print(node, G.node[node]['tag'])
#             color = colors[int(G.node[node]['tag'])]
#             node_trace['marker']['color'] += tuple([color])
#             node_trace['text'] += tuple([node])
#
#         edge_trace = go.Scatter(
#             x=[],
#             y=[],
#             line=dict(width=1, color='black'),
#             hoverinfo='none',
#             mode='lines')
#
#         special_edges = []
#
#         for edge in G.edges():
#             if G.node[edge[0]]['tag'] != G.node[edge[1]]['tag']:
#                 special_edges.append((edge[0], edge[1]))
#                 continue  # we do not need to draw the different partition edges
#
#             # draw the edges in the same partition
#             x0, y0 = G.node[edge[0]]['pos']
#             x1, y1 = G.node[edge[1]]['pos']
#             edge_trace['x'] += tuple([x0, x1, None])
#             edge_trace['y'] += tuple([y0, y1, None])
#
#         colored_edges = go.Scatter(
#                          mode='lines',
#                          line=dict(width=1, color='red'),
#                          x=[],
#                          y=[])
#
#         for edge in special_edges:
#             x0, y0 = G.node[edge[0]]['pos']
#             x1, y1 = G.node[edge[1]]['pos']
#             colored_edges['x'] += tuple([x0, x1, None])
#             colored_edges['y'] += tuple([y0, y1, None])
#
#         data = [edge_trace, node_trace, colored_edges]
#
#         layout = go.Layout(
#             title=name,
#             titlefont=dict(size=16),
#             showlegend=False,
#             hovermode='closest',
#             margin=dict(b=20, l=5, r=5, t=40),
#             annotations=[dict(
#                 text=name,
#                 showarrow=False,
#                 xref="paper", yref="paper",
#                 x=0.005, y=-0.002)],
#             xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#             yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
#
#         fig = go.Figure(data, layout)
#
#         plotly.offline.plot(fig, auto_open=True, filename="output/{}.html".format(name))
#         # py.iplot(fig, filename='KL')
