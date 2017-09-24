#!/usr/bin/python3
"""
    doctest style unit tests for degnerate cases involving zilde the empty vector

    WIP - grows as more functions are implemented.

    The tests in this module exercise monadic and dyadic functions with

        either one or both operands are zilde or the result is zilde

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

def     zilde():
    """
    >>> test(r"⍬")
    ⍬
    >>> test(r"⍴ ⍬")
    0
    >>> test(r"≡ ⍬")
    1
    >>> test(r"≢ ⍬")
    0
    """
    pass

# ------------------------------

def     conjugate_plus():
    """
    >>> test(r"+ ⍬")
    ⍬

    >>> test(r"⍬ + ⍬")
    ⍬
    >>> test(r"1.2 + ⍬")
    ⍬
    >>> test(r"⍬ + 1.2")
    ⍬

    >>> test(r"1 2 3 + ⍬")
    LENGTH ERROR
    >>> test(r"⍬ + 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"- ⍬")
    ⍬

    >>> test(r"⍬ - ⍬")
    ⍬
    >>> test(r"1.2 - ⍬")
    ⍬
    >>> test(r"⍬ - 1.2")
    ⍬

    >>> test(r"1 2 3 - ⍬")
    LENGTH ERROR
    >>> test(r"⍬ - 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"× ⍬")
    ⍬

    >>> test(r"⍬ × ⍬")
    ⍬
    >>> test(r"1.2 × ⍬")
    ⍬
    >>> test(r"⍬ × 1.2")
    ⍬

    >>> test(r"1 2 3 × ⍬")
    LENGTH ERROR
    >>> test(r"⍬ × 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"÷ ⍬")
    ⍬

    >>> test(r"⍬ ÷ ⍬")
    ⍬
    >>> test(r"1.2 ÷ ⍬")
    ⍬
    >>> test(r"⍬ ÷ 1.2")
    ⍬

    >>> test(r"1 2 3 ÷ ⍬")
    LENGTH ERROR
    >>> test(r"⍬ ÷ 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     ceil_maximum():
    """
    >>> test(r"⌈ ⍬")
    ⍬

    >>> test(r"⍬ ⌈ ⍬")
    ⍬
    >>> test(r"1.2 ⌈ ⍬")
    ⍬
    >>> test(r"⍬ ⌈ 1.2")
    ⍬

    >>> test(r"1 2 3 ⌈ ⍬")
    LENGTH ERROR
    >>> test(r"⍬ ⌈ 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"⌊ ⍬")
    ⍬

    >>> test(r"⍬ ⌊ ⍬")
    ⍬
    >>> test(r"1.2 ⌊ ⍬")
    ⍬
    >>> test(r"⍬ ⌊ 1.2")
    ⍬

    >>> test(r"1 2 3 ⌊ ⍬")
    LENGTH ERROR
    >>> test(r"⍬ ⌊ 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"| ⍬")
    ⍬

    >>> test(r"⍬ | ⍬")
    ⍬
    >>> test(r"1.2 | ⍬")
    ⍬
    >>> test(r"⍬ | 1.2")
    ⍬

    >>> test(r"1 2 3 | ⍬")
    LENGTH ERROR
    >>> test(r"⍬ | 1 2 3")
    LENGTH ERROR
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"* ⍬")
    ⍬

    >>> test(r"⍬ * ⍬")
    ⍬
    >>> test(r"1.2 * ⍬")
    ⍬
    >>> test(r"⍬ * 1.2")
    ⍬

    >>> test(r"1 2 3 * ⍬")
    LENGTH ERROR
    >>> test(r"⍬ * 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"⍟ ⍬")
    ⍬

    >>> test(r"⍬ ⍟ ⍬")
    ⍬
    >>> test(r"1.2 ⍟ ⍬")
    ⍬
    >>> test(r"⍬ ⍟ 1.2")
    ⍬

    >>> test(r"1 2 3 ⍟ ⍬")
    LENGTH ERROR
    >>> test(r"⍬ ⍟ 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"! ⍬")
    ⍬

    >>> test(r"⍬ ! ⍬")
    ⍬
    >>> test(r"1.2 ! ⍬")
    ⍬
    >>> test(r"⍬ ! 1.2")
    ⍬

    >>> test(r"1 2 3 ! ⍬")
    LENGTH ERROR
    >>> test(r"⍬ ! 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     roll_deal():
    """
    >>> test(r"? ⍬")
    ⍬

    >>> test(r"⍬ ? ⍬")
    RANK ERROR
    >>> test(r"1.2 ? ⍬")
    RANK ERROR
    >>> test(r"⍬ ? 1.2")
    RANK ERROR

    >>> test(r"1 2 3 ? ⍬")
    RANK ERROR
    >>> test(r"⍬ ? 1 2 3")
    RANK ERROR
    """
    pass

# ------------------------------

def     pi_circular():
    """
    >>> test(r"○ ⍬")
    ⍬

    >>> test(r"⍬ ○ ⍬")
    ⍬
    >>> test(r"1.2 ○ ⍬")
    ⍬
    >>> test(r"⍬ ○ 1.2")
    ⍬

    >>> test(r"1 2 3 ○ ⍬")
    LENGTH ERROR
    >>> test(r"⍬ ○ 1 2 3")
    LENGTH ERROR
    """
    pass

# ------------------------------

def     or_gcd():
    """
    >>> test(r"∨ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ∨ ⍬")
    ⍬
    >>> test(r"⍬ ∨ 1")
    ⍬
    >>> test(r"1 ∨ ⍬")
    ⍬

    >>> test(r"⍬ ∨ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ∨ ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"∧ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ∧ ⍬")
    ⍬
    >>> test(r"⍬ ∧ 1")
    ⍬
    >>> test(r"1 ∧ ⍬")
    ⍬

    >>> test(r"⍬ ∧ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ∧ ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"⍱ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ⍱ ⍬")
    ⍬
    >>> test(r"⍬ ⍱ 1")
    ⍬
    >>> test(r"1 ⍱ ⍬")
    ⍬

    >>> test(r"⍬ ⍱ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ⍱ ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"⍲ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ⍲ ⍬")
    ⍬
    >>> test(r"⍬ ⍲ 1")
    ⍬
    >>> test(r"1 ⍲ ⍬")
    ⍬

    >>> test(r"⍬ ⍲ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ⍲ ⍬")
    LENGTH ERROR
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"< ⍬")
    VALENCE ERROR

    >>> test(r"⍬ < ⍬")
    ⍬
    >>> test(r"⍬ < 1.2")
    ⍬
    >>> test(r"1.2 < ⍬")
    ⍬

    >>> test(r"⍬ < 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 < ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     le():
    """
    >>> test(r"≤ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ≤ ⍬")
    ⍬
    >>> test(r"⍬ ≤ 1.2")
    ⍬
    >>> test(r"1.2 ≤ ⍬")
    ⍬

    >>> test(r"⍬ ≤ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ≤ ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"≥ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ≥ ⍬")
    ⍬
    >>> test(r"⍬ ≥ 1.2")
    ⍬
    >>> test(r"1.2 ≥ ⍬")
    ⍬

    >>> test(r"⍬ ≥ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ≥ ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     gt():
    """
    >>> test(r"> ⍬")
    VALENCE ERROR

    >>> test(r"⍬ > ⍬")
    ⍬
    >>> test(r"⍬ > 1.2")
    ⍬
    >>> test(r"1.2 > ⍬")
    ⍬

    >>> test(r"⍬ > 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 > ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"= ⍬")
    VALENCE ERROR

    >>> test(r"⍬ = ⍬")
    ⍬
    >>> test(r"⍬ = 1.2")
    ⍬
    >>> test(r"1.2 = ⍬")
    ⍬

    >>> test(r"⍬ = 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 = ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"≠ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ≠ ⍬")
    ⍬
    >>> test(r"⍬ ≠ 1.2")
    ⍬
    >>> test(r"1.2 ≠ ⍬")
    ⍬

    >>> test(r"⍬ ≠ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ≠ ⍬")
    LENGTH ERROR
    """
    pass

# ------------------------------

def     depth_match():
    """
    >>> test(r"≡ ⍬")
    1

    >>> test(r"⍬ ≡ ⍬")
    1
    >>> test(r"⍬ ≡ 1.2")
    0
    >>> test(r"1.2 ≡ ⍬")
    0

    >>> test(r"⍬ ≡ 1 2 3")
    0
    >>> test(r"1 2 3 ≡ ⍬")
    0
    """
    pass

# --------------

def     tally_notMatch():
    """
    >>> test(r"≢ ⍬")
    0

    >>> test(r"⍬ ≢ ⍬")
    0
    >>> test(r"⍬ ≢ 1.2")
    1
    >>> test(r"1.2 ≢ ⍬")
    1

    >>> test(r"⍬ ≢ 1 2 3")
    1
    >>> test(r"1 2 3 ≢ ⍬")
    1
    """
    pass

# ------------------------------

def     rho():
    """
    >>> test(r"⍴ ⍬")
    0
    >>> test(r"⍴ 1")
    ⍬

    >>> test(r"⍬ ⍴ ⍬")
    0
    >>> test(r"⍬ ⍴ 1.2")
    1.2
    >>> test(r"1.2 ⍴ ⍬")
    DOMAIN ERROR

    >>> test(r"⍬ ⍴ 1 2 3")
    1

    >>> test(r"1 2 3 ⍴ ⍬")
    WIP - LENGTH ERROR

    >>> test(r"6 ⍴ ⍬")
    0 0 0 0 0 0

    >>> test(r"0 ⍴ 1.2")
    ⍬
    >>> test(r"0 ⍴ 1 2 3")
    ⍬
    """
    pass

# --------------

def     comma():
    """
    >>> test(r", ⍬")
    ⍬

    >>> test(r"⍬ , ⍬")
    ⍬
    >>> test(r"⍬ , 1.2")
    1.2
    >>> test(r"1.2 , ⍬")
    1.2

    >>> test(r"⍴ ⍬ , 1.2")
    1
    >>> test(r"⍴ 1.2 , ⍬")
    1

    >>> test(r"⍬ , 1 2 3")
    1 2 3
    >>> test(r"1 2 3 , ⍬")
    1 2 3

    >>> test(r"⍴ ⍬ , 1 2 3")
    3
    >>> test(r"⍴ 1 2 3 , ⍬")
    3
    """
    pass

# --------------

def     transpose():
    """
    >>> test(r"⍉ ⍬")
    ⍬

    >>> test(r"⍬ ⍉ ⍬")
    LENGTH ERROR
    >>> test(r"1 ⍉ ⍬")
    ⍬

    >>> test(r"1.2 ⍉ ⍬")
    DOMAIN ERROR
    >>> test(r"⍬ ⍉ 1.2")
    1.2

    >>> test(r"⍬ ⍉ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ⍉ ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     reverse_rotate():
    """
    >>> test(r"⌽ ⍬")
    ⍬

    >>> test(r"⍬ ⌽ ⍬")
    RANK ERROR
    >>> test(r"⍬ ⌽ 1.2")
    RANK ERROR
    >>> test(r"1.2 ⌽ ⍬")
    DOMAIN ERROR

    >>> test(r"⍬ ⌽ 0")
    RANK ERROR
    >>> test(r"0 ⌽ ⍬")
    ⍬

    >>> test(r"⍬ ⌽ 1 2 3")
    RANK ERROR
    >>> test(r"1 2 3 ⌽ ⍬")
    RANK ERROR
    """
    pass

# --------------

def     enclose_partition():
    """
    >>> test(r"⊂ ⍬")
    (⍬)
    >>> test(r"≡ ⊂ ⍬")
    2
    >>> test(r"≢ ⊂ ⍬")
    1

    >>> test(r"⍬ ⊂ ⍬")
    ⍬
    >>> test(r"⍬ ⊂ 1.2")
    RANK ERROR
    >>> test(r"1.2 ⊂ ⍬")
    DOMAIN ERROR

    >>> test(r"⍬ ⊂ 0")
    RANK ERROR
    >>> test(r"0 ⊂ ⍬")
    ⍬
    >>> test(r"1 ⊂ ⍬")
    (⍬)

    >>> test(r"⍬ ⊂ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ⊂ ⍬")
    LENGTH ERROR
    """
    pass

# --------------

def     disclose_pick():
    """
    >>> test(r"⊃ ⍬")
    ⍬
    >>> test(r"⊃ ⍬ ⍬")
    WIP - LENGTH ERROR

    >>> test(r"⍬ ⊃ 10")
    10
    >>> test(r"⍬ ⊃ ,10")
    10
    >>> test(r"⍬ ⊃ 10 20 30")
    10 20 30

    >>> test(r"⍬ ⊃ ⍬")
    ⍬

    >>> test(r"-1 ⊃ ⍬")
    INDEX ERROR
    >>> test(r"0 ⊃ ⍬")
    INDEX ERROR
    >>> test(r"1 ⊃ ⍬")
    INDEX ERROR
    """
    pass

# ------------------------------

def     iota():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⍳ 0")
    ⍬

    >>> test(r"⍬ ⍳ ⍬")
    ⍬
    >>> test(r"⍬ ⍳ 1.2")
    1
    >>> test(r"1.2 ⍳ ⍬")
    ⍬

    >>> test(r"⍬ ⍳ 1 2 3")
    1 1 1
    >>> test(r"1 2 3 ⍳ ⍬")
    ⍬

    >>> setIndexOrigin(0)

    >>> test(r"⍳ 0")
    ⍬

    >>> test(r"⍬ ⍳ ⍬")
    ⍬
    >>> test(r"⍬ ⍳ 1.2")
    0
    >>> test(r"1.2 ⍳ ⍬")
    ⍬

    >>> test(r"⍬ ⍳ 1 2 3")
    0 0 0
    >>> test(r"1 2 3 ⍳ ⍬")
    ⍬

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     tilde():
    """
    >>> test(r"~ ⍬")
    ⍬

    >>> test(r"⍬ ~ ⍬")
    ⍬
    >>> test(r"⍬ ~ 1")
    ⍬
    >>> test(r"1 ~ ⍬")
    1

    >>> test(r"1 ~ 1")
    ⍬
    >>> test(r"1 2 3 ~ 1 2 3")
    ⍬
    """
    pass

# --------------

def     unique_union():
    """
    >>> test(r"∪ ⍬")
    ⍬

    >>> test(r"⍬ ∪ ⍬")
    ⍬
    >>> test(r"⍬ ∪ 1.2")
    1.2
    >>> test(r"1.2 ∪ ⍬")
    1.2

    >>> test(r"⍬ ∪ 1 2 3")
    1 2 3
    >>> test(r"1 2 3 ∪ ⍬")
    1 2 3
    """
    pass

# --------------

def     intersection():
    """
    only dyadic

    >>> test(r"∩ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ∩ ⍬")
    ⍬
    >>> test(r"⍬ ∩ 1.2")
    ⍬
    >>> test(r"1.2 ∩ ⍬")
    ⍬

    >>> test(r"⍬ ∩ 1 2 3")
    ⍬
    >>> test(r"1 2 3 ∩ ⍬")
    ⍬
    """
    pass

# --------------

def     tail_drop():
    """
    >>> test(r"↓ ⍬")
    ⍬

    >>> test(r"↓ 1")
    ⍬
    >>> test(r"↓ ,1")
    ⍬

    >>> test(r"⍬ ↓ ⍬")
    ⍬
    >>> test(r"⍬ ↓ 1.2")
    1.2
    >>> test(r"1 ↓ ⍬")
    ⍬

    >>> test(r"3 ↓ 1 2 3")
    ⍬
    >>> test(r"¯3 ↓ 1 2 3")
    ⍬
    >>> test(r"6 ↓ 1 2 3")
    ⍬
    >>> test(r"¯6 ↓ 1 2 3")
    ⍬
    """
    pass


# --------------

def     head_take():
    """
    >>> test(r"↑ ⍬")
    ⍬

    >>> test(r"⍬ ↑ ⍬")
    ⍬
    >>> test(r"⍬ ↑ 1.2")
    1.2
    >>> test(r"1 ↑ ⍬")
    0
    >>> test(r"2 ↑ ⍬")
    0 0

    >>> test(r"0 ↑ 1")
    ⍬
    >>> test(r"0 ↑ 1 2 3")
    ⍬
    """
    pass

# --------------

def     compress_replicate():
    """
    only dyadic

    >>> test(r"/ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ / ⍬")
    ⍬
    >>> test(r"⍬ / 1.2")
    ⍬
    >>> test(r"1.2 / ⍬")
    DOMAIN ERROR
    >>> test(r"1 / ⍬")
    ⍬

    >>> test(r"1 2 3 / ⍬")
    LENGTH ERROR
    >>> test(r"⍬ / 1 2 3")
    LENGTH ERROR

    >>> test(r"0 / 1 2 3")
    ⍬
    >>> test(r"0 0 0 / 1 2 3")
    ⍬
    """
    pass

# --------------

def     expand():
    """
    only dyadic

    >>> test(r"\\ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ \\ ⍬")
    ⍬
    >>> test(r"⍬ \\ 1.2")
    ⍬
    >>> test(r"1.2 \\ ⍬")
    DOMAIN ERROR
    >>> test(r"1 \\ ⍬")
    ⍬

    >>> test(r"⍬ \\ 1 2 3")
    LENGTH ERROR

    >>> test(r"0 \\ ⍬")
    0
    >>> test(r"0 0 \\ ⍬")
    0 0
    >>> test(r"0 0 0 \\ ⍬")
    0 0 0
    """
    pass

# ------------------------------

def     encode():
    """
    only dyadic

    >>> test(r"⊤ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ⊤ ⍬")
    ⍬
    >>> test(r"⍬ ⊤ 17")
    ⍬
    >>> test(r"16 ⊤ ⍬")
    ⍬

    >>> test(r"1 2 3 ⊤ ⍬")
    ⍬
    >>> test(r"⍬ ⊤ 1 2 3")
    ⍬
    """
    pass

# --------------

def     decode():
    """
    only dyadic

    >>> test(r"⊥ ⍬")
    VALENCE ERROR

    >>> test(r"⍬ ⊥ ⍬")
    0
    >>> test(r"⍬ ⊥ 1 1")
    0
    >>> test(r"16 16 ⊥ ⍬")
    0

    >>> test(r"1 2 3 ⊥ ⍬")
    0
    >>> test(r"⍬ ⊥ 1 2 3")
    0

    >>> test(r"0 ⊥ 1 2 3")
    3
    >>> test(r"0 0 0 ⊥ 1 2 3")
    3
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    if test and __name__:
        import doctest
        doctest.testmod()

# EOF
