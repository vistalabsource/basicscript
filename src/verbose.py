from antlr4.error.ErrorListener import ErrorListener


class Verbose(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, ln, col, msg, e):
        raise SyntaxError(f"[LOCATION]: line: {ln}, column: {col}\n[SYNTAX_ERROR]: {msg}") 
