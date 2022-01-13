##  @file       Exception.py
#   @brief      Exception class definition.
#   @image      html    Exception.png   "Exception class chart"
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

##  @class  Exception
#
#   @brief  Contain exception data.
class Exception():
    
    ##  The constructor.
    #   @brief  prepares frame
    #   @param  message     (str)       exception message
    def __init__(self, message):
        self.__message      = message
        self.__trace        = trace()   # gets Stack.getTrace()
    
    ##  repr
    #   @brief      string representation
    #   @return     data    (str)       exception message + trace
    def __repr__(self):
        result              = "EXCEPTION:\t" + self.__message
        for frame in self.__trace.reverse():
            result         += frame
        return result
    
    ##  message
    #   @brief  get variable
    #   @return type        (str)       exception message
    def message(self):
        return self.__message
    
    ##  getTrace
    #   @brief  get variable
    #   @return type        (list)      trace data
    def getTrace(self):
        return self.__trace.reverse()
    