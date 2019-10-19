# from androguard.misc import AnalyzeAPK
# from androguard.core.analysis.analysis import ExternalMethod
#
# import matplotlib.pyplot as plt
# import networkx as nx
#
# a, d, dx = AnalyzeAPK("APK_files/mamoc_demo-debug.apk")
#
# from networkx.drawing.nx_agraph import graphviz_layout
# import pygraphviz as pgv
#
# CFG = nx.DiGraph()
#
# # Note: If you create the CFG from many classes at the same time, the drawing
# # will be a total mess...
#
# # for c in dx.find_classes():
# #     orig_class = c.get_vm_class()
# #
# #     print("Found Class --> {}".format(orig_class))
# #     print("# of methods: ", c.get_nb_methods())
# #
# #     if isinstance(orig_class, ExternalClass):
# #         is_this_external = True
# #         # If this class is external, there will be very likely
# #         # no xref_to stored! If there is, it is probably a bug in androguard...
# #     else:
# #         is_this_external = False
# #
# #     CFG.add_node(orig_class, external=is_this_external)
# #
# #     for other_class, callee, offset in c.get_xref_to():
# #         if isinstance(callee, ExternalClass):
# #             is_external = True
# #         else:
# #             is_external = False
# #
# #         if callee not in CFG.node:
# #             CFG.add_node(callee, external=is_external)
# #
# #         # As this is a DiGraph and we are not interested in duplicate edges,
# #         # check if the edge is already in the edge set.
# #         # If you need all calls, you probably want to check out MultiDiGraph
# #         if not CFG.has_edge(orig_class, callee):
# #             CFG.add_edge(orig_class, callee)
# #
# # pos = nx.spring_layout(CFG)
# #
# # internal = []
# # external = []
# #
# # for n in CFG.node:
# #     if isinstance(n, ExternalClass):
# #         external.append(n)
# #     else:
# #         internal.append(n)
# #
# # print(internal)
# # print(external)
#
# # print(dx.get_class_analysis("Luk/ac/standrews/cs/mamoc_test/NQueens/Queens;").get_vm_class().source())
#
# for m in dx.find_methods(classname="Luk/ac/standrews/cs/mamoc/SearchText/SearchActivity;"):
#     orig_method = m.get_method()
#     print("Found Method --> {}".format(orig_method))
#     # orig_method might be a ExternalMethod too...
#     # so you can check it here also:
#     if isinstance(orig_method, ExternalMethod):
#         is_this_external = True
#         # If this class is external, there will be very likely
#         # no xref_to stored! If there is, it is probably a bug in androguard...
#     else:
#         is_this_external = False
#
#     CFG.add_node(orig_method, external=is_this_external)
#
#     for other_class, callee, offset in m.get_xref_to():
#         if isinstance(callee, ExternalMethod):
#             is_external = True
#         else:
#             is_external = False
#
#         if callee not in CFG.node:
#             CFG.add_node(callee, external=is_external)
#
#         # As this is a DiGraph and we are not interested in duplicate edges,
#         # check if the edge is already in the edge set.
#         # If you need all calls, you probably want to check out MultiDiGraph
#         if not CFG.has_edge(orig_method, callee):
#             CFG.add_edge(orig_method, callee)
#
# # CFG.graph['node'] = {'shape':'circle'}
# # CFG.graph['edges'] = {'arrowsize':'4.0'}
#
# pos = graphviz_layout(CFG, prog='fdp')
# # circo, fdp, nop, wc, acyclic, gvpr, gvcolor, ccomps, sccmap, tred, sfdp, unflatten
# internal = []
# external = []
#
# for n in CFG.node:
#     if isinstance(n, ExternalMethod):
#         external.append(n)
#     else:
#         internal.append(n)
#
# print(internal)
# print(external)
#
# nx.draw_networkx_nodes(CFG, pos=pos, node_color='g', nodelist=internal)
# nx.draw_networkx_nodes(CFG, pos=pos, node_color='r', nodelist=external)
# nx.draw_networkx_edges(CFG, pos, arrow=True)
# nx.draw_networkx_labels(CFG, pos=pos, font_size=8,
#                         labels={x: "{}\n{}".format(x.get_name(), x.get_class_name()) for x in CFG.adj})
# plt.axis('off')
# # plt.tight_layout()
#
# plt.draw()
# plt.savefig("output/SearchActivity.png", bbox_inches='tight')
# plt.show()
#
# # A = to_agraph(CFG)
# # print(A)
# # A.layout('dot')
# # A.draw('output/abcd.png')
