from enum import Enum

JSON_COMMA = ','
JSON_COLON = ':'
JSON_LEFTBRACKET = '['
JSON_RIGHTBRACKET = ']'
JSON_LEFTBRACE = '{'
JSON_RIGHTBRACE = '}'
JSON_QUOTE = '"'
JSON_WHITESPACE = [' ', '\t', '\b', '\n', '\r']
JSON_SYNTAX = [JSON_COMMA, JSON_COLON, JSON_LEFTBRACKET, JSON_RIGHTBRACKET,
               JSON_LEFTBRACE, JSON_RIGHTBRACE]
FALSE_LEN = len('false')
TRUE_LEN = len('true')
NULL_LEN = len('null')

class TokenKind(Enum):
    EndOfStringToken = "EndOfStringToken"
    StringToken = "StringToken"
    BadToken = "BadToken"
    SyntaxToken = "SyntaxToken"
    NumberToken = "NumberToken"
    BoolToken = "BoolToken"
    NoneToken = "NoneToken"

class Token:
    def __init__(self, kind, position, value) -> None:
        self.kind = kind
        self.position = position
        self.value = value

class Lexer:
    def __init__(self, string):
        self.string = string
        self.position = 0

    def next(self):
        self.position += 1

    def lex_string(self):
        if self.string[self.position] == JSON_QUOTE:
            self.next()
        else:
            return None, self.position
        
        start = self.position 

        for c in self.string[start:]:
            if c == JSON_QUOTE:
                self.next()
                return self.string[start:self.position-1], start
            else:
                self.next()

        raise Exception('Expected end-of-string quote')
    
    def lex_number(self):
        if self.string[self.position].isdigit():
            start = self.position
            
            while self.string[self.position].isdigit():
                self.next()

            return self.string[start:self.position], start
        
        return None, self.position
    
    def lex_bool(self):
        start = self.position
        string_len = len(self.string[start:])

        if string_len >= TRUE_LEN and self.string[start:start+TRUE_LEN] == 'true':
            self.position += TRUE_LEN
            return True, start
        elif string_len >= FALSE_LEN and self.string[start:start+FALSE_LEN] == 'false':
            self.position += FALSE_LEN
            return False, start

        return None, self.position
    
    def lex_null(self):
        start = self.position
        string_len = len(self.string[self.position:])

        if string_len >= NULL_LEN and self.string[self.position:self.position+NULL_LEN] == 'null':
            self.position += NULL_LEN
            return True, start

        return None, self.position

    def nextToken(self):
        if self.position >= len(self.string):
            return Token(TokenKind.EndOfStringToken, self.position, None)
        
        # skip all whitespaces except it is inside a current running string
        while self.string[self.position] in JSON_WHITESPACE:
            self.next()
            if self.position >= len(self.string):
                return Token(TokenKind.EndOfStringToken, self.position, None)
        
        string, string_position = self.lex_string()
        if string is not None:
            return Token(TokenKind.StringToken, string_position, string)
        
        number, number_position = self.lex_number()
        if number is not None:
            return Token(TokenKind.NumberToken, number_position, number) 
        
        bool, bool_position = self.lex_bool()
        if bool is not None:
            return Token(TokenKind.BoolToken, bool_position, bool)
        
        null, null_position = self.lex_null()
        if null is not None:
            return Token(TokenKind.NoneToken, null_position, None)
        
        if self.string[self.position] in JSON_SYNTAX:
            token = Token(TokenKind.SyntaxToken, self.position, self.string[self.position])
            self.next()
            return token
        
        return Token(TokenKind.BadToken, self.position + 1, self.string[self.position])


def main():
    lexer = Lexer('{"key": {}}')
    tokens = []

    while True:
        token = lexer.nextToken()

        if (token.kind == TokenKind.EndOfStringToken):
            break
        elif (token.kind == TokenKind.BadToken):
            # exit with code 1
            raise Exception('Unexpected character: {}'.format(token.value)) 

        tokens.append(token.value)

    return tokens
    

if __name__ == "__main__":
    main()