#!/usr/bin/python3
"""
    doctest style unit tests for 2x2 matrices

    WIP - grows as more functions are implemented.

    The tests in this module exercise monadic and dyadic functions with

        either one or both operands are a 2x2 array

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
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"+ A")
    1 2
    3 4

    >>> test(r"A + A")
    2 4
    6 8
    >>> test(r"A + 0 1")
    1 3
    3 5
    >>> test(r"(1 0) + A")
    2 2
    4 4
    >>> test(r"A + 3")
    4 5
    6 7
    >>> test(r"2 + A")
    3 4
    5 6
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"- A")
    ¯1 ¯2
    ¯3 ¯4

    >>> test(r"A - A")
    0 0
    0 0
    >>> test(r"A - 0 1")
    1 1
    3 3
    >>> test(r"(1 0) - A")
    0 ¯2
    ¯2 ¯4
    >>> test(r"A - 3")
    ¯2 ¯1
    0 1
    >>> test(r"2 - A")
    1 0
    ¯1 ¯2
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"× 2 2 ⍴ 0 2 ¯2 0.5")
    0 1
    ¯1 1

    >>> test(r"A × A")
    1 4
    9 16
    >>> test(r"A × 0 1")
    0 2
    0 4
    >>> test(r"(1 0) × A")
    1 0
    3 0
    >>> test(r"A × 3")
    3 6
    9 12
    >>> test(r"2 × A")
    2 4
    6 8
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"÷ A")
    1 0.5
    0.3333333333 0.25

    >>> test(r"A ÷ A")
    1 1
    1 1
    >>> test(r"A ÷ 1 2")
    1 1
    3 2
    >>> test(r"(2 1) ÷ A")
    2 0.5
    0.6666666667 0.25
    >>> test(r"A ÷ 4")
    0.25 0.5
    0.75 1
    >>> test(r"12 ÷ A")
    12 6
    4 3
    """
    pass

# --------------

def     ceil_maximum():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⌈ A - ÷ A")
    0 2
    3 4

    >>> test(r"A ⌈ A")
    1 2
    3 4
    >>> test(r"A ⌈ 1 8")
    1 8
    3 8
    >>> test(r"(8 1) ⌈ A")
    8 2
    8 4
    >>> test(r"A ⌈ 3")
    3 3
    3 4
    >>> test(r"2 ⌈ A")
    2 2
    3 4
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⌊ A - ÷ A")
    0 1
    2 3

    >>> test(r"A ⌊ A")
    1 2
    3 4
    >>> test(r"A ⌊ 1 8")
    1 2
    1 4
    >>> test(r"(8 1) ⌊ A")
    1 1
    3 1
    >>> test(r"A ⌊ 3")
    1 2
    3 3
    >>> test(r"2 ⌊ A")
    1 2
    2 2
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"| 2 2 ⍴ 0 2 ¯2 0.5")
    0 2
    2 0.5

    >>> test(r"A | A")
    0 0
    0 0
    >>> test(r"A | 1 2")
    0 0
    1 2
    >>> test(r"(2 1) | A")
    1 0
    1 0
    >>> test(r"A | 3")
    0 1
    0 3
    >>> test(r"2 | A")
    1 0
    1 0
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"* A")
    2.718281828 7.389056099
    20.08553692 54.59815003

    >>> test(r"A * A")
    1 4
    27 256
    >>> test(r"A * 0 1")
    1 2
    1 4
    >>> test(r"(1 0) * A")
    1 0
    1 0
    >>> test(r"A * 3")
    1 8
    27 64
    >>> test(r"2 * A")
    2 4
    8 16
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"A ← 2 2 ⍴ 2 4 10 0.1")
    2 4
    10 0.1
    >>> test(r"A")
    2 4
    10 0.1
    >>> test(r"⍟ A")
    0.6931471806 1.386294361
    2.302585093 ¯2.302585093

    >>> test(r"A ⍟ A")
    1 1
    1 1
    >>> test(r"A ⍟ 2 10")
    1 1.660964047
    0.3010299957 ¯1
    >>> test(r"(10 2) ⍟ A")
    0.3010299957 2
    1 ¯3.321928095
    >>> test(r"A ⍟ 4")
    2 1
    0.6020599913 ¯0.6020599913
    >>> test(r"10 ⍟ A")
    0.3010299957 0.6020599913
    1 ¯1
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"! A")
    1 2
    6 24

    >>> test(r"A ! A")
    1 1
    1 1
    >>> test(r"A ! 1 2")
    1 1
    0 0
    >>> test(r"(2 1) ! A")
    0 2
    3 4
    >>> test(r"A ! 3")
    3 3
    1 0
    >>> test(r"2 ! A")
    0 1
    3 6
    """
    pass

# --------------

def     roll_deal():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⍴ ? A")
    2 2

    >>> test(r"A ? A")
    RANK ERROR
    >>> test(r"A ? 0 1")
    RANK ERROR
    >>> test(r"(1 0) ? A")
    RANK ERROR
    >>> test(r"A ? 3")
    RANK ERROR
    >>> test(r"2 ? A")
    RANK ERROR
    """
    pass

# ------------------------------

def     pi_circular():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"○ A")
    3.141592654 6.283185307
    9.424777961 12.56637061

    >>> test(r"A ○ A")
    0.8414709848 ¯0.4161468365
    ¯0.1425465431 4.123105626
    >>> test(r"A ○ 0 1")
    0 0.5403023059
    0 1.414213562
    >>> test(r"(2 1) ○ A")
    0.5403023059 0.9092974268
    ¯0.9899924966 ¯0.7568024953
    >>> test(r"A ○ 3")
    0.1411200081 ¯0.9899924966
    ¯0.1425465431 3.16227766
    >>> test(r"2 ○ A")
    0.5403023059 ¯0.4161468365
    ¯0.9899924966 ¯0.6536436209
    """
    pass

# ------------------------------

def     or_gcd():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"∨ A")
    VALENCE ERROR

    >>> test(r"A ∨ A")
    1 2
    3 4
    >>> test(r"A ∨ 1 2")
    1 2
    1 2
    >>> test(r"(2 1) ∨ A")
    1 1
    1 1
    >>> test(r"A ∨ 3")
    1 1
    3 1
    >>> test(r"2 ∨ A")
    1 2
    1 2
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"∧ A")
    VALENCE ERROR

    >>> test(r"A ∧ A")
    1 2
    3 4
    >>> test(r"A ∧ 1 2")
    1 2
    3 4
    >>> test(r"(2 1) ∧ A")
    2 2
    6 4
    >>> test(r"A ∧ 3")
    3 6
    3 12
    >>> test(r"2 ∧ A")
    2 2
    6 4
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"A ← 2 2 ⍴ 0 1 1 0")
    0 1
    1 0
    >>> test(r"A")
    0 1
    1 0
    >>> test(r"⍱ A")
    VALENCE ERROR

    >>> test(r"A ⍱ A")
    1 0
    0 1
    >>> test(r"A ⍱ 0 1")
    1 0
    0 0
    >>> test(r"(1 0) ⍱ A")
    0 0
    0 1
    >>> test(r"A ⍱ 1")
    0 0
    0 0
    >>> test(r"0 ⍱ A")
    1 0
    0 1
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"A ← 2 2 ⍴ 0 1 1 0")
    0 1
    1 0
    >>> test(r"A")
    0 1
    1 0
    >>> test(r"⍲ A")
    VALENCE ERROR

    >>> test(r"A ⍲ A")
    1 0
    0 1
    >>> test(r"A ⍲ 0 1")
    1 0
    1 1
    >>> test(r"(1 0) ⍲ A")
    1 1
    0 1
    >>> test(r"A ⍲ 1")
    1 0
    0 1
    >>> test(r"0 ⍲ A")
    1 1
    1 1
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"A ← 2 2 ⍴ 0 1 1 0")
    0 1
    1 0
    >>> test(r"A")
    0 1
    1 0

    >>> test(r"A < A")
    0 0
    0 0
    >>> test(r"A < 0 1")
    0 0
    0 1
    >>> test(r"(1 0) < A")
    0 1
    0 0
    >>> test(r"A < 1")
    1 0
    0 1
    >>> test(r"0 < A")
    0 1
    1 0
    """
    pass

# --------------

def     le():
    """
    >>> test(r"A ← 2 2 ⍴ 0 1 1 0")
    0 1
    1 0
    >>> test(r"A")
    0 1
    1 0

    >>> test(r"A ≤ A")
    1 1
    1 1
    >>> test(r"A ≤ 0 1")
    1 1
    0 1
    >>> test(r"(1 0) ≤ A")
    0 1
    1 1
    >>> test(r"A ≤ 1")
    1 1
    1 1
    >>> test(r"0 ≤ A")
    1 1
    1 1
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"A ← 2 2 ⍴ 0 1 1 0")
    0 1
    1 0
    >>> test(r"A")
    0 1
    1 0

    >>> test(r"A ≥ A")
    1 1
    1 1
    >>> test(r"A ≥ 0 1")
    1 1
    1 0
    >>> test(r"(1 0) ≥ A")
    1 0
    1 1
    >>> test(r"A ≥ 1")
    0 1
    1 0
    >>> test(r"0 ≥ A")
    1 0
    0 1
    """
    pass

# --------------

def     gt():
    """
    >>> test(r"A ← 2 2 ⍴ 0 1 1 0")
    0 1
    1 0
    >>> test(r"A")
    0 1
    1 0

    >>> test(r"A > A")
    0 0
    0 0
    >>> test(r"A > 0 1")
    0 0
    1 0
    >>> test(r"(1 0) > A")
    1 0
    0 0
    >>> test(r"A > 1")
    0 0
    0 0
    >>> test(r"0 > A")
    0 0
    0 0
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"A ← 2 2 ⍴ 0 1 1 0")
    0 1
    1 0
    >>> test(r"A")
    0 1
    1 0

    >>> test(r"A = A")
    1 1
    1 1
    >>> test(r"A = 0 1")
    1 1
    0 0
    >>> test(r"(1 0) = A")
    0 0
    1 1
    >>> test(r"A = 1")
    0 1
    1 0
    >>> test(r"0 = A")
    1 0
    0 1
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"A ← 2 2 ⍴ 0 1 1 0")
    0 1
    1 0
    >>> test(r"A")
    0 1
    1 0

    >>> test(r"A ≠ A")
    0 0
    0 0
    >>> test(r"A ≠ 0 1")
    0 0
    1 1
    >>> test(r"(1 0) ≠ A")
    1 1
    0 0
    >>> test(r"A ≠ 1")
    1 0
    0 1
    >>> test(r"0 ≠ A")
    0 1
    1 0
    """
    pass

# ------------------------------

def     depth_match():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"≡ A")
    1

    >>> test(r"A ≡ A")
    1
    """
    pass

# --------------

def     tally_notMatch():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"≢ A")
    2

    >>> test(r"A ≢ A")
    0
    """
    pass

# ------------------------------

def     rho():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⍴ A")
    2 2

    >>> test(r"A ⍴ A")
    RANK ERROR
    >>> test(r"A ⍴ 0 1")
    RANK ERROR
    >>> test(r"A ⍴ 3")
    RANK ERROR
    >>> test(r"1 1 ⍴ A")
    WIP - MATRIX ERROR
    >>> test(r"2 ⍴ A")
    1 2
    """
    pass

# --------------

def     comma():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r", A")
    1 2 3 4

    >>> test(r"A , A")
    WIP - RANK ERROR
    """
    pass

# --------------

def     enlist_membership():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"∊ A")
    1 2 3 4

    >>> test(r"A ∊ A")
    1 1
    1 1
    """
    pass

# --------------

def     find():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⍷ A")
    VALENCE ERROR

    >>> test(r"A ⍷ A")
    1 0
    0 0
    """
    pass

# --------------

def     transpose():
    """
    #>>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⍉ A")
    1 3
    2 4

    >>> test(r"A ⍉ A")
    RANK ERROR
    >>> test(r"A ⍉ 0 1")
    RANK ERROR
    >>> test(r"A ⍉ 3")
    RANK ERROR

    >>> test(r"(1 1) ⍉ A")
    1 4
    >>> test(r"2 ⍉ A")
    LENGTH ERROR
    """
    pass

# --------------

def     reverse_rotate():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⌽ A")
    2 1
    4 3
    >>> test(r"⊖ A")
    3 4
    1 2

    >>> test(r"A ⌽ A")
    RANK ERROR
    >>> test(r"A ⌽ 0 1")
    RANK ERROR
    >>> test(r"A ⌽ 3")
    RANK ERROR

    >>> test(r"(1 0) ⌽ A")
    2 1
    3 4
    >>> test(r"2 ⌽ A")
    1 2
    3 4

    >>> test(r"A ⊖ A")
    RANK ERROR
    >>> test(r"A ⊖ A")
    RANK ERROR
    >>> test(r"A ⊖ 0 1")
    RANK ERROR
    >>> test(r"A ⊖ 3")
    RANK ERROR

    >>> test(r"(1 0) ⊖ A")
    3 2
    1 4
    >>> test(r"2 ⊖ A")
    1 2
    3 4
    """
    pass

# --------------

def     enclose_partition():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⊂ A")
    (1 3
     2 4)

    >>> test(r"A ⊂ A")
    RANK ERROR
    >>> test(r"A ⊂ 0 1")
    RANK ERROR
    >>> test(r"A ⊂ 3")
    RANK ERROR

    >>> test(r"(1 0) ⊂ A")
    (1
    3)
    >>> test(r"2 ⊂ A")
    (1 2
    3 4)
    """
    pass

# --------------

def     disclose_pick():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⊃ A")
    1 3
    2 4

    >>> test(r"A ⊃ A")
    RANK ERROR
    >>> test(r"A ⊃ 0 1")
    RANK ERROR
    >>> test(r"(1 0) ⊃ A")
    RANK ERROR
    >>> test(r"A ⊃ 3")
    RANK ERROR
    >>> test(r"2 ⊃ A")
    RANK ERROR
    """
    pass

# ------------------------------

def     iota():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⍳ A")
    RANK ERROR

    >>> test(r"A ⍳ A")
    RANK ERROR
    >>> test(r"A ⍳ 0 1")
    RANK ERROR
    >>> test(r"A ⍳ 3")
    RANK ERROR

    >>> test(r"(1 0) ⍳ A")
    1 3
    3 3
    >>> test(r"2 ⍳ A")
    2 1
    2 2

    >>> setIndexOrigin(0)

    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    0 1
    2 3
    >>> test(r"A")
    0 1
    2 3
    >>> test(r"⍳ A")
    RANK ERROR

    >>> test(r"A ⍳ A")
    RANK ERROR
    >>> test(r"A ⍳ 0 1")
    RANK ERROR
    >>> test(r"A ⍳ 3")
    RANK ERROR

    >>> test(r"(1 0) ⍳ A")
    0 2
    2 2
    >>> test(r"2 ⍳ A")
    1 0
    1 1

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     tilde():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"~ 2 2 ⍴ 1")
    0 0
    0 0

    >>> test(r"A ~ A")
    RANK ERROR
    >>> test(r"A ~ 0 1")
    RANK ERROR
    >>> test(r"A ~ 3")
    RANK ERROR

    >>> test(r"(1 0) ~ A")
    0
    >>> test(r"2 ~ A")
    ⍬
    """
    pass

# --------------

def     unique_union():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"∪ A")
    RANK ERROR

    >>> test(r"A ∪ A")
    RANK ERROR
    >>> test(r"A ∪ 0 1")
    RANK ERROR
    >>> test(r"(1 0) ∪ A")
    RANK ERROR
    >>> test(r"A ∪ 3")
    RANK ERROR
    >>> test(r"2 ∪ A")
    RANK ERROR
    """
    pass

# --------------

def     intersection():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"∩ A")
    VALENCE ERROR

    >>> test(r"A ∩ A")
    RANK ERROR
    >>> test(r"A ∩ 0 1")
    RANK ERROR
    >>> test(r"(1 0) ∩ A")
    RANK ERROR
    >>> test(r"A ∩ 3")
    RANK ERROR
    >>> test(r"2 ∩ A")
    RANK ERROR
    """
    pass

# --------------

def     tail_drop():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"↓ A")
    RANK ERROR

    >>> test(r"A ↓ A")
    RANK ERROR
    >>> test(r"A ↓ 0 1")
    RANK ERROR
    >>> test(r"A ↓ 3")
    RANK ERROR

    >>> test(r"(1 0) ↓ A")
    3 4
    >>> test(r"2 ↓ A")
    LENGTH ERROR
    """
    pass

# --------------

def     head_take():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"↑ A")
    1

    >>> test(r"A ↑ A")
    RANK ERROR
    >>> test(r"A ↑ 0 1")
    RANK ERROR
    >>> test(r"A ↑ 3")
    RANK ERROR

    >>> test(r"(1 1) ↑ A")
    1
    >>> test(r"2 ↑ A")
    LENGTH ERROR
    """
    pass

# --------------

def     compress_replicate():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"/ A")
    SYNTAX ERROR

    >>> test(r"A / A")
    RANK ERROR
    >>> test(r"A / 0 1")
    RANK ERROR
    >>> test(r"A / 3")
    RANK ERROR

    >>> test(r"(1 0) / A")
    1
    3
    >>> test(r"2 / A")
    WIP - RANK ERROR
    """
    pass

# --------------

def     expand():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"\ A")
    SYNTAX ERROR

    >>> test(r"A \ A")
    RANK ERROR
    >>> test(r"A \ 0 1")
    RANK ERROR
    >>> test(r"A \ 3")
    RANK ERROR

    >>> test(r"(1 0 1) \ A")
    1 0 2
    3 0 4
    >>> test(r"2 \ A")
    DOMAIN ERROR ?
    """
    pass

# ------------------------------

def     encode():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⊤ A")
    VALENCE ERROR

    >>> test(r"A ⊤ A")
    RANK ERROR

    >>> test(r"A ⊤ 0 1")
    WIP - RANK ERROR
    >>> test(r"(1 0) ⊤ A")
    WIP - RANK ERROR

    >>> test(r"A ⊤ 3")
    0 0
    0 3
    >>> test(r"2 ⊤ A")
    1 0
    1 0
    """
    pass

# --------------

def     decode():
    """
    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"⊥ A")
    VALENCE ERROR

    >>> test(r"A ⊥ A")
    5 8
    7 12
    """
    pass

# --------------

def     gradeUp():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"A ← 2 2 ⍴ 'ABCD'")
    AB
    CD
    >>> test(r"A")
    AB
    CD
    >>> test(r"⍋ A")
    1 2

    >>> test(r"A ⍋ A")
    1 2

    >>> setIndexOrigin(0)

    >>> test(r"A ← 2 2 ⍴ 'ABCD'")
    AB
    CD
    >>> test(r"A")
    AB
    CD
    >>> test(r"⍋ A")
    0 1

    >>> test(r"A ⍋ A")
    0 1

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     gradeDown():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"A ← 2 2 ⍴ 'ABCD'")
    AB
    CD
    >>> test(r"A")
    AB
    CD
    >>> test(r"⍒ A")
    2 1

    >>> test(r"A ⍒ A")
    2 1

    >>> setIndexOrigin(0)

    >>> test(r"A ← 2 2 ⍴ 'ABCD'")
    AB
    CD
    >>> test(r"A")
    AB
    CD
    >>> test(r"⍋ A")
    1 0

    >>> test(r"A ⍋ A")
    1 0

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
