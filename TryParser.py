#!/usr/bin/env python3

import sys

from lark import Lark, Tree, Token, Transformer
import lark

class TryParser:
    def __init__(self):
        infile = open("Try.lark")
        language: str = infile.read()
        infile.close()
        self.__parser = Lark(language)

    def parse(self, input):
        tree = self.__parser.parse(input)
        return tree

class TryTransformer(lark.visitors.Transformer_InPlace):
    valuelist = list
    expression = list
    def OPERATOR(self, items):
        return items[0]
    def list(self, items):
        #print('list:', item)
        return list(items)
    def pair(self, key_value):
        #print(key_value)
        k, v = key_value
        return k, v
    def dict(self, items):
        #print(items)
        return dict(items)
    def tree(self, item):
        #print(item)
        results = []
        for child in item.children:
            results.append(child)
        return results
    def number(self, items):
        #print(items)
        return int(items[0])
    def instruction(self, items):
        #print(items)
        #return items
        return Instruction(items[0], items[1])

class Instruction:
    def __init__(self, name, arguments):
        #print('INSTRUCTION: {0} {1}'.format(name, arguments))
        self.name = name
        self.arguments = arguments
    
    def __repr__(self):
        return "{{Instruction {0}: {1}}}".format(self.name, self.arguments)

    def getName(self):
        return self.name

    def getArguments(self):
        return self.arguments
        

def printIt(items, info, indent = ""):
    indentMore = indent + "\t"
    print("{0}[ Begin {1}:".format(indent, info))
    for item in items:
        if isinstance(item, lark.Tree):
            printIt(item.children, item.data, indentMore)
        else:
            print("{0}{1},".format(indentMore, item))
    print("{0}End {1} ]".format(indent, info))

class Interpreter():
    def __init__(self):
        pass
    
    def __repr__(self):
        return 'Trylang Interpreter'
    
    def interpret(self, tree):
        #print(tree)
        self.__tree = tree
        for child in tree:
            if child.getName() == 'print':
                operation = child.getName()
                params = child.getArguments()
                if (len(params) > 1) and (params[1] == '+'):
                    print(self.evaluate(params))
                else:
                    if len(params) == 1:
                        print(params[0])
                    else:
                        result = ''
                        for i in range(len(params)):
                            if not i == 0:
                                result += ' '
                            result += str(params[i])
                        print(result)
    
    def evaluate(self, expr):
        if  expr[1] == '+':
            return expr[0] + expr[2]


if __name__ == '__main__':
    # read in file
    infile = open("try.try")
    input: str = infile.read()
    infile.close()
    
    # parse file
    parser = TryParser()
    tree   = parser.parse(input)
    
    # transform tree
    TrTrans = TryTransformer()
    x_form_tree = TrTrans.transform(tree)
    result = []
    for child in x_form_tree.children:
        result.append(child)
    print(result)
    #control = '[{Instruction print: [8]}, {Instruction print: [7, 9]}]'
    #print(control)
    #print('match:', str(result) == control)
    
    # Interpreter fun!
    #I   = Interpreter()
    #I.interpret(result)
