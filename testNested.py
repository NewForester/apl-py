#!/usr/bin/python3
"""
    doctest style unit tests for APL nested vectors

    WIP - grows as more functions are implemented.

    The tests in this module exercise monadic and dyadic functions with

        either one or two nested vector operands

    Other cases are covered in other test modules.

    Each test passes an APL expression to the evaluate function.
    Both positive and negative (e.g. DOMAIN ERROR) cases are tested.

    Note:
        testDyadic --eager      # run with eager evaluation
        testDyadic --lazy       # run with lazy evaluation
"""

from test.base import preamble, testResult as test

# ------------------------------

def     conjugate_plus():
    """
    >>> test(r"+ 1 (2 3) 4")
    1 (2 3) 4

    >>> test(r"8 + 1 (2 3) 4")
    9 (10 11) 12
    >>> test(r"1 (2 3) 4 + 5")
    6 (7 8) 9
    >>> test(r"1 (2 3) 4 + 5 (6 7) 8")
    6 (8 10) 12

    >>> test(r"1 (2 3) 4 + (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 + 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"1 (2 3) 4 + (5 6) 0 (7 8)")
    (6 7) (2 3) (11 12)
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"- 1 (2 3) 4")
    ¯1 (¯2 ¯3) ¯4

    >>> test(r"8 - 1 (2 3) 4")
    7 (6 5) 4
    >>> test(r"1 (2 3) 4 - 5")
    ¯4 (¯3 ¯2) ¯1
    >>> test(r"1 (2 3) 4 - 5 (6 7) 8")
    ¯4 (¯4 ¯4) ¯4

    >>> test(r"1 (2 3) 4 - (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 - 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"1 (2 3) 4 - (5 6) 0 (7 8)")
    (¯4 ¯5) (2 3) (¯3 ¯4)
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"× 1 (2 3) 4")
    1 (1 1) 1

    >>> test(r"8 × 1 (2 3) 4")
    8 (16 24) 32
    >>> test(r"1 (2 3) 4 × 5")
    5 (10 15) 20
    >>> test(r"1 (2 3) 4 × 5 (6 7) 8")
    5 (12 21) 32

    >>> test(r"1 (2 3) 4 × (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 × 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"1 (2 3) 4 × (5 6) 0 (7 8)")
    (5 6) (0 0) (28 32)
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"÷ 1 (2 3) 4")
    1 (0.5 0.3333333333) 0.25

    >>> test(r"8 ÷ 1 (2 3) 4")
    8 (4 2.666666667) 2
    >>> test(r"1 (2 3) 4 ÷ 5")
    0.2 (0.4 0.6) 0.8
    >>> test(r"1 (2 3) 4 ÷ 5 (6 7) 8")
    0.2 (0.3333333333 0.4285714286) 0.5

    >>> test(r"1 (2 3) 4 ÷ (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 ÷ 1 (2 0 3) 4", True)
    DOMAIN ERROR

    >>> test(r"1 (2 3) 4 ÷ (5 6) 10 (7 8)")
    (0.2 0.1666666667) (0.2 0.3) (0.5714285714 0.5)
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    import doctest
    doctest.testmod()

# EOF
