"""
    the top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version supports:
        mixed scalar/vector expressions with subexpressions in parentheses
        system commands, system variables and workspace variables
        strings - parsing, printing and their use in expressions
        output using the ⎕← and ⍞← operators
"""

import re

from functools import reduce

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

def     _print_result (result,newline=True):
    """
    print the result when APL expression evaluation succeeds
    """
    print(str(result),end='\n' if newline else '')

# ------------------------------

def     print_error (error,expr,prompt="",where=""):
    """
    print the error response when APL expression evaluation fails
    """
    print('\r' + ' '*(len(prompt)+expr.find(error.expr)),end="^\n")
    print(error.message,where)

# ------------------------------

def     _findUnquoted(expr,char,spos=0):
    """
    find the first occurrence in char that is not in a string literal
    """
    cpos = expr.find(char,spos)
    if cpos == -1:
        return cpos

    mpos = reduce(lambda a, x: x if x < a and x != -1 else a, map(lambda x: expr.find(x,spos), ('"',"'")),cpos)

    if mpos == cpos:
        return cpos

    spos = expr.find(expr[mpos],mpos+1)
    if spos == -1:
        apl_error("SYNTAX ERROR",expr[mpos:])

    return _findUnquoted(expr,char,spos+1)

# ------------------------------

def     evaluate_and_print_line (line,silent=False):
    """
    evaluate and print possibly more than one expression
    """
    pos = _findUnquoted(line,'⋄')

    if pos == -1:
        evaluate_and_print(line,True,True,silent)
        return

    evaluate_and_print(line[:pos],True,False,silent)

    line = line[pos + 1:].lstrip()
    if line:
        evaluate_and_print_line(line,silent)

# ------------------------------

def     evaluate_and_print (expr,bol=False,eol=True,silent=False):
    """
    evaluate and print an expression
    """
    expr = expr.lstrip()

    if expr:
        result = evaluate(expr,bol,eol)
        if result is not None and not silent:
            _print_result(result)

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

def     evaluate_with_output (expr,consumed,bol,newline):
    """
    evaluate, print and return an intermediary result
    """
    rhs = evaluate(expr[consumed:])

    if newline:
        _print_result(rhs)
    else:
        if rhs.isVector() and not rhs.isString():
            _print_result(apl_vector([rhs]),False)
        else:
            _print_result(rhs,False)

    return rhs if not bol else None, len(expr)

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
            try:
                return (float(number.replace('¯','-')), len(number))
            except ValueError as e:
                if not reduce (lambda a,x: a or x == number,('.', '¯', "¯."),False):
                    raise(e)

    return (None, 0)

# ------------------------------

def     _isCompoundOperator (operator,expr):
    """
    does expression start with the given compound operator ?
    """
    start = len(expr)

    while operator:
        if not expr.startswith(operator[0]):
            return 0

        expr = expr[1:].lstrip()
        operator = operator[1:]

    return start - len(expr)

# ------------------------------

def     parse (expr,bol,eol):
    """
    Extract and evaluate the next token in a APL expression (left to right)

    Beware indirect recursion
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
            consumed = _isCompoundOperator("⎕←",expr)
            if consumed:
                value, consumed = evaluate_with_output(expr,consumed,bol,True)
            else:
                value, consumed = evaluate_system_variable(expr)
        elif leader == '⍞':
            consumed = _isCompoundOperator("⍞←",expr)
            if consumed:
                value, consumed = evaluate_with_output(expr,consumed,bol,bol and eol)
            else:
                apl_error("SYNTAX ERROR")
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
        elif leader == '⍝':
            value, consumed = None, len(expr)
        else:
            value, consumed = extract_number(expr)

        if value is not None:
            if type(value) == apl_scalar:
                value = value.python()
            lhs.append(value)

            bol = False

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

def     evaluate (expression,bol=False,eol=True):
    """
    Evaluate an APL expression

    this routine is recursive
    """
    try:
        expr = expression.lstrip()

        if not expr:
            apl_error("SYNTAX ERROR")

        lhs, expr = parse(expr,bol,eol)

        if not expr:
            return lhs

        if lhs is None:
            function = monadic_function(expr)
            rhs = evaluate(expr[1:])
            return function(rhs)
        else:
            function = dyadic_function(expr)
            rhs = evaluate(expr[1:])
            return function(lhs,rhs)

    except apl_exception as error:
        if not error.expr:
           error.expr = expr
        raise(error)

# EOF
