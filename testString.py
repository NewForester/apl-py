#!/usr/bin/python3
"""
    doctest style unit tests for strings

    WIP - grows as functions are implemented

    The tests in this module exercise monadic and dyadic functions with

        either one or two string operands

    Other cases are covered in other test modules.

    Each test passes an APL expression to the evaluate function.
    Both positive and negative (e.g. DOMAIN ERROR) cases are tested.
"""

from evaluate import evaluate

from apl_cio import APL_cio as apl_cio
from apl_error import APL_exception as apl_exception

# ------------------------------

def     test(expr):
    """
    test both positive and negative outcomes
    """
    try:
        cio = apl_cio()
        cio.printResult(evaluate(expr, cio))
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     stringMathematical():
    """
    For the mathematical functions
        + - × ÷ ⌈ ⌊ |
        * ⍟ ? ! ⌹ ○
        ~ ∨ ∧ ⍱ ⍲
        < ≤ ≥ > = ≠

    and any string argument S:

        fn S
        S fn S
        X fn S
        S fn X

    yield DOMAIN ERROR

    except where the monadic form yields VALENCE ERROR

    >>> test(r"+ 'Hello'")
    DOMAIN ERROR
    >>> test(r"- 'Hello'")
    DOMAIN ERROR
    >>> test(r"× 'Hello'")
    DOMAIN ERROR
    >>> test(r"÷ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' + 'Goodbye'")
    DOMAIN ERROR
    >>> test(r"'Hello' - 'Goodbye'")
    DOMAIN ERROR
    >>> test(r"'Hello' × 'Goodbye'")
    DOMAIN ERROR
    >>> test(r"'Hello' ÷ 'Goodbye'")
    DOMAIN ERROR

    >>> test(r"1 + 'Hello'")
    DOMAIN ERROR
    >>> test(r"1 - 'Hello'")
    DOMAIN ERROR
    >>> test(r"1 × 'Hello'")
    DOMAIN ERROR
    >>> test(r"1 ÷ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' + 1")
    DOMAIN ERROR
    >>> test(r"'Hello' - 1")
    DOMAIN ERROR
    >>> test(r"'Hello' × 1")
    DOMAIN ERROR
    >>> test(r"'Hello' ÷ 1")
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     stringCompare():
    """
    >>> test(r"1 = 'Hello'")
    0 0 0 0 0
    >>> test(r"1 ≠ 'Hello'")
    1 1 1 1 1

    >>> test(r"'Hello' = 'Hello'")
    1 1 1 1 1
    >>> test(r"'hello' ≠ 'Hello'")
    1 0 0 0 0

    >>> test(r"'H' = 72")
    1
    >>> test(r'"H" ≠ 72')
    0

    >>> test(r"'Hello' = 'Goodbye'")
    LENGTH ERROR
    >>> test(r"'Hello' ≠ 'Goodbye'")
    LENGTH ERROR
    """
    pass

# --------------

def     stringMatch():
    """
    >>> test(r"'Hello' ≡ 'H', 'ello'")
    1
    >>> test(r"'Hello' ≡ 'Hello'")
    1

    >>> test(r"'Hello' ≢ 'J', 'ello'")
    1
    >>> test(r"'Hello' ≢ 'Jello'")
    1

    !>>> test(r"(1 'Hello' 3) ≡ 1 'Jello' 3")
    0

    !>>> test(r"(1 'Hello' 3) ≡ 1 'Hello' 3")
    1
    """
    pass

# ------------------------------

def     stringDepthTally():
    """
    >>> test(r"≡ 'Hello'")
    1

    >>> test(r"≡ 1 'Hello' 3")
    2

    >>> test(r"≢ 'Hello'")
    5

    >>> test(r"≢ 1 'Hello' 3")
    3
    """
    pass

# --------------

def     stringRho():
    """
    >>> test(r"⍴ 'Hello'")
    5
    >>> test(r"⍴ 'Hello' 'Paul'")
    2
    >>> test(r"⍴ 1 'Hello' 2")
    3

    >>> test(r"⍴ 'H'")
    ⍬
    >>> test(r'⍴ "H"')
    1

    >>> test(r"4 ⍴ 'Hello'")
    Hell
    >>> test(r"5 ⍴ 'Hello'")
    Hello
    >>> test(r"6 ⍴ 'Hello'")
    HelloH
    """
    pass

# ------------------------------

def     stringComma():
    """
    >>> test(r", 'Hello'")
    Hello
    >>> test(r", 'Hello' 'Paul'")
    'Hello' 'Paul'
    >>> test(r", 1 'Hello' 2")
    1 'Hello' 2

    >>> test(r", 'H'")
    H
    >>> test(r', "H"')
    H

    >>> test(r"⍴ , 'H'")
    1
    >>> test(r'⍴ , "H"')
    1

    >>> test(r"'Hello' , ' ' , 'Paul'")
    Hello Paul

    >>> test(r"1 2 3 , 'Hello'")
    1 2 3 'Hello'
    >>> test(r"'Hello' , 1 2 3")
    'Hello' 1 2 3
    >>> test(r"1 2 3 , 'H'")
    1 2 3 'H'
    >>> test(r'1 2 3 , "H"')
    1 2 3 'H'
    """
    pass

# --------------

def     stringRotate():
    """
    >>> test(r"⌽ 'niagara'")
    aragain
    >>> test(r"⊖ 'nigeria'")
    airegin

    >>> test(r"1 ⌽ 'nope'")
    open
    >>> test(r"2 ⊖ 'anna'")
    naan

    >>> test(r'1 ⌽ "a"')
    a
    >>> test(r'2 ⊖ "b"')
    b

    >>> test(r"'H' ⌽ 'nope'")
    DOMAIN ERROR
    >>> test(r"'Hi' ⊖ 'anna'")
    DOMAIN ERROR
    """
    pass

# --------------

def     stringTranspose():
    """
    >>> test(r"'H' ⍉ 1 2 3")
    DOMAIN ERROR

    >>> test(r"⍉ 'Hello'")
    Hello

    >>> test(r"1 ⍉ 'Hello'")
    Hello
    """
    pass

# ------------------------------

def     stringTilda():
    """
    >>> test(r"~ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ~ 'Hello'")
    1
    >>> test(r"'Hello' ~ 1")
    Hello
    >>> test(r"'Hello' ~ 'hello'")
    H

    >>> test(r"'Hello' ~ 'Hello'")
    <BLANKLINE>
    """
    pass

# --------------

def     stringIota():
    """
    >>> test(r"⍳ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ⍳ 'Hello'")
    2 2 2 2 2
    >>> test(r"'Hello' ⍳ 1")
    6
    >>> test(r"'Hello' ⍳ 'hello'")
    6 2 3 3 5

    >>> test(r"'Hello' ⍳ 72")
    6
    """
    pass

# --------------

def     stringDrop():
    """
    >>> test(r'↓ ""')
    <BLANKLINE>
    >>> test(r"↓ 'Hello'")
    ello
    >>> test(r"1 ↓ 'Hello'")
    ello

    >>> test(r"¯9 ↓ 'abcdef'")
    <BLANKLINE>
    >>> test(r"¯6 ↓ 'abcdef'")
    <BLANKLINE>
    >>> test(r"¯3 ↓ 'abcdef'")
    abc
    >>> test(r"0 ↓ 'abcdef'")
    abcdef
    >>> test(r"3 ↓ 'abcdef'")
    def
    >>> test(r"6 ↓ 'abcdef'")
    <BLANKLINE>
    >>> test(r"9 ↓ 'abcdef'")
    <BLANKLINE>
    """
    pass

# --------------

def     stringTake():
    """
    >>> test(r"1 ↑ 'Hello'")
    H
    >>> test(r"↑ 'Hello'")
    H
    >>> test(r'↑ ""')
    <BLANKLINE>

    >>> test(r"¯9 ↑ 'abcdef'")
       abcdef
    >>> test(r"¯6 ↑ 'abcdef'")
    abcdef
    >>> test(r"¯3 ↑ 'abcdef'")
    def
    >>> test(r"0 ↑ 'abcdef'")
    <BLANKLINE>
    >>> test(r"3 ↑ 'abcdef'")
    abc
    >>> test(r"6 ↑ 'abcdef'")
    abcdef
    >>> test(r"(9 ↑ 'abcdef'), '!'")
    abcdef   !
    """
    pass

# --------------

def     stringUnion():
    """
    >>> test(r"'Hi' ∪ 'Hello'")
    Hiello
    >>> test(r"'ll' ∪ 'Hello'")
    llHeo
    >>> test(r"'l' ∪ 'Hello'")
    lHeo

    !!! test(r""Hi" ∪ 1 2 3")
    "Hi" 1 2 3
    """
    pass

# --------------

def     stringIntersection():
    """
    >>> test(r"'Hi' ∩ 'Hello'")
    H
    >>> test(r"'ll' ∩ 'Hello'")
    ll
    >>> test(r"'l' ∩ 'Hello'")
    l

    !!! test(r""Hi" ∩ 1 2 3")
    ⍬
    """
    pass

# --------------

def     stringCompress():
    """
    >>> test(r"1 0 1 / 'ABC'")
    AC
    >>> test(r"1 2 3 / 'ABC'")
    ABBCCC
    >>> test(r"1 ¯2 3 / 'ABC'")
    A  CCC
    """
    pass

# --------------

def     stringExpand():
    """
    >>> test(r"1 0 1 0 1 \\ 'ABC'")
    A B C
    >>> test(r"1 0 2 0 3 \\ 'ABC'")
    A BB CCC
    >>> test(r"¯1 1 ¯2 1 ¯3 1 \\ 'ABC'")
     A  B   C
    """
    pass

# --------------

def     stringEncodeDecode():
    """
    >>> test(r"'Hello' ⊤ 17")
    DOMAIN ERROR
    >>> test(r"16 16 ⊤ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ⊥ 1 1")
    DOMAIN ERROR
    >>> test(r"16 16 ⊥ 'Hello'")
    DOMAIN ERROR
    """
    pass

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
