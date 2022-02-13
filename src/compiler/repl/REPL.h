#ifndef REPL_H
#define REPL_H

#include <iostream>
#include <string>

class Evaluator;

class REPL
{
    private:
        std::istream&   instream;   // reference to input stream
        std::ostream&   outstream;  // reference to output stream
        Evaluator&      evaluator;  // reference to Evaluator
 
        std::string     welcome;    // Welcom Screen
        std::string     prompt;     // repl prompt
        std::string     help;       // help screen
    
        std::string     user_input; // typed entry
        std::string     result;     // results of evaluation
    
    protected:
        /* read
         * @brief   Read user input.
         */
        void read();
        
        /* evaluate
         * @brief   Evaluate the input.
         */
        void evaluate();
        
        /* print
         * @brief   Print rhe output.
         */
        void print();
        
    public:
        
        /* destructor
         * @brief Tear down REPL.
         */
        ~REPL();

        /* constructor
         * @brief   Set up repl.
         * @details Store instream, outstream, and Evaluator references. Also store contents of welcome.txt, prompt.txt, and help.txt.
         * @param   instream            (reference)
         * @param   outstream           (reference)
         * @param   Evaluator           (reference)
         */
        REPL(std::istream& INSTREAM, std::ostream& OUTSTREAM, Evaluator& EVALUATOR);
        REPL(const REPL& rhs) = delete;     // Copy Constructor
        REPL(REPL&&) = delete;              // Move Constructor
        REPL& operator=(const REPL& rhs);   // assignment operator
        REPL& operator=(REPL&& rhs);        // assignment operator
        
        /* loop
         * @brief   Control the process.
         * @note    This is the only method to call directly.
         */
        void loop();

  inline std::string getProduct() const
  {
    return result;
  }
};

std::ostream& operator<<(std::ostream& os, const REPL& rhs);

#endif
