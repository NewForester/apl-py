#!/usr/bin/python3
"""
    doctest style unit tests for APL strings

    WIP - grows as more functions are implemented.

    The tests in this module exercise monadic and dyadic functions with

        either one or two string operands

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
    >>> test(r"+ 'H'")
    DOMAIN ERROR
    >>> test(r"+ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 + 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' + 1")
    DOMAIN ERROR
    >>> test(r"'Hello' + 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 + 'one'")
    DOMAIN ERROR
    >>> test(r"'one' + 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"- 'H'")
    DOMAIN ERROR
    >>> test(r"- 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 - 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' - 1")
    DOMAIN ERROR
    >>> test(r"'Hello' - 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 - 'one'")
    DOMAIN ERROR
    >>> test(r"'one' - 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"× 'H'")
    DOMAIN ERROR
    >>> test(r"× 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 × 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' × 1")
    DOMAIN ERROR
    >>> test(r"'Hello' × 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 × 'one'")
    DOMAIN ERROR
    >>> test(r"'one' × 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"÷ 'H'")
    DOMAIN ERROR
    >>> test(r"÷ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ÷ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ÷ 1")
    DOMAIN ERROR
    >>> test(r"'Hello' ÷ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 ÷ 'one'")
    DOMAIN ERROR
    >>> test(r"'one' ÷ 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     ceil_maximum():
    """
    >>> test(r"⌈ 'H'")
    DOMAIN ERROR
    >>> test(r"⌈ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ⌈ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⌈ 1")
    DOMAIN ERROR
    >>> test(r"'Hello' ⌈ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 ⌈ 'one'")
    DOMAIN ERROR
    >>> test(r"'one' ⌈ 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"⌊ 'H'")
    DOMAIN ERROR
    >>> test(r"⌊ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ⌊ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⌊ 1")
    DOMAIN ERROR
    >>> test(r"'Hello' ⌊ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 ⌊ 'one'")
    DOMAIN ERROR
    >>> test(r"'one' ⌊ 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"| 'H'")
    DOMAIN ERROR
    >>> test(r"| 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 | 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' | 1")
    DOMAIN ERROR
    >>> test(r"'Hello' | 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 | 'one'")
    DOMAIN ERROR
    >>> test(r"'one' | 1 2 3")
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"* 'H'")
    DOMAIN ERROR
    >>> test(r"* 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 * 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' * 1")
    DOMAIN ERROR
    >>> test(r"'Hello' * 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 * 'one'")
    DOMAIN ERROR
    >>> test(r"'one' * 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"⍟ 'H'")
    DOMAIN ERROR
    >>> test(r"⍟ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ⍟ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⍟ 1")
    DOMAIN ERROR
    >>> test(r"'Hello' ⍟ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 ⍟ 'one'")
    DOMAIN ERROR
    >>> test(r"'one' ⍟ 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"! 'H'")
    DOMAIN ERROR
    >>> test(r"! 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ! 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ! 1")
    DOMAIN ERROR
    >>> test(r"'Hello' ! 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 ! 'one'")
    DOMAIN ERROR
    >>> test(r"'one' ! 1 2 3")
    DOMAIN ERROR
    """
    pass

# --------------

def     roll_deal():
    """
    >>> test(r"? 'H'")
    DOMAIN ERROR
    >>> test(r"? 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ? 'Hello'")
    RANK ERROR
    >>> test(r"'Hello' ? 1")
    RANK ERROR
    >>> test(r"'Hello' ? 'Hello'")
    RANK ERROR

    >>> test(r"1 2 3 ? 'one'")
    RANK ERROR
    >>> test(r"'one' ? 1 2 3")
    RANK ERROR
    """
    pass

# ------------------------------

def     pi_circular():
    """
    >>> test(r"○ 'H'")
    DOMAIN ERROR
    >>> test(r"○ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 ○ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ○ 1")
    DOMAIN ERROR
    >>> test(r"'Hello' ○ 'Hello'")
    DOMAIN ERROR

    >>> test(r"1 2 3 ○ 'one'")
    DOMAIN ERROR
    >>> test(r"'one' ○ 1 2 3")
    DOMAIN ERROR

    >>> test(r"'Hello' ○ 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     or_gcd():
    """
    >>> test(r"∨ 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' ∨ 72")
    DOMAIN ERROR
    >>> test(r'"H" ∨ 72')
    DOMAIN ERROR

    >>> test(r"'Hello' ∨ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ∨ 1")
    DOMAIN ERROR
    >>> test(r"1 ∨ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ∨ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ∨ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ∨ 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"∧ 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' ∧ 72")
    DOMAIN ERROR
    >>> test(r'"H" ∧ 72')
    DOMAIN ERROR

    >>> test(r"'Hello' ∧ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ∧ 1")
    DOMAIN ERROR
    >>> test(r"1 ∧ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ∧ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ∧ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ∧ 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"⍱ 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' ⍱ 72")
    DOMAIN ERROR
    >>> test(r'"H" ⍱ 72')
    DOMAIN ERROR

    >>> test(r"'Hello' ⍱ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⍱ 1")
    DOMAIN ERROR
    >>> test(r"1 ⍱ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ⍱ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ⍱ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ⍱ 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"⍲ 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' ⍲ 72")
    DOMAIN ERROR
    >>> test(r'"H" ⍲ 72')
    DOMAIN ERROR

    >>> test(r"'Hello' ⍲ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ⍲ 1")
    DOMAIN ERROR
    >>> test(r"1 ⍲ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ⍲ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ⍲ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ⍲ 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"< 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' < 72")
    DOMAIN ERROR
    >>> test(r'"H" < 72')
    DOMAIN ERROR

    >>> test(r"'Hello' < 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' < 1")
    DOMAIN ERROR
    >>> test(r"1 < 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' < 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 < 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' < 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# --------------

def     le():
    """
    >>> test(r"≤ 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' ≤ 72")
    DOMAIN ERROR
    >>> test(r'"H" ≤ 72')
    DOMAIN ERROR

    >>> test(r"'Hello' ≤ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ≤ 1")
    DOMAIN ERROR
    >>> test(r"1 ≤ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ≤ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ≤ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ≤ 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"≥ 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' ≥ 72")
    DOMAIN ERROR
    >>> test(r'"H" ≥ 72')
    DOMAIN ERROR

    >>> test(r"'Hello' ≥ 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' ≥ 1")
    DOMAIN ERROR
    >>> test(r"1 ≥ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ≥ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ≥ 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' ≥ 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# --------------

def     gt():
    """
    >>> test(r"> 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' > 72")
    DOMAIN ERROR
    >>> test(r'"H" > 72')
    DOMAIN ERROR

    >>> test(r"'Hello' > 'Hello'")
    DOMAIN ERROR
    >>> test(r"'Hello' > 1")
    DOMAIN ERROR
    >>> test(r"1 > 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' > 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 > 'Hello'")
    DOMAIN ERROR

    >>> test(r"'Hello' > 'Goodbye'")
    DOMAIN ERROR
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"= 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' = 72")
    0
    >>> test(r"⍴ 'H' = 72")
    ⍬
    >>> test(r'"H" = 72')
    0
    >>> test(r'⍴ "H" = 72')
    1

    >>> test(r"'Hello' = 'Hello'")
    1 1 1 1 1
    >>> test(r"'Hello' = 1")
    0 0 0 0 0
    >>> test(r"1 = 'Hello'")
    0 0 0 0 0

    >>> test(r"'Hello' = 'hello'")
    0 1 1 1 1

    >>> test(r"'Hello' = 1 2 3", True)
    LENGTH ERROR
    >>> test(r"1 2 3 = 'Hello'", True)
    LENGTH ERROR

    >>> test(r"'Hello' = 'Goodbye'", True)
    LENGTH ERROR
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"≠ 'Hello'")
    VALENCE ERROR

    >>> test(r"'H' ≠ 72")
    1
    >>> test(r"⍴ 'H' ≠ 72")
    ⍬
    >>> test(r'"H" ≠ 72')
    1
    >>> test(r'⍴ "H" ≠ 72')
    1

    >>> test(r"'Hello' ≠ 'Hello'")
    0 0 0 0 0
    >>> test(r"'Hello' ≠ 1")
    1 1 1 1 1
    >>> test(r"1 ≠ 'Hello'")
    1 1 1 1 1

    >>> test(r"'Hello' ≠ 'hello'")
    1 0 0 0 0

    >>> test(r"'Hello' ≠ 1 2 3", True)
    LENGTH ERROR
    >>> test(r"1 2 3 ≠ 'Hello'", True)
    LENGTH ERROR

    >>> test(r"'Hello' ≠ 'Goodbye'", True)
    LENGTH ERROR
    """
    pass

# ------------------------------

def     depth_match():
    """
    >>> test(r"≡ ''")
    1
    >>> test(r"≡ ' '")
    0
    >>> test(r"≡ 'Hello'")
    1
    >>> test(r"≡ 'H' 'ello'")
    2

    >>> test(r"'Hello' ≡ 'Hello'")
    1
    >>> test(r"'Hello' ≡ 'H', 'ello'")
    1
    >>> test(r"'Hello' ≡ 'J', 'Hello'")
    0

    >>> test(r"'Hello' ≡ 1.2")
    0
    >>> test(r"1.2 ≡ 'Hello'")
    0

    >>> test(r"'Hello' ≡ 1 2 3")
    0
    >>> test(r"1 2 3 ≡ 'Hello'")
    0
    """
    pass

# --------------

def     tally_notMatch():
    """
    >>> test(r"≢ ''")
    0
    >>> test(r"≢ ' '")
    1
    >>> test(r"≢ 'Hello'")
    5
    >>> test(r"≢ 'H' 'ello'")
    2

    >>> test(r"'Hello' ≢ 'Hello'")
    0
    >>> test(r"'Hello' ≢ 'H', 'ello'")
    0
    >>> test(r"'Hello' ≢ 'J', 'Hello'")
    1

    >>> test(r"'Hello' ≢ 1.2")
    1
    >>> test(r"1.2 ≢ 'Hello'")
    1

    >>> test(r"'Hello' ≢ 1 2 3")
    1
    >>> test(r"1 2 3 ≢ 'Hello'")
    1
    """
    pass

# ------------------------------

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
    1 2 3 Hello
    >>> test(r"'Hello' , 1 2 3")
    Hello 1 2 3
    >>> test(r"1 2 3 , 'H'")
    1 2 3 H
    >>> test(r'1 2 3 , "H"')
    1 2 3 H
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
    ''
    """
    pass

# --------------

def     stringIota():
    """
    >>> test(r"⍳ 'Hello'")
    DOMAIN ERROR

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"1 ⍳ 'Hello'")
    2 2 2 2 2
    >>> test(r"'Hello' ⍳ 1")
    6
    >>> test(r"'Hello' ⍳ 'hello'")
    6 2 3 3 5

    >>> test(r"'Hello' ⍳ 72")
    6

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     stringDrop():
    """
    >>> test(r'↓ ""')
    ''
    >>> test(r"↓ 'Hello'")
    ello
    >>> test(r"1 ↓ 'Hello'")
    ello

    >>> test(r"¯9 ↓ 'abcdef'")
    ''
    >>> test(r"¯6 ↓ 'abcdef'")
    ''
    >>> test(r"¯3 ↓ 'abcdef'")
    abc
    >>> test(r"0 ↓ 'abcdef'")
    abcdef
    >>> test(r"3 ↓ 'abcdef'")
    def
    >>> test(r"6 ↓ 'abcdef'")
    ''
    >>> test(r"9 ↓ 'abcdef'")
    ''
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
    ''

    >>> test(r"¯9 ↑ 'abcdef'")
       abcdef
    >>> test(r"¯6 ↑ 'abcdef'")
    abcdef
    >>> test(r"¯3 ↑ 'abcdef'")
    def
    >>> test(r"0 ↑ 'abcdef'")
    ''
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
    preamble()
    import doctest
    doctest.testmod()

# EOF
