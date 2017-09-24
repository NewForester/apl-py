#!/usr/bin/python3
"""
    doctest style unit tests for APL monadic functions

    WIP - grows as more monadic functions are implemented.

    The tests in this module exercise monadic functions with

        numeric scalar and vector arguments only.

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

def     monadic():
    """
    >>> test(r"⌹ 1")
    FUNCTION NOT YET IMPLEMENTED

    >>> test(r"¯ 1")
    INVALID TOKEN
    """
    pass

# ------------------------------

def     conjugate_plus():
    """
    >>> test(r"+ 0")
    0

    >>> test(r"+ 0 0.5 1 2")
    0 0.5 1 2
    >>> test(r"+ ¯0 ¯0.5 ¯1 ¯2")
    0 ¯0.5 ¯1 ¯2
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"- 0")
    0

    >>> test(r"- 0 0.5 1 2")
    0 ¯0.5 ¯1 ¯2
    >>> test(r"- ¯0 ¯0.5 ¯1 ¯2")
    0 0.5 1 2
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"× 0")
    0

    >>> test(r"× 0 0.5 1 2")
    0 1 1 1
    >>> test(r"× ¯0 ¯0.5 ¯1 ¯2")
    0 ¯1 ¯1 ¯1
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"÷ 0")
    DOMAIN ERROR
    >>> test(r"÷ 1")
    1

    >>> test(r"÷ 0.25 0.5 1 2")
    4 2 1 0.5
    >>> test(r"÷ ¯0.25 ¯0.5 ¯1 ¯2")
    ¯4 ¯2 ¯1 ¯0.5
    """
    pass

# --------------

def     ceil_maximum():
    """
    >>> test(r"⌈ 0")
    0

    >>> test(r"⌈ 0.25 0.5 1.1 9.9")
    1 1 2 10
    >>> test(r"⌈ ¯0.25 ¯0.5 ¯1.1 ¯9.9")
    0 0 ¯1 ¯9
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"⌊ 0")
    0

    >>> test(r"⌊ 0.25 0.5 1.1 9.9")
    0 0 1 9
    >>> test(r"⌊ ¯0.25 ¯0.5 ¯1.1 ¯9.9")
    ¯1 ¯1 ¯2 ¯10
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"| 0")
    0

    >>> test(r"| 0.25 0.5 1.1 9.9")
    0.25 0.5 1.1 9.9
    >>> test(r"| ¯0.25 ¯0.5 ¯1.1 ¯9.9")
    0.25 0.5 1.1 9.9
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"* 1 0 ¯1")
    2.718281828 1 0.3678794412

    >>> test(r"* 1 2 3 4 5")
    2.718281828 7.389056099 20.08553692 54.59815003 148.4131591
    >>> test(r"* ¯1 ¯2 ¯3 ¯4 ¯5")
    0.3678794412 0.1353352832 0.04978706837 0.01831563889 0.006737946999
    >>> test(r"* 0.125 0.25 0.5")
    1.133148453 1.284025417 1.648721271
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"⍟ 0")
    DOMAIN ERROR
    >>> test(r"⍟ -1")
    DOMAIN ERROR

    >>> test(r"⍟ 2.718281828459045 1.0 0.36787944117144233")
    1 0 ¯1

    >>> test(r"⍟ 1 2 3 4 5")
    0 0.6931471806 1.098612289 1.386294361 1.609437912
    >>> test(r"⍟ 0.125 0.25 0.5")
    ¯2.079441542 ¯1.386294361 ¯0.6931471806
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"! -1")
    DOMAIN ERROR
    >>> test(r"! 0")
    1

    >>> test(r"? 1")
    1
    >>> test(r"? ,1")
    1

    >>> test(r"⍴ ? 1")
    ⍬
    >>> test(r"⍴ ? ,1")
    1

    >>> test(r"! 1 2 3 4 5")
    1 2 6 24 120
    >>> test(r"! 0.125 0.25 0.5")
    0.9417426998 0.9064024771 0.8862269255
    """
    pass

# --------------

def     roll_deal():
    """
    randomness makes positive testing a little tricky

    >>> test(r"? 0")
    DOMAIN ERROR
    >>> test(r"? -1")
    DOMAIN ERROR
    >>> test(r"? 1")
    1
    >>> test(r"? 1÷2")
    DOMAIN ERROR

    >>> test(r"! 1")
    1
    >>> test(r"! ,1")
    1

    >>> test(r"⍴ ! 1")
    ⍬
    >>> test(r"⍴ ! ,1")
    1

    >>> test(r"⍴ ? ⍳ 6")
    6
    """
    pass

# ------------------------------

def     pi_circular():
    """
    >>> test(r"○ 1")
    3.141592654

    >>> test(r"○ ¯1 0 1")
    ¯3.141592654 0 3.141592654
    >>> test(r"○ ¯0.5 0.5")
    ¯1.570796327 1.570796327
    >>> test(r"○ ¯2 2")
    ¯6.283185307 6.283185307
    """
    pass

# ------------------------------

def     tilde():
    """
    >>> test(r"~ 1")
    0
    >>> test(r"~ 0")
    1

    >>> test(r"⍴ ~ 1")
    ⍬
    >>> test(r"⍴ ~ ,1")
    1

    >>> test(r"~ ¯1")
    DOMAIN ERROR
    >>> test(r"~ 0.5")
    DOMAIN ERROR

    >>> test(r"~ 0 1 0 ")
    1 0 1
    """
    pass

# --------------

def     or_gcd():
    """
    >>> test(r"∨ 1")
    VALENCE ERROR
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"∧ 1")
    VALENCE ERROR
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"⍱ 1")
    VALENCE ERROR
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"⍲ 1")
    VALENCE ERROR
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"< 1")
    VALENCE ERROR
    """
    pass

# --------------

def     le():
    """
    >>> test(r"≤ 1")
    VALENCE ERROR
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"≥ 1")
    VALENCE ERROR
    """
    pass

# --------------

def     gt():
    """
    >>> test(r"> 1")
    VALENCE ERROR
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"= 1")
    VALENCE ERROR
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"≠ 1")
    VALENCE ERROR
    """
    pass

# ------------------------------

def     depth_match():
    """
    depth function

    >>> test(r"≡ 1.2")
    0
    >>> test(r"≡ 1 2 3")
    1
    """
    pass

# --------------

def     tally_notMatch():
    """
    tally function

    >>> test(r"≢ 1.2")
    1
    >>> test(r"≢ 1 2 3")
    3
    """
    pass

# ------------------------------

def     iota():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⍳ -1")
    DOMAIN ERROR
    >>> test(r"⍳ 0")
    ⍬
    >>> test(r"⍳ 1")
    1
    >>> test(r"⍳ 2")
    1 2
    >>> test(r"⍳ 3.142")
    DOMAIN ERROR

    >>> test(r"⍳ 1 1")
    WIP - LENGTH ERROR

    >>> setIndexOrigin(0)

    >>> test(r"⍳ -1")
    DOMAIN ERROR
    >>> test(r"⍳ 0")
    ⍬
    >>> test(r"⍳ 1")
    0
    >>> test(r"⍳ 2")
    0 1
    >>> test(r"⍳ 3.142")
    DOMAIN ERROR

    >>> test(r"⍳ 1 1")
    WIP - LENGTH ERROR

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     rho():
    """
    >>> test(r"⍴ 1.2")
    ⍬
    >>> test(r"⍴ ,1.2")
    1
    >>> test(r"⍴ 1 2 3")
    3
    """
    pass

# --------------

def     comma():
    """
    >>> test(r", 1.2")
    1.2
    >>> test(r"⍴ , 1.2")
    1

    >>> test(r", 1 2 3")
    1 2 3
    >>> test(r"⍴ , 1 2 3")
    3
    """
    pass

# --------------

def     transpose():
    """
    >>> test(r"⍉ 1.2")
    1.2

    >>> test(r"⍴ ⍉ 1.2")
    ⍬
    >>> test(r"⍴ ⍉ ,1.2")
    1

    >>> test(r"⍉ 1 2 3")
    1 2 3
    """
    pass

# --------------

def     enclose_partition():
    """
    >>> test(r"⊂ 1.2")
    1.2
    >>> test(r"≡ ⊂ 1.2")
    0
    >>> test(r"≢ ⊂ 1.2")
    1

    >>> test(r"⊂ ,1.2")
    (1.2)
    >>> test(r"≡ ⊂ ,1.2")
    2
    >>> test(r"≢ ⊂ ,1.2")
    1

    >>> test(r"⊂ 1 2 3")
    (1 2 3)
    >>> test(r"≡ ⊂ 1 2 3")
    2
    >>> test(r"≢ ⊂ 1 2 3")
    1
    """
    pass

# --------------

def     reverse_rotate():
    """
    >>> test(r"⌽ 1.2")
    1.2

    >>> test(r"⍴ ⌽ 1.2")
    ⍬
    >>> test(r"⍴ ⌽ ,1.2")
    1

    >>> test(r"⌽ 1 2 3")
    3 2 1
    """
    pass

# --------------

def     unique_union():
    """
    >>> test(r"∪ 0")
    0

    >>> test(r"∪ 0.5 1.5 0.5 1.5 0.5 1.5 ¯0.5 ¯1.5")
    0.5 1.5 ¯0.5 ¯1.5

    >>> test(r"⍴ ∪ 0.5 1.5 0.5 1.5 0.5 1.5 ¯0.5 ¯1.5")
    4
    """
    pass

# --------------

def     intersection():
    """
    >>> test(r"∩ 1")
    VALENCE ERROR
    """
    pass

# --------------

def     tail_drop():
    """
    >>> test(r"↓ 1 2 3")
    2 3
    >>> test(r"↓ 0.1 0.2 0.3")
    0.2 0.3
    >>> test(r"↓ ¯1 ¯2 ¯3")
    ¯2 ¯3
    """
    pass

# --------------

def     head_take():
    """
    >>> test(r"↑ 1")
    1
    >>> test(r"↑ ,1")
    1

    >>> test(r"⍴ ↑ 1")
    ⍬
    >>> test(r"⍴ ↑ ,1")
    ⍬

    >>> test(r"↑ 1 2 3")
    1
    >>> test(r"↑ 0.1 0.2 0.3")
    0.1
    >>> test(r"↑ ¯1 ¯2 ¯3")
    ¯1
    """
    pass

# --------------

def     compress_replicate():
    """
    >>> test(r"/ 1")
    VALENCE ERROR
    """
    pass

# --------------

def     expand():
    """
    >>> test(r"\\ 1")
    VALENCE ERROR
    """
    pass

# ------------------------------

def     encode():
    """
    >>> test(r"⊤ 1")
    VALENCE ERROR
    """
    pass

# --------------

def     decode():
    """
    >>> test(r"⊥ 1")
    VALENCE ERROR
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    if test and __name__:
        import doctest
        doctest.testmod()

# EOF
