from exprScanner import Scanner

def main():
    with open('input.txt', 'r') as file:
        text = file.read()

    scanner = Scanner(text)

    print(scanner.getTokenSteam())

if __name__ == '__main__': main()
