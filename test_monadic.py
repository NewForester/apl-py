#!/usr/bin/python3
"""
    Unit test for monadic.py - doctest style

    There are a handful of tests for each monadic APL function.

    WIP - grows as monadic.py grows

    WIP - scalar parameters only
"""

from apl_exception import APL_Exception as apl_exception

from monadic import monadic_function

# ------------------------------

def     monadic_test (symbol,B):
    """
    >>> monadic_test ('+',1)
    1
    >>> monadic_test ('+',0)
    0
    >>> monadic_test ('+',-1)
    -1

    >>> monadic_test ('-',1)
    -1
    >>> monadic_test ('-',0)
    0
    >>> monadic_test ('-',-1)
    1

    >>> monadic_test ('×',1)
    1
    >>> monadic_test ('×',0)
    0
    >>> monadic_test ('×',-1)
    -1

    >>> monadic_test ('÷',1)
    1.0
    >>> monadic_test ('÷',0)
    DOMAIN ERROR
    >>> monadic_test ('÷',-1)
    -1.0

    >>> monadic_test ('⌈',1.5)
    2
    >>> monadic_test ('⌈',0)
    0
    >>> monadic_test ('⌈',-1.5)
    -1

    >>> monadic_test ('⌊',1.5)
    1
    >>> monadic_test ('⌊',0)
    0
    >>> monadic_test ('⌊',-1.5)
    -2

    >>> monadic_test ('*',1)
    2.7182818285
    >>> monadic_test ('*',0)
    1.0
    >>> monadic_test ('*',-1)
    0.3678794412

    >>> monadic_test ('⍟',2.718281828459045)
    1.0
    >>> monadic_test ('⍟',1.0)
    0.0
    >>> monadic_test ('⍟',0.36787944117144233)
    -1.0
    >>> monadic_test ('⍟',0)
    DOMAIN ERROR

    >>> monadic_test ('|',1)
    1.0
    >>> monadic_test ('|',0)
    0.0
    >>> monadic_test ('|',-1)
    1.0

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
        return round(monadic_function(symbol)(B),10)
    except apl_exception as e:
        print (e.message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
