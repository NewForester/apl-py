#!/usr/bin/python3
"""
    functions germane to APL test modules
"""

import sys

import systemVariables

from evaluate import evaluate, evaluateAndPrint

from aplCio import aplCio
from aplError import aplException, aplQuit

# ------------------------------

def     testCommand(expr):
    """
    evaluate an expression that is a system command

    handle both positive and negative outcomes
    """
    try:
        evaluate(expr, aplCio())
    except aplException as error:
        print(error.message)

# --------------

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

# --------------

def     testResult(expr, overrideLazy=False):
    """
    evaluate an expression then format and print the result

    handle both positive and negative outcomes

    Often the negative outcome in lazy evaluation mode involves printing backspaces

        doctest.NORMALIZE_WHITESPACE = 1

    does not have the desired effect, hence the messing around the with the evaluation mode.
    """
    if overrideLazy:
        overrideLazy = not systemVariables.eagerEvaluation()

    if overrideLazy:
        systemVariables.setEvaluationMode(1)

    try:
        cio = aplCio()
        cio.printResult(evaluate(expr, cio))
    except aplException as error:
        print(error.message)

    if overrideLazy:
        systemVariables.setEvaluationMode(0)

# ------------------------------

def     saveIndexOrigin():
    return systemVariables.indexOrigin()

# --------------

def     setIndexOrigin(io):
    systemVariables.setIndexOrigin(io)

# --------------

def     restoreIndexOrigin(io):
    systemVariables.setIndexOrigin(io)

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
    process command line flags - see <test-script> -h
    """
    flags, args = parseCommandLineArgs(sys.argv)

    for flag in flags:
        if flag in ("-ee=0", "--lazy"):
            systemVariables.setEvaluationMode(0)

        elif flag in ("-ee=1", "--eager"):
            systemVariables.setEvaluationMode(1)

        elif flag in ("-io=0"):
            systemVariables.setIndexOrigin(0)

        elif flag in ("-io=1"):
            systemVariables.setIndexOrigin(1)

        elif flag in ("-h", "--help"):
            print(_help())
            aplQuit(0)

        else:
            aplQuit(3, "{0} not recognised: perhaps try -h".format(flag))

# ------------------------------

def     _help():
    """
APL unit tests implemented in Python all recognise the following flags:

    -ee=0 --lazy        ⎕EE ← 0 ⍝ lazy evaluation mode - default
    -ee=1 --eager       ⎕EE ← 1 ⍝ eager evaluation mode

    -io=0               ⎕IO ← 0
    -io=1               ⎕IO ← 1 ⍝ default

    -h --help           print this help text and exit

Note: the command line flags may be used to set the inital values of
⎕EE and ⎕IO but beware the tests themselves may set one or both of these.

Note: --help may be fielded by a shell script wrapper aroung the Python
test script so -h is to be preferred.
    """
    return _help.__doc__

# EOF
