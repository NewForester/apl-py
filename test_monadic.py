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
    2.718281828459045
    >>> monadic_test ('*',0)
    1.0
    >>> monadic_test ('*',-1)
    0.36787944117144233

    >>> monadic_test ('⍟',2.718281828459045)
    1.0
    >>> monadic_test ('⍟',1.0)
    0.0
    >>> monadic_test ('⍟',0.36787944117144233)
    -1.0
    >>> monadic_test ('⍟',0)
    DOMAIN ERROR

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
        return monadic_function(symbol)(B)
    except apl_exception as e:
        print (e.message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
