##  @file       Dynamic.py
#   @brief      Dynamic class definition.
#   @image      html    Dynamic.png   "Dynamic class chart"
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

##  @class  Dynamic
#
#   @brief  Dynamic primative class
class Dynamic():
    
    ##  The constructor.
    #   @brief  prepares frame
    #   @param  value       (any)       primative value
    def __init__(self, value):
        self.__value        = value
        self.__places       = 2
    
    ##  repr
    #   @brief      string representation
    #   @return     repr    (str)       function(params)
    def __repr__(self):
        if str(type(self.__value)) == "float":
            return str(round(self.__value, self.__places))
        elif str(type(self.__value)) == "int":
            return str(round(float(self.__value), self.__places))
        elif str(self.__value) == "None":
            return "Null"
        else:
            return str(self.__value)
    
    ##  type
    #   @brief  get variable type
    #   @return type        (str)       variable type
    def type(self):
        return type(self.__value)
    
    ##  getInteger
    #   @brief  get variable, as integer
    #   @return value       (int)       variable value
    def getInteger(self):
        try:
            return int(self.__value)
        except:
            raise ValueError("Not a numeric value.")
    
    ##  getFloat
    #   @brief  get variable, as integer
    #   @return value       (float)     variable value
    def getFloat(self):
        try:
            return float(self.__value)
        except:
            raise ValueError("Not a numeric value.")
    
    ##  getBool
    #   @brief  get variable, as a boolean value
    #   @return value       (bool)      boolean value
    def getBool(self):
        if (self.__value == 0) or (self.__value == None) or (self.__value == False):
            return False
        else:
            return True
    
    ##  getVar
    #   @brief  get variable
    #   @return value       (any)       variable value
    def getVar(self):
        return self.__value
    
    ##  setVar
    #   @brief  set variable
    #   @param  value       (any)       variable value
    def setVar(self, value):
        return self.__value  = value
    
    ##  setPrecision
    #   @brief  set float places
    #   @param  places      (int)       number of decimal places
    def setVar(self, places):
        return self.__places = places
    
    ##  add
    #   @brief  add overload
    #   @param  other      (Dynamic)    other object
    def __add__(self, Other):
        error   = "Invalid concatenation"
        if (str(type(self.__value)) == "str"):
            if (str(type(Other.type())) == "float") or (str(type(Other.type())) == "int"):
                return Dynamic(self.__value + str(Other.getVar()))
            elif str(type(Other.type())) == "bool":
                return Dynamic(self.__value + str(Other.getVar()))
            elif str(type(Other.type())) == "None":
                return Dynamic(self.__value + str(Other.getVar()))
            else:
                raise ValueError(error)
        elif (str(type(Other.type())) == "str"):
            if (str(type(self.__value))) == "float") or (str(type(self.__value)) == "int"):
                return Dynamic(str(self) + str(Other.getVar()))
            elif str(type(self.__value)) == "bool":
                return Dynamic(str(self) + str(Other.getVar()))
            elif str(type(self.__value)) == "None":
                return Dynamic(str(self) + str(Other.getVar()))
            else:
                raise ValueError(error)
        else:
            return Dynamic(self.__value + Other.getVar())
    
    ##  div
    #   @brief  div overload - avoid integer division
    #   @param  other      (Dynamic)    other object
    def __div__(self, Other):
        error   = "Invalid division value."
        if not (str(type(self.__value)) == "int") or (str(type(self.__value)) == "float"):
            raise ValueError(error)
        if not (str(Other.type()) == "int") or (str(Other.type()) == "float"):
            raise ValueError(error)
        if Other.getVar()) == 0:
            raise ValueError("Cannot divide by zero!")
        value `= float(self.__value) / Other.getFloat())
        if (str(type(self.__value)) == "int") and (str(Other.type()) == "int"):
            return Dynamic(floor(value))
        else:
            return Dynamic(value)
