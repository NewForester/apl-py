#!/usr/bin/python3
"""
    doctest style unit tests for cases involving array prototypes

    WIP - grows as more functions are implemented.

    The tests in this module exercise monadic and dyadic functions with

        yield an array prototype (one that has no length)

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
    >>> test(r"⍬ ≡ + ⍬")
    1
    >>> test(r"'' ≡ + ''")
    1

    >>> test(r"⍬ ≡ ⍬ + ⍬")
    1
    >>> test(r"'' ≡ '' + ''")
    1

    >>> test(r"⍬ ≡ ⍬ + 1")
    1
    >>> test(r"'' ≡ '' + 1")
    1

    >>> test(r"⍬ ≡ 1 + ⍬")
    1
    >>> test(r"'' ≡ 1 + ''")
    1

    >>> test(r"⍬ ≡ '' + ⍬")
    1
    >>> test(r"'' ≡ 0 + ''")
    1
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"⍬ ≡ - ⍬")
    1
    >>> test(r"'' ≡ - ''")
    1

    >>> test(r"⍬ ≡ ⍬ - ⍬")
    1
    >>> test(r"'' ≡ '' - ''")
    1

    >>> test(r"⍬ ≡ ⍬ - 1")
    1
    >>> test(r"'' ≡ '' - 1")
    1

    >>> test(r"⍬ ≡ 1 - ⍬")
    1
    >>> test(r"'' ≡ 1 - ''")
    1

    >>> test(r"⍬ ≡ '' - ⍬")
    1
    >>> test(r"'' ≡ 0 - ''")
    1
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"⍬ ≡ × ⍬")
    1
    >>> test(r"'' ≡ × ''")
    1

    >>> test(r"⍬ ≡ ⍬ × ⍬")
    1
    >>> test(r"'' ≡ '' × ''")
    1

    >>> test(r"⍬ ≡ ⍬ × 1")
    1
    >>> test(r"'' ≡ '' × 1")
    1

    >>> test(r"⍬ ≡ 1 × ⍬")
    1
    >>> test(r"'' ≡ 1 × ''")
    1

    >>> test(r"⍬ ≡ '' × ⍬")
    1
    >>> test(r"'' ≡ 0 × ''")
    1
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"⍬ ≡ ÷ ⍬")
    1
    >>> test(r"'' ≡ ÷ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ÷ ⍬")
    1
    >>> test(r"'' ≡ '' ÷ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ÷ 1")
    1
    >>> test(r"'' ≡ '' ÷ 1")
    1

    >>> test(r"⍬ ≡ 1 ÷ ⍬")
    1
    >>> test(r"'' ≡ 1 ÷ ''")
    1

    >>> test(r"⍬ ≡ '' ÷ ⍬")
    1
    >>> test(r"'' ≡ 0 ÷ ''")
    1
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    import doctest
    doctest.testmod()

# EOF
