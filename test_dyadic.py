#!/usr/bin/python3
"""
    Unit test for dyadic.py - doctest style

    There are a handful of tests for each dyadic APL function.

    WIP - grows as dyadic.py grows

    WIP - scalar parameters only
"""

from apl_exception import APL_Exception as apl_exception

from dyadic import dyadic_function

# ------------------------------

def     dyadic_test (A,symbol,B):
    """
    >>> dyadic_test  (1,'+',0)
    1
    >>> dyadic_test  (0,'+',1)
    1
    >>> dyadic_test  (-1,'+',0)
    -1
    >>> dyadic_test  (0,'+',-1)
    -1

    >>> dyadic_test  (1,'-',0)
    1
    >>> dyadic_test  (0,'-',1)
    -1
    >>> dyadic_test  (-1,'-',0)
    -1
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
    0.0
    >>> dyadic_test (1,'÷',0)
    DOMAIN ERROR
    >>> dyadic_test (0,'÷',-1)
    -0.0
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
    -1
    >>> dyadic_test  (0,'⌊',-1)
    -1

    >>> dyadic_test  (1,'*',0)
    1.0
    >>> dyadic_test  (0,'*',1)
    0.0
    >>> dyadic_test  (-1,'*',0)
    1.0
    >>> dyadic_test  (0,'*',-1)
    DOMAIN ERROR

    >>> dyadic_test  (1,'⍟',0)
    DOMAIN ERROR
    >>> dyadic_test  (0,'⍟',1)
    0.0
    >>> dyadic_test  (-1,'⍟',0)
    DOMAIN ERROR
    >>> dyadic_test  (0,'⍟',-1)
    0.0

    >>> dyadic_test  (2,'⍟',4)
    2.0
    >>> dyadic_test  (2,'⍟',1024)
    10.0
    >>> dyadic_test  (10,'⍟',100)
    2.0
    >>> dyadic_test  (10,'⍟',1000000)
    6.0

    >>> dyadic_test  (3,'|',3)
    0.0
    >>> dyadic_test  (3,'|',4)
    1.0
    >>> dyadic_test  (3,'|',5)
    2.0
    >>> dyadic_test  (3,'|',-3)
    0.0
    >>> dyadic_test  (3,'|',-4)
    2.0
    >>> dyadic_test  (3,'|',-5)
    1.0

    >>> dyadic_test  (-3,'|',3)
    0.0
    >>> dyadic_test  (-3,'|',4)
    -2.0
    >>> dyadic_test  (-3,'|',5)
    -1.0
    >>> dyadic_test  (-3,'|',-3)
    0.0
    >>> dyadic_test  (-3,'|',-4)
    -1.0
    >>> dyadic_test  (-3,'|',-5)
    -2.0

    >>> dyadic_test  (0,'|',1)
    1
    >>> dyadic_test  (0,'|',0)
    0
    >>> dyadic_test  (0,'|',-1)
    -1

    >>> dyadic_test  (1,'?',1)
    (1,)
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
    -1
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
    0.0
    >>> dyadic_test  (2,'○',0)
    1.0
    >>> dyadic_test  (3,'○',0)
    0.0
    >>> dyadic_test  (4,'○',0)
    1.0
    >>> dyadic_test  (5,'○',0)
    0.0
    >>> dyadic_test  (6,'○',0)
    1.0
    >>> dyadic_test  (7,'○',0)
    0.0

    >>> dyadic_test  (0,'○',0.5)
    0.8660254037844386
    >>> dyadic_test  (4,'○',2)
    2.23606797749979
    >>> dyadic_test  (-4,'○',2)
    1.7320508075688772

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
    42.0
    >>> dyadic_test (21,'∧',15)
    105.0
    >>> dyadic_test (7.5,'∧',-5)
    -15.0
    >>> dyadic_test (-7.5,'∧',5)
    -15.0

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
        return dyadic_function(symbol)(A,B)
    except apl_exception as e:
        print (e.message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
