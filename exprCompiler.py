from exprParser import Node

class Compiler:
    def __init__(self, node: Node):
        self.varNumber = -1
        self.symbolTable = {}
        self.getCompCode
        self.compCode = ''

        self.makeCompCode(node)
        self.compCode = self.compCode[1:] + '\n'
 
    def getCompCode(self):
        return self.compCode

    def makeCompCode(self, node: Node):
        match(node.getNodeToken()[0]):
            case 'number':
                return int(node.token[1])
            
            case 'plus':
                self.varNumber += 1
                var = f't{self.varNumber}'

                temCompCode = '\n' + f'{var} = {self.makeCompCode(node.sons[0])} + {self.makeCompCode(node.sons[1])}'
                self.compCode += temCompCode

                return var
            
            case 'times':
                self.varNumber += 1
                var = f't{self.varNumber}'

                temCompCode = '\n' + f'{var} = {self.makeCompCode(node.sons[0])} * {self.makeCompCode(node.sons[1])}'
                self.compCode += temCompCode
                
                return var
 