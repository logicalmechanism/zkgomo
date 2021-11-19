import helper
import object
import wallet
import copy
import pickle

def load_chain(chain_file_path):
    try:
        with open(chain_file_path, 'rb') as f:
            C = pickle.load(f)
    except FileNotFoundError:
        return None
    return C

def save_chain(C, chain_file_path):
    with open(chain_file_path, 'wb+') as f:
        pickle.dump(C, f)

class Chain:
    def __init__(self):
        self.block_number  = 0
        self.block_actions = []
        self.block_hash    = ""
        self.objs          = []
        self.db            = {}
    
    def update_hash(self):
        self.db[self.block_number] = { 'objects' : copy.deepcopy(self.objs)
                                     , 'actions' : self.block_actions
                                     , 'hash'    : self.block_hash
                                     }
        addition = str(self.block_number) + str(self.objs) + str(self.block_actions) + self.block_hash
        self.block_hash = helper.getHash(addition)
        self.increment()
    
    def increment(self):
        self.block_number += 1
        self.block_actions = []
        self.objs = []
    
    def add_action(self, action):
        if action not in self.block_actions:
            self.block_actions.append(action)
    
    def has_obj(self, obj):
        if obj in self.objs:
            return True
        return False
    
    def add_obj(self, obj, W):
        if obj not in self.objs:
            W.objs.append(obj)
            self.objs.append(obj)
        return W
    
    def remove_obj(self, obj, W):
        if obj in self.objs:
            W.objs.remove(obj)
            self.objs.remove(obj)
        G = W.V
        if len(self.objs) == 0:
            W.update_state(G)
        else:
            W.state = wallet.calculate_state(W)
        return W
    
    def add_object_to_chain(self, W):
        obj = object.create_obj(True)
        W = self.add_obj(obj, W)
        W.state = wallet.calculate_state(W)
        self.add_action(W.state)
        W.actions += 1
        return W
    
    def print_and_update(self):
        print('Actions', self.block_actions)
        oo = copy.deepcopy(self.objs)
        a = []
        for o in oo:
            a.append(object.color_hash(o))
        print("Objects:", a)
        self.update_hash()
        print('Block:', self.block_hash)
    
    def prove_ownership(self, W, obj):
        if obj not in W.objs:
            return False
        return wallet.calculate_state(W) == W.state
    
    
    