import networkx as nx
import random
import string
import helper
import coloring

def color_hash(G):
    C = coloring.minimal_coloring(G, True)
    data = C.nodes(data=True)
    return helper.getHash(data)

def graph_n_nodes_and_e_edges(N, E, seed_phrase="", params={'color': 0}):
    """
    Create a graph with N nodes and E edges with each node have the parameters
    from param.
    """
    random.seed(helper.string_to_int(seed_phrase))
    G = nx.Graph()
    for n in range(N):
        G.add_nodes_from([n], **params)
    for e in range(E):
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)
        while a == b:
            a = random.randint(0, N-1)
            b = random.randint(0, N-1)
        G.add_edge(a, b)
    return G

def simple_isomorph(G, mapping):
    return nx.relabel.relabel_nodes(G, mapping)

def create_product(G, H):
    K = nx.algorithms.operators.product.tensor_product(G, H)
    return K

def create_obj(flag=False, seed_phrase="", params={'color': 0}):
    if seed_phrase == '':
        seed_phrase = random.random()
    if flag is True:
        N = 3
    else:
        N = 70
    E = N*(N-1)//2
    G = graph_n_nodes_and_e_edges(N, E, seed_phrase, params)
    if flag is True:
        mapping = {}
        for n in range(N):
            mapping[n] = string.ascii_letters[n]
        G = simple_isomorph(G, mapping)
    return G

def create_mapping(data, N):
    order = []
    for n in helper.hash_to_list(data, N):
        if n not in order:
            order.append(n)
    if len(order) != N:
        for a in [i for i in range(N)]:
            if a not in order:
                order.append(a)
    mapping = {}
    for n in range(N):
        mapping[n] = order[n]
    return mapping