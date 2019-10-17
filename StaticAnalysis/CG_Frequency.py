import time
from androguard.misc import AnalyzeAPK


platform_file = open("../Android-API-Files/android_platform_packages.txt", "r")
platform_lines = platform_file.read().splitlines()
platform_list = ["L" + p.replace('.', '/') for p in platform_lines]

# print(platform_list)

support_file = open("../Android-API-Files/android_support_packages.txt", "r")
support_lines = support_file.read().splitlines()
support_list = ["L" + s.replace('.', '/') for s in support_lines]

api_candidates = platform_list + support_list


def frequency(dx, callgraph):
    api_freq = dict()
    call_freq = dict()
    for c in dx.get_classes():
        for key, items in c.xrefto.items():
            for item in items:
                kind, method, offset = item
                if method in api_freq:
                    api_freq[method] += 1
                else:
                    api_freq[method] = 1

    for (m1, m2) in callgraph.edges():

        if (m1, m2) in api_freq:
            call_freq[(m1, m2)] += 1
        else:
            call_freq[(m1, m2)] = 1

    return call_freq


def filter_methods(dx):
    callgraph = dx.get_call_graph()

    filtered_callgraph = callgraph.copy()

    for (m1, m2) in callgraph.edges():
        if m1.get_class_name().startswith(tuple(api_candidates)) or \
                m2.get_class_name().startswith(tuple(api_candidates)):
            filtered_callgraph.remove_edge(m1, m2)
            # continue
            print("removed " + m1.get_class_name() + " AND " + m2.get_class_name())

    return filtered_callgraph


def main():

    a, d, dx = AnalyzeAPK('../APK_files/app-debug.apk')

    method_integer_dict = dict()
    file = open('../output/methodCalls.txt', 'w')
    i = 1

    filtered_callgraph = filter_methods(dx)
    # for (m1, m2), count in sorted(app_methods.items(), key=lambda b: b[1], reverse=True):
    #     file.write(str(m1) + "," + str(m2) + "," + str(count) + "\n")
    for (m1, m2) in filtered_callgraph.edges():
        if m1 not in method_integer_dict:
            method_integer_dict[m1] = i
            i += 1
        if m2 not in method_integer_dict:
            method_integer_dict[m2] = i
            i += 1
        file.write(str(method_integer_dict.get(m1)) + "," + str(method_integer_dict.get(m2)) + "\n")
    file.close()

    # for (m1, m2) in filtered_callgraph.edges():
    #
    #     ancestors = nx.ancestors(filtered_callgraph, m1)
    #     ancestors.add(m1)
    #     graph = filtered_callgraph.subgraph(ancestors)
    #
    #     # Drawing
    #     pos = nx.spring_layout(graph, iterations=500)
    #     nx.draw_networkx_nodes(graph, pos=pos, node_color='r')
    #     nx.draw_networkx_edges(graph, pos, arrow=True)
    #     nx.draw_networkx_labels(graph, pos=pos, labels={x: str(x) for x in graph.nodes}, font_size=8)
    #     plt.axis('off')
    #     plt.draw()
    #     plt.show()


if __name__ == '__main__':
    main()
