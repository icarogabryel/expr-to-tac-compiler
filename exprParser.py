class Node:
    def __init__(self, token) -> None:
        self.token = token
        self.sons = []

    def addSon(self, node):
        self.sons.append(node)
    
class Parser:
    def __init__(self, tokenStream) -> None:
        self.tokenStream = tokenStream
        self.index = -1

        self.parse()

    def getCurrentToken(self):
        return self.tokenStream[self.index]
    
    def peekNextToken(self):
        return self.tokenStream[self.index + 1]
    
    def getNextToken(self):
        self.index +=1
        return self.tokenStream[self.index]

    def matchToken(self, expectedToken):
        if tokenRecived := self.getNextToken[0] != expectedToken:
            raise Exception(f'Sintax Error: {expectedToken} expected. Instead, {tokenRecived} recived.')
        else:
            return tokenRecived
    
    def parse(self):
        self.init()
    
    def init(): # todo: chage to first
        pass

    def factor(self):
        if self.peekNextToken[0] == 'lParen':
            self.matchToken('lParen')
            node = self.expr()
            self.matchToken('rParen')

            return node

        else:
            token = self.matchToken('number')
            node = Node(token)

            return node

    def term(self):
        try:
            sonNode1 = self.term()

            token = self.matchToken('times')
            node = Node(token)

            node.addSon(sonNode1)

            sonNode2 = self.factor()
            node.addSon(sonNode2)

            return node
        
        except:
            node = self.factor()
            return node

    def expr(self):
        try:
            sonNode1 = self.expr()

            token = self.matchToken('plus')
            node = Node(token)

            node.addSon(sonNode1)

            sonNode2 = self.term()
            node.addSon(sonNode2)

            return node
        
        except:
            node = self.term()
            return node
