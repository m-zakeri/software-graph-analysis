import operator

import networkx as nx
import collections
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.isomorphism import isomorphvf2

from subgraph_finder import subgraph_match


def show_degree_distribiution(G,grap_path):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    plt.loglog(degree_sequence, '.', marker='o')
    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    plt.savefig(grap_path)
    plt.show()



def average_degree(G):
    sum_degree = 0
    for n,d in G.degree():
        sum_degree+=d
    print("degree average: "+str(sum_degree/(2*G.number_of_nodes())))




def get_top_five_closeness(G):
    page_rank_dictionary = nx.closeness_centrality(G)
    print("top five in closeness: {}".format(dict(sorted(page_rank_dictionary.items(), key=operator.itemgetter(1), reverse=True)[:5])))

def get_top_five_page_rank_central(G):
    page_rank_dictionary = nx.pagerank_numpy(G)
    print("top five in page rank: {}".format(dict(sorted(page_rank_dictionary.items(), key=operator.itemgetter(1), reverse=True)[:5])))



def get_top_class_in_connection(G):
    p = sorted(G.degree,key=lambda x: x[1], reverse=True)
    print("top class in connection",p[:5])

def best_person_in_java(G):
    p = sorted(G.degree, key=lambda x: x[1], reverse=True)[0]
    print("the top person in java : {} with {} accept and answer".format(p[0], p[1]))


def export_gephi_project(graph, graph_name):
    nx.write_gexf(graph,graph_name+".gexf")


def create_graph_from_connection(connctions,graph_path):
    G = nx.MultiDiGraph()
    for node in connctions:
                G.add_edge(node.source,node.target,connection_type=node.connection_type)
    print("number of edges : {}".format(G.number_of_edges()))
    print("number of nodes : {}".format(G.number_of_nodes()))
    average_degree(G)
    get_top_class_in_connection(G)
    get_top_five_page_rank_central(G)
    get_top_five_closeness(G)

    G2 = nx.MultiDiGraph()
    G2.add_edge("Caller class","Interface",connection_type="Association")
    G2.add_edge("concrete class","Interface",connection_type="Generalization")
    subgraph_match(G,G2,"strategy")
    G3 = nx.MultiDiGraph()
    G3.add_edge("proxy class", "concrete class", connection_type="Association")
    G3.add_edge("concrete class", "Interface", connection_type="Generalization")
    G3.add_edge("proxy class", "Interface", connection_type="Generalization")
    subgraph_match(G,G3,"proxy")


    export_gephi_project(G, graph_path)
    show_degree_distribiution(G,graph_path)
