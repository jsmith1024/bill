#!/usr/bin/env python3

#import sys
from Statement          import Statement
#from lark import Lark, Tree, Token, Transformer
import lark
from llvmlite           import ir   #, IRBuilder

##  @class IRTransformer
#   @brief transform Subset code into LLVM IR
class IRTransformer(lark.visitors.Transformer_InPlace):
    tree        = list
    valuelist   = list
    #expression  = list
    def OPERATOR(self, items):
        return items[0]
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
    def tree(self, item):
        #print(item)
        results = []
        for child in item.children:
            results.append(child)
        return results
    def number(self, items):
        #print(items)
        return int(items[0])
    #def statement(self, items):
        ##print(items)
        ##print(type(items))
        ##print(type(items[0]))
        #if isinstance(items[0], lark.tree.Tree):
            #items = self.tree(items[0])
        #return Statement(items[0], items[1])
    def expression(self, item):
        pass
    def function_def(self, item):
        print('FUNCTION:')
        print(item[2].children)
        print()
        int8 = ir.IntType(8)
        fnty = ir.FunctionType(int8, [])
        module = ir.Module(name=__file__)
        func = ir.Function(module, fnty, name=item[0].value)
        block = func.append_basic_block(name=item[0].value)
        #print(block)
        builder = ir.IRBuilder(block)
        #result = builder.add(3, 4)
        #builder.ret(result)
        
        #for child in item[2].children:
            ##print('CHILD:', child)
            #x = self.transform(child)
            ##print(x)
        
        #x       = 0
        #y       = 0
        #cond    = ir.IRBuilder.icmp_unsigned('==', x, y, name='test')
        #print(cond)
        #lhs     = 7     #ir.IRBuilder.ret(7)
        #rhs     = 8     #ir.IRBuilder.ret(8)
        #result  = ir.IRBuilder.select(cond, lhs, rhs)
        
        x = ir.GlobalVariable(ir.Module('bob'), ir.IntType(8), item[0].value)
        y = ir.GlobalVariable(ir.Module('bob'), ir.IntType(8), item[0].value)
        result = builder.fadd(x, y, name="res")
        builder.ret(result)
        
        return module
    def declare_variable(self, item):
        #print('DECLARE_VARIABLE:')
        #print(item)
        x = ir.GlobalVariable(ir.Module(name=__file__), ir.IntType(8), item[0].value)
        x.initializer = 0
        return x
    def reserved_word(self, item):
        pass
    def if_statement(self, item):
        pass
