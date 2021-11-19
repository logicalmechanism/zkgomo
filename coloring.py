def minimal_coloring(G, second_pass):
    if second_pass is False:
        return G
    second_pass = False
    for n in G.nodes:
        a = G.nodes[n]
        for e in G.edges(n):
            b = G.nodes[e[1]]
            if a['color'] == b['color']:
                G.nodes[e[1]]['color'] += 1
                second_pass = True
    return minimal_coloring(G, second_pass)