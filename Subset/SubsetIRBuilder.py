#!/usr/bin/env python3

from llvmlite import ir

##  @class SubsetIRBuilder
#   @brief build intermediate representation
class SubsetIRBuilder():
    def __init__(self, t_tree):
        self.__t_tree   = t_tree
    
    def __repr__(self):
        return "SubsetIRBuilder"
    
    def build(self):
        
    
    #def OPERATOR(self, items):
        #return items[0]
    #def list(self, items):
        ##print('list:', item)
        #return list(items)
    #def pair(self, key_value):
        ##print(key_value)
        #k, v = key_value
        #return k, v
    #def dict(self, items):
        ##print(items)
        #return dict(items)
    ##def tree(self, item):
        ###print(item)
        ##results = []
        ##for child in item.children:
            ##results.append(child)
        ##return results
    #def number(self, items):
        ##print(items)
        #return int(items[0])
    #def statement(self, items):
        ##print(items)
        ##print(type(items))
        ##print(type(items[0]))
        #if isinstance(items[0], lark.tree.Tree):
            #items = self.tree(items[0])
        #return Statement(items[0], items[1])
