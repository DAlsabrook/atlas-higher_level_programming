# Directory Title

python-everything_is_object

## Description

This is a directory for answering questions given about objects, code outcomes,
and other python concepts

### Files

* What function would you use to print the type of an object?
    * [0-answer](0-answer.txt)
* How do you get the variable identifier
(which is the memory address in the CPython implementation)?
    * [1-answer](1-answer.txt)
* In the following code, do a and b point to the same object?
    * [2-answer](2-answer.txt)
* In the following code, do a and b point to the same object?
    * [3-answer](3-answer.txt)
* In the following code, do a and b point to the same object?
    * [4-answer](4-answer.txt)
* In the following code, do a and b point to the same object?
    * [5-answer](5-answer.txt)
* What do these 3 lines print?

    s1 = "Best School"

    s2 = s1

    print(s1 == s2)
    * [6-answer](6-answer.txt)
* What do these 3 lines print?

    s1 = "Best"

    s2 = s1

    print(s1 is s2)
    * [7-answer](7-answer.txt)
* What do these 3 lines print?

    s1 = "Best School"

    s2 = "Best School"

    print(s1 == s2)
    * [8-answer](8-answer.txt)
* What do these 3 lines print?

    s1 = "Best School"

    s2 = "Best School"

    print(s1 is s2)
    * [9-answer](9-answer.txt)
* What do these 3 lines print?

    l1 = [1, 2, 3]

    l2 = [1, 2, 3]

    print(l1 == l2)
    * [10-answer](10-answer.txt)
* What do these 3 lines print?

    l1 = [1, 2, 3]

    l2 = [1, 2, 3]

    print(l1 is l2)
    * [11-answer](11-answer.txt)
* What do these 3 lines print?

    l1 = [1, 2, 3]

    l2 = l1

    print(l1 == l2)
    * [12-answer](12-answer.txt)
* What do these 3 lines print?

    l1 = [1, 2, 3]

    l2 = l1

    print(l1 is l2)
    * [13-answer](13-answer.txt)
* What does this script print?

    l1 = [1, 2, 3]

    l2 = l1

    l1.append(4)

    print(l2)
    * [14-answer](14-answer.txt)
* What does this script print?

    l1 = [1, 2, 3]

    l2 = l1

    l1 = l1 + [4]

    print(l2)
    * [15-answer](15-answer.txt)
* What does this script print?

    def increment(n):

        n += 1

    a = 1

    increment(a)

    print(a)
    * [16-answer](16-answer.txt)
* What does this script print?

    def increment(n):

        n.append(4)

    l = [1, 2, 3]

    increment(l)

    print(l)
    * [17-answer](17-answer.txt)
* What does this script print?

    def assign_value(n, v):

        n = v

    l1 = [1, 2, 3]

    l2 = [4, 5, 6]

    assign_value(l1, l2)

    print(l1)
    * [18-answer](18-answer.txt)
* Function that returns a copy of a list (uses slicing)
    * [19-copy_list](19-copy_list.py)
* a = ()

    Is a a tuple?
    * [20-answer](20-answer.txt)
* a = (1, 2)

    Is a a tuple?
    * [21-answer](21-answer.txt)
* a = (1)

    Is a a tuple?
    * [22-answer](22-answer.txt)
* a = (1, )

    Is a a tuple?
    * [23-answer](23-answer.txt)
* What does this script print?

    a = (1)

    b = (1)

    a is b
    * [24-answer](24-answer.txt)
* What does this script print?

    a = (1, 2)

    b = (1, 2)

    a is b
    * [25-answer](25-answer.txt)
* What does this script print?

    a = ()

    b = ()

    a is b
    * [26-answer](26-answer.txt)
* id(a)

    139926795932424

     a

    [1, 2, 3, 4]

     a = a + [5]

     id(a)

    Will the last line of this script print 139926795932424?
    * [27-answer](27-answer.txt)
*  a
    [1, 2, 3]

     id (a)

    139926795932424

     a += [4]

     id(a)

    Will the last line of this script print 139926795932424?
    * [28-answer](28-answer.txt)

## Author

[David Alsabrook](https://github.com/DAlsabrook)
