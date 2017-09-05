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

# ------------------------------

def     zilde(expr):
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

# ------------------------------

def     zildeIota():
    """
    zilde with iota (⍳)

    >>> test(r"⍳ 0")
    ⍬
    """
    pass

# --------------

def     zildeDepthMatch():
    """
    zilde with depth/match (≡)

    >>> test(r"≡ ⍬")
    1

    >>> test(r"⍬ ≡ ⍬")
    1
    >>> test(r"⍬ ≡ 1")
    0
    >>> test(r"1 ≡ ⍬")
    0

    >>> test(r"⍬ ≡ 1 2")
    0
    >>> test(r"1 2 ≡ ⍬")
    0
    """
    pass

# --------------

def     zildeTallyNoMatch():
    """
    zilde with tally (≢)

    >>> test(r"≢ ⍬")
    0

    >>> test(r"⍬ ≢ ⍬")
    0
    >>> test(r"⍬ ≢ 1")
    1
    >>> test(r"1 ≢ ⍬")
    1

    >>> test(r"⍬ ≢ 1 2")
    1
    >>> test(r"1 2 ≢ ⍬")
    1
    """
    pass

# --------------

def     zildeRho():
    """
    zilde with rho (⍴)

    >>> test(r"⍴ ⍬")
    0

    >>> test(r"⍴ 1")
    ⍬

    >>> test(r"⍬ ⍴ ⍬")
    0
    >>> test(r"⍬ ⍴ 1")
    1
    >>> test(r"1 ⍴ ⍬")
    0

    >>> test(r"6 ⍴ ⍬")
    0 0 0 0 0 0

    >>> test(r"0 ⍴ 1")
    ⍬
    >>> test(r"0 ⍴ 1 2 3")
    ⍬
    """
    pass

# --------------

def     zildeComma():
    """
    zilde with comma (,)

    >>> test(r", ⍬")
    ⍬

    >>> test(r"⍬ , ⍬")
    ⍬
    >>> test(r"⍬ , 1")
    1
    >>> test(r"1 , ⍬")
    1

    >>> test(r"⍴ ⍬ , 1")
    1
    >>> test(r"⍴ 1 , ⍬")
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

def     zildeReverseRotate():
    """
    zilde with reverse/rotate last axis (⌽) and reverse/rotate first axis (⊖)

    >>> test(r"⌽ ⍬")
    ⍬

    >>> test(r"⍬ ⌽ ⍬")
    RANK ERROR
    >>> test(r"⍬ ⌽ 0")
    RANK ERROR
    >>> test(r"0 ⌽ ⍬")
    ⍬

    >>> test(r"⊖ ⍬")
    ⍬

    >>> test(r"⍬ ⊖ ⍬")
    RANK ERROR
    >>> test(r"⍬ ⊖ 0")
    RANK ERROR
    >>> test(r"0 ⊖ ⍬")
    ⍬
    """
    pass

# --------------

def     zildeTranspose():
    """
    zilde with transpose (⍉)

    >>> test(r"⍉ ⍬")
    ⍬

    >>> test(r"⍬ ⍉ ⍬")
    LENGTH ERROR
    >>> test(r"1 ⍉ ⍬")
    ⍬
    >>> test(r"⍬ ⍉ 1")
    1
    """
    pass

# ------------------------------

def     zildeWithout():
    """
    zilde with without (~)

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

def     zildeDrop():
    """
    zilde with drop (↓)

    >>> test(r"↓ ⍬")
    ⍬

    >>> test(r"↓ 1")
    ⍬
    >>> test(r"↓ ,1")
    ⍬

    >>> test(r"⍬ ↓ ⍬")
    ⍬
    >>> test(r"⍬ ↓ 1")
    1
    >>> test(r"1 ↓ ⍬")
    ⍬
    >>> test(r"⍬ ↓ ,1")
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

def     zildeTake():
    """
    zilde with take (↑)

    >>> test(r"↑ ⍬")
    ⍬

    >>> test(r"⍬ ↑ ⍬")
    ⍬
    >>> test(r"⍬ ↑ 1")
    1
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

def     zildeUniqueUnion():
    """
    zilde with unique/union (∪)

    >>> test(r"∪ ⍬")
    ⍬

    >>> test(r"⍬ ∪ ⍬")
    ⍬
    >>> test(r"⍬ ∪ 1 2 3")
    1 2 3
    >>> test(r"1 2 3 ∪ ⍬")
    1 2 3
    """
    pass

# --------------

def     zildeIntersection():
    """
    zilde with intersection (∩)

    >>> test(r"⍬ ∩ ⍬")
    ⍬
    >>> test(r"⍬ ∩ 1 2 3")
    ⍬
    >>> test(r"1 2 3 ∩ ⍬")
    ⍬

    >>> test(r"1 ∩ 2")
    ⍬
    """
    pass

# --------------

def     zildeCompress():
    """
    zilde with compress (/)

    >>> test(r"⍬ / ⍬")
    ⍬
    >>> test(r"⍬ / 1")
    ⍬
    >>> test(r"1 / ⍬")
    ⍬

    >>> test(r"1 2 3 / ⍬")
    LENGTH ERROR
    >>> test(r"⍬ / 1 2 3")
    LENGTH ERROR

    !!! >>> test(r"0 / 1 2 3")
    ⍬
    >>> test(r"0 0 0 / 1 2 3")
    ⍬
    """
    pass

# --------------

def     zildeExpand():
    """
    zilde with expand (\\)

    >>> test(r"⍬ \\ ⍬")
    ⍬
    >>> test(r"⍬ \\ 21")
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

# --------------

def     zildeEncode():
    """
    zilde with encode (⊤)

    >>> test(r"⍬ ⊤ ⍬")
    ⍬
    >>> test(r"⍬ ⊤ 17")
    ⍬
    >>> test(r"16 ⊤ ⍬")
    ⍬
    """
    pass

# --------------

def     zildeDecode():
    """
    zilde with decode (⊥)

    >>> test(r"⍬ ⊥ ⍬")
    0
    >>> test(r"⍬ ⊥ 1 1")
    0
    >>> test(r"16 16 ⊥ ⍬")
    0
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    import doctest
    doctest.testmod()

# EOF
