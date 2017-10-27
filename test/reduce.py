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

# --------------

def     ceil_maximum():
    """
    >>> test(r"⌈/ ⍬")
    ¯∞

    >>> test(r"⌈/ 7")
    7
    >>> test(r"⌈/ 0 1")
    1
    >>> test(r"⌈/ 1 2")
    2
    >>> test(r"⌈/ 1 2 3")
    3
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"⌊/ ⍬")
    ∞

    >>> test(r"⌊/ 7")
    7
    >>> test(r"⌊/ 0 1")
    0
    >>> test(r"⌊/ 1 2")
    1
    >>> test(r"⌊/ 1 2 3")
    1
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"|/ ⍬")
    0

    >>> test(r"|/ 7")
    7
    >>> test(r"|/ 0 1")
    1
    >>> test(r"|/ 1 2")
    0
    >>> test(r"|/ 1 2 3")
    0
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"*/ ⍬")
    1

    >>> test(r"*/ 7")
    7
    >>> test(r"*/ 0 1")
    0
    >>> test(r"*/ 2 2")
    4
    >>> test(r"*/ 2 2 2")
    16
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"⍟/ ⍬")
    DOMAIN ERROR

    >>> test(r"⍟/ 7")
    7
    >>> test(r"⍟/ 0 1")
    0
    >>> test(r"⍟/ 2 16")
    4
    >>> test(r"⍟/ 4 16 65536")
    1
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"!/ ⍬")
    1

    >>> test(r"!/ 7")
    7
    >>> test(r"!/ 0 1")
    1
    >>> test(r"!/ 3 5")
    10
    >>> test(r"!/ 2 4 6")
    105
    """
    pass

# --------------

def     roll_deal():
    """
    >>> test(r"?/ ⍬")
    DOMAIN ERROR

    >>> test(r"1 ≡ ?/ 1")
    1
    >>> test(r"?/ 1 1")
    (1)
    >>> test(r"?/ 1 1 1")
    (1)
    """
    pass

# ------------------------------

def     pi_circular():
    """
    >>> test(r"|/ ⍬")
    0

    >>> test(r"|/ 7")
    7
    >>> test(r"|/ 0 1")
    1
    >>> test(r"|/ 1 2")
    0
    >>> test(r"|/ 1 2 3")
    0
    """
    pass

# ------------------------------

def     or_gcd():
    """
    >>> test(r"∨/ ⍬")
    0

    >>> test(r"∨/ 7")
    7
    >>> test(r"∨/ 0 1")
    1
    >>> test(r"∨/ 2 4")
    2
    >>> test(r"∨/ 12 18 21")
    3
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"∧/ ⍬")
    1

    >>> test(r"∧/ 7")
    7
    >>> test(r"∧/ 0 1")
    0
    >>> test(r"∧/ 1 2")
    2
    >>> test(r"∧/ 1 2 3")
    6
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"⍱/ ⍬")
    DOMAIN ERROR

    >>> test(r"⍱/ 7")
    7
    >>> test(r"⍱/ 0 1")
    0
    >>> test(r"⍱/ 1 0")
    0
    >>> test(r"⍱/ 1 0 1")
    0
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"⍲/ ⍬")
    DOMAIN ERROR

    >>> test(r"⍲/ 7")
    7
    >>> test(r"⍲/ 0 1")
    1
    >>> test(r"⍲/ 1 0")
    1
    >>> test(r"⍲/ 1 0 1")
    0
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"</ ⍬")
    0

    >>> test(r"</ 7")
    7
    >>> test(r"</ 0 1")
    1
    >>> test(r"</ 1 2")
    1
    >>> test(r"</ 1 2 3")
    0
    """
    pass

# --------------

def     le():
    """
    >>> test(r"≤/ ⍬")
    1

    >>> test(r"≤/ 7")
    7
    >>> test(r"≤/ 0 1")
    1
    >>> test(r"≤/ 1 2")
    1
    >>> test(r"≤/ 1 2 3")
    1
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"≥/ ⍬")
    1

    >>> test(r"≥/ 7")
    7
    >>> test(r"≥/ 0 1")
    0
    >>> test(r"≥/ 1 2")
    0
    >>> test(r"≥/ 1 2 3")
    1
    """
    pass

# --------------

def     gt():
    """
    >>> test(r">/ ⍬")
    0

    >>> test(r">/ 7")
    7
    >>> test(r">/ 0 1")
    0
    >>> test(r">/ 1 2")
    0
    >>> test(r">/ 1 2 3")
    1
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"=/ ⍬")
    1

    >>> test(r"=/ 7")
    7
    >>> test(r"=/ 0 1")
    0
    >>> test(r"=/ 1 2")
    0
    >>> test(r"=/ 1 2 3")
    0
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"≠/ ⍬")
    0

    >>> test(r"≠/ 7")
    7
    >>> test(r"≠/ 0 1")
    1
    >>> test(r"≠/ 1 2")
    1
    >>> test(r"≠/ 1 2 3")
    0
    """
    pass

# ------------------------------

def     depth_match():
    """
    >>> test(r"≡/ ⍬")
    DOMAIN ERROR

    >>> test(r"≡/ 7")
    7
    >>> test(r"≡/ 0 1")
    0
    >>> test(r"≡/ 1 2")
    0
    >>> test(r"≡/ 1 2 3")
    0
    """
    pass

# --------------

def     tally_notMatch():
    """
    >>> test(r"≢/ ⍬")
    DOMAIN ERROR

    >>> test(r"≢/ 7")
    7
    >>> test(r"≢/ 0 1")
    1
    >>> test(r"≢/ 1 2")
    1
    >>> test(r"≢/ 1 2 3")
    0
    """
    pass

# ------------------------------

def     rho():
    """
    >>> test(r"⍴ ⍬")
    0
    """
    pass

# --------------

def     comma():
    """
    >>> test(r", ⍬")
    ⍬
    """
    pass

# --------------

def     enlist_membership():
    """
    >>> test(r"∊/ ⍬")
    DOMAIN ERROR

    >>> test(r"∊/ 7")
    7
    >>> test(r"∊/ 0 1")
    0
    >>> test(r"∊/ 1 2")
    0
    >>> test(r"∊/ 1 2 3")
    0
    """
    pass

# --------------

def     find():
    """
    >>> test(r"⍷/ ⍬")
    DOMAIN ERROR

    >>> test(r"⍷/ 7")
    7
    >>> test(r"⍷/ 0 1")
    0
    >>> test(r"⍷/ 1 2")
    0
    >>> test(r"⍷/ 1 2 3")
    0
    """
    pass

# --------------

def     transpose():
    """
    >>> test(r"⍉ ⍬")
    ⍬
    """
    pass

# --------------

def     reverse_rotate():
    """
    >>> test(r"⌽ ⍬")
    ⍬
    """
    pass

# --------------

def     enclose_partition():
    """
    >>> test(r"⊂ ⍬")
    (⍬)
    """
    pass

# --------------

def     disclose_pick():
    """
    >>> test(r"⊃ ⍬")
    ⍬
    """
    pass

# ------------------------------

def     iota():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⍳ 0")
    ⍬

    >>> setIndexOrigin(0)

    >>> test(r"⍳ 0")
    ⍬

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     tilde():
    """
    >>> test(r"~ ⍬")
    ⍬
    """
    pass

# --------------

def     unique_union():
    """
    >>> test(r"∪ ⍬")
    ⍬
    """
    pass

# --------------

def     intersection():
    """
    >>> test(r"∩ ⍬")
    VALENCE ERROR
    """
    pass

# --------------

def     tail_drop():
    """
    >>> test(r"↓ ⍬")
    ⍬
    """
    pass


# --------------

def     head_take():
    """
    >>> test(r"↑ ⍬")
    ⍬
    """
    pass

# --------------

def     compress_replicate():
    """
    >>> test(r"/ ⍬")
    SYNTAX ERROR
    """
    pass

# --------------

def     expand():
    """
    >>> test(r"\\ ⍬")
    SYNTAX ERROR
    """
    pass

# ------------------------------

def     encode():
    """
    >>> test(r"⊤ ⍬")
    VALENCE ERROR
    """
    pass

# --------------

def     decode():
    """
    >>> test(r"⊥ ⍬")
    VALENCE ERROR
    """
    pass

# --------------

def     gradeUp():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⍋ ⍬")
    ⍬

    >>> setIndexOrigin(0)

    >>> test(r"⍋ ⍬")
    ⍬

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     gradeDown():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⍒ ⍬")
    ⍬

    >>> setIndexOrigin(0)

    >>> test(r"⍒ ⍬")
    ⍬

    >>> restoreIndexOrigin(IO)
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
