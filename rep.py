"""
    The top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version supports strict right-to-left evaluation of monadic and dyadic functions
"""

import sys
import re

from monadic import monadic_function
from dyadic import dyadic_function

from apl_exception import APL_Exception as apl_exception

# ------------------------------

_reNumber = re.compile(r'[0-9]*\.?[0-9]*([eE][-+]?[0-9]+)?')

# ------------------------------

def     evaluate(expression):
    """
    Evaluate an APL expression

        - strict right-to-left evaluation of
        - sequences of monadic and dyadic functions
        - without parentheses to alter the order of evaluation
    """

    try:
        lhs = None

        if not expression:
            return lhs

        # try a number

        match = _reNumber.match(expression)
        if match:
            number = match.group(0)
            if number:
                lhs = float(number)
                expression = expression[len(number):].lstrip()

        if not expression:
            return lhs

        if lhs is None:
            # try a monadic function

            function = monadic_function(expression)
            rhs = evaluate(expression[1:].lstrip())
            return function(rhs)
        else:
            # try a dyadic function

            function = dyadic_function(expression)
            rhs = evaluate(expression[1:].lstrip())
            return function(lhs,rhs)

    except apl_exception as e:
        if not e.line:
           e.line = expression
        raise (e)

# ------------------------------

def     read_evaluate_print (prompt):
    """
    Read input, echo input
    """
    try:
        while True:
            print(end=prompt)
            line = input().lstrip()
            if line:
                if line[0] == ')':
                    if line[0:4].upper() == ')OFF':
                        apl_exit("Bye bye")

            result = None
            try:
                result = evaluate(line)
                if result is not None:
                    print('⎕ {:g}'.format(result))
            except apl_exception as e:
                print(' '*(len(prompt)+len(line)-len(e.line)),end="^\n")
                print('⎕ {:s}'.format(e.message))

    except EOFError:
        apl_exit(None)

# ------------------------------

def     apl_quit ():
    """
    Quit without clean up
    """
    print()
    sys.exit(0)

# ------------------------------

def     apl_exit (message):
    """
    Clean up and quit
    """
    if message is None:
        print()
    else:
        print(message)
    sys.exit(0)

# EOF
