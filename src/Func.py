from .Env import Environment
from .ReturnExc import ReturnExc


class Function:
    def __init__(self, params, body, closure):
        self.params = params
        self.body = body
        self.closure = closure
        
    def call(self, interp, args):
        old = interp.env
        env = Environment(self.closure)
        for i, p in enumerate(self.params):
            env.var[p] = args[i] if i < len(args) else None
        interp.env = env
        try:
            interp.visit(self.body)
        except ReturnExc as e:
            return e.value
        finally:
            interp.env = old
        return None