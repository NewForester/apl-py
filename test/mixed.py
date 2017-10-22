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
from test.base import saveIndexOrigin, setIndexOrigin, restoreIndexOrigin

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
    WIP - LENGTH ERROR
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
    WIP - LENGTH ERROR
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
    WIP - LENGTH ERROR
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
    WIP - LENGTH ERROR
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
    WIP - LENGTH ERROR
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
    WIP - LENGTH ERROR
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
    WIP - LENGTH ERROR
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"* M")
    DOMAIN ERROR

    >>> test(r"M * M")
    DOMAIN ERROR
    >>> test(r"1.2 * M")
    DOMAIN ERROR
    >>> test(r"M * 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 * M")
    DOMAIN ERROR
    >>> test(r"M * 1 2 3")
    DOMAIN ERROR

    >>> test(r"M * ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"⍟ M")
    DOMAIN ERROR

    >>> test(r"M ⍟ M")
    DOMAIN ERROR
    >>> test(r"1.2 ⍟ M")
    DOMAIN ERROR
    >>> test(r"M ⍟ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ⍟ M")
    DOMAIN ERROR
    >>> test(r"M ⍟ 1 2 3")
    DOMAIN ERROR

    >>> test(r"M ⍟ ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"! M")
    DOMAIN ERROR

    >>> test(r"M ! M")
    DOMAIN ERROR
    >>> test(r"1.2 ! M")
    DOMAIN ERROR
    >>> test(r"M ! 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ! M")
    DOMAIN ERROR
    >>> test(r"M ! 1 2 3")
    DOMAIN ERROR

    >>> test(r"M ! ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     roll_deal():
    """
    randomness makes positive testing a little tricky

    >>> test(r"M ← 'abc', 1 2 3")
    abc 1 2 3

    >>> test(r"? M")
    DOMAIN ERROR

    >>> test(r"M ? M")
    RANK ERROR
    >>> test(r"1.2 ? M")
    RANK ERROR
    >>> test(r"M ? 1.2")
    RANK ERROR

    >>> test(r"1 2 3 ? M")
    RANK ERROR
    >>> test(r"M ? 1 2 3")
    RANK ERROR

    >>> test(r"M ? ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# ------------------------------

def     pi_circular():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"○ M")
    DOMAIN ERROR

    >>> test(r"M ○ M")
    DOMAIN ERROR
    >>> test(r"1.2 ○ M")
    DOMAIN ERROR
    >>> test(r"M ○ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ○ M")
    DOMAIN ERROR
    >>> test(r"M ○ 1 2 3")
    DOMAIN ERROR

    >>> test(r"M ○ ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# ------------------------------

def     or_gcd():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"∧ M")
    VALENCE ERROR

    >>> test(r"M ∧ M")
    DOMAIN ERROR
    >>> test(r"1.2 ∧ M")
    DOMAIN ERROR
    >>> test(r"M ∧ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ∧ M")
    DOMAIN ERROR
    >>> test(r"M ∧ 1 2 3")
    DOMAIN ERROR

    >>> test(r"('abc', 1 2 3) ∧ 'abc', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ∧ 'pqr', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ∧ 4 5 6, 'abc'")
    DOMAIN ERROR

    >>> test(r"M ∧ ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"∧ M")
    VALENCE ERROR

    >>> test(r"M ∧ M")
    DOMAIN ERROR
    >>> test(r"1.2 ∧ M")
    DOMAIN ERROR
    >>> test(r"M ∧ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ∧ M")
    DOMAIN ERROR
    >>> test(r"M ∧ 1 2 3")
    DOMAIN ERROR

    >>> test(r"('abc', 1 2 3) ∧ 'abc', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ∧ 'pqr', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ∧ 4 5 6, 'abc'")
    DOMAIN ERROR

    >>> test(r"M ∧ ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"⍱ M")
    VALENCE ERROR

    >>> test(r"M ⍱ M")
    DOMAIN ERROR
    >>> test(r"1.2 ⍱ M")
    DOMAIN ERROR
    >>> test(r"M ⍱ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ⍱ M")
    DOMAIN ERROR
    >>> test(r"M ⍱ 1 2 3")
    DOMAIN ERROR

    >>> test(r"('abc', 1 2 3) ⍱ 'abc', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ⍱ 'pqr', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ⍱ 4 5 6, 'abc'")
    DOMAIN ERROR

    >>> test(r"M ⍱ ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"⍲ M")
    VALENCE ERROR

    >>> test(r"M ⍲ M")
    DOMAIN ERROR
    >>> test(r"1.2 ⍲ M")
    DOMAIN ERROR
    >>> test(r"M ⍲ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ⍲ M")
    DOMAIN ERROR
    >>> test(r"M ⍲ 1 2 3")
    DOMAIN ERROR

    >>> test(r"('abc', 1 2 3) ⍲ 'abc', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ⍲ 'pqr', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ⍲ 4 5 6, 'abc'")
    DOMAIN ERROR

    >>> test(r"M ⍲ ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"< M")
    VALENCE ERROR

    >>> test(r"M < M")
    DOMAIN ERROR
    >>> test(r"1.2 < M")
    DOMAIN ERROR
    >>> test(r"M < 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 < M")
    DOMAIN ERROR
    >>> test(r"M < 1 2 3")
    DOMAIN ERROR

    >>> test(r"('abc', 1 2 3) < 'abc', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) < 'pqr', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) < 4 5 6, 'abc'")
    DOMAIN ERROR

    >>> test(r"M < ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     le():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"≤ M")
    VALENCE ERROR

    >>> test(r"M ≤ M")
    DOMAIN ERROR
    >>> test(r"1.2 ≤ M")
    DOMAIN ERROR
    >>> test(r"M ≤ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ≤ M")
    DOMAIN ERROR
    >>> test(r"M ≤ 1 2 3")
    DOMAIN ERROR

    >>> test(r"('abc', 1 2 3) ≤ 'abc', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ≤ 'pqr', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ≤ 4 5 6, 'abc'")
    DOMAIN ERROR

    >>> test(r"M ≤ ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"≥ M")
    VALENCE ERROR

    >>> test(r"M ≥ M")
    DOMAIN ERROR
    >>> test(r"1.2 ≥ M")
    DOMAIN ERROR
    >>> test(r"M ≥ 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 ≥ M")
    DOMAIN ERROR
    >>> test(r"M ≥ 1 2 3")
    DOMAIN ERROR

    >>> test(r"('abc', 1 2 3) ≥ 'abc', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ≥ 'pqr', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) ≥ 4 5 6, 'abc'")
    DOMAIN ERROR

    >>> test(r"M ≥ ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     gt():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"> M")
    VALENCE ERROR

    >>> test(r"M > M")
    DOMAIN ERROR
    >>> test(r"1.2 > M")
    DOMAIN ERROR
    >>> test(r"M > 1.2")
    DOMAIN ERROR

    >>> test(r"1 2 3 > M")
    DOMAIN ERROR
    >>> test(r"M > 1 2 3")
    DOMAIN ERROR

    >>> test(r"('abc', 1 2 3) > 'abc', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) > 'pqr', 4 5 6")
    DOMAIN ERROR
    >>> test(r"('abc', 4 5 6) > 4 5 6, 'abc'")
    DOMAIN ERROR

    >>> test(r"M > ⍳⍴M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"= M")
    VALENCE ERROR

    >>> test(r"M = M")
    1 1 1 1 1 1
    >>> test(r"1.2 = M")
    0 0 0 0 0 0
    >>> test(r"M = 1.2")
    0 0 0 0 0 0

    >>> test(r"1 2 3 = M", True)
    LENGTH ERROR
    >>> test(r"M = 1 2 3", True)
    LENGTH ERROR

    >>> test(r"('abc', 1 2 3) = 'abc', 4 5 6")
    1 1 1 0 0 0
    >>> test(r"('abc', 4 5 6) = 'pqr', 4 5 6")
    0 0 0 1 1 1
    >>> test(r"('abc', 4 5 6) = 4 5 6, 'abc'")
    0 0 0 0 0 0

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"M = ⍳⍴M")
    WIP - LENGTH ERROR

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"M ← 'abc', 4 5 6")
    abc 4 5 6

    >>> test(r"≠ M")
    VALENCE ERROR

    >>> test(r"M ≠ M")
    0 0 0 0 0 0
    >>> test(r"1.2 ≠ M")
    1 1 1 1 1 1
    >>> test(r"M ≠ 1.2")
    1 1 1 1 1 1

    >>> test(r"1 2 3 ≠ M", True)
    LENGTH ERROR
    >>> test(r"M ≠ 1 2 3", True)
    LENGTH ERROR

    >>> test(r"('abc', 1 2 3) ≠ 'abc', 4 5 6")
    0 0 0 1 1 1
    >>> test(r"('abc', 4 5 6) ≠ 'pqr', 4 5 6")
    1 1 1 0 0 0
    >>> test(r"('abc', 4 5 6) ≠ 4 5 6, 'abc'")
    1 1 1 1 1 1

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"M ≠ ⍳⍴M")
    WIP - LENGTH ERROR

    >>> restoreIndexOrigin(IO)
    """
    pass

# ------------------------------

def     depth_match():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"≡ M")
    1

    >>> test(r"M ≡ M")
    1
    >>> test(r"1.2 ≡ M")
    0
    >>> test(r"M ≡ 1.2")
    0

    >>> test(r"1 2 3 ≡ M")
    0
    >>> test(r"M ≡ 1 2 3")
    0

    >>> test(r"M ≡ ⌽ 1 2 3 'abc'")
    0
    >>> test(r"M ≡ ⌽ 'cba', 3 2 1")
    1
    """
    pass

# --------------

def     tally_notMatch():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"≢ M")
    6

    >>> test(r"M ≢ M")
    0
    >>> test(r"1.2 ≢ M")
    1
    >>> test(r"M ≢ 1.2")
    1

    >>> test(r"1 2 3 ≢ M")
    1
    >>> test(r"M ≢ 1 2 3")
    1

    >>> test(r"M ≢ ⌽ 1 2 3 'abc'")
    1
    >>> test(r"M ≢ ⌽ 'cba', 3 2 1")
    0
    """
    pass

# --------------

def     rho():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"⍴ M")
    6
    >>> test(r"⍴ M, M")
    12

    >>> test(r"1 ⍴ M")
    1
    >>> test(r"2 ⍴ M")
    1 2
    >>> test(r"3 ⍴ M")
    1 2 3
    >>> test(r"4 ⍴ M")
    1 2 3 a
    >>> test(r"5 ⍴ M")
    1 2 3 ab
    >>> test(r"6 ⍴ M")
    1 2 3 abc

    >>> test(r"7 ⍴ M")
    1 2 3 abc 1
    >>> test(r"11 ⍴ M")
    1 2 3 abc 1 2 3 ab
    >>> test(r"13 ⍴ M")
    1 2 3 abc 1 2 3 abc 1
    """
    pass

# --------------

def     comma():
    """
    >>> test(r"1 2 3 , ''")
    1 2 3
    >>> test(r'1 2 3 , ""')
    1 2 3

    >>> test(r"⍴ 1 2 3 , ''")
    3
    >>> test(r'⍴ 1 2 3 , ""')
    3

    >>> test(r"1 2 3 , 'H'")
    1 2 3 H
    >>> test(r'1 2 3 , "H"')
    1 2 3 H

    >>> test(r"⍴ 1 2 3 , 'H'")
    4
    >>> test(r'⍴ 1 2 3 , "H"')
    4

    >>> test(r"1 2 3 , 'Hello'")
    1 2 3 Hello
    >>> test(r"'Hello' , 1 2 3")
    Hello 1 2 3

    >>> test(r"⍴ 1 2 3 , 'Hello'")
    8
    >>> test(r"⍴ 'Hello' , 1 2 3")
    8
    """
    pass

# --------------

def     enlist_membership():
    """
    >>> test(r"∊ 1 2 3 , 'Hello'")
    1 2 3 Hello
    >>> test(r"≢ ∊ 1 2 3 , 'Hello'")
    8
    >>> test(r"≡ ∊ 1 2 3 , 'Hello'")
    1

    >>> test(r"∊ 'Hello' , 1 2 3")
    Hello 1 2 3
    >>> test(r"≢ ∊ 'Hello' , 1 2 3")
    8
    >>> test(r"≡ ∊ 'Hello' , 1 2 3")
    1

    >>> test(r"∊ 1 2 3 'Hello'")
    1 2 3 Hello
    >>> test(r"≢ ∊ 1 2 3 'Hello'")
    8
    >>> test(r"≡ ∊ 1 2 3 'Hello'")
    1

    >>> test(r"∊ 'Hello' 1 2 3")
    Hello 1 2 3
    >>> test(r"≢ ∊ 'Hello' 1 2 3")
    8
    >>> test(r"≡ ∊ 'Hello' 1 2 3")
    1

    >>> test(r"2 4 6 ∊ 1 2 3 , 'Hello'")
    1 0 0
    >>> test(r"'Hell' ∊ 1 2 3 , 'Hello'")
    1 1 1 1
    >>> test(r"2 4 6 'Hell' ∊ 1 2 3 , 'Hello'")
    1 0 0 0
    >>> test(r"(2 4 6, 'Hell') ∊ 1 2 3 , 'Hello'")
    1 0 0 1 1 1 1
    """
    pass

# --------------

def     find():
    """
    only dyadic

    >>> test(r"1 2 3 ⍷ 1 2 3 , 'Hello'")
    1 0 0 0 0 0 0 0
    >>> test(r"'Hello' ⍷ 1 2 3 , 'Hello'")
    0 0 0 1 0 0 0 0
    >>> test(r"3 'H' ⍷ 1 2 3 , 'Hello'")
    0 0 1 0 0 0 0 0
    >>> test(r"(2 3, 'He') ⍷ 1 2 3 , 'Hello'")
    0 1 0 0 0 0 0 0
    """
    pass

# --------------

def     transpose():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"⍉ M")
    1 2 3 abc

    >>> test(r"1 ⍉ M")
    1 2 3 abc
    """
    pass

# --------------

def     reverse_rotate():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"⌽ M")
    cba 3 2 1

    >>> test(r"3 ⌽ M")
    abc 1 2 3
    >>> test(r"¯3 ⌽ M")
    abc 1 2 3

    >>> test(r"1 ⌽ M")
    2 3 abc 1
    >>> test(r"¯1 ⌽ M")
    c 1 2 3 ab
    """
    pass

# --------------

def     enclose_partition():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"⊂ M")
    (1 2 3 abc)
    >>> test(r"⊂ ⌽ M")
    (cba 3 2 1)

    >>> test(r"1 1 1 2 2 2 ⊂ M")
    (1 2 3) 'abc'
    >>> test(r"1 0 1 2 0 2 ⊂ M")
    (1) (3) 'a' 'c'
    >>> test(r"1 ¯1 1 2 ¯2 2 ⊂ M")
    DOMAIN ERROR

    >>> test(r"1 1 2 2 3 3 ⊂ M")
    (1 2) (3 a) 'bc'
    """
    pass

# --------------

def     disclose_pick():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"⊃ M")
    1 2 3 abc
    >>> test(r"⊃ ⌽ M")
    cba 3 2 1

    >>> test(r"M ≡ ⊃⊂ M")
    1
    >>> test(r"M ≡ ⌽ ⊃⊂ ⌽ M")
    1

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"3 ⊂ M")
    (1 2 3 abc)

    >>> setIndexOrigin(0)

    >>> test(r"3 ⊂ M")
    (1 2 3 abc)

    >>> restoreIndexOrigin(IO)
    """
    pass

# ------------------------------

def     iota():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⍳ M")
    WIP - LENGTH ERROR

    >>> test(r"M ⍳ M")
    1 2 3 4 5 6
    >>> test(r"1 2 3 ⍳ M")
    1 2 3 4 4 4
    >>> test(r"'abc' ⍳ M")
    4 4 4 1 2 3

    >>> setIndexOrigin(0)

    >>> test(r"⍳ M")
    WIP - LENGTH ERROR

    >>> test(r"M ⍳ M")
    0 1 2 3 4 5
    >>> test(r"1 2 3 ⍳ M")
    0 1 2 3 3 3
    >>> test(r"'abc' ⍳ M")
    3 3 3 0 1 2

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     tilde():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"~ M")
    DOMAIN ERROR

    >>> test(r"1 2 3 ~ M")
    ⍬
    >>> test(r"'abc' ~ M")
    ''

    >>> test(r"M ~ 2 'b'")
    1 3 ac
    >>> test(r"M ~ 2, 'b'")
    1 3 ac
    """
    pass

# --------------

def     unique_union():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"∪ M")
    1 2 3 abc

    >>> test(r"1 2 3 ∪ M")
    1 2 3 abc
    >>> test(r"'abc' ∪ M")
    abc 1 2 3

    >>> test(r"M ∪ 4 5 6")
    1 2 3 abc 4 5 6
    >>> test(r"M ∪ 'pqr'")
    1 2 3 abcpqr
    """
    pass

# --------------

def     intersection():
    """
    only dyadic

    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"∩ M")
    VALENCE ERROR

    >>> test(r"1 2 3 ∩ M")
    1 2 3
    >>> test(r"'abc' ∩ M")
    abc

    >>> test(r"M ∩ 4 5 6, 'abc'")
    abc
    >>> test(r"M ∩ 1 2 3, 'pqr'")
    1 2 3
    """
    pass

# --------------

def     tail_drop():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"↓ M")
    2 3 abc
    >>> test(r"↓ ⌽M")
    ba 3 2 1

    >>> test(r"0 ↓ M")
    1 2 3 abc
    >>> test(r"2 ↓ M")
    3 abc
    >>> test(r"¯2 ↓ M")
    1 2 3 a

    >>> test(r"0 ↓ ⌽M")
    cba 3 2 1
    >>> test(r"2 ↓ ⌽M")
    a 3 2 1
    >>> test(r"¯2 ↓ ⌽M")
    cba 3
    """
    pass

# --------------

def     head_take():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"↑ M")
    1
    >>> test(r"↑ ⌽M")
    c

    >>> test(r"0 ↑ M")
    ⍬
    >>> test(r"4 ↑ M")
    1 2 3 a
    >>> test(r"¯4 ↑ M")
    3 abc

    >>> test(r"0 ↑ ⌽M")
    ''
    >>> test(r"4 ↑ ⌽M")
    cba 3
    >>> test(r"¯4 ↑ ⌽M")
    a 3 2 1

    >>> test(r"'«', (8 ↑ M), '»'")
    « 1 2 3 abc 0 0 »
    >>> test(r"'«', (¯8 ↑ M), '»'")
    « 0 0 1 2 3 abc»

    >>> test(r"'«', (8 ↑ ⌽M), '»'")
    «cba 3 2 1   »
    >>> test(r"'«', (¯8 ↑ ⌽M), '»'")
    «  cba 3 2 1 »
    """
    pass

# --------------

def     compress_replicate():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    only dyadic

    >>> test(r"/ M")
    SYNTAX ERROR

    >>> test(r"0 1 0 1 0 1 / M")
    2 ac

    >>> test(r"2 1 2 1 2 1 / M")
    1 1 2 3 3 abbc
    >>> test(r"¯2 1 ¯2 1 ¯2 1 / M")
    0 0 2 0 0 a 0 0 c

    >>> test(r"2 1 2 1 2 1 / ⌽ M")
    ccbaa 3 2 2 1
    >>> test(r"¯2 1 ¯2 1 ¯2 1 / ⌽ M")
      b   3    1

    >>> test(r"M / M", True)
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     expand():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    only dyadic

    >>> test(r"\\ M")
    SYNTAX ERROR

    >>> test(r"0 1 0 1 0 1 0 1 0 1 0 1 \\ M")
    0 1 0 2 0 3 0 a 0 b 0 c
    >>> test(r"2 1 2 1 2 1 \\ M")
    1 1 2 3 3 abbc
    >>> test(r"¯2 1 ¯2 1 ¯2 1 ¯2 1 ¯2 1 ¯2 1 \\ M")
    0 0 1 0 0 2 0 0 3 0 0 a 0 0 b 0 0 c

    >>> test(r"0 1 0 1 0 1 0 1 0 1 0 1 \\ ⌽ M")
     c b a  3   2   1
    >>> test(r"2 1 2 1 2 1 \\ ⌽ M")
    ccbaa 3 2 2 1
    >>> test(r"¯2 1 ¯2 1 ¯2 1 ¯2 1 ¯2 1 ¯2 1 \\ ⌽ M")
      c  b  a   3    2    1

    >>> test(r"M \\ M", True)
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     encode():
    """
    only dyadic

    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"⊤ M")
    VALENCE ERROR

    >>> test(r"M ⊤ 13579")
    DOMAIN ERROR

    >>> test(r"M ⊤ M")
    WIP - LENGTH ERROR
    """
    pass

# --------------

def     decode():
    """
    only dyadic

    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> test(r"⊥ M")
    VALENCE ERROR

    >>> test(r"1 2 3 ⊥ M")
    LENGTH ERROR
    >>> test(r"1 2 3 ⊥ ⌽ M")
    DOMAIN ERROR
    >>> test(r"'abc' ⊥ M")
    DOMAIN ERROR
    >>> test(r"1 2 3 4 5 6 ⊥ M")
    DOMAIN ERROR
    """
    pass

# --------------

def     gradeUp():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⍋ M")
    4 5 6 1 2 3
    >>> test(r"⍋ ⌽M")
    3 2 1 6 5 4

    >>> test(r"M ⍋ M")
    DOMAIN ERROR
    >>> test(r"M ⍋ ⌽M")
    DOMAIN ERROR

    >>> test(r"M ⍋ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⍋ M")
    DOMAIN ERROR

    >>> setIndexOrigin(0)

    >>> test(r"⍋ M")
    3 4 5 0 1 2
    >>> test(r"⍋ ⌽M")
    2 1 0 5 4 3

    >>> test(r"M ⍋ M")
    DOMAIN ERROR
    >>> test(r"M ⍋ ⌽M")
    DOMAIN ERROR

    >>> test(r"M ⍋ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⍋ M")
    DOMAIN ERROR

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     gradeDown():
    """
    >>> test(r"M ← 1 2 3, 'abc'")
    1 2 3 abc

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⍒ M")
    3 2 1 6 5 4
    >>> test(r"⍒ ⌽M")
    4 5 6 1 2 3

    >>> test(r"M ⍒ M")
    DOMAIN ERROR
    >>> test(r"M ⍒ ⌽M")
    DOMAIN ERROR

    >>> test(r"M ⍒ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⍒ M")
    DOMAIN ERROR

    >>> setIndexOrigin(0)

    >>> test(r"⍒ M")
    2 1 0 5 4 3
    >>> test(r"⍒ ⌽M")
    3 4 5 0 1 2

    >>> test(r"M ⍒ M")
    DOMAIN ERROR
    >>> test(r"M ⍒ ⌽M")
    DOMAIN ERROR

    >>> test(r"M ⍒ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⍒ M")
    DOMAIN ERROR

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
