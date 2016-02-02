### Lecture 6: Objects

* [Introduction](https://www.youtube.com/watch?v=PauHW4ObHDo)

* [Tuples](https://www.youtube.com/watch?v=d-SBFpxf8Bk)
  * A tuple is an ordered sequence of elements (that can be of different type).
  * Defined as `tuple_var = ( ele1, ele2, ... )`
  * Operations:
    * `+` for concatination.
    * Indexing using `[index]
    * Slicing using [start_ind:end_ind]
    * Create a singleton using `(ele1,)`. Note that the comma is needed to indicate that this is a tuple.

* [Lists](https://www.youtube.com/watch?v=jx0WwCGCh-0)
  * Similar to tuples in the operations defined above - but use `[]` instead of `()`.
  * Lists are mutable!
  * Aliasing - If you build a list that refrences other list(s) as its element(s), then if these lists change, the new list will too!
  
* [Operation on Lists](https://www.youtube.com/watch?v=CJh-mscFZgU)
  * Interate through elements in a list.
  * `append()` to a list (mutates list).
  * Concatenate lists with `+`.
  * Clone lists using `new_list = old_list[:]` (simply uning the name will only create a pointer to the old list).

* [Functions as Objects](https://www.youtube.com/watch?v=Kndq_cHHWOI)
  * Functions are first class objects:
    * They have types.
    * Can be elements of data structures like lists.
    * They can appear in expressions: as part of an assignment statement and as an arguement to a function.
  * The python function `map()` can be used to apply a function to lists of inputs.

* [Dictionaries](https://www.youtube.com/watch?v=mixmc-woOF8)
  * Dictionaries: Generalizations of lsits - indices are not ints but can be any immutable type and are referred to as keys.
  * Entries of dictionaries are unordered.
  
<br>

[Back to course notes](../Course_Notes.md)
