### Lecture 2: Core Elements of Programs

* [Introduction](https://www.youtube.com/watch?v=9rVsdCMxeiA)

* [Types of Programming Languages](https://www.youtube.com/watch?v=BvooIjkNJ24)
  * Programming language: defines syntax and semantics needed to transltate computational ideas into mechanical steps.
  * Types of programming languages:
    * Low Level: 
      * Uses instructions similar to internal control unit.
      * Pipeline: I/P -> Checker (syntax/ static symantics) -> Interpreter -> Output.
    * High Level:
      * Uses higher level abstractions.
      * Two sub-types:
        * Compiled Language: 
          * High level abstractions are converted back to low level instructions before execution.
          * Pipeline: I/P -> Checker -> Compiler -> Object Code -> Interpreter -> Output.
          * e.g. C, Fortran.
          * Advantage: Code is faster.
          * Disadvantage: In case of failure, difficult to point to part of original source code that caused failure.
        * Interpreted Language:
          * Special program converts source code to internal data structure and then nterpreter sequentially converts each step to low level instruction and then executes.
          * e.g. Java, Python, Ruby.
          * Advantage: In case of failure, can know exactly where the program failed.
          * Disadvantage: Code is a little slower (as we are converting to machine language on the fly).

* [Python Objects](https://www.youtube.com/watch?v=Ejy6ILfh_hk)
  * Type of instructions:
    * Definitions: Statements that are evaluated and stored away.
    * Commands: Statements that are executed by the interpreter.
  * Data Objects:
    * Have a _type_ that defines the operations that can be performed on the object.
    * Can be scalare.g. int., float, bool; or non-scalar.
  * Expressions - combination of objects and operators. Simple form _object_ _operator_ _object_.
  * Operators on ints and floats:
    * Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`.
      * Operator precedence: brackets, power, multiplication & division, addition & subtraction. For equal precedence: Left to Right.
    * Comparisons: `>`, `<`, `>=`, `<=`, `==`, `!=`.
  * Operators on bools: `not`, `and`, `or`.
    * Operator precedence: brackets, not, and, or.
  * Type casting: Converting from one data type to another.  

* [Variables and Naming](https://www.youtube.com/watch?v=hXyXRmJA8RU)
  * Assignment statements can be used to create a binding between a name and a value.

* [Strings](https://www.youtube.com/watch?v=oJa01jCfTCU)
  * Strings are of type `str` and are defined using single or double quotes e.g. `'123'` or `"abc"`.
  * String multiplication: `2*'abc'` gives `abcabcabc`.
  * String concatination: `'abc' + '123'` gives `abc123`.
  * String length: use `len()`.
  * Index into strings using `[]`. Note that `'abc'[3]` will return an error since the index starts from 0, but `'abc'[-1]` will give `c`. `'abc'[-4]` will also give an error.
  * Slice strings using `str[start:end:<steps>]`. Python is forgiving if the end index exceeds the bounds. The optional parameter `steps` returns only every `steps` element e.g. `'Hello World'[1:8:3]` will return `eoo`.

* [Simple Scripts](https://www.youtube.com/watch?v=7-mC6P2B6Ac)
  * Getting input using `raw_input()` and printing output using `print()`.
  * Using a script file.
  * A straight line program: one which executes each statement in order, without any variation in order.
  * Comments in Python begin with a `#`.

* [Branching Programs](https://www.youtube.com/watch?v=l4C_D90rBcY)
  * Conditonal statements with `if`, `elif`, `else`.
  * Branching programs allow us to make choices to do different things. However each statement gets executed only once.
  * Such programs run in _constant time_ and run time depends only on the length of the program.

[Back to course notes](../Course_Notes.md)
