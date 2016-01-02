#!/usr/bin/python2

from sys import argv

from index import Index
from interpret import interpret
from token import Token
from token import build_tokens

def init_tokens(files):
    tokens = []
    for filename in files:
        tokens += build_tokens(filename)
    return tokens

def init_memory(size):
    memory = []
    while len(memory) < size:
        memory.append(Index(0))
    return memory

if __name__ == '__main__':
    if len(argv) < 2:
        print 'You need to provide a file to interpret.'
        exit(-1)
    tokens = init_tokens(argv[1:])
    memory = init_memory(30000)
    interpret(tokens, memory)

