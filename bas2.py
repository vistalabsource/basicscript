from src.Tree import *
from lib.BasicScriptLexer import BasicScriptLexer
from lib.BasicScriptParser import BasicScriptParser
from antlr4 import *
import sys
from src.verbose import Verbose

def main(path):
    try:
        input_stream = FileStream(path, encoding='utf-8')
        lexer = BasicScriptLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(Verbose())
        stream = CommonTokenStream(lexer)
        parser = BasicScriptParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(Verbose())
        tree = parser.program()
        Tree().visit(tree)
    except FileNotFoundError:
        print(f"[ERROR]: Script file not found: '{path}'")
    except Exception as e:
        print(f"{e}")
        
    
if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) < 2:
        print("Basc Interpreter v1.0.0")
        print("Usage: basc <script> [options]")
        print("--version: print version information")
        print("--help: print help information")
        sys.exit(1)
    if '--version' in args:
        print("Basc v1.0.0")
        sys.exit(0)
    if '--help' in args:
        print("Usage: basc <script> [options]")
        print("--version: print version information")
        print("--help: print help information")
        sys.exit(0)

    main(sys.argv[1])
