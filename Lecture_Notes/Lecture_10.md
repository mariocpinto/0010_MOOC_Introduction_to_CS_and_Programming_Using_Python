### Lecture 10: Memory and Search

* [Introduction](https://www.youtube.com/watch?v=jL4wZ8-RjTs)

* [Search Algorithms](https://www.youtube.com/watch?v=ZP_Q0vU-wU8)
  * Hard to invent new efficient algorithms - easier to reduce problems to known solutions.
  * Search algorithm: Method of finding an item or group of items with specific properties within a collection of items (search space).
  e.g. finding square root using exhaustive search, bisection method and Newton-Raphson method.
  * Python uses indirection to access elements of a list of arbitrary size objects in constant time.
  This is achieved by representing a list as a combination of a length and a sequence of fixed sized pointers to objects.
  * Based on this, linear search is linear (in Python).
  We can't do better than this if we do not know anything about the elements in the list.

* [Binary Search](https://www.youtube.com/watch?v=WqKqfr_tX0Y)
  * If the list is ordered, we can use the bisection method to efficiently search for elements.
  * Complexity is O(log2 n).

* [Selection Sort](https://www.youtube.com/watch?v=O1Is56hu4EU)
  * For an unsorted list: sorting + binary search is going to cost more than linear search.
  However, if we amortize costs for k searches, then the former may prove to be more economical.
  * Basic idea of selection sort: Find the smallest element and swap it with the element in the first position,
  find next smallest and swap it with the element in the second position, and so on.
  * Complexity: O(n^2).

* [Selection Sort Demo](https://www.youtube.com/watch?v=G0qUN3eTqlo)
  * Another [fun demo](https://www.youtube.com/watch?v=Ns4TPTC8whw).

* [Amortized Cost Analysis](https://www.youtube.com/watch?v=0b0bWcbQmFk)

* [Merge Sort](https://www.youtube.com/watch?v=bGWgqvhUfPU)
  * Merge sort:
    * Divide and conquer approach.
    * If list of length 0 or 1, done.
    * Else, split the list into two parts and sort each part.
    * Merge results (by looking at the first element of each sorted list).
  * Merging in linear in time.
  * Complexity of merge sort is n*log(n).
  * This does come with a cost in space, as it makes a copy of the list.

* [Merge Sort Demo](https://www.youtube.com/watch?v=O74Bw-NcCkY)
  * Another [fun demo](https://www.youtube.com/watch?v=XaqR3G_NVoo).

* [Hashing](https://www.youtube.com/watch?v=iw4BEqvvgiw)
  * Hashing allows us to do even better than merge sort + binary search.
  * As part of hashing:
    * Key is converted to an int using a hash function.
    * Int is used to index into a list.
    * If there is a collision (i.e. an entry already existing), then the entry is added to the existing sub list.
    * To retrieve data, we use a similar procedure, with linear search when there is are more than one entries in a location.
    * In Python, this is implemented in dictionaries.
  * Hashing allows search in almost O(1) (by a space trade-off so that the hash table is sufficiently large,
  with a good hash function to get close to uniform distribution and minimal collisions).

* [Selection and Merge Sort Demos with MIT Students](https://www.youtube.com/watch?v=iP_52CL5gYg)
  * [Selection Sort](https://www.youtube.com/watch?v=x6cDls2PWAU).
  * [Merge Sort](https://www.youtube.com/watch?v=u8Q9wNmL7G4).

<br>

[Back to course notes](../Course_Notes.md)
