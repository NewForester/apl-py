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

# --------------

def     ceil_maximum():
    """
    >>> test(r"⌈ 1.1 (2.2 3.3) 4.4")
    2 (3 4) 5

    >>> test(r"8.8 ⌈ 1.1 (2.2 3.3) 4.4")
    8.8 (8.8 8.8) 8.8
    >>> test(r"1.1 (2.2 3.3) 4.4 ⌈ 5.5")
    5.5 (5.5 5.5) 5.5
    >>> test(r"1.1 (2.2 3.3) 4.4 ⌈ 5.5 (6.6 7.7) 8.8")
    5.5 (6.6 7.7) 8.8

    >>> test(r"1.1 (2.2 3.3) 4.4 ⌈ (1.1 2.2) (3.3 4.4)", True)
    LENGTH ERROR
    >>> test(r"1.1 (2.2 3.3) 4.4 ⌈ 1.1 (2.2 0 3.3) 4.4", True)
    LENGTH ERROR

    >>> test(r"1.1 (2.2 3.3) 4.4 ⌈ (5.5 6.6) 1.1 (7.7 8.8)")
    (5.5 6.6) (2.2 3.3) (7.7 8.8)
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"⌊ 1.1 (2.2 3.3) 4.4")
    1 (2 3) 4

    >>> test(r"8.8 ⌊ 1.1 (2.2 3.3) 4.4")
    1.1 (2.2 3.3) 4.4
    >>> test(r"1.1 (2.2 3.3) 4.4 ⌊ 5.5")
    1.1 (2.2 3.3) 4.4
    >>> test(r"1.1 (2.2 3.3) 4.4 ⌊ 5.5 (6.6 7.7) 8.8")
    1.1 (2.2 3.3) 4.4

    >>> test(r"1.1 (2.2 3.3) 4.4 ⌊ (1.1 2.2) (3.3 4.4)", True)
    LENGTH ERROR
    >>> test(r"1.1 (2.2 3.3) 4.4 ⌊ 1.1 (2.2 0 3.3) 4.4", True)
    LENGTH ERROR

    >>> test(r"1.1 (2.2 3.3) 4.4 ⌊ (5.5 6.6) 1.1 (7.7 8.8)")
    (1.1 1.1) (1.1 1.1) (4.4 4.4)
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"| 1.1 (2.2 3.3) 4.4")
    1.1 (2.2 3.3) 4.4

    >>> test(r"8.8 | 1.1 (2.2 3.3) 4.4")
    1.1 (2.2 3.3) 4.4
    >>> test(r"1.1 (2.2 3.3) 4.4 | 5.5")
    0 (1.1 2.2) 1.1
    >>> test(r"1.1 (2.2 3.3) 4.4 | 5.5 (6.6 7.7) 8.8")
    0 (0 1.1) 0

    >>> test(r"1.1 (2.2 3.3) 4.4 | (1.1 2.2) (3.3 4.4)", True)
    LENGTH ERROR
    >>> test(r"1.1 (2.2 3.3) 4.4 | 1.1 (2.2 0 3.3) 4.4", True)
    LENGTH ERROR

    >>> test(r"1.1 (2.2 3.3) 4.4 | (5.5 6.6) 1.1 (7.7 8.8)")
    (0 0) (1.1 1.1) (3.3 0)
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"* 1.1 (2.2 3.3) 4.4")
    3.004166024 (9.025013499 27.11263892) 81.45086866

    >>> test(r"8.8 * 1.1 (2.2 3.3) 4.4")
    10.93782421 (119.6359985 1308.557522) 14312.77214
    >>> test(r"1.1 (2.2 3.3) 4.4 * 5.5")
    1.689117138 (76.44071568 710.9297188) 3459.311899
    >>> test(r"1.1 (2.2 3.3) 4.4 * 5.5 (6.6 7.7) 8.8")
    1.689117138 (181.9657674 9830.086446) 459603.7389

    >>> test(r"1.1 (2.2 3.3) 4.4 * (1.1 2.2) (3.3 4.4)", True)
    LENGTH ERROR
    >>> test(r"1.1 (2.2 3.3) 4.4 * 1.1 (2.2 0 3.3) 4.4", True)
    LENGTH ERROR

    >>> test(r"1.1 (2.2 3.3) 4.4 * (5.5 6.6) 1.1 (7.7 8.8)")
    (1.689117138 1.875822419) (2.380482258 3.718479006) (90071.12952 459603.7389)
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"⍟ 1.1 (2.2 3.3) 4.4")
    0.0953101798 (0.7884573604 1.193922468) 1.481604541

    >>> test(r"8.8 ⍟ 1.1 (2.2 3.3) 4.4")
    0.04382577508 (0.3625505167 0.5489925386) 0.6812752584
    >>> test(r"1.1 (2.2 3.3) 4.4 ⍟ 5.5")
    17.88631703 (2.162130989 1.427854938) 1.150609387
    >>> test(r"1.1 (2.2 3.3) 4.4 ⍟ 5.5 (6.6 7.7) 8.8")
    17.88631703 (2.393369311 1.709675781) 1.467835486

    >>> test(r"1.1 (2.2 3.3) 4.4 ⍟ (1.1 2.2) (3.3 4.4)", True)
    LENGTH ERROR
    >>> test(r"1.1 (2.2 3.3) 4.4 ⍟ 1.1 (2.2 0 3.3) 4.4", True)
    DOMAIN ERROR

    >>> test(r"1.1 (2.2 3.3) 4.4 ⍟ (5.5 6.6) 1.1 (7.7 8.8)")
    (17.88631703 19.7992455) (0.1208818442 0.07982945486) (1.377709282 1.467835486)
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"! 1 (2 3) 4")
    1 (2 6) 24

    >>> test(r"8 ! 1 (2 3) 4")
    0 (0 0) 0
    >>> test(r"1 (2 3) 4 ! 5")
    5 (10 10) 5
    >>> test(r"1 (2 3) 4 ! 5 (6 7) 8")
    5 (15 35) 70

    >>> test(r"1 (2 3) 4 ! (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 ! 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"1 (2 3) 4 ! (5 6) 10 (7 8)")
    (5 6) (45 120) (35 70)
    """
    pass

# --------------

def     roll_deal():
    """
    randomness makes positive testing a little tricky

    >>> test(r"≡ ? 1 (2 3) 4")
    2

    >>> test(r"8 ? 1 (2 3) 4")
    RANK ERROR
    >>> test(r"1 (2 3) 4 ? 5")
    RANK ERROR
    >>> test(r"1 (2 3) 4 ? 5 (6 7) 8")
    RANK ERROR

    >>> test(r"1 (2 3) 4 ? (1 2) (3 4)")
    RANK ERROR
    >>> test(r"1 (2 3) 4 ? 1 (2 0 3) 4")
    RANK ERROR

    >>> test(r"1 (2 3) 4 ? (5 6) 1 (7 8)")
    RANK ERROR
    """
    pass

# ------------------------------

def     pi_circular():
    """
    >>> test(r"○ 1 (2 3) 4")
    3.141592654 (6.283185307 9.424777961) 12.56637061

    >>> test(r"4 ○ 1 (2 3) 4")
    1.414213562 (2.236067977 3.16227766) 4.123105626
    >>> test(r"1 (2 3) 4 ○ 4")
    ¯0.7568024953 (¯0.6536436209 1.157821282) 4.123105626
    >>> test(r"1 (2 3) 4 ○ 5 (6 7) 8")
    ¯0.9589242747 (0.9601702867 0.8714479827) 8.062257748

    >>> test(r"1 (2 3) 4 ○ (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 ○ 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"1 (2 3) 4 ○ (5 6) 1 (7 8)")
    (¯0.9589242747 ¯0.2794154982) (0.5403023059 1.557407725) (7.071067812 8.062257748)
    """
    pass

# ------------------------------

def     or_gcd():
    """
    >>> test(r"∨ 1 (0 1) 0")
    VALENCE ERROR

    >>> test(r"0 ∨ 1 (0 1) 0")
    1 (0 1) 0
    >>> test(r"1 (0 1) 0 ∨ 1")
    1 (1 1) 1
    >>> test(r"1 (0 1) 0 ∨ 1 (0 1) 0")
    1 (0 1) 0

    >>> test(r"1 (0 1) 0 ∨ (1 0) (1 0)", True)
    LENGTH ERROR
    >>> test(r"1 (0 1) 0 ∨ 1 (0 0 1) 0", True)
    LENGTH ERROR

    >>> test(r"1 (0 1) 0 ∨ (1 0) 0 (1 0)")
    (1 1) (0 1) (1 0)
    >>> test(r"1 ('Hello') 0 ∨ (1 0) 'Hello' (1 0)", True)
    DOMAIN ERROR
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"∧ 1 (0 1) 0")
    VALENCE ERROR

    >>> test(r"0 ∧ 1 (0 1) 0")
    0 (0 0) 0
    >>> test(r"1 (0 1) 0 ∧ 1")
    1 (0 1) 0
    >>> test(r"1 (0 1) 0 ∧ 1 (0 1) 0")
    1 (0 1) 0

    >>> test(r"1 (0 1) 0 ∧ (1 0) (1 0)", True)
    LENGTH ERROR
    >>> test(r"1 (0 1) 0 ∧ 1 (0 0 1) 0", True)
    LENGTH ERROR

    >>> test(r"1 (0 1) 0 ∧ (1 0) 0 (1 0)")
    (1 0) (0 0) (0 0)
    >>> test(r"1 ('Hello') 0 ∧ (1 0) 'Hello' (1 0)", True)
    DOMAIN ERROR
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"⍱ 1 (0 1) 0")
    VALENCE ERROR

    >>> test(r"0 ⍱ 1 (0 1) 0")
    0 (1 0) 1
    >>> test(r"1 (0 1) 0 ⍱ 1")
    0 (0 0) 0
    >>> test(r"1 (0 1) 0 ⍱ 1 (0 1) 0")
    0 (1 0) 1

    >>> test(r"1 (0 1) 0 ⍱ (1 0) (1 0)", True)
    LENGTH ERROR
    >>> test(r"1 (0 1) 0 ⍱ 1 (0 0 1) 0", True)
    LENGTH ERROR

    >>> test(r"1 (0 1) 0 ⍱ (1 0) 0 (1 0)")
    (0 0) (1 0) (0 1)
    >>> test(r"1 ('Hello') 0 ⍱ (1 0) 'Hello' (1 0)", True)
    DOMAIN ERROR
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"⍲ 1 (0 1) 0")
    VALENCE ERROR

    >>> test(r"0 ⍲ 1 (0 1) 0")
    1 (1 1) 1
    >>> test(r"1 (0 1) 0 ⍲ 1")
    0 (1 0) 1
    >>> test(r"1 (0 1) 0 ⍲ 1 (0 1) 0")
    0 (1 0) 1

    >>> test(r"1 (0 1) 0 ⍲ (1 0) (1 0)", True)
    LENGTH ERROR
    >>> test(r"1 (0 1) 0 ⍲ 1 (0 0 1) 0", True)
    LENGTH ERROR

    >>> test(r"1 (0 1) 0 ⍲ (1 0) 0 (1 0)")
    (0 1) (1 1) (1 1)
    >>> test(r"1 ('Hello') 0 ⍲ (1 0) 'Hello' (1 0)", True)
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"< 1 (2 3) 4")
    VALENCE ERROR

    >>> test(r"2 < 1 (2 3) 4")
    0 (0 1) 1
    >>> test(r"1 (2 3) 4 < 3")
    1 (1 0) 0
    >>> test(r"1 (2 3) 4 < 5 (2 3) 8")
    1 (0 0) 1

    >>> test(r"1 (2 3) 4 < (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 < 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"5 (2 3) 8 < (5 6) 0 (7 8)")
    (0 1) (0 0) (0 0)
    >>> test(r"5 ('Hello') 8 < (5 6) 'Hello' (7 8)", True)
    DOMAIN ERROR
    """
    pass

# --------------

def     le():
    """
    >>> test(r"≤ 1 (2 3) 4")
    VALENCE ERROR

    >>> test(r"2 ≤ 1 (2 3) 4")
    0 (1 1) 1
    >>> test(r"1 (2 3) 4 ≤ 3")
    1 (1 1) 0
    >>> test(r"1 (2 3) 4 ≤ 5 (2 3) 8")
    1 (1 1) 1

    >>> test(r"1 (2 3) 4 ≤ (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 ≤ 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"5 (2 3) 8 ≤ (5 6) 0 (7 8)")
    (1 1) (0 0) (0 1)
    >>> test(r"5 ('Hello') 8 ≤ (5 6) 'Hello' (7 8)", True)
    DOMAIN ERROR
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"≥ 1 (2 3) 4")
    VALENCE ERROR

    >>> test(r"2 ≥ 1 (2 3) 4")
    1 (1 0) 0
    >>> test(r"1 (2 3) 4 ≥ 3")
    0 (0 1) 1
    >>> test(r"1 (2 3) 4 ≥ 5 (2 3) 8")
    0 (1 1) 0

    >>> test(r"1 (2 3) 4 ≥ (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 ≥ 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"5 (2 3) 8 ≥ (5 6) 0 (7 8)")
    (1 0) (1 1) (1 1)
    >>> test(r"5 ('Hello') 8 ≥ (5 6) 'Hello' (7 8)", True)
    DOMAIN ERROR
    """
    pass

# --------------

def     gt():
    """
    >>> test(r"> 1 (2 3) 4")
    VALENCE ERROR

    >>> test(r"2 > 1 (2 3) 4")
    1 (0 0) 0
    >>> test(r"1 (2 3) 4 > 3")
    0 (0 0) 1
    >>> test(r"1 (2 3) 4 > 5 (2 3) 8")
    0 (0 0) 0

    >>> test(r"1 (2 3) 4 > (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 > 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"5 (2 3) 8 > (5 6) 0 (7 8)")
    (0 0) (1 1) (1 0)
    >>> test(r"5 ('Hello') 8 > (5 6) 'Hello' (7 8)", True)
    DOMAIN ERROR
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"= 1 (2 3) 4")
    VALENCE ERROR

    >>> test(r"2 = 1 (2 3) 4")
    0 (1 0) 0
    >>> test(r"1 (2 3) 4 = 3")
    0 (0 1) 0
    >>> test(r"1 (2 3) 4 = 5 (2 3) 8")
    0 (1 1) 0

    >>> test(r"1 (2 3) 4 = (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 = 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"5 (2 3) 8 = (5 6) 0 (7 8)")
    (1 0) (0 0) (0 1)
    >>> test(r"5 ('Hello') 8 = (5 6) 'Hello' (7 8)")
    (1 0) (1 1 1 1 1) (0 1)
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"≠ 1 (2 3) 4")
    VALENCE ERROR

    >>> test(r"2 ≠ 1 (2 3) 4")
    1 (0 1) 1
    >>> test(r"1 (2 3) 4 ≠ 3")
    1 (1 0) 1
    >>> test(r"1 (2 3) 4 ≠ 5 (2 3) 8")
    1 (0 0) 1

    >>> test(r"1 (2 3) 4 ≠ (1 2) (3 4)", True)
    LENGTH ERROR
    >>> test(r"1 (2 3) 4 ≠ 1 (2 0 3) 4", True)
    LENGTH ERROR

    >>> test(r"5 (2 3) 8 ≠ (5 6) 0 (7 8)")
    (0 1) (1 1) (1 0)
    >>> test(r"5 ('Hello') 8 ≠ (5 6) 'Hello' (7 8)")
    (0 1) (0 0 0 0 0) (1 0)
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    import doctest
    doctest.testmod()

# EOF
