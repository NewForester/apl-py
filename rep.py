"""
    The top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version supports expressions with parentheses

    It also recognises strings.  For now, those in apostrophes evaluate to 0 and those in quotes to 1

    It also evaluates:
      - system variables - reference and assignment
      - system commands - invocation

    For now, workspace names evaluate to 2.
"""

import sys
import re

from monadic import monadic_function
from dyadic import dyadic_function

from system_vars import system_variable
from system_cmds import system_command

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

def     extract_subexpression (expr):
    """
    Extract leading subexpression in parentheses from expression
    """
    subexpression = expression_within_parentheses(expr,0,0)

    return (evaluate(subexpression[1:-1]), len(subexpression))

# ------------------------------

def     extract_name (expr,prefix):
    """
    Extract leading name from expression
    """
    if not prefix:
        lhs = (2)
        match = _reName.match(expr)
    elif prefix == '⎕':
        lhs = (3)
        match = _reName.match(expr[1:])
    elif prefix == ')':
        lhs = (4)
        match = _reName.match(expr[1:])
    else:
        match = None

    if match:
        name = match.group(0)
        if name:
            print(name)
            return (lhs, len(prefix)+len(name))

    return (None, 0)

# ------------------------------

def     evaluate_system_variable (expr):
    """
    Evaluate or assign to a system variable
    """
    match = _reName.match(expr[1:])
    if match:
        name = match.group(0)
        if name:
            rhs_expr = expr[len(name)+1:].lstrip()
            if rhs_expr and rhs_expr[0] == '←':
                rhs = evaluate(rhs_expr[1:].lstrip())
                lhs = system_variable(name,rhs)
                return (lhs, len(expr))
            else:
                lhs = system_variable(name)
                return (lhs, len(name)+1)

    return (None, 0)

# ------------------------------

def     handle_system_command (expr):
    """
    Invoke a system command
    """
    match = _reName.match(expr[1:])
    if match:
        name = match.group(0)
        if name:
            system_command(name, expr[len(name)+1:])
            return (None, len(expr))

    return (None, 0)

# ------------------------------

def     extract_string (expr,delim):
    """
    Extract leading string from expression
    """
    if delim == "'":
        lhs = 0
        match = _reAposString.match(expr)
    elif delim == '"':
        lhs = 1
        match = _reQuotString.match(expr)
    else:
        match = None

    if match:
        string = match.group(0)
        if string:
            print(string.replace(delim*2,delim))
            return (lhs, len(string))

    return (None, 0)

# ------------------------------

def     extract_number (expr):
    """
    Extract leading number from expression
    """
    match = _reNumber.match(expr)

    if match:
        number = match.group(0)
        if number:
            return (float(number.replace('¯','-')), len(number))

    return (None, 0)

# ------------------------------

def     evaluate(expression):
    """
    Evaluate an APL expression

        - strict right-to-left evaluation of
        - sequences of monadic and dyadic functions
        - with parentheses to alter the order of evaluation
        - strings recognised
        - system variables and system commands handled
        - workspace names only recognised
    """

    try:
        lhs = None

        if not expression:
            return lhs

        consumed = 0
        leader = expression[0]

        if leader == '(':
            lhs, consumed = extract_subexpression(expression)
        elif leader.isalpha():
            lhs, consumed = extract_name(expression,"")
        elif leader == '⎕':
            lhs, consumed = evaluate_system_variable(expression)
        elif leader == ')':
            lhs, consumed = handle_system_command(expression)
        elif leader == "'":
            lhs, consumed = extract_string(expression,leader)
        elif leader == '"':
            lhs, consumed = extract_string(expression,leader)
        else:
            lhs, consumed = extract_number(expression)

        if consumed:
            expression = expression[consumed:].lstrip()

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
    Read input, evaluate it and output the result
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
