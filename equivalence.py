import helper
import coloring

def color_ordering(G):
    color_order = []
    for n in G.nodes:
        color_order.append(G.nodes(data=True)[n]['color'])
    return color_order


def check_color_private_verse_public(G, I):
    C = coloring.minimal_coloring(G, True)
    private = helper.getHash(color_ordering(C))
    C = coloring.minimal_coloring(I, True)
    public = helper.getHash(color_ordering(C))
    return private == public

def check_data_private_verse_public(G, I):
    C = coloring.minimal_coloring(G, True)
    private = helper.getHash(C.nodes(data=True))
    C = coloring.minimal_coloring(I, True)
    public = helper.getHash(C.nodes(data=True))
    return private == public

def check_state(a, b):
    return a == b