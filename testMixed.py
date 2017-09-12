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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    RANK ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    DOMAIN ERROR
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
    0 0 0 1 1 1

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
    1 1 1 0 0 0

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

    !!! >>> test(r"M ≡ ⌽ 1 2 3 'abc'")
    0
    !!! >>> test(r"M ≡ ⌽ 'cba', 3 2 1")
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

    !!! >>> test(r"M ≢ ⌽ 1 2 3 'abc'")
    1
    !!! >>> test(r"M ≢ ⌽ 'cba', 3 2 1")
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

# ------------------------------

if __name__ == "__main__":
    preamble()
    import doctest
    doctest.testmod()

# EOF
