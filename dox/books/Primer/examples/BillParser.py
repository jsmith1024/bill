#!/usr/bin/env python3

#import sys

from lark import Lark, Tree, Token  # , Transformer
import lark
from lark.indenter import Indenter

##  @class BillParser
#   @brief parse Bill code
class BillParser():
    
    ##  constructor
    #   @brief  setup parser
    def __init__(self):
        self.__filename = "Bill.lark"
        infile          = open(self.__filename)
        language: str   = infile.read()
        infile.close()
        self.__parser   = Lark(language)        #, parser="lalr")
    
    ##  string representation
    #   @brief  return "BillParser: Bill.lark"
    def __repr__(self):
        return  'BillParser: ' + self.__filename
    
    ##  parse
    #   @brief  parse source code
    #   @param  source      (str)               source code
    #   @return (lark.tree.Tree)                parse tree
    def parse(self, source):
        try:
            tree = self.__parser.parse(source)
        except lark.exceptions.UnexpectedEOF as e:
            raise RuntimeError(e)
        except:
            raise RuntimeError('Unknown Parsing Error')
        return tree
