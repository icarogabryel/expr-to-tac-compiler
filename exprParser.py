class Node:
    def __init__(self, token) -> None:
        self.token = token
        self.sons = []

    def __repr__(self) -> str:
        return  f'{self.token}:{self.sons}'
    
    def getNodeToken(self):
        return self.token
    
    def isEmpty(self):
        if self.token[0] == 'empty':
            return True
        else:
            return False

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
        tokenReceived = self.getNextToken()[0]

        if tokenReceived != expectedToken:
            raise Exception(f'Syntax Error: {expectedToken} expected. Instead, {tokenReceived} received.')
    
    def parse(self):
        self.ast = self.expr()

    def expr(self) -> Node:
        termNode = self.term()
        exprDashNode = self.exprDash()

        if exprDashNode.isEmpty():
            node = termNode
        else:
            exprDashNode.addSonAtL(termNode)
            node = exprDashNode

        return node
        
    def exprDash(self) -> Node:
        if self.peekNextToken()[0] == 'plus':
            self.matchNextToken('plus')
            node = Node(self.getCurrentToken())

            termNode = self.term()
            exprDashNode = self.exprDash()

            if exprDashNode.isEmpty():
                node.addSonAtR(termNode)
            
            else:
                exprDashNode.addSonAtL(termNode)
                node.addSonAtR(exprDashNode)

        else:
            node = Node(('empty', None))

        return node

    def term(self) -> Node:
        factorNode = self.factor()
        termDashNode = self.termDash()

        if termDashNode.isEmpty():
            node = factorNode
        else:
            termDashNode.addSonAtL(factorNode)
            node = termDashNode

        return node

    def termDash(self) -> Node:
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

    def factor(self) -> Node:
        if self.peekNextToken()[0] == 'lParen':
            self.matchNextToken('lParen')
            node = self.expr()
            self.matchNextToken('rParen')
            
            return node

        else:
            self.matchNextToken('number')
            node = Node(self.getCurrentToken())
            
            return node
