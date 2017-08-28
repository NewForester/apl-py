#!/usr/bin/python3
"""
    functions germane to APL test modules
"""

import sys

from evaluate import evaluate, evaluateAndPrint

from systemVariables import eagerEvaluation, setEvaluationMode

from aplCio import aplCio
from aplError import aplException

# ------------------------------

def     testCommand(expr):
    """
    evaluate an expression that is a systen command

    handle both positive and negative outcomes
    """
    try:
        evaluate(expr, aplCio())
    except aplException as error:
        print(error.message)

# ------------------------------

def     testOutput(expr):
    """
    evaluate a line that may comprise several expressions

    handle both positive and negative outcomes
    """
    try:
        cio = aplCio()
        evaluateAndPrint(expr, cio)
    except aplException as error:
        print(error.message)

# ------------------------------

def     testResult(expr, overrideLazy=False):
    """
    evaluate an expression then format and print the result

    handle both positive and negative outcomes

    Often the negative outcome in lazy evaluation mode involves printing backspaces

        doctest.NORMALIZE_WHITESPACE = 1

    does not have the desired effect, hence the messing around the with the evaluation mode.
    """
    if overrideLazy:
        overrideLazy = not eagerEvaluation()

    if overrideLazy:
        setEvaluationMode(1)

    try:
        cio = aplCio()
        cio.printResult(evaluate(expr, cio))
    except aplException as error:
        print(error.message)

    if overrideLazy:
        setEvaluationMode(0)

# ------------------------------

def     parseCommandLineArgs(args):
    """
    separate command line args into (optional) flags and an (optional) APL expression
    """
    if len(args) == 1:
        flags, args = [], []
    elif '--' in args:
        pivot = args.index("--")
        flags, args = args[1:pivot], args[pivot + 1:]
    elif args[1][0] == '-':
        flags, args = args[1:], []
    else:
        flags, args = [], args[1:]

    if flags != []:
        flags = ' '.join(flags).replace(' -', ':-').split(':')

    if args != []:
        args = ' '.join(args)

    return flags, args

# ------------------------------

def     preamble():
    """
    allows a choice between eager and lazy evaluation
    """
    flags, args = parseCommandLineArgs(sys.argv)

    for flag in flags:
        if flag in ("-ee=0", "--lazy"):
            setEvaluationMode(0)

        elif flag in ("-ee=1", "--eager"):
            setEvaluationMode(1)

# EOF
