import object
import coloring
import helper
import equivalence
import random
import pickle

def advance_key(W):
    S = W.S
    for _ in range(0):
        data = helper.getHash(S)
        mapping = object.create_mapping(data, S.number_of_nodes())
        S = object.simple_isomorph(S, mapping)
    C = coloring.minimal_coloring(S, True)
    data = C.nodes(data=True)
    mapping = object.create_mapping(data, S.number_of_nodes())
    V = object.simple_isomorph(S, mapping)
    return V


def trade(C, W1, W2, obj):
    if W1.has_obj(obj) is True:
        index = W1.objs.index(obj)
        W2.add_obj(W1.objs[index])
        W2.state = calculate_state(W2)
        C.add_action(W2.state)
        W2.actions += 1
        W1.remove_obj(W1.objs[index])
        W1.state = calculate_state(W1)
        C.add_action(W1.state)
        W1.actions += 1
    return C, W1, W2

def create_seed_phrase():
    words = helper.get_word_list()
    return [random.choice(words) for _ in range(12)]

def create_wallet(C, wallet_file_path, seed_phrase=''):
    if seed_phrase == '':
        seed_phrase = random.random()
    W = Wallet(seed_phrase)
    if W.state not in C.block_actions:
        C.block_actions.append(W.state)
    with open(wallet_file_path, 'wb+') as f:
        pickle.dump(W, f)
    return C, W

def load_wallet(wallet_file_path):
    with open(wallet_file_path, 'rb') as f:
        W = pickle.load(f)
    return W

def save_wallet(W, wallet_file_path):
    with open(wallet_file_path, 'wb+') as f:
        pickle.dump(W, f)

def create_or_load_wallet(C, wallet_file_path, seed_phrase=''):
    from os.path import exists
    if exists(wallet_file_path) is True:
        W = load_wallet(wallet_file_path)
    else:
        C, W = create_wallet(C, wallet_file_path, seed_phrase)
    return C, W
        

def create_key_pair(seed_phrase):
    G = object.create_obj(False, seed_phrase)
    C = coloring.minimal_coloring(G, True)
    data = C.nodes(data=True)
    mapping = object.create_mapping(data, G.number_of_nodes())
    I = object.simple_isomorph(G, mapping)
    return G, I


def calculate_state(W):
    G = advance_key(W)
    for obj in W.objs:
        G = object.create_product(G, obj)
    return object.color_hash(G)


class Wallet:
    def __init__(self, seed_phrase):
        self.S, self.V = create_key_pair(seed_phrase)
        self.objs      = []
        self.state     = object.color_hash(self.V)
        self.actions   = 0
    
    def update_state(self, G):
        self.state = object.color_hash(G)

    def has_obj(self, obj):
        if obj in self.objs:
            return True
        return False
    
    def add_obj(self, obj):
        if obj not in self.objs:
            self.objs.append(obj)
    
    def remove_obj(self, obj):
        if obj in self.objs:
            self.objs.remove(obj)
