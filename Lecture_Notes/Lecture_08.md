### Lecture 8: Assertions and Exceptions

* [Introduction](https://www.youtube.com/watch?v=9bsFTZT7Cr8)

* [Exceptions](https://www.youtube.com/watch?v=o-dCfTwhMag)
  * Examples of exceptions: IndexError, TypeError, Syntax Error, NameError, AttributeError, ValueError, IOError.
  * Dealing with exceptions:
    * Fail silently: bad idea!
    * Return _error_ value:
      * What value? 
      * Caller must include error handling code
    * Stop execution, signal error condition.
  *Python provides the try except block to deal with exceptions:
    ```python
    try:
        <lines of code>
    except:
        <what to do in case of an exception>
    ```
  * Other extensions to `try` are:
    * `else`: Run when try body runs with no exceptions.
    * `finally`: Always run after try, except and else, even if they raise an error or issue a break, continue or return;
    useful for cleanup code.

* [Error Handling](https://www.youtube.com/watch?v=_mlbioa1mNk)
  * Error handling example.
  
* [Exceptions as Control Flow](https://www.youtube.com/watch?v=trWUo8ZakeA)

* [Assertions](https://www.youtube.com/watch?v=Xh9abDGtg7I)
  * `assert` statements can be used to raise `AssertionError` if the state of the input / computation does not match assumptions.
  * Using assertions is good defensive programming practice.
  * Can be used both for pre-conditions as well as post-conditions.

<br>

[Back to course notes](../Course_Notes.md)
