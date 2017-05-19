#!/usr/bin/python3
"""
    Unit test for monadic.py - doctest style

    There are a handful of tests for each monadic APL function.

    WIP - grows as monadic.py grows

    WIP - scalar parameters (cast to apl_scalar) only
"""

from monadic import monadic_function

from apl import print_result

from apl_quantity import APL_scalar as apl_scalar
from apl_error import APL_exception as apl_exception

# ------------------------------

def     monadic_test (symbol,B):
    """
    >>> monadic_test ('+',1)
    1
    >>> monadic_test ('+',0)
    0
    >>> monadic_test ('+',-1)
    ¯1

    >>> monadic_test ('-',1)
    ¯1
    >>> monadic_test ('-',0)
    0
    >>> monadic_test ('-',-1)
    1

    >>> monadic_test ('×',1)
    1
    >>> monadic_test ('×',0)
    0
    >>> monadic_test ('×',-1)
    ¯1

    >>> monadic_test ('÷',1)
    1
    >>> monadic_test ('÷',0)
    DOMAIN ERROR
    >>> monadic_test ('÷',-1)
    ¯1

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
