from exprScanner import Scanner
from exprParser import Parser
from exprCompiler import Compiler

def main():
    with open('input.txt', 'r') as file:
        inText = file.read()

    scanner = Scanner(inText)
    parser = Parser(scanner.getTokenSteam())
    compiler = Compiler(parser.getAst())

    outText = compiler.getCompCode()
    
    with open('output.txt', 'w') as file:
        file.write(outText)

if __name__ == '__main__': main()
