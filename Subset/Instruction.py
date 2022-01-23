#!/usr/bin/env python3

#import sys

#from lark import Lark, Tree, Token, Transformer
#import lark

class SubsetStatement:
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

