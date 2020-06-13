from networkx.algorithms import community
import networkx as nx
from networkx.algorithms import community
from networkx.algorithms.community import quality

from networkx.algorithms import isomorphism

def subgraph_match(G,pattern,type_pattern):
    GM = isomorphism.GraphMatcher(G, pattern)
    count = 0
    node_set = set()
    for subgraph in GM.subgraph_isomorphisms_iter():
        match = True

        for node in subgraph:

            for pattern_node in subgraph:
                if G.get_edge_data(node, pattern_node) != pattern.get_edge_data(subgraph[node], subgraph[pattern_node]):
                    match = False
        if match == True:
            for node in subgraph:
                node_set.add(node)
            count += 1
            print(subgraph)
    print("number of class in "+type_pattern+" pattern / total class: ", len(node_set) / G.number_of_edges(),"\n\n")

