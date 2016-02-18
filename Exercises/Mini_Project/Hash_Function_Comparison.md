### Comparing Hash Functions

As part of problem 8 in [lecture 10](../../Lecture_Notes/Lecture_10.md) of the edx MOOC
[Introduction to Computer Science and Programming Using Python](https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-6),
three hash function are provided:

* First Hash Function:
```python
def hash(s):
    return string.ascii_lowercase.index(s[0])
```
* Second Hash Function:
```python
def hash(s):
    return string.ascii_lowercase.index(s[-1])
```
* Third Hash Function:
```python
def hash(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26
```

Asif Mehedi contributed [code](reference_file.py) to plot the performance
of the above three hash functions on a [list](words.txt) of 80,000+ English words.

This work has been extended to compare the performance of the above three hash functions
on the top 10,000 English, French, German and Dutch words.

