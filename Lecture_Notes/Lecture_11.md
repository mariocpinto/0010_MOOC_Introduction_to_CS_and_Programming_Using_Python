### Lecture 11: Classes

* [Classes: User-defined Types](https://www.youtube.com/watch?v=Qzj5zPHg6sE)
  * Everything is an object and has a type.
  * Objects are data abstractions that encapsulate:
    * an internal representation.
    * an interface for interacting with the object.
  * Advantages of OOP:
    * Divide and conquer development.
    * Classes make it easy to reuse code.

* [A Class Example](https://www.youtube.com/watch?v=bfpZRBTo5xc)
  * In python the `class` statement is used to define new types:
  `class class_name(super_class)`
  * To define initial values, define the `__init__` method:
  e.g.
  ```python
  class Coordinate(object):
    def __init__(self, x, y):
      self.x = x
      self.y = y

  c = Coordinate(3,4)
  ```

* [An Environment View of Classes](https://www.youtube.com/watch?v=xUv3fooko58)

* [Adding Methods to a Class](https://www.youtube.com/watch?v=AyLZkuFZsyo)
  * `__str__` method is used to define what gets printed when an object is called with the print statement:
  e.g.
  ```python
  def __str__(self):
    return "<"+self.x+","+self.y+">"
  ```
  * The `isinstance(object,class)`function can be used to check if an object is of a particular class type.

* [Example Class: A Set of Integers](https://www.youtube.com/watch?v=I9D9xfTHJ5E)
  * Example implementation of a class of a set of integers.
  
  <br>

  [Back to course notes](../Course_Notes.md)
