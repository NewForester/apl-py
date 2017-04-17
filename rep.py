"""
    The top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version supports expressions with parentheses

    It also recognises strings.  For now, those in apostrophes evaluate to 0 and those in quotes to 1

    It also recognises names.  For now, ordinary names evaluate to 2, system variable names to 3 and system command names to 4.
"""

import sys
import re

from monadic import monadic_function
from dyadic import dyadic_function

from apl_exception import APL_Exception as apl_exception

# ------------------------------

_reNumber = re.compile(r'¯?[0-9]*\.?[0-9]*([eE][-+¯]?[0-9]+)?')
_reName   = re.compile(r'[A-Za-z][A-Z_a-z0-9]*')

_reAposString = re.compile(r"'([^']|'')*'")
_reQuotString = re.compile(r'"([^"]|"")*"')

# ------------------------------

def     print_result (result):
    if result is not None:
        print('{:g}'.format(result).replace('-','¯'))

# ------------------------------

def     expression_within_parentheses (expr,opos,cpos):
    """
    Find expression in parentheses

    Raises SYNTAX ERROR (closing parenthesis missing)
    """
    pos = expr[cpos + 1:].find(')')
    if pos == -1:
        raise (apl_exception("SYNTAX ERROR"))
    cpos += pos + 1

    pos = expr[opos + 1:cpos].find('(')
    if pos == -1:
        return expr[:cpos + 1]
    opos += pos + 1

    return expression_within_parentheses(expr,opos,cpos)

# ------------------------------

def     evaluate(expression):
    """
    Evaluate an APL expression

        - strict right-to-left evaluation of
        - sequences of monadic and dyadic functions
        - with parentheses to alter the order of evaluation
        - strings and names recognised
    """

    try:
        lhs = None

        if not expression:
            return lhs

        if expression[0] == '(':
            # try expression in parentheses

            subexpression = expression_within_parentheses(expression,0,0)
            lhs = evaluate(subexpression[1:-1])
            expression = expression[len(subexpression):].lstrip()

        elif expression[0].isalpha():
            # try a name (user defined variable or function)

            match = _reName.match(expression)
            if match:
                name = match.group(0)
                if name:
                    print(name)
                    lhs = 2
                    expression = expression[len(name):].lstrip()

        elif expression[0] == '⎕':
            # try a system variable name

            match = _reName.match(expression[1:])
            if match:
                name = match.group(0)
                if name:
                    print(name)
                    lhs = 3
                    expression = expression[len(name)+1:].lstrip()

        elif expression[0] == ')':
            # try a system command name

            match = _reName.match(expression[1:])
            if match:
                name = match.group(0)
                if name:
                    print(name)
                    lhs = 4
                    expression = expression[len(name)+1:].lstrip()

        elif expression[0] == "'":
            # try a string in apostrophes

            match = _reAposString.match(expression)
            if match:
                string = match.group(0)
                if string:
                    print(string.replace("''","'"))
                    lhs = 0
                    expression = expression[len(string):].lstrip()

        elif expression[0] == '"':
            # try a string in quotes

            match = _reQuotString.match(expression)
            if match:
                string = match.group(0)
                if string:
                    print(string.replace('""','"'))
                    lhs = 1
                    expression = expression[len(string):].lstrip()

        else:
            # try a number

            match = _reNumber.match(expression)
            if match:
                number = match.group(0)
                if number:
                    lhs = float(number.replace('¯','-'))
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
            print('⎕',end=' ')
            try:
                print_result(evaluate(line))
            except apl_exception as e:
                print(' '*(len(prompt)+len(line)-len(e.line)),end="^\n")
                print(e.message)

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
