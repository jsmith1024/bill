#!/usr/bin/env python3

#import sys
from Statement          import Statement
#from lark import Lark, Tree, Token, Transformer
import lark

##  @class SubsetTransformer
#   @brief transform Subset code
class SubsetTransformer(lark.visitors.Transformer_InPlace):
    tree        = list
    valuelist   = list
    expression  = list
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
    #def tree(self, item):
        ##print(item)
        #results = []
        #for child in item.children:
            #results.append(child)
        #return results
    def number(self, items):
        #print(items)
        return int(items[0])
    def statement(self, items):
        #print(items)
        #print(type(items))
        #print(type(items[0]))
        if isinstance(items[0], lark.tree.Tree):
            items = self.tree(items[0])
        return Statement(items[0], items[1])

#def printIt(items, info, indent = ""):
    #indentMore = indent + "\t"
    #print("{0}[ Begin {1}:".format(indent, info))
    #for item in items:
        #if isinstance(item, lark.Tree):
            #printIt(item.children, item.data, indentMore)
        #else:
            #print("{0}{1},".format(indentMore, item))
    #print("{0}End {1} ]".format(indent, info))

