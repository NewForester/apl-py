"""
    the top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version supports mixed scalar/vector expressions with subexpressions in parentheses

    Expression evaluation includes system commands, system variables and workspace variables

    It also recognises strings.  For now, those in apostrophes evaluate to 0 and those in quotes to 1
"""

import re

from monadic import monadic_function
from dyadic import dyadic_function

from system_vars import system_variable
from system_cmds import system_command

from workspace_vars import workspace_variable

from apl_quantity import APL_quantity as apl_value, APL_scalar as apl_scalar, APL_vector as apl_vector, APL_string as apl_string
from apl_error import APL_exception as apl_exception, apl_error

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
        apl_error("SYNTAX ERROR")
    cpos += pos + 1

    pos = expr[opos + 1:cpos].find('(')
    if pos == -1:
        return expr[:cpos + 1]
    opos += pos + 1

    return expression_within_parentheses(expr,opos,cpos)

# ------------------------------

def     evaluate_subexpression (expr):
    """
    Extract and evaluate a leading subexpression in parentheses
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
                lhs = workspace_variable(name,rhs.resolve())
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
                lhs = system_variable(name,rhs.resolve())
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
            return (apl_string(string), len(string))

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

def     parse(expr):
    """
    Extract and evaluate the next token in a APL expression (left to right)

    Beware indirection recursion
    """
    lhs = []

    while True:
        leader = expr[0]
        consumed = 0

        if leader == '(':
            value, consumed = evaluate_subexpression(expr)
        elif leader.isalpha():
            value, consumed = evaluate_name(expr)
        elif leader == '⎕':
            value, consumed = evaluate_system_variable(expr)
        elif leader == ')':
            if len(lhs):
                apl_error("SYNTAX ERROR")
            value, consumed = handle_system_command(expr)
        elif leader == "'":
            value, consumed = extract_string(expr,leader)
        elif leader == '"':
            value, consumed = extract_string(expr,leader)
        elif leader == '⍬':
            value, consumed = apl_vector([]), 1
        else:
            value, consumed = extract_number(expr)

        if value is not None:
            if type(value) == apl_scalar:
                value = value.python()
            lhs.append(value)

        if consumed == 0:
            break
        else:
            expr = expr[consumed:]

        if not expr or expr[0] != ' ':
            break
        else:
            expr = expr.lstrip()

        if not expr:
            break

    if len(lhs) == 0:
        lhs = None
    elif len(lhs) > 1:
        lhs = apl_vector(lhs)
    else:
        lhs = lhs[0]
        if not isinstance(lhs,apl_value):
            lhs = apl_scalar(lhs)

    return (lhs, expr)

# ------------------------------

def     evaluate(expression):
    """
    Evaluate an APL expression

    this routine is recursive
    """

    try:
        expr = expression.lstrip()

        if not expr:
            apl_error("SYNTAX ERROR")

        lhs, expr = parse(expr)

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

    except apl_exception as error:
        if not error.expr:
           error.expr = expr
        raise (error)

# EOF
