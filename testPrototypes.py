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

# --------------

def     ceil_maximum():
    """
    >>> test(r"⍬ ≡ ⌈ ⍬")
    1
    >>> test(r"'' ≡ ⌈ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ⌈ ⍬")
    1
    >>> test(r"'' ≡ '' ⌈ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ⌈ 1")
    1
    >>> test(r"'' ≡ '' ⌈ 1")
    1

    >>> test(r"⍬ ≡ 1 ⌈ ⍬")
    1
    >>> test(r"'' ≡ 1 ⌈ ''")
    1

    >>> test(r"⍬ ≡ '' ⌈ ⍬")
    1
    >>> test(r"'' ≡ 0 ⌈ ''")
    1
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"⍬ ≡ ⌊ ⍬")
    1
    >>> test(r"'' ≡ ⌊ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ⌊ ⍬")
    1
    >>> test(r"'' ≡ '' ⌊ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ⌊ 1")
    1
    >>> test(r"'' ≡ '' ⌊ 1")
    1

    >>> test(r"⍬ ≡ 1 ⌊ ⍬")
    1
    >>> test(r"'' ≡ 1 ⌊ ''")
    1

    >>> test(r"⍬ ≡ '' ⌊ ⍬")
    1
    >>> test(r"'' ≡ 0 ⌊ ''")
    1
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"⍬ ≡ | ⍬")
    1
    >>> test(r"'' ≡ | ''")
    1

    >>> test(r"⍬ ≡ ⍬ | ⍬")
    1
    >>> test(r"'' ≡ '' | ''")
    1

    >>> test(r"⍬ ≡ ⍬ | 1")
    1
    >>> test(r"'' ≡ '' | 1")
    1

    >>> test(r"⍬ ≡ 1 | ⍬")
    1
    >>> test(r"'' ≡ 1 | ''")
    1

    >>> test(r"⍬ ≡ '' | ⍬")
    1
    >>> test(r"'' ≡ 0 | ''")
    1
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"⍬ ≡ * ⍬")
    1
    >>> test(r"'' ≡ * ''")
    1

    >>> test(r"⍬ ≡ ⍬ * ⍬")
    1
    >>> test(r"'' ≡ '' * ''")
    1

    >>> test(r"⍬ ≡ ⍬ * 1")
    1
    >>> test(r"'' ≡ '' * 1")
    1

    >>> test(r"⍬ ≡ 1 * ⍬")
    1
    >>> test(r"'' ≡ 1 * ''")
    1

    >>> test(r"⍬ ≡ '' * ⍬")
    1
    >>> test(r"'' ≡ 0 * ''")
    1
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"⍬ ≡ ⍟ ⍬")
    1
    >>> test(r"'' ≡ ⍟ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ⍟ ⍬")
    1
    >>> test(r"'' ≡ '' ⍟ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ⍟ 1")
    1
    >>> test(r"'' ≡ '' ⍟ 1")
    1

    >>> test(r"⍬ ≡ 1 ⍟ ⍬")
    1
    >>> test(r"'' ≡ 1 ⍟ ''")
    1

    >>> test(r"⍬ ≡ '' ⍟ ⍬")
    1
    >>> test(r"'' ≡ 0 ⍟ ''")
    1
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"⍬ ≡ ! ⍬")
    1
    >>> test(r"'' ≡ ! ''")
    1

    >>> test(r"⍬ ≡ ⍬ ! ⍬")
    1
    >>> test(r"'' ≡ '' ! ''")
    1

    >>> test(r"⍬ ≡ ⍬ ! 1")
    1
    >>> test(r"'' ≡ '' ! 1")
    1

    >>> test(r"⍬ ≡ 1 ! ⍬")
    1
    >>> test(r"'' ≡ 1 ! ''")
    1

    >>> test(r"⍬ ≡ '' ! ⍬")
    1
    >>> test(r"'' ≡ 0 ! ''")
    1
    """
    pass

# --------------

def     roll_deal():
    """
    >>> test(r"⍬ ≡ ? ⍬")
    1
    >>> test(r"'' ≡ ? ''")
    1
    """
    pass

# ------------------------------

def     pi_circular():
    """
    >>> test(r"⍬ ≡ ○ ⍬")
    1
    >>> test(r"'' ≡ ○ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ○ ⍬")
    1
    >>> test(r"'' ≡ '' ○ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ○ 1")
    1
    >>> test(r"'' ≡ '' ○ 1")
    1

    >>> test(r"⍬ ≡ 1 ○ ⍬")
    1
    >>> test(r"'' ≡ 1 ○ ''")
    1

    >>> test(r"⍬ ≡ '' ○ ⍬")
    1
    >>> test(r"'' ≡ 0 ○ ''")
    1
    """
    pass

# ------------------------------

def     or_gcd():
    """
    >>> test(r"⍬ ≡ ⍬ ∨ ⍬")
    1
    >>> test(r"'' ≡ '' ∨ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ∨ 1")
    1
    >>> test(r"'' ≡ '' ∨ 1")
    1

    >>> test(r"⍬ ≡ 1 ∨ ⍬")
    1
    >>> test(r"'' ≡ 1 ∨ ''")
    1

    >>> test(r"⍬ ≡ '' ∨ ⍬")
    1
    >>> test(r"'' ≡ 0 ∨ ''")
    1
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"⍬ ≡ ⍬ ∧ ⍬")
    1
    >>> test(r"'' ≡ '' ∧ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ∧ 1")
    1
    >>> test(r"'' ≡ '' ∧ 1")
    1

    >>> test(r"⍬ ≡ 1 ∧ ⍬")
    1
    >>> test(r"'' ≡ 1 ∧ ''")
    1

    >>> test(r"⍬ ≡ '' ∧ ⍬")
    1
    >>> test(r"'' ≡ 0 ∧ ''")
    1
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"⍬ ≡ ⍬ ⍱ ⍬")
    1
    >>> test(r"'' ≡ '' ⍱ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ⍱ 1")
    1
    >>> test(r"'' ≡ '' ⍱ 1")
    1

    >>> test(r"⍬ ≡ 1 ⍱ ⍬")
    1
    >>> test(r"'' ≡ 1 ⍱ ''")
    1

    >>> test(r"⍬ ≡ '' ⍱ ⍬")
    1
    >>> test(r"'' ≡ 0 ⍱ ''")
    1
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"⍬ ≡ ⍬ ⍲ ⍬")
    1
    >>> test(r"'' ≡ '' ⍲ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ⍲ 1")
    1
    >>> test(r"'' ≡ '' ⍲ 1")
    1

    >>> test(r"⍬ ≡ 1 ⍲ ⍬")
    1
    >>> test(r"'' ≡ 1 ⍲ ''")
    1

    >>> test(r"⍬ ≡ '' ⍲ ⍬")
    1
    >>> test(r"'' ≡ 0 ⍲ ''")
    1
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"⍬ ≡ ⍬ ≤ ⍬")
    1
    >>> test(r"'' ≡ '' ≤ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ≤ 1")
    1
    >>> test(r"'' ≡ '' ≤ 1")
    1

    >>> test(r"⍬ ≡ 1 ≤ ⍬")
    1
    >>> test(r"'' ≡ 1 ≤ ''")
    1

    >>> test(r"⍬ ≡ '' ≤ ⍬")
    1
    >>> test(r"'' ≡ 0 ≤ ''")
    1
    """
    pass

# --------------

def     le():
    """
    >>> test(r"⍬ ≡ ⍬ < ⍬")
    1
    >>> test(r"'' ≡ '' < ''")
    1

    >>> test(r"⍬ ≡ ⍬ < 1")
    1
    >>> test(r"'' ≡ '' < 1")
    1

    >>> test(r"⍬ ≡ 1 < ⍬")
    1
    >>> test(r"'' ≡ 1 < ''")
    1

    >>> test(r"⍬ ≡ '' < ⍬")
    1
    >>> test(r"'' ≡ 0 < ''")
    1
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"⍬ ≡ ⍬ ≥ ⍬")
    1
    >>> test(r"'' ≡ '' ≥ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ≥ 1")
    1
    >>> test(r"'' ≡ '' ≥ 1")
    1

    >>> test(r"⍬ ≡ 1 ≥ ⍬")
    1
    >>> test(r"'' ≡ 1 ≥ ''")
    1

    >>> test(r"⍬ ≡ '' ≥ ⍬")
    1
    >>> test(r"'' ≡ 0 ≥ ''")
    1
    """
    pass

# --------------

def     gt():
    """
    >>> test(r"⍬ ≡ ⍬ > ⍬")
    1
    >>> test(r"'' ≡ '' > ''")
    1

    >>> test(r"⍬ ≡ ⍬ > 1")
    1
    >>> test(r"'' ≡ '' > 1")
    1

    >>> test(r"⍬ ≡ 1 > ⍬")
    1
    >>> test(r"'' ≡ 1 > ''")
    1

    >>> test(r"⍬ ≡ '' > ⍬")
    1
    >>> test(r"'' ≡ 0 > ''")
    1
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"⍬ ≡ ⍬ = ⍬")
    1
    >>> test(r"'' ≡ '' = ''")
    1

    >>> test(r"⍬ ≡ ⍬ = 1")
    1
    >>> test(r"'' ≡ '' = 1")
    1

    >>> test(r"⍬ ≡ 1 = ⍬")
    1
    >>> test(r"'' ≡ 1 = ''")
    1

    >>> test(r"⍬ ≡ '' = ⍬")
    1
    >>> test(r"'' ≡ 0 = ''")
    1
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"⍬ ≡ ⍬ ≠ ⍬")
    1
    >>> test(r"'' ≡ '' ≠ ''")
    1

    >>> test(r"⍬ ≡ ⍬ ≠ 1")
    1
    >>> test(r"'' ≡ '' ≠ 1")
    1

    >>> test(r"⍬ ≡ 1 ≠ ⍬")
    1
    >>> test(r"'' ≡ 1 ≠ ''")
    1

    >>> test(r"⍬ ≡ '' ≠ ⍬")
    1
    >>> test(r"'' ≡ 0 ≠ ''")
    1
    """
    pass

# ------------------------------

def     depth_match():
    """
    >>> test(r"⍬ ≡ ⍬")
    1
    >>> test(r"⍬ ≡ ''")
    0
    >>> test(r"'' ≡ ⍬")
    0
    >>> test(r"'' ≡ ''")
    1
    """
    pass

# --------------

def     tally_notMatch():
    """
    >>> test(r"⍬ ≢ ⍬")
    0
    >>> test(r"⍬ ≢ ''")
    1
    >>> test(r"'' ≢ ⍬")
    1
    >>> test(r"'' ≢ ''")
    0
    """
    pass

# ------------------------------

def     rho():
    """
    >>> test(r"⍬ ≡ 0 ⍴ 1 2 3")
    1
    >>> test(r"(,0) ≡ 1 ⍴ 0 ⍴ 1 2 3")
    1

    >>> test(r"'' ≡ 0 ⍴ 'abc'")
    1
    >>> test(r"(,' ') ≡ 1 ⍴ 0 ⍴ 'abc'")
    1
    """
    pass

# --------------

def     comma():
    """
    >>> test(r"⍬ ≡ , ⍬")
    1
    >>> test(r"'' ≡ , ''")
    1

    >>> test(r"⍬ ≡ 0 ⍴ , 1")
    1
    >>> test(r"'' ≡ 0 ⍴ , 'a'")
    1

    >>> test(r"(,' ') ≡ 1 ⍴ 0 ⍴ ⍬ , '!'")
    1
    >>> test(r"(,0) ≡ 1 ⍴ 0 ⍴ '' , 1")
    1
    """
    pass

# --------------

def     transpose():
    """
    >>> test(r"⍬ ≡ ⍉ ⍬")
    1
    >>> test(r"'' ≡ ⍉ ''")
    1

    >>> test(r"(,0) ≡ 1 ⍴ 1 ⍉ ⍬")
    1
    >>> test(r"(,' ') ≡ 1 ⍴ 1 ⍉ ''")
    1
    """
    pass

# --------------

def     reverse_rotate():
    """
    >>> test(r"⍬ ≡ ⌽ ⍬")
    1
    >>> test(r"'' ≡ ⌽ ''")
    1

    >>> test(r"⍬ ≡ 0 ⍴ ⌽ 'a' 1")
    1
    >>> test(r"'' ≡ 0 ⍴ ⌽ 1 'a'")
    1

    >>> test(r"(,' ') ≡ 1 ⍴ 0 ⍴ 1 ⌽ 1 '!' 3")
    1
    >>> test(r"(,0) ≡ 1 ⍴ 0 ⍴ 1 ⌽ 'a' 1 'c'")
    1
    """
    pass

# ------------------------------

def     iota():
    """
    no tests
    """
    pass

# --------------

def     tilde():
    """
    >>> test(r"(,0) ≡ 1 ⍴ 1 2 3 ~ 1 2 3")
    1
    >>> test(r"(,' ') ≡ 1 ⍴ 'Hello' ~ 'Hello'")
    1
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    import doctest
    doctest.testmod()

# EOF
