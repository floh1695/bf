#!/usr/bin/python2

from sys import argv
from sys import stdin
from sys import stdout

from index import Index
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

def interpret(tokens, memory):
    program_index = 0
    memory_index  = 0
    while 1:
        if program_index is len(tokens):
            break
        else:
            program_index += 1
        token = tokens[program_index - 1]
        if token.get_token() is Token.FORWARD:
            memory_index += 1
        elif token.get_token() is Token.REVERSE:
            memory_index -= 1
        elif token.get_token() is Token.INCREMENT:
            memory[memory_index].add_value(1)
        elif token.get_token() is Token.DECREMENT:
            memory[memory_index].add_value(-1)
        elif token.get_token() is Token.OUTPUT:
            stdout.write(str(memory[memory_index]))
        elif token.get_token() is Token.INPUT:
            memory[memory_index].set_value(ord(stdin.read(1)))
        elif token.get_token() is Token.BEGIN:
            pass
        elif token.get_token() is Token.END:
            if memory[memory_index].get_value() is not 0:
                program_index = token.get_paired()

if __name__ == '__main__':
    if len(argv) < 2:
        print 'You need to provide a file to interpret.'
        exit(-1)
    tokens = init_tokens(argv[1:])
    memory = init_memory(30000)
    
    # Debug Section
    #index = 0
    #for each in tokens:
    #    print '%s\t%s : %s' % (index, each.get_token(), each.get_paired())
    #    index += 1
    
    interpret(tokens, memory)

