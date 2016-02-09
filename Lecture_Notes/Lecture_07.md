### Lecture 7: Debugging

* [Introduction](https://www.youtube.com/watch?v=LxI8Mko_MKs)

* [Testing and Debugging](https://www.youtube.com/watch?v=xnhi9-ud_vI)
  * Testing Methods: Ways of trying code on examples to determine if they are running correctly.
  * Debugging Methods: Ways of fixing code that does not function as intended.
  * Designing for ease of testing and debugging:
    * Break code into components that can be independently debugged / tested.
    * Document constraints on modules.
    * Document assumptions behind code design.
  * We are ready to test when:
    * The program runs without errors.
    * We have a few input, expected output value pairs.

* [Test Suites](https://www.youtube.com/watch?v=f2655NqIYtA)
  * Goal: To show bugs exist.
  * For a test suite: Find a collection of inputs that has high likelihood of revealing bugs, yet is efficient:
    * Partition space of inputs into subsets that provide equivalent information about correctness.
    * Construct test suite that contains one input from each element of the partition.
    * Run test suite.
  * If there is no natural partition of input space, one can perform:
    * Random Testing.
    * Black Box Testing: Use heuristics based on exploring paths through the specifications.
    * Glass Box Testing: Use heuristics based on exploring paths through the code.

* [Black Box Testing](https://www.youtube.com/watch?v=l8Hw2V1tXmc)
  * Advantages:
    * Can be done by someone other than the implementer.
    * Avoids inherent biases of the implementer.
    * Test suite can be reused for a different implementation.

* [Glass Box Testing](https://www.youtube.com/watch?v=EeGAH_Es_7s)
  * A glass box test suite is path complete if every possible path through the code is tested at least once.
  * Rules of thumb for glass-box testing:
    * Exercise both branches of all if statements.
    * Ensure each except clause is executed.
    * For each for loop have tests where:
      * Loop is not entered.
      * Body of loop executed exactly once.
      * Body of loop executed more than once.
    * For each while loop:
      * Same cases as for loop.
      * Cases that catch all ways to exit loop.
    * For recursive functions, test with:
      * No recursive calls.
      * One recursive call.
      * More than one recursive call.

* [Test Drivers and Stubs](https://www.youtube.com/watch?v=j-d7-5lWcT4)
  * Conducting tests:
    * Start with unit testing: 
      * Tests at the module level.
      * Catches algorithmic bugs.
    * Move to integration testing:
      * Tests the system as a whole.
      * Catches interaction bugs.
    * Cycle between these phases.
    * Follow with regression testing to make sure previous code still works as expected.
  * Drivers: Simulate parts of program that use units being tested.
    * Set up the environment needed to run code.
    * Invoke code on predefined sequence of inputs.
    * Save results.
    * Report.
  * Stubs: Simulate part of the program used by units being tested.
  
* [Debugging](https://www.youtube.com/watch?v=euWTTA4YPaY)
  * History of debugging.
  * Overt v/s Covert bugs:
    * Overt: crash / runs forever.
    * Covert: Return an incorrect value that is hard to determine.
  * Persistent v/s Intermittent bugs:
    * Persistent: Every time code is run.
    * Intermittent: Some times, possibly with the same inputs.
  * Order of worrisomeness:
      * Overt and persistent.
      * Overt and intermittent.
      * Covert.

* [Debugging as Search](https://www.youtube.com/watch?v=4cz7_-_VlmI)
  * Example of debugging as search.
  * Some pragmatic hints:
    * Look for usual suspects.
    * Ask why the code si doing what it is doing, not why it isn't doing what you want it to do.
    * The bug is probably not where you think it is.
    * Explain the problem to someone else.
    * Don't believe the documentation.
    * Take a break :).

<br>

[Back to course notes](../Course_Notes.md)
