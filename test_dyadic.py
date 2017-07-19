#!/usr/bin/python3
"""
    doctest style unit tests for dyadic.py

    WIP - grows as operators are implemented in dyadic.py.

    Each test passes a APL expression to the evaluate function.

    Both positive and negative (e.g. DOMAIN ERROR) cases are tested.

    Many of these expressions exercise the vector calculator.
"""

from evaluate import evaluate

from apl_cio import APL_cio as apl_cio
from apl_error import APL_exception as apl_exception

# ------------------------------

def     test (expr):
    """
    test both positive and negative outcomes

    >>> test ('1 ⍕ 1')
    FUNCTION NOT YET IMPLEMENTED
    >>> test ('1 " 1')
    INVALID TOKEN
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

    for ∨ ∧ and |
    >>> test('P10 ← 1 2 3 4 5 6 7 8 9 10')
    1 2 3 4 5 6 7 8 9 10
    >>> test('M10 ← ¯1 ¯2 ¯3 ¯4 ¯5 ¯6 ¯7 ¯8 ¯9 ¯10')
    ¯1 ¯2 ¯3 ¯4 ¯5 ¯6 ¯7 ¯8 ¯9 ¯10
    """
    pass

# ------------------------------

def     dyadic_plus ():
    """
    >>> test('1 + 1')
    2

    >>> test('0 + P')
    0 0.5 1 2
    >>> test('N + 0')
    0 ¯0.5 ¯1 ¯2

    >>> test('P + P')
    0 1 2 4
    >>> test('N + N')
    0 ¯1 ¯2 ¯4
    >>> test('P + N')
    0 0 0 0
    >>> test('N + P')
    0 0 0 0
    """
    pass

# --------------

def     dyadic_minus ():
    """
    >>> test('1 - 1')
    0

    >>> test('0 - P')
    0 ¯0.5 ¯1 ¯2
    >>> test('N - 0')
    0 ¯0.5 ¯1 ¯2

    >>> test('P - P')
    0 0 0 0
    >>> test('N - N')
    0 0 0 0
    >>> test('P - N')
    0 1 2 4
    >>> test('N - P')
    0 ¯1 ¯2 ¯4
    """
    pass

# --------------

def     dyadic_times ():
    """
    >>> test('1 × 1')
    1

    >>> test('1 × P')
    0 0.5 1 2
    >>> test('N × 1')
    0 ¯0.5 ¯1 ¯2

    >>> test('P × P')
    0 0.25 1 4
    >>> test('N × N')
    0 0.25 1 4
    >>> test('P × N')
    0 ¯0.25 ¯1 ¯4
    >>> test('N × P')
    0 ¯0.25 ¯1 ¯4
    """
    pass

# --------------

def     dyadic_divide ():
    """
    >>> test('0 ÷ 0')
    1
    >>> test('1 ÷ 0')
    DOMAIN ERROR
    >>> test('0 ÷ 1')
    0
    >>> test('1 ÷ 1')
    1

    >>> test('1 ÷ PD')
    4 2 1 0.5
    >>> test('ND ÷ 1')
    ¯0.25 ¯0.5 ¯1 ¯2

    >>> test('P ÷ PD')
    0 1 1 1
    >>> test('N ÷ ND')
    0 1 1 1
    >>> test('P ÷ ND')
    0 ¯1 ¯1 ¯1
    >>> test('N ÷ PD')
    0 ¯1 ¯1 ¯1
    """
    pass

# --------------

def     dyadic_maximum ():
    """
    >>> test('1 ⌈ 1')
    1

    >>> test('0 ⌈ PM')
    0.25 0.5 1.9 2.1
    >>> test('NM ⌈ 0')
    0 0 0 0

    >>> test('PM ⌈ PM')
    0.25 0.5 1.9 2.1
    >>> test('NM ⌈ NM')
    ¯0.25 ¯0.5 ¯1.9 ¯2.1
    >>> test('PM ⌈ NM')
    0.25 0.5 1.9 2.1
    >>> test('NM ⌈ PM')
    0.25 0.5 1.9 2.1
    """
    pass

# --------------

def     dyadic_minimum ():
    """
    >>> test('1 ⌊ 1')
    1

    >>> test('0 ⌊ PM')
    0 0 0 0
    >>> test('NM ⌊ 0')
    ¯0.25 ¯0.5 ¯1.9 ¯2.1

    >>> test('PM ⌊ PM')
    0.25 0.5 1.9 2.1
    >>> test('NM ⌊ NM')
    ¯0.25 ¯0.5 ¯1.9 ¯2.1
    >>> test('PM ⌊ NM')
    ¯0.25 ¯0.5 ¯1.9 ¯2.1
    >>> test('NM ⌊ PM')
    ¯0.25 ¯0.5 ¯1.9 ¯2.1
    """
    pass

# --------------

def     dyadic_residue ():
    """
    >>> test('0 | 0')
    0
    >>> test('1 | 1')
    0

    >>> test('0 | PM')
    0.25 0.5 1.9 2.1
    >>> test('NM | 0')
    0 0 0 0

    >>> test('PM | PM')
    0 0 0 0
    >>> test('NM | NM')
    0 0 0 0
    >>> test('PM | NM')
    0 0 0 0
    >>> test('NM | PM')
    0 0 0 0

    >>> test('P10 | 10')
    0 0 1 2 0 4 3 2 1 0
    >>> test('M10 | 10')
    0 0 ¯2 ¯2 0 ¯2 ¯4 ¯6 ¯8 0
    """
    pass

# --------------

def     dyadic_exp ():
    """
    >>> test('0 * ¯1')
    DOMAIN ERROR
    >>> test('¯2 ¯1 0 1 2 * 0')
    1 1 1 1 1

    >>> test('1 * P')
    1 1 1 1
    >>> test('N * 1')
    0 ¯0.5 ¯1 ¯2

    >>> test('P * P')
    1 0.7071067812 1 4
    >>> test('N * N')
    DOMAIN ERROR
    >>> test('P * N')
    1 1.414213562 1 0.25
    >>> test('N * P')
    DOMAIN ERROR
    """
    pass

# --------------

def     dyadic_log ():
    """
    >>> test('0 ⍟ ¯1 0 1')
    0 1 0

    >>> test('1 ⍟ ¯1')
    DOMAIN ERROR
    >>> test('1 ⍟ 0')
    DOMAIN ERROR
    >>> test('1 ⍟ 1')
    1

    >>> test('¯1 ⍟ 0')
    DOMAIN ERROR
    >>> test('¯1 ⍟ ¯1 1')
    1 0

    >>> test('1 ⍟ P')
    DOMAIN ERROR
    >>> test('N ⍟ 1')
    0 0 0 0

    >>> test('P ⍟ P')
    1 1 1 1
    >>> test('N ⍟ N')
    1 1 1 1
    >>> test('P ⍟ N')
    DOMAIN ERROR
    >>> test('N ⍟ P')
    DOMAIN ERROR

    >>> test('2 ⍟ 0.5 2 4 16 256 1024')
    ¯1 1 2 4 8 10
    >>> test('10 ⍟ 0.1 10 1000 1000000')
    ¯1 1 3 6
    """
    pass

# --------------

def     dyadic_deal ():
    """
    randomness makes positive testing a little tricky

    >>> test('1 ? ¯1')
    DOMAIN ERROR
    >>> test('1 ? 0')
    DOMAIN ERROR
    >>> test('1 ? 1')
    1

    >>> test('0.5 ? 2')
    DOMAIN ERROR
    >>> test('1 ? 1.5')
    DOMAIN ERROR

    >>> test('2 ? 1')
    DOMAIN ERROR

    >>> test('1 ? 10 10')
    RANK ERROR
    >>> test('1 1 ? 10')
    RANK ERROR
    """
    pass

# --------------

def     dyadic_combinations ():
    """
    >>> test('¯1 ! ¯1 0 1')
    1 0 0
    >>> test('0 ! ¯1 0 1')
    1 1 1
    >>> test('1 ! ¯1 0 1')
    ¯1 0 1

    >>> test('1 ! P')
    0 0.5 1 2

    > >> test('N ! 1')
    0 ¯0.5 ¯1 ¯2

    >>> test('P ! P')
    1 1 1 1
    >>> test('N ! N')
    1 1 1 1
    >>> test('P ! N')
    1 0 ¯1 3
    >>> test('N ! P')
    1 0.5 0 0

    >>> test('0 1 2 3 4 ! 4')
    1 4 6 4 1
    >>> test('0 1 2 3 4 5 ! 5')
    1 5 10 10 5 1
    """
    pass

# --------------

def     dyadic_trigonometry ():
    """
    Only test values that return real number - ignore the imaginary results for now

    >>> test('B ← ○ ¯2 ¯1.5 ¯1 ¯0.5 0 0.5 1 1.5 2')
    ¯6.283185307 ¯4.71238898 ¯3.141592654 ¯1.570796327 0 1.570796327 3.141592654 4.71238898 6.283185307

    >>> test('1 ○ B')
    2.449293598e¯16 1 ¯1.224646799e¯16 ¯1 0 1 1.224646799e¯16 ¯1 ¯2.449293598e¯16
    >>> test('2 ○ B')
    1 ¯1.836970199e¯16 ¯1 6.123233996e¯17 1 6.123233996e¯17 ¯1 ¯1.836970199e¯16 1
    >>> test('3 ○ B')
    2.449293598e¯16 ¯5.443746451e+15 1.224646799e¯16 ¯1.633123935e+16 0 1.633123935e+16 ¯1.224646799e¯16 5.443746451e+15 ¯2.449293598e¯16

    >>> test('5 ○ B')
    ¯267.744894 ¯55.6543976 ¯11.54873936 ¯2.301298902 0 2.301298902 11.54873936 55.6543976 267.744894
    >>> test('6 ○ B')
    267.7467615 55.66338089 11.59195328 2.509178479 1 2.509178479 11.59195328 55.66338089 267.7467615
    >>> test('7 ○ B')
    ¯0.9999930253 ¯0.999838614 ¯0.9962720762 ¯0.9171523357 0 0.9171523357 0.9962720762 0.999838614 0.9999930253

    !>>> test('¯1 ○ B')
    ¯1.570796327J2.52463066 ¯1.570796327J2.231889253 ¯1.570796327J1.811526272 ¯1.570796327J1.023227479 0 1.570796327J¯1.023227479 1.570796327J¯1.811526272 1.570796327J¯2.231889253 1.570796327J¯2.52463066
    !>>> test('¯2 ○ B')
    3.141592654J2.52463066 3.141592654J2.231889253 3.141592654J1.811526272 3.141592654J1.023227479 1.570796327 0J¯1.023227479 0J¯1.811526272 0J¯2.231889253 0J¯2.52463066
    !>>> test('¯3 ○ B')
    ¯1.412965137 ¯1.361691683 ¯1.262627256 ¯1.003884822 0 1.003884822 1.262627256 1.361691683 1.412965137

    >>> test('¯1 ○ 0')
    0
    >>> test('¯2 ○ 0')
    1.570796327
    >>> test('¯3 ○ B')
    ¯1.412965137 ¯1.361691683 ¯1.262627256 ¯1.003884822 0 1.003884822 1.262627256 1.361691683 1.412965137

    !>>> test('¯5 ○ B')
    ¯2.537297501 ¯2.254414593 ¯1.862295743 ¯1.233403118 0 1.233403118 1.862295743 2.254414593 2.537297501
    !>>> test('¯6 ○ B')
    2.52463066J3.141592654 2.231889253J3.141592654 1.811526272J3.141592654 1.023227479J3.141592654 0J1.570796327 1.023227479 1.811526272 2.231889253 2.52463066
    !>>> test('¯7 ○ B')
    ¯0.1605195575J1.570796327 ¯0.2154808611J1.570796327 ¯0.329765315J1.570796327 ¯0.7524692671J1.570796327 0 0.7524692671J¯1.570796327 0.329765315J¯1.570796327 0.2154808611J¯1.570796327 0.1605195575J¯1.570796327

    >>> test('¯5 ○ B')
    ¯2.537297501 ¯2.254414593 ¯1.862295743 ¯1.233403118 0 1.233403118 1.862295743 2.254414593 2.537297501
    >>> test('¯6 ○ ○ 0.5 1 1.5 2')
    1.023227479 1.811526272 2.231889253 2.52463066
    >>> test('¯7 ○ 0')
    0

    !>>> test('0 ○ B')
    0J6.20309742 0J4.605063507 0J2.978188107 0J1.211363323 1 0J¯1.211363323 0J¯2.978188107 0J¯4.605063507 0J¯6.20309742
    >>> test('0 ○ 0')
    1
    >>> test('4 ○ B')
    6.362265132 4.817323936 3.296908309 1.862095889 1 1.862095889 3.296908309 4.817323936 6.362265132
    >>> test('¯4 ○ B')
    DOMAIN ERROR
    """
    pass

# --------------

def     dyadic_or ():
    """
    >>> test('0 ∨ 0 1')
    0 1
    >>> test('1 ∨ 0 1')
    1 1

    >>> test('P10 ∨ 10')
    1 2 1 2 5 2 1 2 1 10
    >>> test('M10 ∨ 10')
    1 2 1 2 5 2 1 2 1 10
    >>> test('P10 ∨ ¯10')
    1 2 1 2 5 2 1 2 1 10
    >>> test('M10 ∨ ¯10')
    1 2 1 2 5 2 1 2 1 10

    >>> test('7.5 ∨ ¯5 5')
    2.5 2.5
    >>> test('¯7.5 ∨ ¯5 5')
    2.5 2.5
    """
    pass

# --------------

def     dyadic_and ():
    """
    >>> test('0 ∧ 0 1')
    0 0
    >>> test('1 ∧ 0 1')
    0 1

    >>> test('P10 ∧ 10')
    10 10 30 20 10 30 70 40 90 10
    >>> test('M10 ∧ 10')
    ¯10 ¯10 ¯30 ¯20 ¯10 ¯30 ¯70 ¯40 ¯90 ¯10
    >>> test('P10 ∧ ¯10')
    ¯10 ¯10 ¯30 ¯20 ¯10 ¯30 ¯70 ¯40 ¯90 ¯10
    >>> test('M10 ∧ ¯10')
    10 10 30 20 10 30 70 40 90 10

    >>> test('7.5 ∧ ¯5 5')
    ¯15 15
    >>> test('¯7.5 ∧ ¯5 5')
    15 ¯15
    """
    pass

# --------------

def     dyadic_nor ():
    """
    >>> test('0 ⍱ ¯1')
    DOMAIN ERROR
    >>> test('¯1 ⍱ 0')
    DOMAIN ERROR
    >>> test('0 ⍱ 0 1')
    1 0
    >>> test('1 ⍱ 0 1')
    0 0
    >>> test('0.5 ⍱ 0')
    DOMAIN ERROR
    >>> test('1 ⍱ 0.5')
    DOMAIN ERROR
    """
    pass

# --------------

def     dyadic_nand ():
    """
    >>> test('0 ⍲ ¯1')
    DOMAIN ERROR
    >>> test('¯1 ⍲ 0')
    DOMAIN ERROR
    >>> test('0 ⍲ 0 1')
    1 1
    >>> test('1 ⍲ 0 1')
    1 0
    >>> test('0.5 ⍲ 0')
    DOMAIN ERROR
    >>> test('1 ⍲ 0.5')
    DOMAIN ERROR
    """
    pass

# --------------

def     dyadic_compare ():
    """
    >>> test('AC ← ¯0.5 ¯0.5 0.5 0.5')
    ¯0.5 ¯0.5 0.5 0.5
    >>> test('BC ← ¯0.5 0.5 ¯0.5 0.5')
    ¯0.5 0.5 ¯0.5 0.5

    >>> test('AC < BC')
    0 1 0 0
    >>> test('AC ≤ BC')
    1 1 0 1
    >>> test('AC = BC')
    1 0 0 1
    >>> test('AC ≥ BC')
    1 0 1 1
    >>> test('AC > BC')
    0 0 1 0
    >>> test('AC ≠ BC')
    0 1 1 0

    >>> test('AC ← AC + ⎕CT')
    ¯0.5 ¯0.5 0.5 0.5
    >>> test('BC ← BC - ⎕CT')
    ¯0.5 0.5 ¯0.5 0.5

    >>> test('AC = BC')
    0 0 0 0
    >>> test('AC ≠ BC')
    1 1 1 1

    >>> test('AC ← AC + 10')
    9.5 9.5 10.5 10.5
    >>> test('BC ← BC + 10')
    9.5 10.5 9.5 10.5

    >>> test('AC < BC')
    0 1 0 0
    >>> test('AC ≤ BC')
    1 1 0 1
    >>> test('AC = BC')
    1 0 0 1
    >>> test('AC ≥ BC')
    1 0 1 1
    >>> test('AC > BC')
    0 0 1 0
    >>> test('AC ≠ BC')
    0 1 1 0
    """
    pass

# --------------

def     dyadic_without ():
    """
    >>> test('1 ~ 1')
    ⍬
    >>> test('1 ~ 0')
    1

    >>> test('1 5 2 4 3 ~ ⍬')
    1 5 2 4 3
    >>> test('1 5 2 4 3 ~ 2')
    1 5 4 3
    >>> test('1 5 2 4 3 ~ 2 2')
    1 5 4 3

    >>> test('1 2 3 4 5 ~ 5 4 3 2 1')
    ⍬
    >>> test('2 2 2 2 2 ~ 2 2')
    ⍬
    >>> test('2 2 2 2 2 ~ 3 6 9')
    2 2 2 2 2
    """
    pass

# --------------

def     dyadic_iota ():
    """
    >>> test('⎕IO ← 1')
    1
    >>> test('1 ⍳ 1')
    1
    >>> test('1 ⍳ 0')
    2

    >>> test('⎕IO ← 0')
    0
    >>> test('1 ⍳ 1')
    0
    >>> test('1 ⍳ 0')
    1

    >>> test('⎕IO ← 1')
    1
    >>> test('1 5 2 4 3 ⍳ 2')
    3
    >>> test('1 5 2 4 3 ⍳ 1 2 3 4 5')
    1 3 5 4 2

    >>> test('⎕IO ← 0')
    0
    >>> test('1 5 2 4 3 ⍳ 2')
    2
    >>> test('1 5 2 4 3 ⍳ 1 2 3 4 5')
    0 2 4 3 1

    >>> test('⎕IO ← 1')
    1
    >>> test('2 2 2 2 2 ⍳ 2 2')
    1 1
    >>> test('2 2 2 2 2 ⍳ 3 6 9')
    6 6 6
    """
    pass

# --------------

def     dyadic_rho ():
    """
    >>> test('1 ⍴ 0')
    0
    >>> test('⍴ 1 ⍴ 0')
    1

    >>> test('8 ⍴ ⍳ 4')
    1 2 3 4 1 2 3 4
    >>> test('8 ⍴ ⍳ 8')
    1 2 3 4 5 6 7 8
    >>> test('8 ⍴ ⍳ 16')
    1 2 3 4 5 6 7 8

    >>> test('3 ⍴ ⍳ 4')
    1 2 3
    >>> test('4 ⍴ ⍳ 4')
    1 2 3 4
    >>> test('5 ⍴ ⍳ 4')
    1 2 3 4 1

    >>> test('1 2 ⍴ 1 2 ')
    RANK ERROR
    """
    pass

# --------------

def     dyadic_comma ():
    """
    >>> test('1 , 0')
    1 0
    >>> test('⍴ 1 , 0')
    2

    >>> test('0 1, 2')
    0 1 2
    >>> test('0, 1 2')
    0 1 2
    >>> test('0 1, 2 3')
    0 1 2 3
    """
    pass

# --------------

def     dyadic_drop_take ():
    """
    >>> test('3 ↓ 1 2 3 4 5 6')
    4 5 6
    >>> test('¯3 ↓ 1 2 3 4 5 6')
    1 2 3
    >>> test('0 ↓ 1 2 3 4 5 6')
    1 2 3 4 5 6
    >>> test('3 ↓ 1 2 3')
    ⍬
    >>> test('¯3 ↓ 1 2 3')
    ⍬
    >>> test('6 ↓ 1 2 3')
    ⍬
    >>> test('¯6 ↓ 1 2 3')
    ⍬

    >>> test('3.3 ↓ 1 2 3 4 5 6')
    DOMAIN ERROR
    >>> test('3 3 ↓ 1 2 3 4 5 6')
    LENGTH ERROR

    >>> test('3 ↑ 1 2 3 4 5 6')
    1 2 3
    >>> test('¯3 ↑ 1 2 3 4 5 6')
    4 5 6
    >>> test('0 ↑ 1 2 3 4 5 6')
    ⍬
    >>> test('3 ↑ 1 2 3')
    1 2 3
    >>> test('¯3 ↑ 1 2 3')
    1 2 3
    >>> test('6 ↑ 1 2 3')
    1 2 3 0 0 0
    >>> test('¯6 ↑ 1 2 3')
    0 0 0 1 2 3

    >>> test('3.3 ↑ 1 2 3 4 5 6')
    DOMAIN ERROR
    >>> test('3 3 ↑ 1 2 3 4 5 6')
    LENGTH ERROR
    """
    pass

# --------------

def     dyadic_rotate ():
    """
    >>> test('1 ⌽ 1 2 3 4 5 6')
    2 3 4 5 6 1
    >>> test('2 ⊖ 1 2 3 4 5 6')
    3 4 5 6 1 2

    >>> test('¯1 ⌽ 1 2 3 4 5 6')
    6 1 2 3 4 5
    >>> test('¯2 ⊖ 1 2 3 4 5 6')
    5 6 1 2 3 4

    >>> test('6 ⌽ 1 2 3 4 5 6')
    1 2 3 4 5 6
    >>> test('0 ⊖ 1 2 3 4 5 6')
    1 2 3 4 5 6
    >>> test('¯6 ⌽ 1 2 3 4 5 6')
    1 2 3 4 5 6

    >>> test('7 ⌽ 1 2 3 4 5 6')
    2 3 4 5 6 1
    >>> test('¯7 ⊖ 1 2 3 4 5 6')
    6 1 2 3 4 5

    >>> test('1 ⌽ 3')
    3
    >>> test('2 ⊖ 3')
    3

    >>> test('1 2 ⊖ 1 2 3 4 5 6')
    RANK ERROR
    >>> test('1.5 ⊖ 1 2 3 4 5 6')
    DOMAIN ERROR
    """
    pass

# --------------

def     dyadic_union_intersection ():
    """
    >>> test('1 2 3 ∩ 3 2 1')
    1 2 3
    >>> test('1 2 3 ∩ 6 5 4')
    ⍬
    >>> test('1 1 1 ∩ 1')
    1 1 1
    >>> test('1 ∩ 1 1 1')
    1

    >>> test('1 2 3 ∪ 6 5 4')
    1 2 3 6 5 4
    >>> test('1 2 3 ∪ 3 2 1')
    1 2 3
    >>> test('1 1 1 ∪ 1')
    1 1 1
    >>> test('1 ∪ 1 1 1')
    1

    >>> test('"Hi" ∩ "Hello"')
    H
    >>> test('"Hi" ∪ "Hello"')
    Hiello
    >>> test('"ll" ∩ "Hello"')
    ll
    >>> test('"ll" ∪ "Hello"')
    llHeo
    >>> test('"l" ∩ "Hello"')
    l
    >>> test('"l" ∪ "Hello"')
    lHeo

    !!! test('"Hi" ∩ 1 2 3')
    ⍬
    !!! test('"Hi" ∪ 1 2 3')
    "Hi" 1 2 3

    """
    pass

# --------------

def     dyadic_transpose ():
    """
    >>> test('1 ⍉ 1 2 3')
    1 2 3

    >>> test('2 ⍉ 1 2 3')
    DOMAIN ERROR
    >>> test('0 ⍉ 1 2 3')
    DOMAIN ERROR

    >>> test('1 1 ⍉ 1 2 3')
    LENGTH ERROR
    >>> test('1 2 3 ⍉ 1 2 3')
    LENGTH ERROR
    >>> test('1 ⍉ 10')
    LENGTH ERROR
    >>> test('1 ⍉ ,10')
    10
    """
    pass

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
