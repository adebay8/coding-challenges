
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


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.position = 0

    def next(self):
        self.position += 1

    def parse_array(self):
        result  = []

        if self.tokens[self.position] == JSON_RIGHTBRACKET:
            self.next()
            return result
        
        while True:
            value = self.parse()
            result.append(value)

            current_token = self.tokens[self.position]
            self.next()

            if current_token == JSON_RIGHTBRACKET:
                return result
            elif current_token != JSON_COMMA:
                raise Exception("error")

        return []

    def parse_object(self):
        result = {}

        if self.tokens[self.position] == JSON_RIGHTBRACE:
            self.next()
            return result
        
        while True:
            json_key = self.tokens[self.position]

            if type(json_key) is str:
                self.next()
            else:
                raise Exception('Expected string key, got: {}'.format(json_key))
            
            if self.tokens[self.position] != JSON_COLON:
                raise Exception('Expected colon after key in object, got: {}'.format(self.tokens[self.position]))

            self.next()
            json_value = self.parse()

            result[json_key] = json_value

            current_token = self.tokens[self.position]
            self.next()

            if current_token == JSON_RIGHTBRACE:
                return result
            elif current_token != JSON_COMMA:
                raise Exception('Expected comma after pair in object, got: {}'.format(current_token))
            

    def parse(self, is_root=False):
        if not self.tokens or (is_root and self.tokens[self.position] != JSON_LEFTBRACE):
            raise Exception("Invalid JSON token, JSON must start with open curly bracket")
        
        current_token = self.tokens[self.position]
        self.next()

        if current_token == JSON_LEFTBRACE:
            return self.parse_object()
        elif current_token == JSON_LEFTBRACKET:
            return self.parse_array()
        else:
            return current_token