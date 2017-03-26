"""
    The top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version adds trivial apl_quit() and apl_exit() routines to the read-evaluate-print loop.
"""

import sys

def     read_evaluate_print (prompt):
    """
    Read input, echo input
    """
    try:
        while True:
            print(end=prompt)
            line = input()
            print('⎕', line)
    except EOFError:
        apl_exit(None)

def     apl_quit ():
    """
    Quit without clean up
    """
    print ()
    sys.exit(0)

def     apl_exit (message):
    """
    Clean up and quit
    """
    if message is None:
        print ()
    else:
        print (message)
    sys.exit(0)

# EOF
