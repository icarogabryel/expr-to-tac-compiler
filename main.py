from exprScanner import Scanner
from exprParser import Parser
from exprCompiler import Compiler

def main():
    with open('input.txt', 'r') as file:
        text = file.read()

    scanner = Scanner(text)
    parser = Parser(scanner.getTokenSteam())
    compiler = Compiler(parser.getAst())
    
    print(compiler.getCompCode())

if __name__ == '__main__': main()
