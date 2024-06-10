from .lexer import Lexer, TokenKind
from .parser import Parser

def get_tokens(string):
    lexer = Lexer(string)
    tokens = []

    while True:
        token = lexer.nextToken()

        if (token.kind == TokenKind.EndOfStringToken):
            break
        elif (token.kind == TokenKind.BadToken):
            # exit with code 1
            raise Exception('Unexpected character: {}'.format(token.value)) 
        
        # print(tokens)

        tokens.append(token.value)

    return tokens

def parse(string):
    tokens = get_tokens(string)
    parser = Parser(tokens)
    return parser.parse(is_root=True)