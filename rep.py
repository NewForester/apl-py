"""
    The top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version adds a dummy evaluate routine.
"""

import sys

# ------------------------------

def     evaluate(expression):
    """
    Evaluate an APL expression - dummy version
    """
    return (expression)

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
            print('⎕', evaluate(line))
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
