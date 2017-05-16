#!/usr/bin/python3
"""
    Unit test for dyadic.py - doctest style

    There are a handful of tests for each dyadic APL function.

    WIP - grows as dyadic.py grows

    WIP - scalar parameters (cast to apl_scalar) only
"""

from apl_exception import APL_Exception as apl_exception

from dyadic import dyadic_function

from apl import print_result

from apl_quantity import APL_scalar as apl_scalar

# ------------------------------

def     dyadic_test (A,symbol,B):
    """
    >>> dyadic_test  (1,'+',0)
    1
    >>> dyadic_test  (0,'+',1)
    1
    >>> dyadic_test  (-1,'+',0)
    ¯1
    >>> dyadic_test  (0,'+',-1)
    ¯1

    >>> dyadic_test  (1,'-',0)
    1
    >>> dyadic_test  (0,'-',1)
    ¯1
    >>> dyadic_test  (-1,'-',0)
    ¯1
    >>> dyadic_test  (0,'-',-1)
    1

    >>> dyadic_test  (1,'×',0)
    0
    >>> dyadic_test  (0,'×',1)
    0
    >>> dyadic_test  (-1,'×',0)
    0
    >>> dyadic_test  (0,'×',-1)
    0

    >>> dyadic_test (0,'÷',1)
    0
    >>> dyadic_test (1,'÷',0)
    DOMAIN ERROR
    >>> dyadic_test (0,'÷',-1)
    ¯0
    >>> dyadic_test (-1,'÷',0)
    DOMAIN ERROR

    >>> dyadic_test  (1,'⌈',0)
    1
    >>> dyadic_test  (0,'⌈',1)
    1
    >>> dyadic_test  (-1,'⌈',0)
    0
    >>> dyadic_test  (0,'⌈',-1)
    0

    >>> dyadic_test  (1,'⌊',0)
    0
    >>> dyadic_test  (0,'⌊',1)
    0
    >>> dyadic_test  (-1,'⌊',0)
    ¯1
    >>> dyadic_test  (0,'⌊',-1)
    ¯1

    >>> dyadic_test  (1,'*',0)
    1
    >>> dyadic_test  (0,'*',1)
    0
    >>> dyadic_test  (-1,'*',0)
    1
    >>> dyadic_test  (0,'*',-1)
    DOMAIN ERROR

    >>> dyadic_test  (1,'⍟',0)
    DOMAIN ERROR
    >>> dyadic_test  (0,'⍟',1)
    0
    >>> dyadic_test  (-1,'⍟',0)
    DOMAIN ERROR
    >>> dyadic_test  (0,'⍟',-1)
    0

    >>> dyadic_test  (2,'⍟',4)
    2
    >>> dyadic_test  (2,'⍟',1024)
    10
    >>> dyadic_test  (10,'⍟',100)
    2
    >>> dyadic_test  (10,'⍟',1000000)
    6

    >>> dyadic_test  (3,'|',3)
    0
    >>> dyadic_test  (3,'|',4)
    1
    >>> dyadic_test  (3,'|',5)
    2
    >>> dyadic_test  (3,'|',-3)
    0
    >>> dyadic_test  (3,'|',-4)
    2
    >>> dyadic_test  (3,'|',-5)
    1

    >>> dyadic_test  (-3,'|',3)
    0
    >>> dyadic_test  (-3,'|',4)
    ¯2
    >>> dyadic_test  (-3,'|',5)
    ¯1
    >>> dyadic_test  (-3,'|',-3)
    0
    >>> dyadic_test  (-3,'|',-4)
    ¯1
    >>> dyadic_test  (-3,'|',-5)
    ¯2

    >>> dyadic_test  (0,'|',1)
    1
    >>> dyadic_test  (0,'|',0)
    0
    >>> dyadic_test  (0,'|',-1)
    ¯1

    >>> dyadic_test  (1,'?',1)
    1
    >>> dyadic_test  (1,'?',0)
    DOMAIN ERROR
    >>> dyadic_test  (1,'?',-1)
    DOMAIN ERROR
    >>> dyadic_test  (1.5,'?',1)
    DOMAIN ERROR
    >>> dyadic_test  (1,'?',1.5)
    DOMAIN ERROR
    >>> dyadic_test  (2,'?',1)
    DOMAIN ERROR

    >>> dyadic_test  (1,'!',1)
    1
    >>> dyadic_test  (1,'!',0)
    0
    >>> dyadic_test  (1,'!',-1)
    ¯1
    >>> dyadic_test  (0,'!',1)
    1
    >>> dyadic_test  (0,'!',0)
    1
    >>> dyadic_test  (0,'!',-1)
    1
    >>> dyadic_test  (0,'!',5)
    1
    >>> dyadic_test  (1,'!',5)
    5
    >>> dyadic_test  (2,'!',5)
    10
    >>> dyadic_test  (3,'!',5)
    10
    >>> dyadic_test  (4,'!',5)
    5
    >>> dyadic_test  (5,'!',5)
    1

    >>> dyadic_test  (1,'○',0)
    0
    >>> dyadic_test  (2,'○',0)
    1
    >>> dyadic_test  (3,'○',0)
    0
    >>> dyadic_test  (4,'○',0)
    1
    >>> dyadic_test  (5,'○',0)
    0
    >>> dyadic_test  (6,'○',0)
    1
    >>> dyadic_test  (7,'○',0)
    0

    >>> dyadic_test  (0,'○',0.5)
    0.8660254038
    >>> dyadic_test  (4,'○',2)
    2.236067977
    >>> dyadic_test  (-4,'○',2)
    1.732050808

    # --

    >>> dyadic_test (1,'∨',0)
    1
    >>> dyadic_test (0,'∨',0)
    0
    >>> dyadic_test (6,'∨',7)
    1
    >>> dyadic_test (21,'∨',15)
    3
    >>> dyadic_test (7.5,'∨',-5)
    2.5
    >>> dyadic_test (-7.5,'∨',5)
    2.5

    >>> dyadic_test (1,'∧',0)
    0
    >>> dyadic_test (1,'∧',1)
    1
    >>> dyadic_test (6,'∧',7)
    42
    >>> dyadic_test (21,'∧',15)
    105
    >>> dyadic_test (7.5,'∧',-5)
    ¯15
    >>> dyadic_test (-7.5,'∧',5)
    ¯15

    >>> dyadic_test (0,'⍱',1)
    0
    >>> dyadic_test (0,'⍱',0)
    1
    >>> dyadic_test (0,'⍱',-1)
    DOMAIN ERROR
    >>> dyadic_test (-1,'⍱',0)
    DOMAIN ERROR

    >>> dyadic_test (0,'⍲',1)
    1
    >>> dyadic_test (1,'⍲',1)
    0
    >>> dyadic_test (0,'⍲',-1)
    DOMAIN ERROR
    >>> dyadic_test (-1,'⍲',0)
    DOMAIN ERROR

    # --

    >>> dyadic_test  (1,'<',0)
    0
    >>> dyadic_test  (0,'<',1)
    1
    >>> dyadic_test  (0,'<',0)
    0
    >>> dyadic_test  (-1,'<',0)
    1
    >>> dyadic_test  (0,'<',-1)
    0

    >>> dyadic_test  (1,'≤',0)
    0
    >>> dyadic_test  (0,'≤',1)
    1
    >>> dyadic_test  (0,'≤',0)
    1
    >>> dyadic_test  (-1,'≤',0)
    1
    >>> dyadic_test  (0,'≤',-1)
    0

    >>> dyadic_test  (1,'=',0)
    0
    >>> dyadic_test  (0,'=',1)
    0
    >>> dyadic_test  (0,'=',0)
    1
    >>> dyadic_test  (-1,'=',0)
    0
    >>> dyadic_test  (0,'=',-1)
    0

    >>> dyadic_test  (1,'≥',0)
    1
    >>> dyadic_test  (0,'≥',1)
    0
    >>> dyadic_test  (0,'≥',0)
    1
    >>> dyadic_test  (-1,'≥',0)
    0
    >>> dyadic_test  (0,'≥',-1)
    1

    >>> dyadic_test  (1,'>',0)
    1
    >>> dyadic_test  (0,'>',1)
    0
    >>> dyadic_test  (0,'>',0)
    0
    >>> dyadic_test  (-1,'>',0)
    0
    >>> dyadic_test  (0,'>',-1)
    1

    >>> dyadic_test  (1,'≠',0)
    1
    >>> dyadic_test  (0,'≠',1)
    1
    >>> dyadic_test  (0,'≠',0)
    0
    >>> dyadic_test  (-1,'≠',0)
    1
    >>> dyadic_test  (0,'≠',-1)
    1

    # --

    >>> dyadic_test (1,'⍕',1)
    FUNCTION NOT YET IMPLEMENTED
    >>> dyadic_test (1,'"',1)
    INVALID TOKEN
    """
    try:
        print_result(dyadic_function(symbol)(apl_scalar(A),apl_scalar(B)))
    except apl_exception as e:
        print (e.message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
