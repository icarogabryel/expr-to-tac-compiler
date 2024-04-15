class Scanner:
    def __init__(self, text: str):
        self.text = text
        self.tokenStream = []

        self.index = 0

        self.makeTokenStream()

    def makeTokenStream(self):
        while True:
            token = self.getNextToken()

            if token[0] == 'EOF':
                self.tokenStream.append(token)
                break

            self.tokenStream.append(token)

    def getNextToken(self):
            while self.getCurrentChar() is not None:
                if self.getCurrentChar().isspace():
                    self.skipWhiteSpace()
                    continue

                if self.getCurrentChar().isdigit():
                    return ('number',self.interger())
                
                if self.getCurrentChar() == '+':
                    self.advance()
                    return ('plus', '+')
                
                if self.getCurrentChar() == '*':
                    self.advance()
                    return ('times', '*')
                
                if self.getCurrentChar() == '(':
                    self.advance()
                    return ('lParen', '(')
                
                if self.getCurrentChar() == ')':
                    self.advance()
                    return ('rParen', ')')
                
                raise Exception('Invalid char')   

            return ('EOF', None)

    def getCurrentChar(self):
          return self.text[self.index] if self.index < len(self.text) else None
    
    def skipWhiteSpace(self):
         while self.getCurrentChar() is not None and self.getCurrentChar().isspace():
              self.advance()

    def interger(self):
        result = ''

        while self.getCurrentChar() is not None and self.getCurrentChar().isdigit():
            result += self.getCurrentChar()
            self.advance()

        return int(result)

    def advance(self):
         self.index += 1

    def getTokenSteam(self):
        return self.tokenStream
