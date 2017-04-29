"""
    The top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version supports expressions with parentheses

    It also recognises strings.  For now, those in apostrophes evaluate to 0 and those in quotes to 1

    It also evaluates:
      - workspace variables
      - system variables - reference and assignment
      - system commands - invocation
"""

import re

from monadic import monadic_function
from dyadic import dyadic_function

from system_vars import system_variable
from system_cmds import system_command

from workspace_vars import workspace_variable

from apl_exception import APL_Exception as apl_exception, apl_exit

# ------------------------------

_reNumber = re.compile(r'¯?[0-9]*\.?[0-9]*([eE][-+¯]?[0-9]+)?')
_reName   = re.compile(r'[A-Za-z][A-Z_a-z0-9]*')

_reAposString = re.compile(r"'([^']|'')*'")
_reQuotString = re.compile(r'"([^"]|"")*"')

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

def     evaluate_name (expr):
    """
    Evaluate, assign to or create a workspace variable

    does not handle functions
    """
    match = _reName.match(expr)
    if match:
        name = match.group(0)
        if name:
            rhs_expr = expr[len(name):].lstrip()
            if rhs_expr and rhs_expr[0] == '←':
                rhs = evaluate(rhs_expr[1:].lstrip())
                lhs = workspace_variable(name,rhs)
                return (lhs, len(expr))
            else:
                lhs = workspace_variable(name)
                return (lhs, len(name))

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
                rhs = evaluate(rhs_expr[1:])
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
        - workspace variables, system variables and system commands evaluated
        - strings recognised
        """

    try:
        lhs = None

        expr = expression.lstrip()

        if not expr:
            raise (apl_exception("SYNTAX ERROR"))

        consumed = 0
        leader = expr[0]

        if leader == '(':
            lhs, consumed = extract_subexpression(expr)
        elif leader.isalpha():
            lhs, consumed = evaluate_name(expr)
        elif leader == '⎕':
            lhs, consumed = evaluate_system_variable(expr)
        elif leader == ')':
            lhs, consumed = handle_system_command(expr)
        elif leader == "'":
            lhs, consumed = extract_string(expr,leader)
        elif leader == '"':
            lhs, consumed = extract_string(expr,leader)
        else:
            lhs, consumed = extract_number(expr)

        if consumed:
            expr = expr[consumed:].lstrip()

        if not expr:
            return lhs

        if lhs is None:
            # try a monadic function

            function = monadic_function(expr)
            rhs = evaluate(expr[1:])
            return function(rhs)
        else:
            # try a dyadic function

            function = dyadic_function(expr)
            rhs = evaluate(expr[1:])
            return function(lhs,rhs)

    except apl_exception as e:
        if not e.line:
           e.line = expr
        raise (e)

# EOF
