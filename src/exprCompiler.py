from exprParser import Node

class Compiler:
    def __init__(self, node: Node):
        self.tacQuad = []
        self.varNumber = 0

        self.makeTacQuad(node)
 
    def getCompCode(self):
        compCode = ''
        
        for quad in self.tacQuad:
            compCode += f'{quad[0]}, {quad[1]}, {quad[2]}, {quad[3]}\n'

        return compCode

    def makeTacQuad(self, node: Node):
        match(node.getNodeToken()[0]):
            case 'number':
                return int(node.token[1])
            
            case 'plus':
                arg1 = self.makeTacQuad(node.sons[0])
                arg2 = self.makeTacQuad(node.sons[1])

                self.varNumber += 1
                var = f't{self.varNumber}'

                self.tacQuad.append(('+', arg1, arg2, var))

                return var
            
            case 'times':
                arg1 = self.makeTacQuad(node.sons[0])
                arg2 = self.makeTacQuad(node.sons[1])

                self.varNumber += 1
                var = f't{self.varNumber}'

                self.tacQuad.append(('*', arg1, arg2, var))

                return var
