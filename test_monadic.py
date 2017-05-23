#!/usr/bin/python3
"""
    doctest style unit tests for monadic.py

    Each test passes a string to the evaluate function.

    Each string represnts an APL expression involving a monadic function.

    Many of these expressions exercise the vector calculator.

    WIP - grows as monadic.py grows.
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

def     monadic_plus ():
    """
    >>> test('+ 0')
    0

    >>> test('+ P')
    0 0.5 1 2
    >>> test('+ N')
    0 ¯0.5 ¯1 ¯2
    """
    pass

# --------------

def     monadic_minus ():
    """
    >>> test('- 0')
    0

    >>> test('- P')
    0 ¯0.5 ¯1 ¯2
    >>> test('- N')
    0 0.5 1 2
    """
    pass

# --------------

def     monadic_times ():
    """
    >>> test('× 0')
    0

    >>> test('× P')
    0 1 1 1
    >>> test('× N')
    0 ¯1 ¯1 ¯1
    """
    pass

# --------------

def     monadic_divide ():
    """
    >>> test('÷ 0')
    DOMAIN ERROR
    >>> test('÷ 1')
    1

    >>> test('÷ PD')
    4 2 1 0.5
    >>> test('÷ ND')
    ¯4 ¯2 ¯1 ¯0.5
    """
    pass

# ------------------------------

from monadic import monadic_function

from apl_quantity import APL_scalar as apl_scalar

# ------------------------------

def     monadic_test (symbol,B):
    """
    >>> monadic_test ('⌈',1.5)
    2
    >>> monadic_test ('⌈',0)
    0
    >>> monadic_test ('⌈',-1.5)
    ¯1

    >>> monadic_test ('⌊',1.5)
    1
    >>> monadic_test ('⌊',0)
    0
    >>> monadic_test ('⌊',-1.5)
    ¯2

    >>> monadic_test ('*',1)
    2.718281828
    >>> monadic_test ('*',0)
    1
    >>> monadic_test ('*',-1)
    0.3678794412

    >>> monadic_test ('⍟',2.718281828459045)
    1
    >>> monadic_test ('⍟',1.0)
    0
    >>> monadic_test ('⍟',0.36787944117144233)
    ¯1
    >>> monadic_test ('⍟',0)
    DOMAIN ERROR

    >>> monadic_test ('|',1)
    1
    >>> monadic_test ('|',0)
    0
    >>> monadic_test ('|',-1)
    1

    >>> monadic_test ('?',1)
    1
    >>> monadic_test ('?',0)
    DOMAIN ERROR
    >>> monadic_test ('?',-1)
    DOMAIN ERROR

    >>> monadic_test ('!',1)
    1
    >>> monadic_test ('!',0)
    1
    >>> monadic_test ('!',-1)
    DOMAIN ERROR
    >>> monadic_test ('!',2)
    2
    >>> monadic_test ('!',4)
    24
    >>> monadic_test ('!',8)
    40320
    >>> monadic_test ('!',0.5)
    0.8862269255
    >>> monadic_test ('!',0.25)
    0.9064024771
    >>> monadic_test ('!',0.125)
    0.9417426998

    >>> monadic_test ('○',1)
    3.141592654
    >>> monadic_test ('○',0)
    0
    >>> monadic_test ('○',-1)
    ¯3.141592654

    # --

    >>> monadic_test ('~',1)
    0
    >>> monadic_test ('~',0)
    1
    >>> monadic_test ('~',-1)
    DOMAIN ERROR

    # --

    >>> monadic_test ('⍕',1)
    FUNCTION NOT YET IMPLEMENTED
    >>> monadic_test ('"',1)
    INVALID TOKEN
    """
    try:
        print_result(monadic_function(symbol)(apl_scalar(B)))
    except apl_exception as error:
        print(error.message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
