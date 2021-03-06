##  @file       Stack.py
#   @brief      Stack class definition.
#   @image      html    Stack.png   "Stack class chart"
#   @version    1.00

#   Copyright (C) 2020 J. Smith

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the license, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>

from Frame import Frame

##  @class  Stack
#
#   @brief  Store stack frames.
class Stack():
    
    ##  The constructor.
    #   @brief      prepares stack
    def __init__(self):
        self.__stack        = []
    
    ##  repr
    #   @brief      string representation
    #   @return     repr    (str)   stack
    def __repr__(self):
        return self.__stack
    
    ##  addFrame
    #   @brief  Add a frame to the stack.
    #   @param  line        (list)      line of code, lexed
    def addFrame(self, line):
        function            = line[0]
        parameters          = line[1:]
        frame               = dict()
        frame["function"]   = function
        frame["parameters"] = parameters
        self.__stack.append(frame)
    
    ##  popFrame
    #   @brief  Removes a frome from the stack.
    def popFrame(self):
        self.__stack.pop()
    
    ##  getTrace
    #   @brief  Assemble a backtrace.
    #   @return traceace    (list)  backtrace
    def getTrace(self):
        trace = []
        for i in range(len(self.__stack)):
            trace += self.__stack[i]["funstion"] + str(tuple(self.__stack[i]["parameters"]))
        return trace
