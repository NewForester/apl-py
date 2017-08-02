#!/usr/bin/python3
"""
    doctest style unit tests for strings

    WIP - grows as operators are implemented

    Each test passes a APL expression to the evaluate function.

    Each expression has one or two string operand.
"""

from evaluate import evaluate

from apl_cio import APL_cio as apl_cio
from apl_error import APL_exception as apl_exception

# ------------------------------

def     test (expr):
    """
    >>> test("'Hello'")
    Hello
    >>> test("'Hello\\"Jello'")
    Hello"Jello
    >>> test("'Hello''Jello'")
    Hello'Jello
    >>> test("'H'")
    H
    >>> test("''")
    <BLANKLINE>

    >>> test('"Hello"')
    Hello
    >>> test('"Hello\\'Jello"')
    Hello'Jello
    >>> test('"Hello""Jello"')
    Hello"Jello
    >>> test('"H"')
    H
    >>> test('""')
    <BLANKLINE>

    >>> test("'Hello'")
    Hello
    >>> test("'Hello' 'Paul'")
    'Hello' 'Paul'
    >>> test("1 'Hello' 2")
    1 'Hello' 2
    >>> test("'Hello' (19 20) 'Paul'")
    'Hello' (19 20) 'Paul'
    """
    try:
        cio = apl_cio()
        cio.printResult(evaluate(expr,cio))
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     monadicArithmetic():
    """
    >>> test("+ 'Hello'")
    DOMAIN ERROR
    >>> test("- 'Hello'")
    DOMAIN ERROR
    >>> test("× 'Hello'")
    DOMAIN ERROR
    >>> test("÷ 'Hello'")
    DOMAIN ERROR

    >>> test("⌈ 'Hello'")
    DOMAIN ERROR
    >>> test("⌊ 'Hello'")
    DOMAIN ERROR
    >>> test("| 'Hello'")
    DOMAIN ERROR

    >>> test("* 'Hello'")
    DOMAIN ERROR
    >>> test("⍟ 'Hello'")
    DOMAIN ERROR
    >>> test("? 'Hello'")
    DOMAIN ERROR
    >>> test("! 'Hello'")
    DOMAIN ERROR

    >>> test("⌹ 'Hello'")
    FUNCTION NOT YET IMPLEMENTED
    >>> test("○ 'Hello'")
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     dyadicArithmetic():
    """
    >>> test("1 + 'Hello'")
    DOMAIN ERROR
    >>> test("1 - 'Hello'")
    DOMAIN ERROR
    >>> test("1 × 'Hello'")
    DOMAIN ERROR
    >>> test("1 ÷ 'Hello'")
    DOMAIN ERROR

    >>> test("'Hello' + 1")
    DOMAIN ERROR
    >>> test("'Hello' - 1")
    DOMAIN ERROR
    >>> test("'Hello' × 1")
    DOMAIN ERROR
    >>> test("'Hello' ÷ 1")
    DOMAIN ERROR

    >>> test("1 ⌈ 'Hello'")
    DOMAIN ERROR
    >>> test("1 ⌊ 'Hello'")
    DOMAIN ERROR
    >>> test("1 | 'Hello'")
    DOMAIN ERROR

    >>> test("1 * 'Hello'")
    DOMAIN ERROR
    >>> test("1 ⍟ 'Hello'")
    DOMAIN ERROR
    >>> test("1 ? 'Hello'")
    RANK ERROR
    >>> test("1 ! 'Hello'")
    DOMAIN ERROR

    >>> test("1 ⌹ 'Hello'")
    FUNCTION NOT YET IMPLEMENTED
    >>> test("1 ○ 'Hello'")
    DOMAIN ERROR

    >>> test("1 ∨ 'Hello'")
    DOMAIN ERROR
    >>> test("1 ∧ 'Hello'")
    DOMAIN ERROR
    >>> test("1 ⍱ 'Hello'")
    DOMAIN ERROR
    >>> test("1 ⍲ 'Hello'")
    DOMAIN ERROR

    >>> test("1 < 'Hello'")
    DOMAIN ERROR
    >>> test("1 ≤ 'Hello'")
    DOMAIN ERROR
    >>> test("1 ≥ 'Hello'")
    DOMAIN ERROR
    >>> test("1 > 'Hello'")
    DOMAIN ERROR

    >>> test("1 = 'Hello'")
    0 0 0 0 0
    >>> test("1 ≠ 'Hello'")
    1 1 1 1 1
    >>> test("'Hello' = 'Hello'")
    1 1 1 1 1
    >>> test("'hello' ≠ 'Hello'")
    1 0 0 0 0
    >>> test("'H' = 72")
    1
    >>> test('"H" ≠ 72')
    0
    >>> test("'Hello' = 'Goodbye'")
    LENGTH ERROR
    >>> test("'Hello' ≠ 'Goodbye'")
    LENGTH ERROR
    """
    pass

# ------------------------------

def     tilda():
    """
    >>> test("~ 'Hello'")
    DOMAIN ERROR

    >>> test("1 ~ 'Hello'")
    1
    >>> test("'Hello' ~ 1")
    Hello
    >>> test("'Hello' ~ 'hello'")
    H

    >>> test("'Hello' ~ 'Hello'")
    <BLANKLINE>
    """
    pass

# ------------------------------

def     iota():
    """
    >>> test("⍳ 'Hello'")
    DOMAIN ERROR

    >>> test("1 ⍳ 'Hello'")
    2 2 2 2 2
    >>> test("'Hello' ⍳ 1")
    6
    >>> test("'Hello' ⍳ 'hello'")
    6 2 3 3 5

    >>> test("'Hello' ⍳ 72")
    6
    """
    pass

# ------------------------------

def     rho():
    """
    >>> test("⍴ 'Hello'")
    5
    >>> test("⍴ 'Hello' 'Paul'")
    2
    >>> test("⍴ 1 'Hello' 2")
    3

    >>> test("⍴ 'H'")
    ⍬
    >>> test('⍴ "H"')
    1


    >>> test("4 ⍴ 'Hello'")
    Hell
    >>> test("5 ⍴ 'Hello'")
    Hello
    >>> test("6 ⍴ 'Hello'")
    HelloH
    """
    pass

# ------------------------------

def     comma():
    """
    >>> test(", 'Hello'")
    Hello
    >>> test(", 'Hello' 'Paul'")
    'Hello' 'Paul'
    >>> test(", 1 'Hello' 2")
    1 'Hello' 2

    >>> test(", 'H'")
    H
    >>> test(', "H"')
    H

    >>> test("⍴, 'H'")
    1
    >>> test('⍴, "H"')
    1

    >>> test("'Hello' , ' ' , 'Paul'")
    Hello Paul

    >>> test("1 2 3 , 'Hello'")
    1 2 3 'Hello'
    >>> test("'Hello' , 1 2 3")
    'Hello' 1 2 3
    >>> test("1 2 3 , 'H'")
    1 2 3 'H'
    >>> test('1 2 3 , "H"')
    1 2 3 'H'
    """
    pass

# --------------

def     dropTake():
    """
    >>> test('¯9 ↓ "abcdef"')
    <BLANKLINE>
    >>> test('¯6 ↓ "abcdef"')
    <BLANKLINE>
    >>> test('¯3 ↓ "abcdef"')
    abc
    >>> test('0 ↓ "abcdef"')
    abcdef
    >>> test('3 ↓ "abcdef"')
    def
    >>> test('6 ↓ "abcdef"')
    <BLANKLINE>
    >>> test('9 ↓ "abcdef"')
    <BLANKLINE>

    >>> test('¯9 ↑ "abcdef"')
       abcdef
    >>> test('¯6 ↑ "abcdef"')
    abcdef
    >>> test('¯3 ↑ "abcdef"')
    def
    >>> test('0 ↑ "abcdef"')
    <BLANKLINE>
    >>> test('3 ↑ "abcdef"')
    abc
    >>> test('6 ↑ "abcdef"')
    abcdef
    >>> test('(9 ↑ "abcdef"), "!"')
    abcdef   !

    >>> test('↓ ""')
    <BLANKLINE>
    >>> test('↑ ""')
    <BLANKLINE>
    >>> test('1 ↑ "Hello"')
    H
    >>> test('↑ "Hello"')
    H
    """
    pass

# --------------

def     reverseRotate():
    """
    >>> test('⌽ "niagara"')
    aragain
    >>> test('⊖ "nigeria"')
    airegin

    >>> test('1 ⌽ "nope"')
    open
    >>> test('2 ⊖ "anna"')
    naan

    >>> test('1 ⌽ "a"')
    a
    >>> test('2 ⊖ "b"')
    b

    >>> test('"H" ⌽ "nope"')
    DOMAIN ERROR
    >>> test('"Hi" ⊖ "anna"')
    DOMAIN ERROR
    """
    pass

# --------------

def     transpose():
    """
    >>> test("'H' ⍉ 1 2 3")
    DOMAIN ERROR

    >>> test('⍉ "Hello"')
    Hello

    >>> test('1 ⍉ "Hello"')
    Hello
    """
    pass

# --------------

def     compressExpand():
    """
    >>> test('1 0 1 / "ABC"')
    AC
    >>> test('1 2 3 / "ABC"')
    ABBCCC
    >>> test('1 ¯2 3 / "ABC"')
    A  CCC

    >>> test('1 0 1 0 1 \ "ABC"')
    A B C
    >>> test('1 0 2 0 3 \ "ABC"')
    A BB CCC
    >>> test('¯1 1 ¯2 1 ¯3 1 \ "ABC"')
     A  B   C
    """
    pass

# --------------

def     depthTally():
    """
    >>> test('≡ "Hello"')
    1

    >>> test('≡ 1 "Hello" 3')
    2

    >>> test('≢ "Hello"')
    5

    >>> test('≢ 1 "Hello" 3')
    3
    """
    pass

# --------------

def     matchUnmatch():
    """
    >>> test('"Hello" ≡ "H", "ello"')
    1

    >>> test('"Hello" ≡ "Hello"')
    1

    !>>> test('(1 "Hello" 3) ≡ 1 "Jello" 3')
    0

    !>>> test('(1 "Hello" 3) ≡ 1 "Hello" 3')
    1
    """
    pass

# --------------

def     encodeDecode():
    """
    >>> test('"Hello" ⊤ 17')
    DOMAIN ERROR
    >>> test('16 16 ⊤ "Hello"')
    DOMAIN ERROR
    >>> test('"Hello" ⊥ 1 1')
    DOMAIN ERROR
    >>> test('16 16 ⊥ "Hello"')
    DOMAIN ERROR
    """
    pass

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
