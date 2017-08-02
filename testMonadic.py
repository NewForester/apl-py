#!/usr/bin/python3
"""
    doctest style unit tests for monadic.py

    WIP - grows as operators are implemented monadic.py.

    Each test passes a APL expression to the evaluate function.

    Both positive and negative (e.g. DOMAIN ERROR) cases are tested.

    Many of these expressions exercise the vector calculator.
"""

from evaluate import evaluate

from apl_cio import APL_cio as apl_cio
from apl_error import APL_exception as apl_exception

# ------------------------------

def     test(expr):
    """
    test both positive and negative outcomes

    >>> test ('⍕ 1')
    FUNCTION NOT YET IMPLEMENTED
    >>> test ('" 1')
    INVALID TOKEN

    >>> test('∨ 0')
    VALENCE ERROR
    >>> test('∧ 0')
    VALENCE ERROR
    >>> test('⍱ 0')
    VALENCE ERROR
    >>> test('⍲ 0')
    VALENCE ERROR

    >>> test('< 0')
    VALENCE ERROR
    >>> test('≤ 0')
    VALENCE ERROR
    >>> test('= 0')
    VALENCE ERROR
    >>> test('≥ 0')
    VALENCE ERROR
    >>> test('> 0')
    VALENCE ERROR
    >>> test('≠ 0')
    VALENCE ERROR

    >>> test('⍪ 0')
    VALENCE ERROR
    >>> test('⍷ 0')
    VALENCE ERROR
    >>> test('∩ 0')
    VALENCE ERROR

    >>> test('\\ 0')
    VALENCE ERROR
    >>> test('/ 0')
    VALENCE ERROR
    >>> test('⍀ 0')
    VALENCE ERROR
    >>> test('⌿ 0')
    VALENCE ERROR

    >>> test('⊤ 0')
    VALENCE ERROR
    >>> test('⊥ 0')
    VALENCE ERROR
"""
    try:
        cio = apl_cio()
        cio.printResult(evaluate(expr,cio))
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     aardvark ():
    """
    so named to ensure it is run first

    for + - and ×
    >>> test('P ← 0 0.5 1 2')
    0 0.5 1 2
    >>> test('N ← ¯0 ¯0.5 ¯1 ¯2')
    0 ¯0.5 ¯1 ¯2

    for ÷
    >>> test('PD ← 0.25 0.5 1 2')
    0.25 0.5 1 2
    >>> test('ND ← ¯0.25 ¯0.5 ¯1 ¯2')
    ¯0.25 ¯0.5 ¯1 ¯2

    for ⌈ ⌊ and |
    >>> test('PM ← 0.25 0.5 1.9 2.1')
    0.25 0.5 1.9 2.1
    >>> test('NM ← ¯0.25 ¯0.5 ¯1.9 ¯2.1')
    ¯0.25 ¯0.5 ¯1.9 ¯2.1
    """
    pass

# ------------------------------

def     monadicPlus():
    """
    >>> test('+ 0')
    0

    >>> test('+ P')
    0 0.5 1 2
    >>> test('+ N')
    0 ¯0.5 ¯1 ¯2
    """
    pass

# --------------

def     monadicMinus():
    """
    >>> test('- 0')
    0

    >>> test('- P')
    0 ¯0.5 ¯1 ¯2
    >>> test('- N')
    0 0.5 1 2
    """
    pass

# --------------

def     monadicTimes():
    """
    >>> test('× 0')
    0

    >>> test('× P')
    0 1 1 1
    >>> test('× N')
    0 ¯1 ¯1 ¯1
    """
    pass

# --------------

def     monadicDivide():
    """
    >>> test('÷ 0')
    DOMAIN ERROR
    >>> test('÷ 1')
    1

    >>> test('÷ PD')
    4 2 1 0.5
    >>> test('÷ ND')
    ¯4 ¯2 ¯1 ¯0.5
    """
    pass

# --------------

def     monadicCiel():
    """
    >>> test('⌈ 0')
    0

    >>> test('⌈ PM')
    1 1 2 3
    >>> test('⌈ NM')
    0 0 ¯1 ¯2
    """
    pass

# --------------

def     monadicFloor():
    """
    >>> test('⌊ 0')
    0

    >>> test('⌊ PM')
    0 0 1 2
    >>> test('⌊ NM')
    ¯1 ¯1 ¯2 ¯3
    """
    pass

# --------------

def     monadicMagnitude():
    """
    >>> test('| 0')
    0

    >>> test('| PM')
    0.25 0.5 1.9 2.1
    >>> test('| NM')
    0.25 0.5 1.9 2.1
    """
    pass

# --------------

def     monadicExponential():
    """
    >>> test('* 1 0 ¯1')
    2.718281828 1 0.3678794412

    >>> test('* 1 2 3 4 5')
    2.718281828 7.389056099 20.08553692 54.59815003 148.4131591

    >>> test('* ¯1 ¯2 ¯3 ¯4 ¯5')
    0.3678794412 0.1353352832 0.04978706837 0.01831563889 0.006737946999

    >>> test('* 0.125 0.25 0.5')
    1.133148453 1.284025417 1.648721271
    """
    pass

# --------------

def     monadicLogarithm():
    """
    >>> test('⍟ 0')
    DOMAIN ERROR
    >>> test('⍟ -1')
    DOMAIN ERROR

    >>> test('⍟ 2.718281828459045 1.0 0.36787944117144233')
    1 0 ¯1

    >>> test('⍟ 1 2 3 4 5')
    0 0.6931471806 1.098612289 1.386294361 1.609437912

    >>> test('⍟ 0.125 0.25 0.5')
    ¯2.079441542 ¯1.386294361 ¯0.6931471806
    """
    pass

# --------------

def     monadicRoll():
    """
    randomness makes positive testing a little tricky

    >>> test('? 0')
    DOMAIN ERROR
    >>> test('? -1')
    DOMAIN ERROR
    >>> test('? 1')
    1
    >>> test('? 1÷2')
    DOMAIN ERROR
    """
    pass

# --------------

def     monadicFactorial():
    """
    >>> test('! -1')
    DOMAIN ERROR
    >>> test('! 0')
    1
    >>> test('! 1 2 3 4 5')
    1 2 6 24 120
    >>> test('! 0.125 0.25 0.5')
    0.9417426998 0.9064024771 0.8862269255
    """
    pass

# --------------

def     monadicPi():
    """
    >>> test('○ ¯1 0 1')
    ¯3.141592654 0 3.141592654
    >>> test('○ ¯0.5 0.5')
    ¯1.570796327 1.570796327
    >>> test('○ ¯2 2')
    ¯6.283185307 6.283185307
    """
    pass

# --------------

def     monadicNegation():
    """
    >>> test('~ ¯1')
    DOMAIN ERROR
    >>> test('~ 0 1')
    1 0
    >>> test('~ 0.5')
    DOMAIN ERROR
    """
    pass

# --------------

def     monadicIota():
    """
    >>> test('⍳ 0')
    ⍬
    >>> test('⍳ 1')
    1
    >>> test('⍳ 2')
    1 2
    >>> test('⍳ 3.142')
    DOMAIN ERROR
    >>> test('⍳ 1 1')
    RANK ERROR
    """
    pass

# --------------

def     monadicRho():
    """
    >>> test('⍴ 7')
    ⍬
    >>> test('⍴ 1 2 3')
    3
    >>> test('⍴ ⍬')
    0
    """
    pass

# --------------

def     monadicComma():
    """
    >>> test(', 7')
    7
    >>> test(', 1 2 3')
    1 2 3

    >>> test('⍴ , 7')
    1
    >>> test('⍴ , 1 2 3')
    3
    """
    pass

# --------------

def     monadicDropTake():
    """
    >>> test('↓ 1 2 3')
    2 3
    >>> test('↓ 0.1 0.2 0.3')
    0.2 0.3
    >>> test('↓ ¯1 ¯2 ¯3')
    ¯2 ¯3

    >>> test('↑ 1 2 3')
    1
    >>> test('↑ 0.1 0.2 0.3')
    0.1
    >>> test('↑ ¯1 ¯2 ¯3')
    ¯1
    """
    pass

# --------------

def     monadicReverse():
    """
    >>> test('⌽ 1 2 3')
    3 2 1
    >>> test('⊖ 0.1 0.2 0.3')
    0.3 0.2 0.1

    >>> test('⌽ 2')
    2
    >>> test('⊖ 0.2')
    0.2
    """
    pass

# --------------

def     monadicUnique():
    """
    >>> test('∪ 0')
    0

    >>> test('∪ 0 1 0 1 0 1')
    0 1
    """
    pass

# --------------

def     monadicTranspose():
    """
    >>> test('⍉ 0')
    0
    >>> test('⍉ 1 2 3')
    1 2 3
    """
    pass


# --------------

def     monadicDepthTally():
    """
    >>> test('≡ 1')
    0

    >>> test('≡ 1 2 3')
    1

    >>> test('≢ 1')
    1

    >>> test('≢ 1 2 3')
    3
    """
    pass

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
