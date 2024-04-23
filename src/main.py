from exprScanner import Scanner
from exprParser import Parser
from exprCompiler import Compiler

def main():
    with open('input.txt', 'r') as file:
        exprText = file.read()

    scanner = Scanner(exprText)
    parser = Parser(scanner.getTokenSteam())
    compiler = Compiler(parser.getAst())
    tacText = compiler.getCompCode()
    
    with open('output.txt', 'w') as file:
        file.write(tacText)

    print('Compilation successful!')

if __name__ == '__main__': main()
