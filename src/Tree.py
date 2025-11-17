from lib.BasicScriptVisitor import BasicScriptVisitor
from .verbose import *
from .ReturnExc import ReturnExc
from .Func import Function
from .Env import Environment
from .InterpErr import InterpError
from .BreakExc import BreakExc
from .ContinueExc import ContinueExc
from .ThrowExc import ThrowExc
import ast

class Tree(BasicScriptVisitor):
    def __init__(self, loop_limit=100000):
        super().__init__()
        self.env = Environment()
        self.loop_limit = loop_limit
        self.stdlib = {
            'write': lambda args: print(*args),
            'scan': lambda args: input(args[0] + ": "),
            'length': lambda args: len(args[0]),
            'to_int': lambda args: int(args[0]),
            'to_float': lambda args: float(args[0]),
            'to_str': lambda args: str(args[0]),
            'range': lambda args: range(*args),
            # ここに標準ライブラリを追加
        }
        
    
    def loc(self, ctx):
        text = getattr(ctx, "start", None)
        return f"[LOCATION]: line: {getattr(text, 'line', '?')}, column: {getattr(text, 'column', '?')}"
        
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None
    
    def visitStatement(self, ctx):
        return self.visit(ctx.getChild(0))
    
    def visitAssign(self, ctx):
        self.env.set(ctx.ID().getText(), self.visit(ctx.expr()))
    
    def visitExpr_s(self, ctx):
        return self.visit(ctx.expr())
        
    def visitIf(self, ctx):
        if self.truthy(self.visit(ctx.expr())):
            self.visit(ctx.block(0))
        else:
            if ctx.if_():
                self.visit(ctx.if_())
            elif ctx.ELSE():
                self.visit(ctx.block(1))
                
    def visitWhile(self, ctx):
        cnt = 0
        while self.truthy(self.visit(ctx.expr())):
            self.visit(ctx.block())
            cnt += 1
            if cnt > self.loop_limit:
                raise InterpError(f"{self.loc(ctx)}\n[VALUE_ERROR]: Loop limit exceeded.")
            
    def visitFor(self, ctx):
        name = ctx.ID().getText()
        seq = self.visit(ctx.expr())
        if not hasattr(seq, '__iter__'):
            raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: Object '{name}' is not iterable.")
        cnt = 0
        for i in seq:
            self.env.set(name, i)
            try:
                self.visit(ctx.block())
            except ContinueExc:
                pass
            except BreakExc:
                break
            cnt += 1
            if cnt > self.loop_limit:
                raise InterpError(f"{self.loc(ctx)}\n[VALUE_ERROR]: Loop limit exceeded.")
            
    def visitBreak(self, ctx):
        raise BreakExc()
    
    def visitContinue(self, ctx):
        raise ContinueExc()
    
    def visitThrow(self, ctx):
        value = self.visit(ctx.expr())
        raise ThrowExc(value)
    
    def visitTry_catch(self, ctx):
        try:
            self.visit(ctx.block(0))
        except ThrowExc as t:
            name = ctx.ID().getText()
            old = self.env
            self.env = Environment(old)
            try:
                self.env.define(name, t.value)
                self.visit(ctx.block(1))
            finally:
                self.env = old
                
        
            
    def visitBlock(self, ctx):
        old = self.env
        self.env = Environment(old)
        try:
            for stmt in ctx.statement():
                self.visit(stmt)
        finally:
            self.env = old
    
    def visitFunction(self, ctx):
       name = ctx.ID().getText()
       params = [p.getText() for p in (ctx.param_list().ID() if ctx.param_list() else [])]
       func = Function(params, ctx.block(), self.env)
       self.env.define(name, func)
        
    def visitReturn(self, ctx):
        value = self.visit(ctx.expr()) if ctx.expr() else None
        raise ReturnExc(value)
    
    def visitOr(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        return l if self.truthy(l) else r
    
    def visitAnd(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        return r if self.truthy(l) else l
    
    def visitNot(self, ctx):
        return not self.visit(ctx.expr())
    
    def visitEq(self, ctx):
        op = ctx.getChild(1).getText()
        eq = lambda a, b: a == b if op == '==' else a != b
        return self.bin(ctx, eq)
    def visitRel(self, ctx):
        a, b = self.visit(ctx.expr(0)), self.visit(ctx.expr(1));op = ctx.getChild(1).getText()
        try:
            if op == '<':
                return 1 if a < b else 0
            if op == '<=':
                return 1 if a <= b else 0
            if op == '>':
                return 1 if a > b else 0
            if op == '>=':
                return 1 if a >= b else 0  
        except Exception:
            raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: operator '{op}' can only be used with numeric types.")
     
    def visitAddSub(self, ctx):
        a, b = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '+':
            if isinstance(a, str) and isinstance(b, str):
                return a + b
            elif isinstance(a, int) and isinstance(b, int):
                return a + b
            else:
                raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: operator '+' can only be used with string or numeric types.")
        elif op == '-':
            if isinstance(a, int) and isinstance(b, int):
                return a - b
            else:
                raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: operator '-' can only be used with numeric types.")
        else:
            raise InterpError(f"{self.loc(ctx)}\n[SYNTAX_ERROR]: undefined operator '{op}'")
    
    def visitMulDiv(self, ctx):
        a, b = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        op = ctx.op.text
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: operator '{op}' can only be used with numeric types.")
        if op == '/' and b == 0:
            raise InterpError(f"{self.loc(ctx)}\nInterpError: Cannot divide by zero. Division by zero is undefined.")
        return a / b if op == '/' else a * b
        
    def visitMod(self, ctx):
        a, b = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: operator '%' can only be used with numeric types.")
        return a % b
    
    def visitPow(self, ctx):
        a, b = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: operator '**' can only be used with numeric types.")
        return a ** b

    def visitFuncCall(self, ctx):
        name = ctx.ID().getText()
        args = [self.visit(e) for e in (ctx.arg_list().expr() if ctx.arg_list() else [])]
        try:
            value = self.env.get(name)
            if isinstance(value, Function):
                return value.call(self, args)
            if callable(value):
                return value(*args)
        except KeyError:
            pass
        if name in self.stdlib:
            try:
                return self.stdlib[name](args)
            except Exception as e:
                raise InterpError(f"{self.loc(ctx)}\n[RUNTIME_ERROR]: {e}")
        raise InterpError(f"{self.loc(ctx)}\n[NAME_ERROR]: function '{name}' is not defined.")
    
    def visitInt(self, ctx):
        i = ctx.INT().getText()
        return int(i)
    
    def visitFloat(self, ctx):
        f = ctx.FLOAT().getText()
        return float(f)
    
    def visitString(self, ctx):
        string = ctx.STRING().getText()
        try:
            value = ast.literal_eval(string)
        except Exception:
            return string[1:-1]
        return value
    
    def visitTrue(self, ctx):
        return True
    
    def visitFalse(self, ctx):
        return False

    def visitId(self, ctx):
        try:
            return self.env.get(ctx.ID().getText())
        except KeyError:
            raise InterpError(f"{self.loc(ctx)}\n[NAME_ERROR]: variable '{ctx.ID().getText()}' is not defined.")
        
    def visitArray(self, ctx):
        return [self.visit(e) for e in (ctx.arg_list().expr() if ctx.arg_list() else [])]
    
    def visitDict(self, ctx):
        if not ctx.pair_list():
            return {} 
        res = {}
        for p in ctx.pair_list().pair():
            k = bytes(p.STRING().getText[1:-1], 'utf-8').decode('unicode_escape')
            value = self.visit(p.expr())
            res[k] = value
        return res
    
    def visitIndex(self, ctx):
        base = self.visit(ctx.expr(0))
        index = self.visit(ctx.expr(1))
        try:
            return base[index]
        except Exception:
            raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: invalid operation between '{type(base).__name__}' and '{type(index).__name__}'.")
    
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    
    def bin(self, ctx, op_f):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        try:
            return op_f(l, r)
        except Exception:
            raise InterpError(f"{self.loc(ctx)}\n[TYPE_ERROR]: invalid operation between '{type(l).__name__}' and '{type(r).__name__}'.")
        
    def truthy(self, value):
        if value is None:
            return False
        if isinstance(value, int):
            return value != 0
        if isinstance(value, str):
            return len(value) > 0
        return True
