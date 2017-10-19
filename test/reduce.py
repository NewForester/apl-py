#!/usr/bin/python3
"""
    doctest style unit tests for the APL reduce operator

    WIP - grows as more functions are implemented.

    The tests in this module exercise dyadic functions with

        the reduce operator and zilde, scalar and vector operands

    Other cases are covered in other test modules.

    Each test passes an APL expression to the evaluate function.
    Both positive and negative (e.g. DOMAIN ERROR) cases are tested.

    Note:
        testDyadic --eager      # run with eager evaluation
        testDyadic --lazy       # run with lazy evaluation
"""

from test.base import preamble, testResult as test
from test.base import saveIndexOrigin, setIndexOrigin, restoreIndexOrigin

# ------------------------------

def     conjugate_plus():
    """
    >>> test(r"+/ ⍬")
    0

    >>> test(r"+/ 7")
    7
    >>> test(r"+/ 0 1")
    1
    >>> test(r"+/ 1 2")
    3
    >>> test(r"+/ 1 2 3")
    6
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"-/ ⍬")
    0

    >>> test(r"-/ 7")
    7
    >>> test(r"-/ 0 1")
    ¯1
    >>> test(r"-/ 1 2")
    ¯1
    >>> test(r"-/ 1 2 3")
    2
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"×/ ⍬")
    1

    >>> test(r"×/ 7")
    7
    >>> test(r"×/ 0 1")
    0
    >>> test(r"×/ 1 2")
    2
    >>> test(r"×/ 1 2 3")
    6
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"÷/ ⍬")
    1

    >>> test(r"÷/ 7")
    7
    >>> test(r"÷/ 0 1")
    0
    >>> test(r"÷/ 1 2")
    0.5
    >>> test(r"÷/ 1 2 3")
    1.5
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    if test and __name__:
        import doctest
        doctest.testmod()
    else:
        IO = saveIndexOrigin()
        setIndexOrigin(0)
        restoreIndexOrigin(IO)

# EOF
