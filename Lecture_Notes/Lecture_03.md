### Lecture 3: Simple Algorithms

* [Introduction](https://www.youtube.com/watch?v=Y0lczs-_w-I)

* [Iteration](https://www.youtube.com/watch?v=waIE0L9vfiI)
  * An iteration:
    * Starts with a test
    * Executes the loop body once if the test is true & reevaluates the test
    * Repeats until the test evaluates to false.
  * Iterating with `while`.
  * Some properties of iteration loops:
    * Iteration variables should be set outside the loop.
    * Need to test the iteration variable to check if done.
    * Need to change the iteration variable inside the iteration loop, in addition to other work.
  * Program run time now depends on the values of the variables in addition to the length of the code.

* [Guess and Check Algorithms](https://www.youtube.com/watch?v=-4Uvn-JUksI)
  * Decrementing function:
    * Maps set of program variables into an integer.
    * When loop is entered value is non-negative.
    * When value <= 0, loop terminates.
    * Value is decreasing every time through loop.
  * Exhaustive Enumeration: Start with one end for the possible set of values and try each one in turn.
  
* [Loop Mechanisms](https://www.youtube.com/watch?v=SKyhk7j3NJA)
  * Loops with `for`:
    * Form: for _identifier_ in _sequence_: _code block_
    * Identifier initially bound to the first value in sequence.
    * Code block executed.
    * Process repeated for each binding of the identifier.
  * A `break` keyword can be used to break out of a loop.
  * The `range` function can be used to generate a sequence of integers:
    * `range(n)` gives `[0, 1, 2, ... , n-1]`.
    * `range(m,n)` gives `[m, m+1, m+2, ... , n-1]`.
    
* [Floating Point Accuracy](https://www.youtube.com/watch?v=DKCKJJSYRU0)
  * Converting a decimal number to binary: Successively perform `bit = num%2` and `num = num/2`.
  * Not all floats can be represented exactly as a decimal. So, rather than checking the equality of two floats, check that their absolute diffrence is less than some tolerance.

* [Approximation Methods](https://www.youtube.com/watch?v=AQgw8njOMec)
  * While choosing step size:
    * If the step is too small, it will slow down the code.
    * If the step is too large, one may miss the solution without reaching sufficient accuracy.

* [Bisection Search](https://www.youtube.com/watch?v=hX1aUXnDwgA)
  * Explaination of bisection search algorithm.
  * Bisection search radically reduces computation time - highlighting that being smart about generating guesses is important.
  * Bisection search should work well on problems with _ordering_ property - 
     where the value of the function being solved varies monotonically with input value.
  
* [Demo: Bisection Search](https://www.youtube.com/watch?v=-VjpRFaz5f4)

* [Newton-Raphson Root Finding](https://www.youtube.com/watch?v=J1zJNuEFw2U)
  * Elaborates on the Newton-Raphson method ofguess generation for root finding.

[Back to course notes](../Course_Notes.md)
