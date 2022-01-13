##  @file       Frame.py
#   @brief      Frame class definition.
#   @image      html    Frame.png   "Frame class chart"
#   @version    1.00

#   Copyright (C) 2018 J. Smith

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

##  @class  Frame
#
#   @brief  Store frame data.
class Frame():
    
    ##  The constructor.
    #   @brief      prepares frame
    #   @param  function    (str)       function name
    #   @return params      (list)      function parameters
    def __init__(self, function, params):
        self.__function     = function  # function name
        self.__params       = params    # list
        self.__vars         = dict()
    
    ##  repr
    #   @brief      string representation
    #   @return     repr    (str)       function(params)
    def __repr__(self):
        return self.__function + "(" + str(self.__params) + ")"
    
    ##  getTrace
    #   @brief  get variable
    #   @return type        (dict)      trace data
    def getTrace(self):
        return dict(function = self.__function, parameters = self.__params)
    
    ##  getVar
    #   @brief  get variable
    #   @param  key         (var)       variable name
    #   @return value       (any)       variable value
    def getVar(self, key):
        return self.__var[key]
    
    ##  setVar
    #   @brief  set variable
    #   @param  key         (any)       variable name
    #   @param  value       (any)       variable value
    def setVar(self, key, value):
        return self.__var[key]  = value