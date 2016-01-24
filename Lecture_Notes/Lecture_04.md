### Lecture 4: Functions

* [Introduction](https://www.youtube.com/watch?v=vmz9pVWI2S4)

* [Capturing Computations as a Function](https://www.youtube.com/watch?v=zhKN60gDjk8)
  * So far we have covered numbers, assignments, input/output, comparisons, looping constructs - sufficient to be **Turing Complete** i.e. compute anything that is computable!
  * Functions give us abstraction: i.e. allow us to capture computations and treat it as if it were a primitive.
  * In python, functions are defined using `def _function name_ ( _formal parameters_): _function body_.
  * In python, at the begining of a function it is a good practice to describe the purpose of the function and inputs taken enclosed in a series of single or double quotes.
  * Functions have the properties of _decomposition_ and _abstraction_.
  * During a function call:
    * Expressions	for	each	parameter	are	evaluated, bound	to	formal	parameter	names	of	function.
    * Control	transfers	to	first	expression	in	body	of function
    * Body	expressions	executed	until	return	keyword	reached	(returning	value	of	next	expression)	or run	out	of	expressions (returning	None).
    * Invocation	is	bound	to	the	returned	value
    * Control	transfers	to	next	piece	of	code.

* [Environments](https://www.youtube.com/watch?v=jJqP3ZUSy5E)
  * Environment: Formalism for tracking binding of variables and values.
  * Explanation of how environmentsare used to evaluate functions.

* [Computing Powers as an Example](https://www.youtube.com/watch?v=o8tmvzs6F4Q)

* [Understanding Variable Binding](https://www.youtube.com/watch?v=qic9_yRWj5U)
  * Each	funcJon	call	creates	a	new	environment, which	scopes	bindings	of	formal	parameters and	values,	and	of	local	variables	(those created	with	assignments	within	body).
  * Scoping	often	called	static	or	lexical	because	scope	within	which	variable	has	value	is defined	by	extent	of	code	boundaries.

* [How Environments Separate Variable Bindings](https://www.youtube.com/watch?v=CsQrTLde-dM)
  * Each function call creates a new frame with local bindings.

* [Understanding Root Finding](https://www.youtube.com/watch?v=mylsICZfBpo)

* [Modules](https://www.youtube.com/watch?v=wq8v7M3Szr0)
  * One can put a bunch of related functions and variables in a python file - say _mymodule_.py and then access these functions using either:
    * `import` _mymodule_ followed by _mymodule_._myfunction_
    * `from` _mymodule `import *`, in which case you directly access the varaibles and functions without referencing the file name.


[Back to course notes](../Course_Notes.md)
