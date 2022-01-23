#!/usr/bin/env python3
# unit testing SubsetParser.py

import os
import sys
import unittest
## sys.path.append(os.path.realpath(__file__ + '/../../code/usr/share/'))
from SubsetParser               import SubsetParser
#from lark                       import exceptions

class TestAdd_SubsetParser(unittest.TestCase):
    # test SubsetParser
    def test_SubsetParser(self):
        """testing SubsetParser"""
        print()
        
        parse       = SubsetParser()
        control     = 'SubsetParser: Subset.lark'
        self.assertEqual(control, repr(parse))
        
        source      = '# Try this!'
        with self.assertRaises(RuntimeError) as e:
            result  = str(parse.parse(source))
        result      = str(e.exception)
        #print(result)
        control     = 'Unexpected end-of-input. Expected one of: \n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n'
        #print(control)
        #self.assertEqual(control,  result)
        
        source      = '// Try this!'
        with self.assertRaises(RuntimeError) as e:
            result  = str(parse.parse(source))
        result      = str(e.exception)
        #print(result)
        control     = 'Unexpected end-of-input. Expected one of: \n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n'
        #print(control)
        #self.assertEqual(control,  result)
        
        source      = '/* Try this! */'
        with self.assertRaises(RuntimeError) as e:
            result  = str(parse.parse(source))
        result      = str(e.exception)
        #print(result)
        control     = 'Unexpected end-of-input. Expected one of: \n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n\t* IDENTIFIER\n'
        #self.assertEqual(control,  result)
        
        source      = 'return   # none'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(reserved_word, [Token(IDENTIFIER, 'return')])])])"
        #print(control)
        self.assertEqual(control, result)
        
        source      = 'return 8   # outputs 8'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(reserved_word, [Token(IDENTIFIER, 'return'), Tree(number, [Token(DECNUM, '8')])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        source      = 'writeln()'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln')])])])"
        #print(control)
        self.assertEqual(control, result)
        
        source      = 'writeln(8)'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(valuelist, [Tree(number, [Token(DECNUM, '8')])])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        source      = 'writeln(8)   # outputs 8'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(valuelist, [Tree(number, [Token(DECNUM, '8')])])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        source      = 'writeln(8)   /* outputs 8 */'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(valuelist, [Tree(number, [Token(DECNUM, '8')])])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        source      = 'writeln(7, 9)'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(valuelist, [Tree(number, [Token(DECNUM, '7')]), Tree(number, [Token(DECNUM, '9')])])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        source      = 'writeln(7, 9) // 7 9'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(valuelist, [Tree(number, [Token(DECNUM, '7')]), Tree(number, [Token(DECNUM, '9')])])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        source      = 'writeln(2 + 3)\n'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(expression, [Tree(number, [Token(DECNUM, '2')]), Token(OPERATOR, '+'), Tree(number, [Token(DECNUM, '3')])])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        parse       = SubsetParser()
        source      = '# Try this!\n'
        source     += 'writeln(8)\n'
        source     += 'writeln(7,9)\n'
        source     += 'writeln(2 + 3)\n'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(valuelist, [Tree(number, [Token(DECNUM, '8')])])])]), Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(valuelist, [Tree(number, [Token(DECNUM, '7')]), Tree(number, [Token(DECNUM, '9')])])])]), Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(expression, [Tree(number, [Token(DECNUM, '2')]), Token(OPERATOR, '+'), Tree(number, [Token(DECNUM, '3')])])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        parse       = SubsetParser()
        source      = 'writeln(true)'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(bool, [Token(TRUE, 'true')])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        parse       = SubsetParser()
        source      = 'writeln(false)'
        result      = str(parse.parse(source))
        #print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(bool, [Token(FALSE, 'false')])])])])"
        #print(control)
        self.assertEqual(control, result)
        
        parse       = SubsetParser()
        source      = 'if true:\n'
        source     += '    writeln(2 + 3)\n'
        result      = str(parse.parse(source))
        print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(bool, [Token(FALSE, 'false')])])])])"
        #print(control)
        #self.assertEqual(control, result)
        
        parse       = SubsetParser()
        source      = 'if true:\n'
        source     += '    writeln(2 + 3)\n'
        source     += 'else:\n'
        source     += '    writeln(false)'
        result      = str(parse.parse(source))
        print(str(result))
        control     = "Tree(start, [Tree(statement, [Tree(function, [Token(IDENTIFIER, 'writeln'), Tree(bool, [Token(FALSE, 'false')])])])])"
        #print(control)
        #self.assertEqual(control, result)

# main function
if __name__ == '__main__':
    print("\n\nunit testing SubsetParser.py...\n\n")
    unittest.main()
