#!/usr/bin/python3
"""
    doctest style unit tests for dyadic.py

    Each test passes a string to the evaluate function.

    Each string represnts an APL expression involving a dyadic function.

    Many of these expressions exercise the vector calculator.

    WIP - grows as dyadic.py grows.
"""

from evaluate import evaluate

from apl import print_result

from apl_error import APL_exception as apl_exception

# ------------------------------

def     test (expression):
    """
    test both positive and negative outcomes
    """
    try:
        print_result(evaluate(expression))
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     aardvark ():
    """
    so named to ensure it is run first

    >>> test('P ← 0 0.5 1 2')
    0 0.5 1 2
    >>> test('N ← ¯0 ¯0.5 ¯1 ¯2')
    0 ¯0.5 ¯1 ¯2

    >>> test('PD ← 0.25 0.5 1 2')
    0.25 0.5 1 2
    >>> test('ND ← ¯0.25 ¯0.5 ¯1 ¯2')
    ¯0.25 ¯0.5 ¯1 ¯2
    """
    pass

# ------------------------------

def     dyadic_plus ():
    """
    >>> test('1 + 1')
    2

    >>> test('0 + P')
    0 0.5 1 2
    >>> test('N + 0')
    0 ¯0.5 ¯1 ¯2

    >>> test('P + P')
    0 1 2 4
    >>> test('N + N')
    0 ¯1 ¯2 ¯4
    >>> test('P + N')
    0 0 0 0
    >>> test('N + P')
    0 0 0 0
    """
    pass

# --------------

def     dyadic_minus ():
    """
    >>> test('1 - 1')
    0

    >>> test('0 - P')
    0 ¯0.5 ¯1 ¯2
    >>> test('N - 0')
    0 ¯0.5 ¯1 ¯2

    >>> test('P - P')
    0 0 0 0
    >>> test('N - N')
    0 0 0 0
    >>> test('P - N')
    0 1 2 4
    >>> test('N - P')
    0 ¯1 ¯2 ¯4
    """
    pass

# --------------

def     dyadic_times ():
    """
    >>> test('1 × 1')
    1

    >>> test('1 × P')
    0 0.5 1 2
    >>> test('N × 1')
    0 ¯0.5 ¯1 ¯2

    >>> test('P × P')
    0 0.25 1 4
    >>> test('N × N')
    0 0.25 1 4
    >>> test('P × N')
    0 ¯0.25 ¯1 ¯4
    >>> test('N × P')
    0 ¯0.25 ¯1 ¯4
    """
    pass

# --------------

def     dyadic_divide ():
    """
    >>> test('0 ÷ 0')
    1
    >>> test('1 ÷ 0')
    DOMAIN ERROR
    >>> test('0 ÷ 1')
    0
    >>> test('1 ÷ 1')
    1

    >>> test('1 ÷ PD')
    4 2 1 0.5
    >>> test('ND ÷ 1')
    ¯0.25 ¯0.5 ¯1 ¯2

    >>> test('P ÷ PD')
    0 1 1 1
    >>> test('N ÷ ND')
    0 1 1 1
    >>> test('P ÷ ND')
    0 ¯1 ¯1 ¯1
    >>> test('N ÷ PD')
    0 ¯1 ¯1 ¯1
    """
    pass

# ------------------------------

from dyadic import dyadic_function

from apl_quantity import APL_scalar as apl_scalar

# ------------------------------

def     dyadic_test (A,symbol,B):
    """
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
    except apl_exception as error:
        print(error.message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
