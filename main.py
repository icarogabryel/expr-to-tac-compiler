from exprScanner import Scanner
from exprParser import Parser

def main():
    with open('input.txt', 'r') as file:
        text = file.read()

    scanner = Scanner(text)

    parser = Parser(scanner.getTokenSteam())

    n = parser.getAst()
    print(n)

if __name__ == '__main__': main()
