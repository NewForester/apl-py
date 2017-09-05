#!/usr/bin/python3
"""
    doctest style unit tests for APL mixed vectors

    WIP - grows as more functions are implemented.

    The tests in this module exercise monadic and dyadic functions with

        either one or two mixed vector operands

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
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"+ M")
    DOMAIN ERROR

    >>> test(r"M + M")
    DOMAIN ERROR
    >>> test(r"1.2 + M")
    DOMAIN ERROR
    >>> test(r"M + 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 + M")
    DOMAIN ERROR
    >>> test(r"M + 1 2 3")
    DOMAIN ERROR

    >>> test(r"M + ⍳⍴M")
    DOMAIN ERROR
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"- M")
    DOMAIN ERROR

    >>> test(r"M - M")
    DOMAIN ERROR
    >>> test(r"1.2 - M")
    DOMAIN ERROR
    >>> test(r"M - 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 - M")
    DOMAIN ERROR
    >>> test(r"M - 1 2 3")
    DOMAIN ERROR

    >>> test(r"M - ⍳⍴M")
    DOMAIN ERROR
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"× M")
    DOMAIN ERROR

    >>> test(r"M × M")
    DOMAIN ERROR
    >>> test(r"1.2 × M")
    DOMAIN ERROR
    >>> test(r"M × 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 × M")
    DOMAIN ERROR
    >>> test(r"M × 1 2 3")
    DOMAIN ERROR

    >>> test(r"M × ⍳⍴M")
    DOMAIN ERROR
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"÷ M")
    DOMAIN ERROR

    >>> test(r"M ÷ M")
    DOMAIN ERROR
    >>> test(r"1.2 ÷ M")
    DOMAIN ERROR
    >>> test(r"M ÷ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ÷ M")
    DOMAIN ERROR
    >>> test(r"M ÷ 1 2 3")
    DOMAIN ERROR

    >>> test(r"M ÷ ⍳⍴M")
    DOMAIN ERROR
    """
    pass

# --------------

def     ceil_maximum():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"⌈ M")
    DOMAIN ERROR

    >>> test(r"M ⌈ M")
    DOMAIN ERROR
    >>> test(r"1.2 ⌈ M")
    DOMAIN ERROR
    >>> test(r"M ⌈ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ⌈ M")
    DOMAIN ERROR
    >>> test(r"M ⌈ 1 2 3")
    DOMAIN ERROR

    >>> test(r"M ⌈ ⍳⍴M")
    DOMAIN ERROR
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"⌊ M")
    DOMAIN ERROR

    >>> test(r"M ⌊ M")
    DOMAIN ERROR
    >>> test(r"1.2 ⌊ M")
    DOMAIN ERROR
    >>> test(r"M ⌊ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ⌊ M")
    DOMAIN ERROR
    >>> test(r"M ⌊ 1 2 3")
    DOMAIN ERROR

    >>> test(r"M ⌊ ⍳⍴M")
    DOMAIN ERROR
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"| M")
    DOMAIN ERROR

    >>> test(r"M | M")
    DOMAIN ERROR
    >>> test(r"1.2 | M")
    DOMAIN ERROR
    >>> test(r"M | 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 | M")
    DOMAIN ERROR
    >>> test(r"M | 1 2 3")
    DOMAIN ERROR

    >>> test(r"M | ⍳⍴M")
    DOMAIN ERROR
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    import doctest
    doctest.testmod()

# EOF
