#include "./REPL.h"
#include <iostream>
#include <fstream>
#include <string>

Generator::Generator(std::istream& INSTREAM, std::ostream& OUTSTREAM,Evaluator&  EVALUATOR)
{
    std::cout << "Construct\n\n";
    
    instream    = INSTREAM;
    outstream   = OUTSTREAM;
    Evaluator   = EVALUATOR;
    
    // Read in files.
    ifstream in_file("welcome.txt", ifstream::in);
    in_file >> welcome;
    in_file.close();
    
    ifstream in_file("prompt.txt", ifstream::in);
    in_file >> prompt;
    in_file.close();
    
    ifstream in_file("help.txt", ifstream::in);
    in_file >> help;
    in_file.close();
}

REPL::read()
{
	std::string text;
    
    std::cout << prompt << " ";
    getline(std::cin, text);
//     std::cout << text << '\n';
    user_input = text;
}

REPL::evaluate()
{
	if(user_input == "help")
    {
        result = user_input;
    }
    else
    {
        result = Evaluator.setInput()   // placeholder
    }
}

REPL::print()
{
	std::cout << result << '\n';
}

REPL::loop()
{
	read();         // call read
    evaluate();     // call evaluate
    print();        // call print
    
    if((user_input == "exit") or (user_input == "quit"))
    {
        return
    }
}

REPL::~REPL()
{
    std::cout << "\nDestruct\n";
    
    delete  instream;
    delete  outstream;
    delete  Evaluator;
}

// std::ostream& operator<<(std::ostream& os, const REPL& rhs)
// {
//     os  << "default precision (6): " << rhs.getProduct() << '\n'
//         << "std::setprecision(10): " << std::setprecision(10) << rhs.getProduct() << '\n'
//         << "max precision:         "
//         << std::setprecision(std::numeric_limits<long double>::digits10 + 1)
//         << rhs.getProduct() << "\n";
//     return os;
// }
