import sys

from exprScanner import Scanner
from exprParser import Parser
from exprCompiler import Compiler

def main():
    args = sys.argv[1:]
    
    if len(args) != 2:
        print('Usage: python main.py [input_file] [output_file]')
        return
    
    with open(args[0], 'r') as file:
        exprText = file.read()

    scanner = Scanner(exprText)
    parser = Parser(scanner.getTokenSteam())
    compiler = Compiler(parser.getAst())
    tacText = compiler.getCompCode()
    
    with open(args[1], 'w') as file:
        file.write(tacText)

    print('Compilation successful!')

if __name__ == '__main__': main()
