
from androguard.misc import AnalyzeAPK
from androguard.core.analysis import analysis


# apk = ExtractCG('APK_files/mamoc_test.apk')
# analysis = apk.extract()
# dx = analysis[0]
# call_graph = analysis[1]

# dx: analysis.Analysis
# apk, dvm, dx = AnalyzeAPK('APK_files/mamoc_test.apk')

# a = apk.APK_files('APK_files/mamoc_test.apk')
# d = dvm.DalvikVMFormat(a.get_dex())
# for current_class in d.get_classes():
#     for method in current_class.get_methods():
#         print
#         method.get_name(), method.get_descriptor()
#         byte_code = method.get_code()
#         if byte_code != None:
#             byte_code = byte_code.get_bc()
#             idx = 0
#             for i in byte_code.get_instructions():
#                 print
#                 "%x " % (idx), i.get_name(), i.get_output()
#                 idx += i.get_length()

# for m in dx.find_methods():
#     print(m)
#
#     ancestors = nx.ancestors(call_graph, m.get_method())
#     ancestors.add(m.get_method())
#     graph = call_graph.subgraph(ancestors)
#
#     # Drawing
#     pos = nx.spring_layout(graph, iterations=500)
#     nx.draw_networkx_nodes(graph, pos=pos, node_color='r')
#     nx.draw_networkx_edges(graph, pos, arrow=True)
#     nx.draw_networkx_labels(graph, pos=pos, labels={x: str(x) for x in graph.nodes}, font_size=8)
#     plt.axis('off')
#     plt.draw()
#     plt.show()

class ExtractCG(object):
    def __init__(self, apkfile, classname=None, methodname=None):
        self.apk_file = apkfile
        self.class_name = classname
        self.method_name = methodname

    def extract(self):
        dx: analysis.Analysis
        a, d, dx = AnalyzeAPK(self.apk_file)
        call_graph = dx.get_call_graph()

        print("APK_files methods: ", len(call_graph))
        # print(type(dx))
        allClasses = dx.get_classes()
        print("all:", len(allClasses))
        external = dx.get_external_classes()
        print("external: ", len(list(external)))
        internal = dx.get_internal_classes()
        print("internal:", len(list(internal)))

        print("external classes info")

        for c in list(external):
            print(c.getClassName())

        return dx, call_graph
