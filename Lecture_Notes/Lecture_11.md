### Lecture 11: Classes

* [Objects]()
  * Everything is an object and has a type.
  * Objects are data abstractions that encapsulate:
    * an internal representation.
    * an interface for interacting with the object.
  * Advantages of OOP:
    * Divide and conquer development.
    * Classes make it easy to reuse code.

* []()
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

* []()
  * An environment view of classes.

* []()
  * `__str__` method is used to define what gets printed when an object is called with the print statement:
  e.g.
  ```python
  def __str__(self):
    return "<"+self.x+","+self.y+">"
  ```
  * The `isinstance(object,class)`function can be used to check if an object is of a particular class type.

* []()
  * Example implementation of a class of a set of integers.
  
  <br>

  [Back to course notes](../Course_Notes.md)
