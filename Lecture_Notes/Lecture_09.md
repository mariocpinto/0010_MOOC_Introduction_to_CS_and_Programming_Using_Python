### Lecture 9: Efficiency and Orders of Growth

* [Introduction](https://www.youtube.com/watch?v=j9as5xwUwA8)

* [Measuring Complexity](https://www.youtube.com/watch?v=Rjk7yfFQCPI)
  * Goals in designing programs:
    * It returns the correct answer on all legal inputs.
    * It performs the computation efficiently.
  * Computational complexity:
    * How much time will it take for the program to run?
    * How much memory will it need to run?
  * Need to balance minimizing computational complexity with conceptual complexity.
  * To measure complexity, we use the concept of a random access machine:
    * Steps are executed sequentially.
    * Steps in an operation take constant time: assignment, comparison, arithmetic operation, accessing object in memory.
  * In order to factor for the variation in run times with changing inputs, one can consider best case, worst case and average / expected case.
  * In summary:
    * Measure complexity as a function of input size.
    * Focus on largest factor in this expression.
    * Focus on worst case scenario.

* [Asymptotic Notation](https://www.youtube.com/watch?v=AU66NP1kQm0)
 * Rules of thumb for asymptotic complexity:
  * Describe running time in terms of number of basic steps.
  * If running time is a sum of multiple terms - keep one with the largest growth rate.
  * If the remaining term is a product, drop any multiplicative constants.
 * Big O notation: Gives the upper bound on the asymptotic growth of a function.

* [Complexity Classes](https://www.youtube.com/watch?v=yeJJdf1sf7Y)
 * The different classes are:
  * O(1): Constant running time.
  * O(log n): Logarithmic running time. e.g. bisection search, binary search.
  * O(n): Linear running time. e.g. linear search, recursive factorial implementation.
  * O(n log n): Log-linear running time. e.g. merge sort.
  * O(n^C): Polynomial running time. e.g. finding the intersection of strings.
  * O(C^n): Exponential running time. e.g. finding all the subsets in a list.
 * The time complexity of some python operations can be found [here](https://wiki.python.org/moin/TimeComplexity).

* [Comparing Complexity Classes](https://www.youtube.com/watch?v=--7OF8BOElA)
 * Graphs of the relative growth of different complexity classes.

<br>

[Back to course notes](../Course_Notes.md)
