# Generated from grammar/BasicScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BasicScriptParser import BasicScriptParser
else:
    from BasicScriptParser import BasicScriptParser

# This class defines a complete generic visitor for a parse tree produced by BasicScriptParser.

class BasicScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasicScriptParser#program.
    def visitProgram(self, ctx:BasicScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#statement.
    def visitStatement(self, ctx:BasicScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#assign.
    def visitAssign(self, ctx:BasicScriptParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#expr_s.
    def visitExpr_s(self, ctx:BasicScriptParser.Expr_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#if.
    def visitIf(self, ctx:BasicScriptParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#while.
    def visitWhile(self, ctx:BasicScriptParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#for.
    def visitFor(self, ctx:BasicScriptParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#try_catch.
    def visitTry_catch(self, ctx:BasicScriptParser.Try_catchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#throw.
    def visitThrow(self, ctx:BasicScriptParser.ThrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#break.
    def visitBreak(self, ctx:BasicScriptParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#continue.
    def visitContinue(self, ctx:BasicScriptParser.ContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#function.
    def visitFunction(self, ctx:BasicScriptParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#param_list.
    def visitParam_list(self, ctx:BasicScriptParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#return.
    def visitReturn(self, ctx:BasicScriptParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#block.
    def visitBlock(self, ctx:BasicScriptParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Or.
    def visitOr(self, ctx:BasicScriptParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Mod.
    def visitMod(self, ctx:BasicScriptParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#MulImplied.
    def visitMulImplied(self, ctx:BasicScriptParser.MulImpliedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#AddSub.
    def visitAddSub(self, ctx:BasicScriptParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#MulDiv.
    def visitMulDiv(self, ctx:BasicScriptParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Parens.
    def visitParens(self, ctx:BasicScriptParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#True.
    def visitTrue(self, ctx:BasicScriptParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Index.
    def visitIndex(self, ctx:BasicScriptParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#String.
    def visitString(self, ctx:BasicScriptParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#False.
    def visitFalse(self, ctx:BasicScriptParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Eq.
    def visitEq(self, ctx:BasicScriptParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Int.
    def visitInt(self, ctx:BasicScriptParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Array.
    def visitArray(self, ctx:BasicScriptParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#FuncCall.
    def visitFuncCall(self, ctx:BasicScriptParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Float.
    def visitFloat(self, ctx:BasicScriptParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Not.
    def visitNot(self, ctx:BasicScriptParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Dict.
    def visitDict(self, ctx:BasicScriptParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#And.
    def visitAnd(self, ctx:BasicScriptParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Rel.
    def visitRel(self, ctx:BasicScriptParser.RelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Pow.
    def visitPow(self, ctx:BasicScriptParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#Id.
    def visitId(self, ctx:BasicScriptParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#arg_list.
    def visitArg_list(self, ctx:BasicScriptParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#pair_list.
    def visitPair_list(self, ctx:BasicScriptParser.Pair_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicScriptParser#pair.
    def visitPair(self, ctx:BasicScriptParser.PairContext):
        return self.visitChildren(ctx)



del BasicScriptParser