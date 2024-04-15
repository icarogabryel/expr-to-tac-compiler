class Node:
    def __init__(self, token) -> None:
        self.token = token
        self.sons = []

    def getNodeToken(self):
        return self.token
    
    def isEmpty(self):
        if self.token[0] == 'empty':
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return  f'{self.token}:{self.sons}'

    def addSonAtR(self, node):
        self.sons.append(node)

    def addSonAtL(self, node):
        self.sons = [node] + self.sons
    
class Parser:
    def __init__(self, tokenStream) -> None:
        self.tokenStream = tokenStream
        self.index = -1
        self.ast = None
        
        self.parse()

    def getAst(self):
        return self.ast
    
    def getCurrentToken(self):
        return self.tokenStream[self.index]
    
    def peekNextToken(self):
        if self.index < len(self.tokenStream) - 1:
            return self.tokenStream[self.index + 1]
    
    def getNextToken(self):
        self.index +=1
        return self.tokenStream[self.index]

    def matchNextToken(self, expectedToken):
        tokenRecived = self.getNextToken()[0]

        if tokenRecived != expectedToken:
            raise Exception(f'Sintax Error: {expectedToken} expected. Instead, {tokenRecived} recived.')
    
    def parse(self):
        self.ast = self.term()

    def expr(self):
        sonNode = self.term()
        node = self.exprDash()
        
        if node.isEmpty():
            return sonNode
        else:
            node.addSonAtL(sonNode)
            return node
        
    def exprDash(self):
        tempIndex = self.index
        try:
            token = self.matchNextToken('plus')
            node = Node(token)

            node.addSonAtR(self.term())

            sonNode = self.term()
            if not sonNode.isEmpty():
                node.addSonAtR(sonNode())
    
        except:
            self.index = tempIndex
            node = Node(('empty', None))
        
        return node

    def term(self):
        factorNode = self.factor()
        termDashNode = self.termDash()

        if termDashNode.isEmpty():
            node = factorNode
        else:
            termDashNode.addSonAtL(factorNode)
            node = termDashNode

        return node

    def termDash(self):
        if self.peekNextToken()[0] == 'times':
            self.matchNextToken('times')
            node = Node(self.getCurrentToken())

            factorNode = self.factor()
            termDashNode = self.termDash()

            if termDashNode.isEmpty():
                node.addSonAtR(factorNode)
            
            else:
                termDashNode.addSonAtL(factorNode)
                node.addSonAtR(termDashNode)

        else:
            node = Node(('empty', None))

        return node

    def factor(self):
        if self.peekNextToken() == 'lParen':
            self.matchNextToken('lParen')
            node = self.expr()
            self.matchNextToken('rParen')
            
            return node

        else:
            self.matchNextToken('number')
            node = Node(self.getCurrentToken())
            
            return node
