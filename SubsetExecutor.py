#!/usr/bin/env python3

from __future__ import print_function
from ctypes import CFUNCTYPE, c_uint8
import llvmlite.binding as llvm

##  @class SubsetExecutor
#   @brief transform Subset code
class SubsetExecutor():
    def __init__(self, mod):
        self.__mod      = mod
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        #self.__result   = ''
    
    def __ repr__(self):
        return "SubsetExecutor" # self.__result
    
    def run(self):
        mod = compile_ir(engine, llvm_ir)
        func_ptr        = engine.get_function_address("main")
        cfunc           = CFUNCTYPE(None)(func_ptr)
        #self.__result   = 
        cfunc()

