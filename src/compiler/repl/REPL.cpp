#include "./REPL.h"

#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>

REPL::REPL(std::istream& INSTREAM, std::ostream& OUTSTREAM, Evaluator& EVALUATOR)
  : instream(INSTREAM)
  , outstream(OUTSTREAM)
  , evaluator(EVALUATOR)
{
    std::cout << "Construct\n\n";
        
    // Read in files.
    {
      std::ifstream in_file("welcome.txt");
      in_file >> welcome;
      in_file.close();
    }
      
    std::ifstream in_file("prompt.txt");
    {
      in_file >> prompt;
      in_file.close();
    }
    
    {
      std::ifstream in_file("help.txt");
      in_file >> help;
      in_file.close();
    }
}

void REPL::read()
{
	std::string text;
    
    std::cout << prompt << " ";
    getline(std::cin, text);
//     std::cout << text << '\n';
    user_input = text;
}

void REPL::evaluate()
{
    if(user_input == "help")
    {
        result = user_input;
    }
    else
    {
      result = "<todo: implement evaluator>"; // evaluator.setInput();   // placeholder
    }
}

void REPL::print()
{
	std::cout << result << '\n';
}

void REPL::loop()
{
    read();         // call read
    evaluate();     // call evaluate
    print();        // call print
    
    if((user_input == "exit") or (user_input == "quit"))
    {
      return;
    }
}

REPL::~REPL()
{
    std::cout << "\nDestruct\n";
}

std::ostream& operator<<(std::ostream& os, const REPL& rhs)
{
    os  << "default precision (6): " << rhs.getProduct() << '\n'
        << "std::setprecision(10): " << std::setprecision(10) << rhs.getProduct() << '\n'
        << "max precision:         "
        << std::setprecision(std::numeric_limits<long double>::digits10 + 1)
        << rhs.getProduct() << "\n";
    return os;
}
