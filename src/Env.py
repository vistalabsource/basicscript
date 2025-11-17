from .InterpErr import InterpError

class Environment:
    def __init__(self, parent=None):
        self.var = {}
        self.parent = parent
    
    def define(self, k, v):
        self.var[k] = v
        
    def set(self, k, v):
        e = self
        while e:
            if k in e.var:
                e.var[k] = v
                return
            e = e.parent
        self.var[k] = v
        
    def get(self, k):
        e = self
        while e:
            if k in e.var:
                return e.var[k]
            e = e.parent
        raise KeyError(k)