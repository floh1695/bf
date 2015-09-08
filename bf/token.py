#!/usr/bin/python2

class Token:
    FORWARD    = '>'
    REVERSE    = '<'
    INCREMENT  = '+'
    DECREMENT  = '-'
    OUTPUT     = '.'
    INPUT      = ','
    BEGIN      = '['
    END        = ']'
    ALL_TOKENS = FORWARD + REVERSE + INCREMENT + DECREMENT + OUTPUT + INPUT + BEGIN + END
    def __init__(self, token, metadata={}):
        self.set_token(token)
        self.metadata = metadata.copy()
        self.set_paired(None)

    def get_token(self):
        return self.token

    def set_token(self, token):
        if token not in Token.ALL_TOKENS:
            raise Exception('Bad token! Please use on of `%s`' %
                    (ALL_TOKENS))
        self.token = token

    def get_paired(self):
        return self.metadata['paired']

    def set_paired(self, index):
        if index == None:
            self.metadata['paired'] = index
        else:
            self.metadata['paired'] = index % 30000

def find_matching_end(array):
    index = 0
    depth = 0
    while 1:
        token = array[index]
        if token is Token.BEGIN:
            depth += 1
        elif token is Token.END:
            depth -= 1
        if depth is 0:
            return index
        index += 1

def process(f):
    str = ''
    while 1:
        byte = f.read(1)
        if not byte:
            break
        if byte in Token.ALL_TOKENS:
            str += byte
    return str

def process_raw(raw_tokens):
    tokens = [None] * len(raw_tokens)
    index = 0
    while index < len(raw_tokens):
        token = raw_tokens[index]
        if token is Token.BEGIN:
            match_index = find_matching_end(raw_tokens[index:]) + index
            tokens[index] = Token(token)
            tokens[index].set_paired(match_index)
            tokens[match_index] = Token(Token.END)
            tokens[match_index].set_paired(index)
        elif token is Token.END:
            pass
        else:
            tokens[index] = Token(token)
        index += 1
    return tokens

def build_tokens(filename):
    raw_tokens = ''
    with file(filename, 'r') as f:
        raw_tokens = process(f)
    return process_raw(raw_tokens)

