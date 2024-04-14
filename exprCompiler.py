from exprParser import Node

class Compiler:
    def __init__(self, node: Node):
        self.varNumber = -1
        self.x = self.getCompCode(node)

    def getCode(self):
        return self.x

    def getCompCode(self, node):
        match(node.token[0]):
            case 'number':
                return int(node.token[1])
            case 'plus':
                self.varNumber += 1
                return f't{self.varNumber}\nt{self.varNumber} = {self.getCompCode(node.children[0])} + {self.getCompCode(node.children[1])}'
            case 'times':
                self.varNumber += 1
                return f't{self.varNumber}\nt{self.varNumber} = {self.getCompCode(node.children[0])} * {self.getCompCode(node.children[1])}'
            
# n1 = Node(('number', '6'))
# n2 = Node(('number', '5'))
# n3 = Node(('number', '4'))

# n4 = Node(('plus', '+'))
# n5 = Node(('times', '*'))

# n5.children = [n2, n1]
# n4.children = [n3, n5]

# a = Compiler(n4)

# print(a.getCode())
