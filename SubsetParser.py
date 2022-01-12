#!/usr/bin/env python3

#import sys

from lark import Lark, Tree, Token, Transformer
import lark

##  @class SubsetParser
#   @brief parse Subset code
class SubsetParser():
    
    ##  constructor
    #   @brief  setup parser
    def __init__(self):
        self.__filename = "Subset.lark"
        infile          = open(self.__filename)
        language: str   = infile.read()
        infile.close()
        self.__parser   = Lark(language)
    
    ##  string representation
    #   @brief  return "SubsetParser: Subset.lark"
    def __repr__(self):
        return  'SubsetParser: ' + self.__filename
    
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
