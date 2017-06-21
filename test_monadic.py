#!/usr/bin/python3
"""
    doctest style unit tests for monadic.py

    WIP - grows as operators are implemented monadic.py.

    Each test passes a APL expression to the evaluate function.

    Both positive and negative (e.g. DOMAIN ERROR) cases are tested.

    Many of these expressions exercise the vector calculator.
"""

from apl import evaluate_and_print_expression

from apl_error import APL_exception as apl_exception

# ------------------------------

def     test (expr):
    """
    test both positive and negative outcomes

    >>> test ('⍕ 1')
    FUNCTION NOT YET IMPLEMENTED
    >>> test ('" 1')
    INVALID TOKEN
    """
    try:
        evaluate_and_print_expression(expr)
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

def     monadic_plus ():
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

def     monadic_minus ():
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

def     monadic_times ():
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

def     monadic_divide ():
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

def     monadic_ciel ():
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

def     monadic_floor ():
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

def     monadic_magnitude ():
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

def     monadic_exp ():
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

def     monadic_log ():
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

def     monadic_roll ():
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

def     monadic_factorial ():
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

def     monadic_pi ():
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

def     monadic_negation ():
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

def     monadic_iota ():
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

def     monadic_rho ():
    """
    >>> test('⍴ 7')
    ⍬
    >>> test('⍴ 1 2 3')
    3
    >>> test('⍴ ⍬')
    0
    """
    pass

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
