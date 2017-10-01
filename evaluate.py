"""
    parse and evaluate APL expressions

    UNDER DEVELOPMENT

    This version supports:
        mixed scalar/vector expressions with subexpressions in parentheses
        system commands, system variables and workspace variables
        strings - parsing, printing and their use in expressions
        output using the ⎕← and ⍞← operators
"""

import re

from copy import copy as shallowcopy
from functools import reduce

from monadicLookup import monadicFunction
from dyadicLookup import dyadicFunction

from systemCommands import systemCommand
from systemVariables import systemVariable, eagerEvaluation

from workspaceVariables import workspaceVariable

from aplQuantity import aplQuantity, makeScalar, makeVector, makeEmptyVector, makeString
from aplError import aplException, assertError

# ------------------------------

_reNumber = re.compile(r'¯?[0-9]*\.?[0-9]*([eE][-+¯]?[0-9]+)?')
_reName = re.compile(r'[A-Za-z][A-Z_a-z0-9]*')

_reAposString = re.compile(r"'([^']|'')*'")
_reQuotString = re.compile(r'"([^"]|"")*"')

# ------------------------------

def     _findUnquoted(expr, char, spos=0):
    """
    find the first occurrence in char that is not in a string literal
    """
    cpos = expr.find(char, spos)
    if cpos == -1:
        return cpos

    mpos = reduce(lambda a, x: x if x < a and x != -1 else a,
                  map(lambda x: expr.find(x, spos), ('"', "'")),
                  cpos)

    if mpos == cpos:
        return cpos

    spos = expr.find(expr[mpos], mpos+1)
    if spos == -1:
        raise aplException("SYNTAX ERROR", expr[mpos:])

    return _findUnquoted(expr, char, spos+1)

# --------------

def     evaluateAndPrint(line, cio, hushLast=False):
    """
    evaluate and print possibly more than one expression
    """
    cio.startNewStmt()

    pos = _findUnquoted(line, '⋄')

    if pos == -1:
        expr = line.lstrip()
        if expr:
            result = evaluate(expr, cio)
            if not hushLast:
                cio.printEndOfLine()
                cio.printImplicit(result)

            return result

    else:
        expr = line[:pos].lstrip()
        if expr:
            result = evaluate(expr, cio)
            cio.printImplicit(result)

        line = line[pos + 1:].lstrip()
        if line:
            return evaluateAndPrint(line, cio, hushLast)

# ------------------------------

def     _expressionWithinParentheses(expr, opos, cpos):
    """
    find expression in parentheses
    """
    pos = expr[cpos + 1:].find(')')
    if pos == -1:
        assertError("SYNTAX ERROR")
    cpos += pos + 1

    pos = expr[opos + 1:cpos].find('(')
    if pos == -1:
        return expr[:cpos + 1]
    opos += pos + 1

    return _expressionWithinParentheses(expr, opos, cpos)

# --------------

def     evaluateSubexpression(expr, cio):
    """
    extract and evaluate a leading subexpression in parentheses
    """
    subexpression = _expressionWithinParentheses(expr, 0, 0)

    return evaluate(subexpression[1:-1], cio), len(subexpression)

# ------------------------------

def     evaluateName(expr, cio):
    """
    evaluate, assign to or create a workspace variable
    """
    match = _reName.match(expr)
    if match:
        name = match.group(0)
        if name:
            try:
                rhs_expr = expr[len(name):].lstrip()
                if rhs_expr and rhs_expr[0] == '←':
                    if cio.newStmt:
                        cio.hushImplicit = True
                        cio.newStmt = False

                    rhs = evaluate(rhs_expr[1:].lstrip(), cio)
                    lhs = workspaceVariable(name, rhs)
                    consumed = len(expr)
                else:
                    lhs = workspaceVariable(name)
                    consumed = len(name)

                return lhs, consumed

            except aplException as error:
                if not error.expr:
                    error.expr = expr
                raise error

    return None, 0

# ------------------------------

def     evaluateBoxIO(expr, cio):
    """
    evaluate, print (possibly) and return an intermediary result
    """
    texpr = expr[1:].lstrip()

    if texpr and texpr[0] == '←':
        # output operator

        newStmt = cio.newStmt
        cio.newStmt = False

        rhs = evaluate(texpr[1:], cio) if newStmt else evaluate(texpr[1:], cio).resolve()

        cio.printExplicit(rhs)

        if newStmt:
            cio.hushImplicit = True
            rhs = None

        return rhs, len(expr)

    else:
        # input operator

        lcio = shallowcopy(cio)
        lcio.startNewLine()
        lcio.prompt = "⎕:    "
        lcio.prefixDone = cio.prefixDone

        try:
            expr = lcio.read(lcio.inFile)
        except EOFError:
            assertError("EOF ERROR")

        try:
            value = evaluateAndPrint(expr, lcio, True)
        except aplException as error:
            lcio.printError(lcio.inFile, error, expr)
            assertError(None)

        cio.prefixDone = lcio.prefixDone

        return value, 1

# ------------------------------

def     evaluateBoxTickIO(expr, cio):
    """
    evaluate, print (possibly) and return an intermediary result
    """
    texpr = expr[1:].lstrip()

    if texpr and texpr[0] == '←':
        # output operator

        newStmt = cio.newStmt
        cio.newStmt = False

        rhs = evaluate(texpr[1:], cio) if newStmt else evaluate(texpr[1:], cio).resolve()

        if rhs.padFill() == ' ':
            cio.userPromptLength = rhs.dimension()
            cio.printExplicit(rhs, '')
        elif rhs.isVector():
            cio.printExplicit(makeVector((rhs,), 1), '')
        else:
            cio.printExplicit(rhs, '')

        if newStmt:
            cio.hushImplicit = True
            rhs = None

        return rhs, len(expr)

    else:
        # input operator

        lcio = shallowcopy(cio)
        lcio.startNewLine()
        lcio.prompt = ""

        try:
            expr = lcio.read(lcio.inFile)
        except EOFError:
            assertError("EOF ERROR")

        value = makeString(cio.userPromptLength*' '+expr, False)

        cio.endOfLine = '\n'

        return value, 1

# ------------------------------

def     evaluateSystemVariable(expr, cio):
    """
    evaluate or assign to a system variable
    """
    match = _reName.match(expr[1:])
    if match:
        name = match.group(0)
        if name:
            try:
                rhs_expr = expr[len(name)+1:].lstrip()
                if rhs_expr and rhs_expr[0] == '←':
                    if cio.newStmt:
                        cio.hushImplicit = True
                        cio.newStmt = False

                    rhs = evaluate(rhs_expr[1:], cio)
                    lhs = systemVariable(name, rhs)
                    consumed = len(expr)
                else:
                    lhs = systemVariable(name)
                    consumed = len(name)+1

                return lhs, consumed

            except aplException as error:
                if not error.expr:
                    error.expr = expr
                raise error

    return None, 0

# ------------------------------

def     handleSystemCommand(expr, cio):
    """
    invoke a system command
    """
    match = _reName.match(expr[1:])
    if match:
        name = match.group(0)
        if name:
            systemCommand(name, expr[len(name)+1:], cio)
            return None, len(expr)

    return None, 0

# ------------------------------

def     extractString(expr, _):
    """
    extract leading string from expression
    """
    delim = expr[0]

    if delim == "'":
        match = _reAposString.match(expr)
    elif delim == '"':
        match = _reQuotString.match(expr)
    else:
        match = None

    if match:
        string = match.group(0)
        if string:
            return makeString(string, True), len(string)

    return None, 0

# ------------------------------

def     extractNumber(expr, _):
    """
    extract leading number from expression
    """
    match = _reNumber.match(expr)

    if match:
        number = match.group(0)
        if number:
            try:
                return float(number.replace('¯', '-')), len(number)
            except ValueError as exception:
                if not reduce(lambda a, x: a or x == number, ('.', '¯', "¯."), False):
                    raise exception

    return None, 0

# ------------------------------

_ParserFunctions = (
    extractNumber,
    extractString,
    extractString,
    handleSystemCommand,
    evaluateSubexpression,
    evaluateBoxIO,
    evaluateBoxTickIO,
    lambda e, c: (makeEmptyVector(), 1),
    lambda e, c: (None, len(e)),
)

# --------------

def     parseFunction(expr, lhs):
    """
    chose function that will parse the next token
    """
    leader = expr[0]

    if leader.isalpha():
        return evaluateName

    if leader == '⎕' and len(expr) > 1 and expr[1].isalpha():
        return evaluateSystemVariable

    if leader == ')' and lhs != []:
        assertError("SYNTAX ERROR")

    return _ParserFunctions["'\")(⎕⍞⍬⍝".find(leader)+1]

# --------------

def     parse(expr, cio):
    """
    extract and evaluate the next subexpression from expr

    called only from evaluate but beware indirect recursion
    """
    lhs = []

    while True:
        function = parseFunction(expr, lhs)

        value, consumed = function(expr, cio)

        if value is not None:
            if isinstance(value, aplQuantity):
                value = value.safeScalar()
            lhs.append(value)

        if consumed == 0:
            break
        else:
            expr = expr[consumed:]

        cio.newStmt = False

        if not expr or expr[0] != ' ':
            break
        else:
            expr = expr.lstrip()

        if not expr:
            break

    return lhs, expr

# ------------------------------

def     evaluate(expression, cio):
    """
    evaluate an APL expression

    called from parse and routines parse calls so beware indirect recursion
    """
    try:
        expr = expression.lstrip()

        if not expr:
            assertError("SYNTAX ERROR")

        lhs, expr = parse(expr, cio)

        if lhs == []:
            lhs = None
        elif len(lhs) > 1:
            lhs = makeVector(tuple(lhs), -1, None)
        elif isinstance(lhs[0], aplQuantity):
            lhs = lhs[0]
        else:
            lhs = makeScalar(lhs[0], None)

        if not expr:
            return lhs

        if cio.newStmt:
            if lhs is None and expr[0] == '⊣':
                cio.hushImplicit = True
            cio.newStmt = False

        function = monadicFunction(expr) if lhs is None else dyadicFunction(expr)

        rhs = evaluate(expr[1:], cio)
        rhs.expressionToGo = expr

        result = function(rhs) if lhs is None else function(lhs, rhs)

        return result.resolve() if eagerEvaluation() else result

    except aplException as error:
        if not error.expr:
            error.expr = expr
        raise error

# EOF
